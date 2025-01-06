#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
from typing import *
from collections import *
from itertools import *


# @lc code=start
class Trie:
    a = ord('a')
    def __init__(self):
        # self.child: DefaultDict[str, Optional[Trie]] = defaultdict(lambda: None)
        self.child: List[Optional[Trie]] = [None] * 26
        self.is_end = False

    def add(self, word: str):
        cur = self
        for c in map(lambda x: ord(x) - Trie.a, word):
            if cur.child[c] is None:
                cur.child[c] = Trie()
            cur = cur.child[c]
        cur.is_end = True
            

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        wlen = len(word)
        def dfs(node: Trie, index: int):
            if wlen == index:
                return node.is_end
            c = word[index]
            if c == ".":
                for k in range(26):
                    if node.child[k] and dfs(node.child[k], index + 1):
                        return True
            else:
                c = ord(c) - Trie.a
                if node.child[c] and dfs(node.child[c], index + 1):
                    return True
            return False

        return dfs(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

    instance: 'WordDictionary' = None
    
    @staticmethod
    def WordDictionary_():
        WordDictionary.instance = WordDictionary()

    addWord_ = lambda *args: WordDictionary.instance.addWord(*args)
    search_ = lambda *args: WordDictionary.instance.search(*args)

def run(methods: List[str], params: List[str]):
    print([getattr(WordDictionary, m)(*p) for m, p in zip(map(lambda x: x + "_", methods), params)])

# run(["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]])

# run(["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
# [[],["baby"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.b."]])

# run(["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
# [[],["baby"],["dad"],["mad"],["pad"],["bad"],[".ad"],[".b.b"]])

# [null,null,null,true,true,false,true,false,false]
run(["WordDictionary","addWord","addWord","search","search","search","search","search","search"],
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]])

# [null,null,null,true,true,true,false,true,false,true,true]
run(["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"],
[[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]])

# [null,null,null,null,null,false,false,null,true,true,false,false,true,false]
run(["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"],
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]])