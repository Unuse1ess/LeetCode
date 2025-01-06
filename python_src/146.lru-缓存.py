#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
from typing import *
from itertools import *
from functools import *

def debug(func):
    def __inner(*args):
        self = args[0]
        LRUCache.attr = "next"
        print(self.head)
        LRUCache.attr = "prev"
        print(self.tail)
        ret = func(*args)
        LRUCache.attr = "next"
        print(self.head)
        LRUCache.attr = "prev"
        print(self.tail)
        print('--' * 40)
        return ret
    return __inner

# @lc code=start
class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev: ListNode = prev
        self.next: ListNode = next

    # def __str__(self) -> str:
        # return f"{self.val}->{getattr(self, LRUCache.attr)}"

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.data = dict()
        self.cnt = 0
        self.capacity = capacity

    def __insert_head(self, node: ListNode):
        node.next = self.head.next
        node.prev = None
        if self.head.next:
            self.head.next.prev = node
        else:
            self.tail.prev = node
        self.head.next = node

    def __remove_node(self, node: ListNode | None) -> ListNode:
        if node is None:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail.prev = node.prev
        node.prev = None
        node.next = None

    # @debug
    def get(self, key: int) -> int:
        ret = -1
        if key in self.data:
            node: ListNode = self.data[key]
            ret = node.val
            self.__remove_node(node)
            self.__insert_head(node)
        return ret
    # @debug
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node: ListNode = self.data[key]
            self.__remove_node(node)
        else:
            if self.cnt == self.capacity:
                _key = self.tail.prev.key
                self.__remove_node(self.tail.prev)
                del self.data[_key]
            else:
                self.cnt += 1
            node = ListNode(key)

        node.val = value
        self.__insert_head(node)
        self.data[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

    attr = "prev"
    instance = None
    get_ = lambda key: LRUCache.instance.get(key)
    put_ = lambda key, value: LRUCache.instance.put(key, value)
    @staticmethod
    def LRUCache_(capacity: int):
        LRUCache.instance = LRUCache(capacity)

def run(methods: List[str], params: List[List[int]]):
    print(
        list(
            map(
                lambda m, p: getattr(LRUCache, m)(*p),
                map(lambda x: x + '_', methods),
                params
            )
        )
    )

methods = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
run(methods, params)

methods = ["LRUCache","put","get"]
params = [[1],[2,1],[2]]
run(methods, params)

methods = ["LRUCache","put","get","put","get","get"]
params = [[1],[2,1],[2],[3,2],[2],[3]]
run(methods, params)

methods = ["LRUCache","put","put","get","put","put","get"]
params = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
run(methods, params)