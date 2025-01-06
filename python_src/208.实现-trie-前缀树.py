#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
from typing import *
from collections import *

# @lc code=start
class Trie:
    def __init__(self):
        # self.words = defaultdict(list)
        self.words = set()
        self.prefix = set()

    def insert(self, word: str) -> None:
        if word in self.words: return

        slen = len(word)
        i = 1
        while i < slen:
            # if word[:i] not in self.words:
            # self.words[word[:i]].append
            self.prefix.add(word[:i])
            i += 1
        self.words.add(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix or prefix in self.words

# @lc code=end
class Trie0:
    def __init__(self):
        self.next: Optional[DefaultDict[str, Trie]] = None
        self.is_end = False

    def insert(self, word: str) -> None:
        if len(word) > 0:
            if self.next is None:
                self.next = defaultdict(Trie)
            self.next[word[0]].insert(word[1:])
            # self.is_end |= len(word) == 1
        else:
            self.is_end = True

    def search(self, word: str) -> bool:
        cur = self
        wlen = len(word)
        i = 0
        while cur.next and i < wlen:
            cur = cur.next[word[i]]
            i += 1
        return cur.is_end and i == wlen
        # if len(word) == 1:
        #     return self.is_end and self.next and word in self.next
        # c = word[0]
        # if c not in self.next:
        #     return False
        # return self.next[c].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        cur = self
        wlen = len(prefix)
        i = 0
        while cur.next and i < wlen:
            cur = cur.next[prefix[i]]
            i += 1

        return i == wlen
        # if len(prefix) == 1:
        #     return prefix in self.next
        # c = prefix[0]
        # if c not in self.next:
        #     return False

        # return self.next[c].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

    instance: 'Trie' = None

    @staticmethod
    def Trie_():
        Trie.instance = Trie()

    insert_ = lambda *args: Trie.instance.insert(*args)
    search_ = lambda *args: Trie.instance.search(*args)
    startsWith_ = lambda *args: Trie.instance.startsWith(*args)

def run(methods: List[str], params: List[str]):
    print([getattr(Trie, m)(*p) for m, p in zip(map(lambda x: x + "_", methods), params)])

run(["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]])

run(["Trie","insert","search","startsWith"],
[[],["a"],["a"],["a"]])

run(["Trie","insert","search","startsWith"],
[[],["ab"],["a"],["a"]])

run(["Trie","search"],
[[],["a"]])

run(["Trie","startsWith"],
[[],["a"]])

# run(["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"],
# [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]])

run(["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search"],
[[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"]])