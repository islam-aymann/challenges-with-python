import itertools
import timeit
from typing import List


class Solution:
    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        sums = {i: sum(i) for i in itertools.combinations(nums, 3)}
        return min(sums.values(), key=lambda x: abs(x - target))

    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        size = len(nums)
        closest = float('inf')
        minimal = float('inf')

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    total = sum([nums[i], nums[j], nums[k]])
                    tmt = abs(total - target)
                    if tmt < minimal:
                        closest = total
                        minimal = tmt
                        if not tmt:
                            return closest
        return closest

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(size - 2):
            j, k = i + 1, size - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == target:
                    return total

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1

        return closest


if __name__ == "__main__":
    # nums, target = [-1, 2, 1, -4], 1
    nums, target = [1, 2, -1, 3, 4, 7, 14, 9], 14  # 14
    # print(Solution().threeSumClosest(nums, target))
    print(
        1000
        * timeit.timeit(
            f"Solution().threeSumClosest({nums}, {target})", number=100000,
            globals=globals()
        ),
        "ms",
    )
