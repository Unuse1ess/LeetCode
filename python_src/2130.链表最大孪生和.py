#
# @lc app=leetcode.cn id=2130 lang=python3
#
# [2130] 链表最大孪生和
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

class Solution0:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p1, p2 = head, head
        lst = []
        while p2.next and p2.next.next:
            lst.append(p1.val)
            p1 = p1.next
            p2 = p2.next.next
        lst.append(p1.val)
        p1 = p1.next

        ret = 0
        pos = -1

        while p1:
            tmp = lst[pos] + p1.val
            if tmp > ret: ret = tmp
            p1 = p1.next
            pos -= 1

        return ret
        
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p1, p2 = head, head
        prev = None
        while p2.next and p2.next.next:
            p2 = p2.next.next

            nxt = p1.next
            p1.next = prev
            prev = p1
            p1 = nxt

        p2 = p1.next
        p1.next = prev

        ret = 0
        while p2:
            tmp = p1.val + p2.val
            if tmp > ret: ret = tmp
            p1 = p1.next
            p2 = p2.next

        return ret
# @lc code=end

s = Solution()
print(s.pairSum(ListNode.create([5,4,2,1])))
print(s.pairSum(ListNode.create([4,2,2,3])))
print(s.pairSum(ListNode.create([1,100000])))

print(s.pairSum(ListNode.create([4,2,2,3,3,1])))