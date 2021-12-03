#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List
import math

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0, 0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        t = 0
        for i, _ in enumerate(nums):
            if i < 2:
                continue
            t = max(nums[i] + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = t
        return t
# @lc code=end


s = Solution()
assert s.rob([1]) == 1
assert s.rob([1, 2]) == 2
assert s.rob([1, 2, 3]) == 4

