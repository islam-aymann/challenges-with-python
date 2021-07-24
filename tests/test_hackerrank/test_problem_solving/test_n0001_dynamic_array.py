import unittest

from hackerrank.problem_solving.n0001_dynamic_array import dynamicArray


class TestDynamicArray(unittest.TestCase):
    def test(self):
        self.assertEqual(
            dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]),
            [7, 3],
        )


if __name__ == "__main__":
    unittest.main()
