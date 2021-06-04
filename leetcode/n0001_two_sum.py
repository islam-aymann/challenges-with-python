import timeit
from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            i += 1

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            try:
                j = nums.index(target - num)
                if -1 < j != i:
                    return [i, j]
            except ValueError:
                pass

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        sortedNums = sorted(zip(nums, range(len(nums))))
        while i < j:
            if sortedNums[i][0] + sortedNums[j][0] == target:
                return [sortedNums[i][1], sortedNums[j][1]]
            elif sortedNums[i][0] + sortedNums[j][0] < target:
                i += 1
            elif sortedNums[i][0] + sortedNums[j][0] > target:
                j -= 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = dict()

        for i, n in enumerate(nums):
            if target - n in history:
                return [history[target - n], i]

            history[n] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
    print(timeit.timeit(f"Solution().twoSum({nums}, {target})",
                        number=10000,
                        globals=globals()))
