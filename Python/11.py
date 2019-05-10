# 11. Container With Most Water

# Share
# Given n non-negative integers a1, a2, ..., an ,
#  where each represents a point at coordinate (i, ai).
#  n vertical lines are drawn
#  such that the two endpoints of line i is at (i, ai)
#  and (i, 0).
#  Find two lines,
#  which together with x-axis forms a container,
#  such that the container contains the most water.

# ..--...........................................................................

# ...-..........==.......................................+W*.....................

# ..--..........==.......................................+W*.....................

# ...-..........==:::::::::::::::::::::::::::::::::::::::*W=:::::::::::::+=+.....

# ..--..........==:::::::::::::::::::::::::::::::::::::::*W=:::::::::::::+=+.....

# ...-..........==:::::::*W=:::::::::::::::::::::::::::::*W=:::::::::::::+=+.....

# ..--..........==:::::::*W=:::::::::::::::::::::::::::::*W=:::::::::::::+=+.....

# ...-..........==:::::::*W=:::::::::::::*W=:::::::::::::*W=:::::::::::::+=+.....

# ..---.........==:::::::*W=:::::::::::::*W=:::::::::::::*W=:::::::::::::+=+.....

# ...-..........==:::::::*W=:::::::::::::*W=:::::*W=:::::*W=:::::::::::::+=+.....

# .----.........==:::::::*W=:::::::::::::*W=:::::*W=:::::*W=:::::::::::::+=+.....

# ...-..........==:::::::*W=:::::::::::::*W=:::::*W=:::::*W=:::::*W=:::::+=+.....

# .---..........==:::::::*W=:::::::::::::*W=:::::*W=:::::*W=:::::*W=:::::+=+.....

# ...-..........==:::::::*W=:::::*W=:::::*W=:::::*W=:::::*W=:::::*W=:::::+=+.....

# ..--..........==:::::::*W=:::::*W=:::::*W=:::::*W=:::::*W=:::::*W=:::::+=+.....

# ...-...=W:....==:::::::*W=:::::*W=:::::*W=:::::*W=:::::*W=:::::*W=:::::+=+.....

# .------=W+----==:::::::*W=:::::=W=:::::*W=:::::=W=:::::=W=:::::=W=:::::*=+-----

# Note: You may not slant the container and n is at least 2.
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            result = max(result, h * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.maxArea)
    t.equal(49, [1, 8, 6, 2, 5, 4, 8, 3, 7])
