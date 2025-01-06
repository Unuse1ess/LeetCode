#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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

# preorder: [root, [left],   [right]]
#            ^l1   ^(l1 + 1) ^(l1 + 1 + i - l2)
# inorder: [[left], root, [right]]
#           ^l2     ^i    ^(i + 1)
class Solution:
    def __init__(self):
        self.__cache = dict()
        self.__pre: List[int] = None
    
    def build_subtree(self, l1, r1, l2, r2) -> Optional[TreeNode]:
        if r1 == l1:
            return None
        if r1 - l1 == 1:
            return TreeNode(self.__pre[l1])
        root_val = self.__pre[l1]
        i = self.__cache[root_val]

        root = TreeNode(root_val)
        root.left = self.build_subtree(l1 + 1, l1 + 1 + i - l2, l2, i)
        root.right = self.build_subtree(l1 + 1 + i - l2, r1, i + 1, r2)

        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        size = len(preorder)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(preorder[0])

        for i, n in enumerate(inorder):
            self.__cache[n] = i
        self.__pre = preorder

        return self.build_subtree(0, size, 0, size)
# @lc code=end

s = Solution()
print(s.buildTree([3,9,20,15,7], [9,3,15,20,7]))
print(s.buildTree([1], [1]))
print(s.buildTree([3,9,20,15,7], [9,3,15,20,7]))

