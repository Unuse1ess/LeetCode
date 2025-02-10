#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
from typing import *

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        if N == 1: return 1

        ret = 0
        pos = 0

        l, r = 0, 0
        while r < N:
            while r < N and chars[l] == chars[r]:
                r += 1
            cnt = r - l
            chars[pos] = chars[l]
            pos += 1
            if cnt > 1:
                dig = list(str(cnt))
                dig_len = len(dig)
                chars[pos: pos + dig_len] = dig
                pos += dig_len
                ret += dig_len
            ret += 1

            l = r

        return ret
# @lc code=end

s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

print(s.compress(list("abcdefg")))
