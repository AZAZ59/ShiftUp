class Any:

    dtype = 'Any'

    def get(self, key, default=None):
        self.__data__.get(key, default)

    def __getitem__(self, item):
        self.__getattr__(item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __delitem__(self, key):
        self.__delattr__(key)

    def __getattr__(self, key):
        return self.key

    def __setattr__(self, key, value):
        if key == 'type':
            self.dtype = value
        self.__data__[key] = value

    def __delattr__(self, item):
        del self.__data__[item]

    def __init__(self, data={}, dtype=None):
        for key, value in data.items():
            self.__setattr__(key, value)
        if dtype is None:
            dtype = self.dtype
        self.dtype = dtype


class User(Any):
    dtype = 'User'


class Group(Any):
    dtype = 'Group'


class Array:

    __dtype__ = Any
    __list__ = []
    __pool__ = None

    def set_pool(self, pool):
        self.__pool__ = pool

    def __getitem__(self, item):
        return self.__list__[item]

    def __setitem__(self, key, value):
        self.__list__[key] = value

    def __delitem__(self, key):
        del self.__list__[key]

    def __getattr__(self, item):
        if self.__pool__ is None:
            array = list(map(lambda x: x.__getattr__(item), self.__list__))
        else:
            array = list(self.__pool__.map(lambda x: x.__getattr__(item), self.__list__))
        if len(array) > 0:
            dtype = array[0].__class__
        else:
            dtype = Any
        return Array(array, dtype)

    def __len__(self):
        return len(self.__list__)

    def __str__(self):
        return str(self.__list__)

    def __init__(self, list=list(), dtype=Any):
        self.__list__ = list
        self.dtype = dtype






