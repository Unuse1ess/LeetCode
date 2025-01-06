#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
from typing import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

    def __str__(self):
        queue = deque()
        queue.append(self)
        res = []
        while len(queue) > 0:
            node: TreeNode = queue.popleft()
            res.append(node.val if node else None)
            if node:
                # if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)
        
        while res[-1] is None:
            del res[-1]
        return str(res)

    def __repr__(self):
        return str(self)
    @staticmethod
    def create(l: List[int | None]) -> "TreeNode":
        if len(l) == 0:
            return None
        root = TreeNode(l[0])
        queue = deque()
        queue.append(root)
        i = 1
        while i < len(l):
            node: TreeNode = queue.popleft()
            node.left = TreeNode(l[i]) if l[i] is not None else None
            if i + 1 < len(l):
                node.right = TreeNode(l[i + 1]) if l[i + 1] is not None else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 2
        return root

class Solution0:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root: TreeNode, bits: int, h: int) -> bool:
        cur = root
        h -= 1
        while cur and h > 0:
            h -= 1
            if (bits >> h) & 1 == 1:
                cur = cur.right
            else:
                cur = cur.left
        return cur is not None
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        h = 0
        cur = root
        while cur:
            cur = cur.left
            h += 1
        
        l, r = 1 << (h - 1), (1 << h) - 1
        flag = None
        while l < r:
            mid = (l + r) >> 1
            flag = self.find(root, mid, h)
            if flag:
                l = mid + 1
            else:
                r = mid - 1
        
        return l - (0 if self.find(root, l, h) else 1)
            
# @lc code=end

s = Solution()
for i in range(1001):
    assert s.countNodes(TreeNode.create([j for j in range(i)])) == i
