import itertools


class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     char_lists = dict()
    #     for i, char in enumerate(s):
    #         dummy = list()
    #         counter = int()
    #         for j in range(i, len(s)):
    #             if s[j] not in dummy:
    #                 dummy.append(s[j])
    #                 counter += 1
    #             else:
    #                 break
    #         char_lists[i] = counter
    #
    #     return max(char_lists.values())

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
    #
    #     # All string characters are unique
    #     if len(s) == len(set(s)):
    #         return len(s)
    #
    #     # The string repeats itself
    #     i = (s + s).find(s, 1, -1)
    #     if i > -1:
    #         return self.lengthOfLongestSubstring(s[:i])
    #
    #     char_lists = dict()
    #     for i, char in enumerate(s):
    #         dummy = list()
    #         counter = int()
    #         for j in range(i, len(s)):
    #             if s[j] not in dummy:
    #                 dummy.append(s[j])
    #                 counter += 1
    #             else:
    #                 break
    #         char_lists[i] = counter
    #
    #     return max(char_lists.values())

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     start = max_length = 0
    #     for i in range(len(s)):
    #         if s[i] in s[:i]:
    #             start = max(start, s[:i].rfind(s[i]) + 1)
    #         max_length = max(max_length, i + 1 - start)
    #     return max_length

    def lengthOfLongestSubstring(self, s):
        start = max_length = 0
        used_char = {}

        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used_char[s[i]] = i

        return max_length


if __name__ == '__main__':
    s = 'abcabcabcd'
    print(Solution().lengthOfLongestSubstring(s))
    # print(timeit.timeit(f"Solution().lengthOfLongestSubstring('{s}')",
    #                     number=10000,
    #                     globals=globals()))
