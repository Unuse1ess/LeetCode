#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size_s = len(s)
        size_t = len(t)

        hist = {}
        for c in t:
            hist[c] = hist.get(c, 0) + 1

        MAX = 1000000
        ans_l = 0
        ans_cnt = MAX
        char_cnt = 0

        l, r = 0, 0
        while l < size_s and s[l] not in hist:
            l += 1
        r = l
        while r < size_s:
            if s[r] in hist:
                if hist[s[r]] > 0:
                    char_cnt += 1
                hist[s[r]] -= 1

                if char_cnt == size_t:
                # if all(hist[k] <= 0 for k in hist):
                    tmp = r - l + 1
                    if tmp < ans_cnt:
                        ans_cnt = tmp
                        ans_l = l

                    while l < r:
                        if s[l] in hist:
                            if hist[s[l]] < 0:
                                hist[s[l]] += 1
                            elif hist[s[l]] == 0:
                                tmp = r - l + 1
                                if tmp < ans_cnt:
                                    ans_cnt = tmp
                                    ans_l = l
                                hist[s[l]] += 1
                                l += 1
                                char_cnt -= 1
                                break
                        l += 1
                        
            r += 1

        ans_cnt = ans_cnt if ans_cnt != MAX else 0
        return s[ans_l: ans_l + ans_cnt]

# @lc code=end

s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(s.minWindow(s = "ABBBBBBBBBBC", t = "ABC"))
print(s.minWindow(s = "ABBBBBABBBBC", t = "ABC"))
print(s.minWindow(s = "a", t = "a"))
print(s.minWindow(s = "a", t = "aa") == "")
print(s.minWindow(s = "a", t = "b") == "")
