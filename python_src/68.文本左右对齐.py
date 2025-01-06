#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from typing import *

# @lc code=start
class Solution:
    def lineJustify(self, words: List[str], width: int, maxWidth: int) -> str:
        size = len(words)
        if size == 1:
            return words[0] + ' ' * (maxWidth - len(words[0]))
        if width == maxWidth:
            return ' '.join(words)

        space = maxWidth - width
        b = 1 + space // (size - 1)
        o = space % (size - 1)
        ret = ''
        for i, s in enumerate(words):
            ret += s + ' ' * (b + (1 if i < o else 0))
        return ret.rstrip(' ')

    def leftJustify(self, words: List[str], maxWidth: int) -> str:
        ret = ' '.join(words)
        pad = maxWidth - len(ret)
        return ret + ' ' * pad

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        line = [words[0]]
        width = len(words[0])
        cnt = 1

        for s in words[1:]:
            cnt += 1
            size_s = len(s)
            width += size_s + 1

            if width > maxWidth:
                ret.append(self.lineJustify(line, width - size_s - 1, maxWidth))
                line.clear()
                width = size_s
                cnt = 1
            # elif width == maxWidth:
            #     ret.append(' '.join(line))
            #     line = [s]
            #     width = size_s
            #     cnt = 1

            line.append(s)

        ret.append(self.leftJustify(line, maxWidth))
        return ret
# @lc code=end

s = Solution()
print('|\n'.join(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)))
print('|\n'.join(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)))
print('|\n'.join(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)))
