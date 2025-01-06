#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#
from typing import *
from collections import defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution0:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        node_list: List[Node] = []
        access_list = defaultdict(list)
        cur = head
        i = 0
        while cur:
            node_list.append(Node(cur.val))
            access_list[cur.random].append(i)
            if i > 0:
                node_list[i - 1].next = node_list[i]
            i += 1
            cur = cur.next

        node_list.append(None)

        cur = head
        i = 0
        while cur:
            for k in access_list[cur]:
                node_list[k].random = node_list[i]
            i += 1
            cur = cur.next

        return node_list[0] 

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        cur = head
        new = head.next
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            prev = cur
            cur = cur.next.next
            prev.next.next = cur.next if cur else None

        return new
# @lc code=end

