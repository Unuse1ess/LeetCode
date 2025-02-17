#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
from typing import *

class ListNode:
    @staticmethod
    def create(l: List[int]) -> "ListNode":
        if len(l) == 0:
            return None
        root = ListNode(l[0])
        node = root
        for i in range(1, len(l)):
            node.next = ListNode(l[i])
            node = node.next
        return root

    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    __repr__ = __str__

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = head
        p = head.next
        prev.next = None
        while p:
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
        return prev
# @lc code=end

s = Solution()
print(s.reverseList(ListNode.create([1,2,3,4,5])))
print(s.reverseList(ListNode.create([1,2])))
print(s.reverseList(ListNode.create([])))
