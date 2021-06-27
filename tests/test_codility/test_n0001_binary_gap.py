import unittest

from codility.n0001_binary_gap import solution


class TestBinaryGap(unittest.TestCase):
    def test(self):
        self.assertEqual(solution(1041), 5)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(32), 0)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(561892), 3)
        self.assertEqual(solution(1376796946), 5)


if __name__ == '__main__':
    unittest.main()
