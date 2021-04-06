import numpy as np


class NumPyCreator:

    def __init__(self):
        return

    def from_list(self, lst, dtype=None):
        if dtype:
            return np.array(lst, dtype=dtype)
        return np.array(lst)

    def from_tuple(self, tpl, dtype=None):
        if dtype:
            return np.array(tpl, dtype=dtype)
        return np.array(tpl)

    def from_iterable(self, itr, dtype=None):
        if dtype:
            return np.array(itr, dtype=dtype)
        return np.array(itr)

    def from_shape(self, shape, value=0, dtype=None):
        if dtype:
            return np.full(shape, value, dtype=dtype)
        return np.full(shape, value)

    def random(self, shape, dtype=None):
        if dtype:
            return np.random.random(shape).astype(dtype)
        return np.random.random(shape)

    def identity(self, n, dtype=None):
        if dtype:
            return np.eye(n, dtype=dtype)
        return np.eye(n)


npc = NumPyCreator()
print(npc.from_list([[1, 2, 3], [6, 3, 4]], dtype='f'))
print(npc.from_tuple(("a", "b", "c")))
print(npc.from_iterable(range(5)))
print(npc.from_shape((3, 5)))
print(npc.random((3, 5), dtype='i'))
print(npc.identity(4, dtype='i'))
