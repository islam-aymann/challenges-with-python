import timeit
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index + 1


if __name__ == "__main__":
    # print(Solution().removeDuplicates([1, 1, 2]))
    print(
        1000
        * timeit.timeit(
            lambda: Solution().removeDuplicates(nums=[1, 1, 2]),
            number=100000,
            globals=globals(),
        )
    )
