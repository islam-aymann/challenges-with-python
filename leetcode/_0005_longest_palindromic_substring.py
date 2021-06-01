class Solution:
    # Brute-Force O(N**3)
    def longestPalindrome1(self, s: str) -> str:
        if s == s[::-1]:
            return s
        ln = len(s)
        window_size = ln - 1
        while window_size > 0:
            for i in range(ln - window_size + 1):
                window = s[i: i + window_size]
                if window == window[::-1]:
                    return window
            window_size -= 1
        return ""

    def is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    # Brute-Force O(N**3)
    def longestPalindrome2(self, s: str) -> str:
        if self.is_palindrome(s):
            return s

        ln = len(s)
        window_size = ln - 1
        while window_size > 0:
            for i in range(ln - window_size + 1):
                window = s[i: i + window_size]
                if self.is_palindrome(window):
                    return window
            window_size -= 1
        return ""

    # Brute-Force O(N**3)
    def longestPalindrome3(self, s: str) -> str:
        ln = len(set(s))
        if ln == 1:
            return s
        elif not ln:
            return ""

        max_sub = ""
        for i, char in enumerate(s):
            j = s.rfind(char)

            while j > -1:
                window = s[i: j + 1]
                if self.is_palindrome(window) and len(max_sub) < len(window):
                    max_sub = window

                j = s[:j].rfind(char)

        return max_sub

    def longestPalindrome4(self, s: str) -> str:
        # Get length of input String
        n = len(s)

        # All subStrings of length 1
        # are palindromes
        max_length = 1
        start = 0

        # Nested loop to mark start
        # and end index
        for i in range(n):
            for j in range(i, n):
                flag = 1

                # Check palindrome
                for k in range(0, ((j - i) // 2) + 1):
                    if s[i + k] != s[j - k]:
                        flag = 0

                # Palindrome
                if flag != 0 and (j - i + 1) > max_length:
                    start = i
                    max_length = j - i + 1

        # Return length of LPS
        return s[start: start + max_length]

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res


if __name__ == "__main__":
    # s = "babadb"
    # s = "aacabdkacaa"
    # s = "cbbd"
    # s = "a"
    # s = "bb"
    # s = "aacabdkacaa"
    s = "aaaabbaa"
    print(Solution().longestPalindrome(s))
    # print(timeit.timeit(f"Solution().longestPalindrome('{s}')",
    #                     number=1000,
    #                     globals=globals()))
