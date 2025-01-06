#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
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

class BSTIterator0:
    def __init__(self, root: Optional[TreeNode]):
        self.__node: List[List[TreeNode]] = [[root, 0]]
    def next(self) -> int:
        while True:
            cur = self.__node[-1]
            if cur[1] == 0:
                cur[1] = 1
                if cur[0].left:
                    self.__node.append([cur[0].left, 0])
            elif cur[1] == 1:
                self.__node.pop()
                if cur[0].right:
                    self.__node.append([cur[0].right, 0])
                return cur[0].val

    def hasNext(self) -> bool:
        return len(self.__node) != 0


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.__stack: List[TreeNode] = []
        self.__cur: TreeNode = root
    def next(self) -> int:
        while self.__cur:
            self.__stack.append(self.__cur)
            self.__cur = self.__cur.left

        self.__cur = self.__stack.pop()
        ret = self.__cur.val
        self.__cur = self.__cur.right
        return ret

    def hasNext(self) -> bool:
        return self.__cur is not None or len(self.__stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

    instance = None
    
    @staticmethod
    def BSTIterator_(l: List[int]):
        BSTIterator.instance = BSTIterator(TreeNode.create(l))

    next_ = lambda: BSTIterator.instance.next()
    hasNext_ = lambda: BSTIterator.instance.hasNext()

def run(methods, params):
    print(list(
        getattr(BSTIterator, m)(*p) for m, p in zip(
            map(lambda x: x + "_", methods),
            params
        )
    ))

methods = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
params = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
run(methods, params)
