import unittest

from hackerrank.problem_solving.n0003_sparse_arrays import matchingStrings


class TestSparseArrays(unittest.TestCase):
    def test(self):
        self.assertEqual(
            matchingStrings(
                ["ab", "ab", "abc"],
                ["ab", "abc", "bc"],
            ),
            [2, 1, 0],
        )

        self.assertEqual(
            matchingStrings(
                ["aba", "baba", "aba", "xzxb"],
                ["aba", "xzxb", "ab"],
            ),
            [2, 1, 0],
        )

        self.assertEqual(
            matchingStrings(
                ["def", "de", "fgh"],
                ["de", "imm", "fgh"],
            ),
            [1, 0, 1],
        )

        self.assertEqual(
            matchingStrings(
                [
                    "abcde",
                    "sdaklfj",
                    "asdjf",
                    "na",
                    "basdn",
                    "sdaklfj",
                    "asdjf",
                    "na",
                    "asdjf",
                    "na",
                    "basdn",
                    "sdaklfj",
                    "asdjf",
                ],
                [
                    "abcde",
                    "sdaklfj",
                    "asdjf",
                    "na",
                    "basdn",
                ],
            ),
            [
                1,
                3,
                4,
                3,
                2,
            ],
        )


if __name__ == "__main__":
    unittest.main()
