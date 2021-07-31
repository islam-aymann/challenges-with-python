import unittest

from hackerrank.problem_solving.n0004_crush import arrayManipulation


class Crush(unittest.TestCase):
    def test(self):
        self.assertEqual(
            arrayManipulation(
                10,
                [
                    [1, 5, 3],
                    [4, 8, 7],
                    [6, 9, 1],
                ],
            ),
            10,
        )
        self.assertEqual(
            arrayManipulation(
                5,
                [
                    [1, 2, 100],
                    [2, 5, 100],
                    [3, 4, 100],
                ],
            ),
            200,
        )


if __name__ == "__main__":
    unittest.main()
