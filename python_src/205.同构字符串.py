#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

class Solution0:
    def isIsomorphic(self, s: str, t: str) -> bool:
        size = len(s)
        m = {}
        n = {}
        for i in range(size):
            if s[i] in m and m[s[i]] != t[i]:
                return False
            # if s[i] in n and n[s[i]] != t[i]:
            #     return False
            # if t[i] in m and m[t[i]] != s[i]:
            #     return False
            if t[i] in n and n[t[i]] != s[i]:
                return False
            m[s[i]] = t[i]
            n[t[i]] = s[i]
        return True

class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        size = len(s)
        s_t = [0 for _ in range(128)]
        t_s = [0 for _ in range(128)]
        ret = 0
        for i in range(size):
            cs = ord(s[i])
            ct = ord(t[i])
            # if s_t[cs] != 0 and s_t[cs != ct:
            #     return False
            # if t_s[ct] != 0 and t_s[ct] != cs:
            #     return False
            ret += s_t[cs] != 0 and s_t[cs] != ct
            ret += t_s[ct] != 0 and t_s[ct] != cs
            s_t[cs] = ct
            t_s[ct] = cs
        return ret == 0

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(t)) == len(set(s)) == len(set(zip(s, t)))
# @lc code=end

s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("badc", "baba"))
