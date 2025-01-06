#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
from typing import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        queue = deque()
        queue.append(self)
        res = []
        while len(queue) > 0:
            node: TreeNode = queue.popleft()
            res.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        
        while res[-1] is None:
            res.pop()
        return str(res)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dq(l: int, r: int) -> Optional[TreeNode]:
            if l > r: return None
            mid = (l + r) >> 1
            node = TreeNode(nums[mid])
            node.left = dq(l, mid - 1)
            node.right = dq(mid + 1, r)

            return node

        return dq(0, len(nums) - 1)
        
# @lc code=end

s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))
print(s.sortedArrayToBST([1,3]))
print(s.sortedArrayToBST(list(range(10))))
