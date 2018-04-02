from threading import Lock


class LockedContainer():

    def __init__(self):
        self.lock = Lock()
        self._value = None
        self._type = None

    @property
    def value(self):
        with self.lock:
            try:
                return self._type(self._value)
            except TypeError:
                return None

    @value.setter
    def value(self, value):
        with self.lock:
            type_ = type(value)
            self._type = type_
            self._value = value
