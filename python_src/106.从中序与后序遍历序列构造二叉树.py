#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
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

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder: [[left], root, [right]]
#           ^l1     ^i    ^(i + 1)
# postorder: [[left], [right],        root]
#             ^l2     ^(l2 + i - l1)  ^(r2 - 1)
class Solution:
    def __init__(self):
        self.__cache = dict()
        self.__post = None

    def build_subtree(self, l1, r1, l2, r2) -> Optional[TreeNode]:
        if r2 - l2 == 0:
            return None
        if r2 - l2 == 1:
            return TreeNode(self.__post[r2 - 1])
        root_val = self.__post[r2 - 1]
        i = self.__cache[root_val]
        root = TreeNode(root_val)
        root.left = self.build_subtree(l1, i, l2, l2 + i - l1)
        root.right = self.build_subtree(i + 1, r1, l2 + i - l1, r2 - 1)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        size = len(inorder)
        if size == 1:
            return TreeNode(inorder[0])
        
        for i, n in enumerate(inorder):
            self.__cache[n] = i
        self.__post = postorder
        
        return self.build_subtree(0, size, 0, size)
# @lc code=end

s = Solution()
print(s.buildTree([9,3,15,20,7], [9,15,7,20,3]))
print(s.buildTree([-1], [-1]))