#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
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
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
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
        # print(root)
        return root

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_eq(p: TreeNode, q: TreeNode | None) -> bool:
        if q is None:
            return False
        return p.val == q.val and p.left == q.left and p.right == q.right
    
    TreeNode.__eq__ = tree_eq
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return p == q
# @lc code=end

s = Solution()
print(s.isSameTree(TreeNode.create([1,2,3]), TreeNode.create([1,2,3])))
print(s.isSameTree(TreeNode.create([1,2]), TreeNode.create([1,None,2])))
print(s.isSameTree(TreeNode.create([1,None,2]), TreeNode.create([1,None,2])))
print(s.isSameTree(TreeNode.create([1,2,1]), TreeNode.create([1,1,2])))
print(s.isSameTree(TreeNode.create([]), TreeNode.create([1])))
print(s.isSameTree(TreeNode.create([1]), TreeNode.create([])))
print(s.isSameTree(TreeNode.create([]), TreeNode.create([])))
