#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, cur_max: int) -> int:
            cnt = 0
            flag = root.val >= cur_max
            if flag: cur_max = root.val
            if root.left:
                cnt += dfs(root.left, cur_max)
            if root.right:
                cnt += dfs(root.right, cur_max)

            return cnt + flag

        return dfs(root, -20000)
        
# @lc code=end

s = Solution()
print(s.goodNodes(TreeNode.create([3,1,4,3,null,1,5])))
print(s.goodNodes(TreeNode.create([3,3,null,4,2])))
print(s.goodNodes(TreeNode.create([1])))
