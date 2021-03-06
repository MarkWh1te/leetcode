# 53. Maximum Subarray
# Given an integer array nums,
#  find the contiguous subarray (containing at least one number)
#  which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try
#  coding another solution using the divide and conquer approach,
#  which is more subtle.
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        current_sum = float("-inf")
        for i in range(1, len(nums)):
            if current_sum > 0:
                current_sum = current_sum + nums[i]
            else:
                current_sum = nums[i]
            dp[i] = max(current_sum, nums[i])
        return max(dp)

    def maxSubArray2(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.maxSubArray)
    t.equal(6, [-2, 1, -3, 4, -1, 2, 1, -5, 4])
    t = Test(s.maxSubArray2)
    t.equal(6, [-2, 1, -3, 4, -1, 2, 1, -5, 4])
