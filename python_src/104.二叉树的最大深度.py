#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def create(l: List[int | None]) -> "TreeNode":
        if len(l) == 0:
            return None
        root = TreeNode(l[0])
        queue = [root]
        i = 1
        while i < len(l):
            node = queue.pop(0)
            node.left = TreeNode(l[i]) if l[i] else None
            if i + 1 < len(l):
                node.right = TreeNode(l[i + 1]) if l[i + 1] else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 2
        return root

class Solution0:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [(root, 1)]
        cnt = 1
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if depth > cnt:
                cnt = depth
            if node:
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return cnt - 1

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)

        return l if l > r else r
        # return max(l, r)
# @lc code=end

s = Solution()
print(s.maxDepth(TreeNode.create([3,9,20,None,None,15,7])))
print(s.maxDepth(TreeNode.create([1,1,None,1,None,1,None])))
print(s.maxDepth(TreeNode.create([1,None,2])))
