#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
from typing import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __str__(self):
        queue = deque()
        queue.append(self)
        res = []
        while len(queue) > 0:
            node: TreeNode = queue.popleft()
            res.append(node.val if node else None)
            if node:
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)
        return str(res)
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
            node.left = TreeNode(l[i]) if l[i] else None
            if i + 1 < len(l):
                node.right = TreeNode(l[i + 1]) if l[i + 1] else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 2
        return root

class Solution0:
    def to_linked_list(self, root: TreeNode) -> Tuple[TreeNode]:
        if root is None:
            return None, None
        if root.left is None and root.right is None:
            return root, root

        if root.left:
            _, tail = self.to_linked_list(root.left)
            _, rtail = self.to_linked_list(root.right)
            tail.right = root.right
            if rtail:
                tail = rtail
            root.right = root.left
            root.left = None
        else:
            _, tail = self.to_linked_list(root.right)
        return root, tail

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        root, _ = self.to_linked_list(root)
        
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        cur = root
        while cur:
            if cur.left:
                tmp = cur.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
        print(root)
# @lc code=end

s = Solution()
s.flatten(TreeNode.create([1,2,5,3,4,None,6]))
s.flatten(TreeNode.create([1,2,5,3,4,7,6,None,None,None,None,8]))
s.flatten(TreeNode.create([]))
s.flatten(TreeNode.create([0]))
