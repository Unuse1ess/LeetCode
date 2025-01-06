#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
        return str(self)
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        queue: Deque[Tuple[TreeNode]] = deque()
        queue.append([root, 0])
        level = 0
        res = []
        prev = root
        while len(queue) > 0:
            node, l = queue.popleft()
            if node.left:
                queue.append([node.left, l + 1])
            if node.right:
                queue.append([node.right, l + 1])
            if l != level:
                level = l
                res.append(prev.val)
            prev = node
        res.append(prev.val)
        return res
# @lc code=end

s = Solution()
print(s.rightSideView(TreeNode.create([1,2,3,None,5,None,4])))
print(s.rightSideView(TreeNode.create([1,2,3,4,None,None,None,5])))
print(s.rightSideView(TreeNode.create([])))
print(s.rightSideView(TreeNode.create([1,None,3])))
