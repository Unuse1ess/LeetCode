#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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


class Solution0:
    def dfs(self):
        while len(self.__node) > 0:
            cur = self.__node[-1]
            if cur[1] == 0:
                cur[1] = 1
                if cur[0].left:
                    self.__node.append([cur[0].left, 0])
            elif cur[1] == 1:
                self.__node.pop()
                if cur[0].right:
                    self.__node.append([cur[0].right, 0])
                self.__operand.append(cur[0].val)
                if len(self.__operand) == 2:
                    diff = abs(self.__operand[0] - self.__operand[1])
                    if diff < self.__diff:
                        self.__diff = diff

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.__diff = 1000000
        self.__node: List[List[TreeNode]] = [[root, 0]]
        self.__operand: Deque[int] = deque(maxlen=2)
        self.__operand.append(2000000)
        self.dfs()
        
        return self.__diff
    
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self):
        while len(self.__stack) > 0 or self.__cur:
            if self.__diff == 1:
                return
            while self.__cur:
                self.__stack.append(self.__cur)
                self.__cur = self.__cur.left
            self.__cur = self.__stack.pop()
            diff = abs(self.__prev.val - self.__cur.val)
            if diff < self.__diff:
                self.__diff = diff

            self.__prev = self.__cur
            self.__cur = self.__cur.right

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.__diff = 10000000
        self.__cur: TreeNode = root
        self.__prev = TreeNode(2000000)
        self.__stack: List[TreeNode] = []
        # self.__operand: Deque[int] = deque(maxlen=2)
        # self.__operand.append(2000000)
        self.dfs()
        
        return self.__diff
# @lc code=end

s = Solution()
print(s.getMinimumDifference(TreeNode.create([4,2,6,1,3])))
print(s.getMinimumDifference(TreeNode.create([1,0,48,None,None,12,49])))
