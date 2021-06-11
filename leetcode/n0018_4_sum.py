from typing import List


class Solution:
    def threeSum(self, nums: List[int], target: int, new_target: int) -> List[
        List[int]]:

        size = len(nums)
        if size < 3:
            return []

        results = []
        for i in range(size - 2):
            j = i + 1
            k = size - 1
            while j < k:
                items = [nums[i], nums[j], nums[k]]
                total = sum(items)

                if total == new_target and items not in results:
                    results.append([target] + items)
                    j += 1
                    k -= 1

                if total < new_target:
                    j += 1
                elif total > new_target:
                    k -= 1

        return results

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:  # 81 ms
        nums.sort()

        results = []
        results_set = []
        for i, num in enumerate(nums):
            three_sum = self.threeSum(nums[:i] + nums[i + 1:], num, target - nums[i])

            for j in three_sum:
                if set(j) not in results_set:
                    results_set.append(set(j))
                    results.append(j)

        return results

    # def fourSum3(self, nums: List[int], target: int) -> List[List[int]]:
    #     nums.sort()
    #     size = len(nums)
    #
    #     results = []
    #     results_set = []
    #
    #     for i in range(size - 3):
    #         j = i + 1
    #         l = size - 1
    #         while j < l - 1:
    #             k = j + 1
    #             while j < k < l:
    #                 items = [nums[i], nums[j], nums[k], nums[l]]
    #                 items_set = set(items)
    #                 total = sum(items)
    #
    #                 if total == target:
    #                     if items_set not in results_set:
    #                         results.append(items)
    #                         results_set.append(items_set)
    #                     break
    #
    #                 if total > target:
    #                     k -= 1
    #
    #                 elif total < target:
    #                     k += 1
    #
    #             if k == j:
    #                 l -= 1
    #             else:
    #                 j += 1
    #
    #     return results

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find_n_sum(nums, target, N, current):
            size = len(nums)
            # if minimum possible sum (every element is first element) > target
            if size < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                return  # or maximum possible sum (every element is first element) <
                # target, it's impossible to get target anyway

            if N == 2:  # 2-sum problem
                l, r = 0, size - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(current + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # reduce to N-1 sum problem
                for i in range(size - N + 1):
                    if i == 0 or nums[i - 1] != nums[i]:
                        find_n_sum(nums[i + 1:], target - nums[i], N - 1, current + [nums[i]])

        results = []
        find_n_sum(sorted(nums), target, 4, [])
        return results


if __name__ == "__main__":
    # nums, target = [1, 0, -1, 0, -2, 2], 0
    # nums, target = [2, 2, 2, 2, 2], 8
    nums, target = [-3, -1, 0, 2, 4, 5], 2
    print(Solution().fourSum(nums, target))
    # print(
    #     1000
    #     * timeit.timeit(
    #         f"Solution().fourSum({nums}, {target})", number=5000,
    #         globals=globals()
    #     ),
    #     "ms",
    # )
