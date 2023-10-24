import numpy as np
import types
from collections.abc import Iterable


class NumPyCreator:
    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            return None
        try:
            return np.array(lst, dtype=dtype)
        except:
            return None

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            return None
        try:
            return np.array(tpl, dtype=dtype)
        except:
            return None

    def from_iterable(self, itr, dtype=None):
        if not isinstance(itr, Iterable):
            return None
        return np.array(itr, dtype=dtype)

    def from_shape(self, shape, value=0, dtype=None):
        if not isinstance(shape, tuple):
            return None
        return np.full(shape, value, dtype=dtype)

    def random(self, shape, dtype=None):
        if not isinstance(shape, tuple):
            return None
        return np.random.random(shape).astype(dtype)

    def identity(self, n, dtype=None):
        return np.eye(n, dtype=dtype)
