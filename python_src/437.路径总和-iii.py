#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
from typing import *
from collections import *
from utils import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        note = defaultdict(int)
        note[0] = 1
        def dfs(root: Optional[TreeNode], p_sum: int) -> int:
            if root is None:
                return 0

            p_sum += root.val
            cnt = note[p_sum - targetSum]
            note[p_sum] += 1
            cnt += dfs(root.left, p_sum)
            cnt += dfs(root.right, p_sum)
            note[p_sum] -= 1

            return cnt

        return dfs(root, 0)
        
# @lc code=end

s = Solution()
print(s.pathSum(TreeNode.create([10,5,-3,3,2,None,11,3,-2,None,1]), 8))
print(s.pathSum(TreeNode.create([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))

## 0
print(s.pathSum(None, 1))

## 0
print(s.pathSum(TreeNode.create([1]), 0))
