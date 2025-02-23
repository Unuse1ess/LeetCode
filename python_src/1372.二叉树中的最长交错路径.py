#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
#
from typing import *
from utils import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(root: Optional[TreeNode], lflag: Optional[bool], depth: int):
            nonlocal ret
            if depth > ret: ret = depth

            if root.left:
                dfs(root.left, True, 1 if lflag else depth + 1)
            if root.right:
                dfs(root.right, False, 1 if not lflag else depth + 1)

        dfs(root, True, 0)

        return ret
# @lc code=end  

s = Solution()
print(s.longestZigZag(TreeNode.create([1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1])))
print(s.longestZigZag(TreeNode.create([1,1,1,null,1,null,null,1,1,null,1])))
print(s.longestZigZag(TreeNode.create([1])))

## 2
print(s.longestZigZag(TreeNode.create([1,null,1,1,1,null,null,null,1])))
