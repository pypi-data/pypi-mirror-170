import logging

from collections.abc import Iterable
from datetime import datetime
from queue import Queue
import pywebworker.worker_config

# this module is registered in worker_config.py
import pywebworker_js


DEFAULT_LOG_LEVEL = logging.DEBUG
# default logger
logger = logging.getLogger(__name__)
logger.setLevel(DEFAULT_LOG_LEVEL)


class WorkerError(Exception):
    def __init__(self, message, *args):
        """
        :param message: details to display in error message

        Generic exception for Worker objects.
        """
        super().__init__(args)
        self.message = message

    def __str__(self):
        return f'Error with worker thread: {self.message}'


class FatalWorkerError(WorkerError):
    def __init__(self, message, worker, *args):
        """
        :param message: details to display in error message
        :param worker: worker to kill

        Exception for worker objects that kills the worker
        """
        super().__init__(args)
        self.message = message
        worker.kill()

    def __str__(self):
        return f'WORKER TERMINATED - FATAL ERROR WITH WORKER THREAD: {self.message}'


class WorkerMessage:
    """Message from a PyWorker web pywebworker"""
    def __init__(self, data, status=False, timestamp=datetime.now()):
        # TODO: add datetime for when message was sent
        self.data = data
        self.status = status
        self.timestamp = timestamp

    def read(self):
        self.status = True
        return self.data

    def received(self) -> datetime:
        return self.timestamp

    def is_read(self) -> bool:
        return self.status

    def __str__(self):
        return f"WorkerMessage{{'" \
               f"Read:{str(self.status)};" \
               f"Received:{self.timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')};" \
               f"}}"


class WorkerMessageQueue:
    """
    Queue that converts web worker events into WorkerMessage objects before queueing for user collection
    """
    def __init__(self):
        self.queue = Queue()

    def put(self, event):
        """
        Converts a web worker event into a WorkerMessage and puts it into a queue
        :param event: Web worker event
        """
        self.queue.put(WorkerMessage(event.data))

    def get(self, block=False, timeout=None) -> WorkerMessage:
        """
        Returns the next item in the Queue. Blocking disabled by default to prevent unintentionally locking the browser
        :param block: whether to wait for the next message
        :param timeout: time to wait for the next message, if applicable
        :return: the next WorkerMessage in the queue
        """
        return self.queue.get(block=block, timeout=timeout)


# You may be asking "couldn't you just use pyodide's js module for this?" The short answer is kinda, the long answer
# is yes, but with a lot more difficulty. Passing messages back and forth can be buggy and in some cases they can be
# missed. The Worker class wraps a JavaScript object that helps to facilitate stable communication for any inheriting
# classes. This is exceptionally helpful for loading python scripts into workers
class Worker:
    """
    Creates a browser-friendly, pythonic way of using web workers with pyodide
    """
    def __init__(self, script, onmessage_actions=None, loglevel=logging.DEBUG):
        """

        :param script: the script to be executed in the web worker thread
        :param onmessage_actions: an iterable of functions to be executed when a message is received from the worker
        :param loglevel: level at which to produce log messages
        """
        # TODO: improve logging
        self.logger = logging.getLogger('PyWorker')
        self.logger.setLevel(loglevel)

        self.script = script
        self.worker = pywebworker_js(script)

        self.messages = list()

        self.__onmessage_actions = list()
        self.set_onmessage(onmessage_actions)

    # some of these might seem unnecessary, but they make importing the script and jumping right in MUCH easier
    def has_unread_messages(self) -> bool:
        """
        Returns True if there are any unread messages
        """
        return self.get_unread_messages() != list()

    def get_unread_messages(self) -> list[WorkerMessage]:
        """adds any missing messages to the message repository and returns anything not marked as opened"""
        return [message for message in self.messages if not message.is_read()]

    def get_next_unread_message(self) -> WorkerMessage:
        """
        Provides the next unread message. If one does not exist, returns None
        :return: the next unread message from the list, if one exists
        """
        return self.get_unread_messages()[0]

    def get_message(self, index) -> WorkerMessage:
        """
        Returns the message at the index
        """
        return self.messages[index]

    def get_messages(self) -> list[WorkerMessage]:
        """
        :return: list of messages
        """
        # TODO: add ability to filter messages by time received
        return self.messages

    def send_message(self, message) -> None:
        """
        Sends a message to the pywebworker
        """
        if self.worker.get_state() == 'Running':
            self.worker.send_message(message)
        else:
            raise WorkerError('Worker is not running; cannot send messages to inactive workers')

    def get_id(self) -> str:
        """
        Returns the unique id value for this pywebworker
        """
        return self.worker.get_id()

    def get_script(self) -> str:
        return self.worker.get_script()

    def set_script(self, script) -> None:
        """
        Sets the script for the worker. Must be set before starting, script cannot be changed once in progress
        :param script: the new script to use
        """
        if self.worker.get_state() != 'Running':
            return self.worker.set_script(script)
        else:
            raise WorkerError('Cannot change script after starting!')

    def add_to_onmessage(self, function) -> None:
        """
        :param function: function or iterable of functions to add to process that runs whenever a message is received
        from the worker
        """
        self.__onmessage_actions += list(function) if isinstance(function, Iterable) else [function]

    def set_onmessage(self, functions) -> None:
        """
        Sets the actions to be run whenever a message is received. Function to populate messages will be automatically
        added
        :param functions: an iterable of functions to be run whenever a message is received from the worker
        """
        to_add = functions if functions else []
        self.__onmessage_actions = [lambda event: self.messages.append(WorkerMessage(event.data))] + to_add

    def get_onmessage(self) -> list:
        """
        Returns all functions that are run when a message is received from the worker. Excludes message collection
        function that is automatically run whenever list is set
        :return: all functions to be run during onmessage process
        """
        return self.__onmessage_actions[1:]

    def __onmessage(self, event) -> None:
        """
        Populates the messages and runs any other provided actions whenever a message is received. New functions can
        be added with add_to_onmessage or set_onmessage. Any exceptions will be captured and logged to prevent
        any single action from breaking any processes dependent on the incoming messages
        :param event: message event from the web worker
        """
        for index, action in enumerate(self.__onmessage_actions):
            try:
                action(event)
            except Exception as e:
                # all exceptions caught and logged to prevent breaking any other processes reliant on the messages
                logger.exception(f'onmessage action {index} failed:\n{e}')

    def start(self) -> str:
        """
        Starts the web pywebworker and the message listening service
        :return: the id value for the worker
        """
        self.worker.start()
        self.worker.pywebworker.onmessage = lambda event: self.__onmessage(event)
        return self.worker.get_id()

    def kill(self) -> None:
        """
        Terminates the web pywebworker. This action is immediate, anything in-progress will be abruptly stopped
        """
        self.worker.kill()

    def __del__(self):
        try:
            self.kill()
        except Exception as e:
            # Currently we just discard all exceptions, the goal is really just to execute the kill command so threads
            # aren't lost to the void
            pass
