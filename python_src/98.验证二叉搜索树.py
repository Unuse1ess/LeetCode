#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.__cur: TreeNode = root
        self.__operand: Deque[TreeNode] = deque(maxlen=2)
        self.__stack: List[TreeNode] = []

        return self.dfs()
    
    def dfs(self) -> bool:
        while len(self.__stack) > 0 or self.__cur:
            while self.__cur:
                self.__stack.append(self.__cur)
                self.__cur = self.__cur.left
            self.__cur = self.__stack.pop()
            self.__operand.append(self.__cur.val)
            if len(self.__operand) == 2 and self.__operand[0] >= self.__operand[1]:
                return False
            self.__cur = self.__cur.right

        return True
# @lc code=end

s = Solution()
print(s.isValidBST(TreeNode.create([5,1,4,None,None,3,6])))
print(s.isValidBST(TreeNode.create([2,1,3])))
print(s.isValidBST(TreeNode.create([5,4,6,None,None,3,7])))
