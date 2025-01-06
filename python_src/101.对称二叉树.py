#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    TreeNode.__eq__ = tree_eq
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root.left == self.invertTree(root.right)
# @lc code=end

