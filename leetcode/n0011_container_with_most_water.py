import timeit
from typing import List


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        mx = 0
        lnh = len(height)
        for i in range(lnh):
            l = height[i]
            for j in range(i + 1, lnh):
                w = j - i
                r = height[j]

                a = min(l, r) * w

                if a > mx:
                    mx = a

        return mx

    def maxArea2(self, height: List[int]) -> int:
        max_area, l, r = 0, 0, len(height) - 1

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

    def maxArea(self, height: List[int]) -> int:
        size = len(height)

        # two pointers, left init as 0, right init as size-1
        left, right = 0, size - 1

        # maximal width between leftmost stick and rightmost stick
        max_width = size - 1

        # area also known as the amount of water
        area = 0

        # trade-off between width and height
        # scan each possible width and compute maximal area
        for width in range(max_width, 0, -1):

            if height[left] < height[right]:
                # the height of lefthand side is shorter
                area = max(area, width * height[left])

                # update left index to righthand side
                left += 1

            else:
                # the height of righthand side is shorter
                area = max(area, width * height[right])

                # update right index to lefthand side
                right -= 1

        return area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # print(timeit.timeit(f"Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])",
    #                     number=100,
    #                     globals=globals()))
