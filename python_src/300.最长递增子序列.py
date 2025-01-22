#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from typing import *

class Solution0:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp: List[int] = [1] * n
        ret = 1

        for i in range(1, n):
            tmp = 0
            for j in range(i):
                if dp[j] > tmp and nums[j] < nums[i]:
                    tmp = dp[j]
            dp[i] = tmp + 1
            if dp[i] > ret: ret = dp[i]
        # return dp[n - 1]
        return ret

# 尽可能慢地让子序列增长。
# 维护数组d[i]，表示长度为i的子序列右端的最小值。
# 二分查找满足d[i] < num < d[i + 1]，替换d[i + 1]，并不影响结果（如果num < d[-1]），
# 因为当num替换了d[-1]时前面的替换才生效（在目前求得的子序列中），否则还是原来的子序列。

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d: List[int] = [nums[0]]

        for num in nums:
            if num > d[-1]:
                d.append(num)
            else:
                l, r = 0, len(d) - 1
                while l <= r:
                    mid = (l + r) >> 1
                    if d[mid] < num:
                        l = mid + 1
                    else:
                        r = mid - 1
                d[r + 1] = num

        return len(d)

# @lc code=end

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([0,1,0,3,2,3]))
print(s.lengthOfLIS([7,7,7,7,7,7,7]))

## 6
print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))


