import unittest
from unittest.mock import patch
import ex00.NumPyCreator as ex00
import numpy as np


class Test_Python_Module_00(unittest.TestCase):
    def test_ex00(self):
        npc = ex00.NumPyCreator()
        ret = npc.from_list([[1, 2, 3], [6, 3, 4]])
        cond = ret == np.array([[1, 2, 3], [6, 3, 4]])
        self.assertTrue(cond.all())
        ret = npc.from_list([[1, 2, 3], [6, 4]])
        self.assertEqual(ret, None)
        ret = npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]])
        cond = ret == np.array([['1', '2', '3'], ['a', 'b', 'c'], [
                               '6', '4', '7']], dtype='<U21')
        self.assertTrue(cond.all())
        ret = npc.from_list(((1, 2), (3, 4)))
        self.assertEqual(ret, None)
        ret = npc.from_tuple(("a", "b", "c"))
        cond = ret == np.array(['a', 'b', 'c'])
        self.assertTrue(cond.all())
        ret = npc.from_tuple(["a", "b", "c"])
        self.assertEqual(ret, None)
        ret = npc.from_iterable(range(5))
        cond = ret == np.array([0, 1, 2, 3, 4])
        self.assertTrue(cond.all())
        shape = (3, 5)
        ret = npc.from_shape(shape)
        cond = ret == np.array(
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.assertTrue(cond.all())
        ret = npc.random(shape)
        ret = npc.identity(4)
        cond = ret == np.array([[1., 0., 0., 0.], [0., 1., 0., 0.], [
                               0., 0., 1., 0.], [0., 0., 0., 1.]])
        self.assertTrue(cond.all())


if __name__ == '__main__':
    unittest.main()
