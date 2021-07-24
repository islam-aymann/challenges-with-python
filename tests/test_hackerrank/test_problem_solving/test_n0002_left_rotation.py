import unittest

from hackerrank.problem_solving.n0002_left_rotation import rotateLeft


class TestLeftRotation(unittest.TestCase):
    def test(self):
        self.assertEqual(rotateLeft(2, [1, 2, 3, 4, 5]), [3, 4, 5, 1, 2])
        self.assertEqual(rotateLeft(4, [1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])
        self.assertEqual(rotateLeft(5, [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(rotateLeft(6, [1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])


if __name__ == '__main__':
    unittest.main()
