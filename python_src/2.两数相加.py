#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
from typing import *
from itertools import *
from functools import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    @classmethod
    def from_list(cls, l: list) -> Optional["ListNode"]:
        if not l:
            return None
        head = cls(l[0])
        cur = head
        for i in l[1:]:
            cur.next = cls(i)
            cur = cur.next
        return head

class Solution0:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = 0

        cur = l1
        base = 1
        while cur:
            res += cur.val * base
            base *= 10
            cur = cur.next
        cur = l2
        base = 1
        while cur:
            res += cur.val * base
            base *= 10
            cur = cur.next

        head = ListNode(res % 10)
        res //= 10
        cur = head
        while res > 0:
            cur.next = ListNode(res % 10)
            cur = cur.next
            res //= 10

        return head

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        head = ListNode(None)
        cur = head
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            res = a + b + carry
            cur.next = ListNode(res % 10)
            cur = cur.next
            carry = res >= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
# @lc code=end

s = Solution()
print(s.addTwoNumbers(ListNode.from_list([2,4,3]), ListNode.from_list([5,6,4])))
print(s.addTwoNumbers(ListNode.from_list([0]), ListNode.from_list([0])))
print(s.addTwoNumbers(ListNode.from_list([9,9,9,9,9,9,9]), ListNode.from_list([9,9,9,9])))
print(s.addTwoNumbers(ListNode.from_list([2,4,9]), ListNode.from_list([5,6,4,9])))
print(s.addTwoNumbers(ListNode.from_list([1,2,3,4,5]), ListNode.from_list([9,9,9,9])))
