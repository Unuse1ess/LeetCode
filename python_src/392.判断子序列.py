#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        size_s = len(s)
        if size_s == 0:
            return True
        
        for c in t:
            if s[i] == c:
                i += 1
            if i == size_s:
                return True

        return False    
# @lc code=end

class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        size_s, size_t = len(s), len(t)
        if size_s == 0:
            return True
        if size_t == 0:
            return False

        dp = [[-1] * 26 for _ in range(size_t)]
        a = ord('a')

        dp[size_t - 1][ord(t[size_t - 1]) - a] = size_t - 1
        
        for i in range(size_t - 2, -1, -1):
            for j in range(0, 26):
                if j == ord(t[i]) - a:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]
        
        k = 0
        for i in range(size_s):
            j = ord(s[i]) - a
            if dp[k][j] == -1:
                return False
            k = dp[k][j] + 1
            if k >= size_t:
                break

        if i != size_s - 1:
            return False
        return True
            
s = Solution()
print(s.isSubsequence(s = "abc", t = "ahbgdc"))
print(s.isSubsequence(s = "axc", t = "ahbgdc"))
print(s.isSubsequence(s = "", t = "ahbgdc"))
