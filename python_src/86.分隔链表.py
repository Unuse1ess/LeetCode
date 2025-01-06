#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    def __str__(self) -> str:
        return f"{self.val}->{self.next}"

    @staticmethod
    def create(l: List[int]) -> "ListNode":
        head = ListNode(None)
        cur = head
        for i in l:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        left = ListNode(None)
        right = ListNode(None)
        cur = head
        l, r = left, right
        while cur:
            fol = cur.next
            if cur.val < x:
                l.next = cur
                cur.next = None
                l = cur
            else:
                r.next = cur
                cur.next = None
                r = cur
            cur = fol

        l.next = right.next

        return left.next
# @lc code=end

s = Solution()
print(s.partition(ListNode.create([1,4,3,2,5,2]), 3))
print(s.partition(ListNode.create([2,1]), 2))
print(s.partition(ListNode.create([10,9,8,1,2,3]), 5))
