#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
from typing import *

# Definition for singly-linked list.
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head = ListNode(None, head)
        cur = head
        i = -1
        while cur:
            i += 1
            if i == left:
                start = prev
            elif left < i <= right:
                fol = cur.next
                cur.next = prev
                prev = cur
                cur = fol

                if i == right:
                    start.next.next = cur
                    start.next = prev
                    break
                else:
                    continue

            prev = cur
            cur = cur.next
        return head.next
# @lc code=end

s = Solution()
print(s.reverseBetween(ListNode.create([1,2,3,4,5]), 2, 4))
print(s.reverseBetween(ListNode.create([1,2,3,4,5]), 1, 3))
print(s.reverseBetween(ListNode.create([1,2,3,4,5]), 1, 2))
print(s.reverseBetween(ListNode.create([1,2,3,4,5]), 5, 5))
print(s.reverseBetween(ListNode.create([5]), 1, 1))
