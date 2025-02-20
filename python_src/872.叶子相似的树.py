#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []

        def dfs1(root: TreeNode, leaf: List[int]):
            if root.left is None and root.right is None:
                leaf.append(root.val)
                return
            if root.left:
                dfs1(root.left, leaf)
            if root.right:
                dfs1(root.right, leaf)
        dfs1(root1, leaf1)

        ret = True
        pos = 0
        def dfs2(root: TreeNode):
            nonlocal ret, pos
            if root.left is None and root.right is None:
                if pos >= len(leaf1) or leaf1[pos] != root.val:
                    ret = False
                    return
                pos += 1
            if root.left and ret:
                dfs2(root.left)
            if root.right and ret:
                dfs2(root.right)
        dfs2(root2)

        return ret and pos == len(leaf1)

# @lc code=end

s = Solution()
print(s.leafSimilar(TreeNode.create([3,5,1,6,2,9,8,null,null,7,4]), TreeNode.create([3,5,1,6,7,4,2,null,null,null,null,null,null,9,8])))
print(s.leafSimilar(TreeNode.create([1,2,3]), TreeNode.create([1,3,2])))


## false
print(s.leafSimilar(TreeNode.create([3,5,1,6,7,4,2,null,null,null,null,null,null,9,11,null,null,8,10]), TreeNode.create([3,5,1,6,2,9,8,null,null,7,4])))