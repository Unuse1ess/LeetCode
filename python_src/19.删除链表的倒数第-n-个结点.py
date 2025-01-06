#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
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

class Solution0:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None: return None

        head = ListNode(None, head)
        lst: List[ListNode] = []
        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next
        lst[-n - 1].next = lst[-n].next

        return head.next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None: return None

        head = ListNode(None, head)
        l, r = head, head
        gap = 0
        while gap <= n:
            r = r.next
            gap += 1

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return head.next
# @lc code=end

s = Solution()
print(s.removeNthFromEnd(ListNode.create([1,2,3,4,5]), 2))
print(s.removeNthFromEnd(ListNode.create([1]), 1))
print(s.removeNthFromEnd(ListNode.create([1,2]), 1))
print(s.removeNthFromEnd(ListNode.create([1,2]), 2))
