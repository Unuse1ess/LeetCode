#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
from typing import *
from collections import *

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        queue = [self]
        res = []
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return str(res)
    @staticmethod
    def create(l: List[int | None]) -> "Node":
        if len(l) == 0:
            return None
        root = Node(l[0])
        queue = [root]
        i = 1
        while i < len(l):
            node = queue.pop(0)
            node.left = Node(l[i]) if l[i] else None
            if i + 1 < len(l):
                node.right = Node(l[i + 1]) if l[i + 1] else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 2
        return root

class Solution0:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        queue = deque()
        queue.append((root, 1))
        level = 0
        prev: Node = None
        # dbg = []

        while len(queue) > 0:
            node, l = queue.popleft()
            node: Node
            if node is None:
                continue
            queue.append((node.left, l + 1))
            queue.append((node.right, l + 1))

            if l == level:
                prev.next = node
                # dbg.append(f"{prev.val}->{node.val}")
            else:
                level = l
            prev = node

        # print(dbg)
        return root

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        head = Node(None, next=root)
        con = deque(maxlen=2)
        cur = head
        left_most = root.left if root.left else root.right
        while True:
            if cur is None:
                if left_most is None:
                    break
                cur = left_most
                left_most = None
                con.clear()
                # continue
            if cur.left:
                con.append(cur.left)
                if left_most is None:
                    left_most = cur.left
            if len(con) == 2:
                a = con.popleft()
                a.next = con[0]
                # print(f"{a.val}->{con[0].val}")
            if cur.right:
                con.append(cur.right)
                if left_most is None:
                    left_most = cur.right
            if len(con) == 2:
                a = con.popleft()
                a.next = con[0]
                # print(f"{a.val}->{con[0].val}")
            cur = cur.next
        return root
# @lc code=end

s = Solution()

# print(s.connect(Node.create([1,2,3,4,5,None,7])))
print(s.connect(Node.create([1,2,3,4,5,8,7,None,None,None,None,9,None,None,10])))
