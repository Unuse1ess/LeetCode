#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

class Solution0:
    def strStr(self, haystack: str, needle: str) -> int:
        h_size, n_size = len(haystack), len(needle)
        if h_size < n_size:
            return -1
        
        for i in range(h_size - n_size + 1):
            if haystack[i : i + n_size] == needle:
                return i
        return -1

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_n = len(needle)
        size_h = len(haystack)
        if size_n > size_h:
            return -1

        kmp = [0 for _ in needle]
        
        for i in range(1, size_n):
            j = kmp[i - 1]
            while j > 0 and needle[i] != needle[j]:
                j = kmp[j - 1]
            kmp[i] = j + (1 if needle[i] == needle[j] else 0)
    
        kmp0 = 0
        for i in range(0, size_h):
            j = kmp0
            while j > 0 and haystack[i] != needle[j]:
                j = kmp[j - 1]
            kmp0 = j + (1 if haystack[i] == needle[j] else 0)
            if kmp0 == size_n:
                return i - size_n + 1

        return -1
# @lc code=end

s = Solution()
print(s.strStr(haystack = "sadbutsad", needle = "sad"))
print(s.strStr(haystack = "leetcode", needle = "leeto"))
print(s.strStr(haystack = "ssassassd", needle = "ssassd"))
print(s.strStr(haystack = "ssassassd", needle = "aooaoa"))
print(s.strStr(haystack = "ssassassd", needle = "ssassassd"))
