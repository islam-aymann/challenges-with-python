from typing import List


class Solution:
    def findMedianSortedArrays1(self,
                                nums1: List[int],
                                nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if l % 2:
            return nums[l // 2]

        return (nums[l // 2 - 1] + nums[l // 2]) / 2

    def findMedianSortedArrays(self,
                               nums1: List[int],
                               nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2


if __name__ == '__main__':
    nums1 = [23, 26, 31, 35]
    nums2 = [3, 5, 7, 9, 11, 16]
    # nums1 = [1, 3, 8, 9, 15]
    # nums2 = [7, 11, 18, 19, 21, 25]

    print(Solution().findMedianSortedArrays(nums1, nums2))
    # print(Solution().findMedianSortedArrays1(nums1, nums2))
    # print(timeit.timeit(f"Solution().findMedianSortedArrays({nums1}, {nums2})",
    #                     number=1000,
    #                     globals=globals()))
