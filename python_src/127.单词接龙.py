#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
from typing import *
from collections import *

class Solution0:
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wlen = len(beginWord)
        bank = set(wordList)
        if endWord not in bank: return 0
        if wlen == 1: return 2

        chekced = set()
        queue = deque()
        queue.append((beginWord, 1))
        while len(queue) > 0:
            s, step = queue.popleft()
            for i in range(wlen):
                # for j in letters[i]:
                for j in Solution0.letters:
                    if s[i] == j: continue
                    tmp = s[:i] + j + s[i + 1:]
                    if tmp == endWord:
                        return step + 1
                    elif tmp in bank and tmp not in chekced:
                        queue.append((tmp, step + 1))
                        chekced.add(tmp)
        return 0
        
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wlen = len(beginWord)
        if endWord not in wordList: return 0
        if wlen == 1: return 2

        self.cur = 0
        self.word2id = dict()
        self.graph = defaultdict(list)
        self.insert(beginWord)
        for word in wordList:
            self.insert(word)

        visited = set()
        queue = deque()
        queue.append((self.word2id[beginWord], 0))
        end_id = self.word2id[endWord]

        while len(queue) > 0:
            word_id, step = queue.popleft()
            if word_id == end_id:
                return (step >> 1) + 1
            for next_id in self.graph[word_id]:
                if next_id not in visited:
                    queue.append((next_id, step + 1))
                    visited.add(next_id)
        return 0

    def add_word(self, word: str) -> int:
        if word not in self.word2id:
            self.word2id[word] = self.cur
            self.cur += 1
            return self.cur - 1
        return self.word2id[word]

    def insert(self, word: str):
        word_id = self.add_word(word)
        tmp = list(word)
        for i, c in enumerate(word):
            tmp[i] = '*'
            new_word = ''.join(tmp)
            new_id = self.add_word(new_word)
            self.graph[new_id].append(word_id)
            self.graph[word_id].append(new_id)
            tmp[i] = c

# @lc code=end

s = Solution()
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
print(s.ladderLength("hot", "dog", ["hot", "dog"]))
