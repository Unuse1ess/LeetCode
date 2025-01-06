#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
from typing import *

# @lc code=start
class Trie:
    a = ord('a')
    def __init__(self):
        self.child: List[Optional[Trie]] = [None] * 26
        self.is_end = False
        # self.depth = -1

    def add(self, word: str):
        cur = self
        for c in map(lambda x: ord(x) - Trie.a, word):
            if cur.child[c] is None:
                cur.child[c] = Trie()
            cur = cur.child[c]
        cur.is_end = True
        # cur.depth = len(word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = Trie()
        res = set()

        def dfs(i: int, j: int, cur: Optional[Trie], s: List[str]):
            if (not 0 <= i < m) or (not 0 <= j < n):
                return

            if board[i][j] == "#":
                return
            c = board[i][j]
            idx = ord(c) - Trie.a
            if cur.child[idx] is None:
                return

            nxt: Trie = cur.child[idx]
            board[i][j] = "#"
            s.append(c)
            # depth = len(s)
            if nxt.is_end:
                res.add(''.join(s))

            dfs(i, j - 1, nxt, s)
            dfs(i, j + 1, nxt, s)
            dfs(i - 1, j, nxt, s)
            dfs(i + 1, j, nxt, s)

            s.pop()
            board[i][j] = c

        for word in words:
            trie.add(word)
        for i in range(m):
            for j in range(n):
                if trie.child[ord(board[i][j]) - Trie.a] is not None:
                    dfs(i, j, trie, [])
        return list(res)
# @lc code=end

s = Solution()
print(s.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))
print(s.findWords(board = [["a","b"],["c","d"]], words = ["abcb"]))
# ["oa","oaa"]
print(s.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"]))
# ["oath","eat","hklf","hf"]
print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain","hklf", "hf"]))
