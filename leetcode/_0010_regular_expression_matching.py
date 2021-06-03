class Solution:
    def isMatch1(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch1(s, p[2:]) or
                    first_match and self.isMatch1(s[1:], p))
        else:
            return first_match and self.isMatch1(s[1:], p[1:])

    def isMatch(self, s, p):
        ms = len(s) + 1
        mp = len(p) + 1

        table = [[False] * (len(s) + 1) for _ in range(mp)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, mp):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, mp):
            for j in range(1, ms):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


if __name__ == "__main__":
    # sp = "aa", "a"
    # sp = "aa", "a*"
    # sp = "ab", ".*"
    # sp = "aab", "c*a*b"
    # sp = "mississippi", "mis*is*p*."
    # sp = "aaap", ".*p"
    # sp = "ab", ".*c"
    # sp = "aaa", "a*a"
    sp = "aaa", "ab*a*c*a"

    print(Solution().isMatch(*sp))
    # print(timeit.timeit(f"Solution().isMatch(*sp)",
    #                     number=1000,
    #                     globals=globals()))
