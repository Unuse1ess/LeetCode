#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        idx = 0
        tmp = [ListNode(0), ListNode(0)]
        odd = tmp[0]
        even = tmp[1]
        p = head
        while p is not None:
            tmp[idx].next = p
            tmp[idx] = tmp[idx].next
            idx ^= 1
            p = p.next
        tmp[idx].next = p

        tmp[0].next = even.next
        return odd.next
        
# @lc code=end

s = Solution()
print(s.oddEvenList(ListNode.create([1,2,3,4,5])))
print(s.oddEvenList(ListNode.create([2,1,3,5,6,4,7])))
