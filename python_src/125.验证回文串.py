#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        l, r = 0, size - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            # print(s[l], s[r])
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# @lc code=end

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("0P"))
print(s.isPalindrome(" "))
