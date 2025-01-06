#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
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
        return str(self.val)
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

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, k: int) -> int:
        while len(self.__stack) > 0 or self.__cur:
            while self.__cur:
                self.__stack.append(self.__cur)
                self.__cur = self.__cur.left
            self.__cur = self.__stack.pop()
            self.__cnt += 1
            if self.__cnt == k:
                return self.__cur.val
            self.__cur = self.__cur.right
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.__cnt = 0
        self.__cur: TreeNode = root
        self.__stack: List[TreeNode] = []

        return self.dfs(k)
        
# @lc code=end

s = Solution()
print(s.kthSmallest(TreeNode.create([3,1,4,None,2]), 1))
print(s.kthSmallest(TreeNode.create([5,3,6,2,4,None,None,1]), 3))
