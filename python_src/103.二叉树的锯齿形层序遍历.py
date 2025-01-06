#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        queue: Deque[Tuple[TreeNode]] = deque()
        queue.append([root, 0])
        level = 0
        res = []
        level_node = []
        flag = 0
        while len(queue) > 0:
            node, l = queue.popleft()
            if node.left:
                queue.append([node.left, l + 1])
            if node.right:
                queue.append([node.right, l + 1])
            if l != level:
                level = l
                if flag == 1:
                    level_node.reverse()
                res.append(level_node)
                level_node = []
                flag ^= 1
            level_node.append(node.val)
        
        
        if flag == 1:
            level_node.reverse()
        res.append(level_node)
        return res

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    push = ["append", "appendleft"]
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        
        queue: Deque[Tuple[TreeNode]] = deque()
        queue.append([root, 0])
        level = 0
        res = []
        level_node = deque()
        flag = 0
        while len(queue) > 0:
            node, l = queue.popleft()
            if node.left:
                queue.append([node.left, l + 1])
            if node.right:
                queue.append([node.right, l + 1])
            if l != level:
                level = l
                res.append(list(level_node))
                level_node = deque()
                flag ^= 1
            getattr(level_node, Solution.push[flag])(node.val)

        res.append(list(level_node))
        return res
# @lc code=end

s = Solution()
print(s.zigzagLevelOrder(TreeNode.create([3,9,20,None,None,15,7])))
print(s.zigzagLevelOrder(TreeNode.create([1])))
print(s.zigzagLevelOrder(TreeNode.create([1,2,3,4,None,None,5,6,None,None,7,8])))
