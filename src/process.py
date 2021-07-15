from queue import Queue
import threading


_queue = Queue()


def _preserve(function):
    def wrapper(*args):
        _queue.put(function(*args))
    return wrapper


class Background:

    def __init__(self, target, args):
        self._target = target
        self._args = args

        self._thread = threading.Thread(target=self._run, args=self._args)

    @_preserve
    def _run(self, *args):
        return self._target(*args)

    def start(self):
        self._thread.start()

    def join(self, timeout=None):
        if timeout is not None:
            assert str(timeout).isnumeric()
            self._thread.join(timeout)
        else:
            self._thread.join()

    def is_alive(self):
        return self._thread.is_alive()

    def get_return_value(self):
        if self._thread.is_alive():
            raise RuntimeError("Process is still running and has not returned yet")
        return _queue.get()
