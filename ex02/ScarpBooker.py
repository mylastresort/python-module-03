import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0, 0)):
        cstart, rstart = position
        climit, rlimit = dim
        climit += cstart
        rlimit += rstart
        return array[cstart: climit, rstart: rlimit]

    def thin(self, array: np.ndarray, n, axis):
        ver = array.shape[0]
        hor = array.shape[1]
        if axis == 0:
            return array[[row % n != 0 for row in range(1, ver + 1)]]
        mask = [[col % n != 0 for col in range(1, hor + 1)] for _ in range(ver)]
        shape = list(array.shape)
        shape[0] = ver
        shape[1] = sum(mask[0])
        return array[mask].reshape(shape)

    def juxtapose(self, array, n, axis):
        # return array * n if axis == 1 else [row * n for row in array]
        pass

    def mosaic(self, array, dim):
        # x, y = dim
        # return [[row * x for row in array] for _ in range(y)]
        pass