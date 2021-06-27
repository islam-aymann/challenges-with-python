import unittest

from codility.n0002_cyclic_rotation import solution


class TestCyclicRotation(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])
        self.assertEqual(solution([], 1), [])


if __name__ == '__main__':
    unittest.main()
