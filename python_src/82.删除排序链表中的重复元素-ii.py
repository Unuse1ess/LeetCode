#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        head = ListNode(None, head)
        l, r = head, head.next
        while r and r.next:
            if l.next.val != r.next.val:
                l = l.next
            else:
                while r.next and l.next.val == r.next.val:
                    r = r.next
                l.next = r.next
            r = r.next
        return head.next
# @lc code=end

s = Solution()
print(s.deleteDuplicates(ListNode.create([1,2,3,3,4,4,5])))
print(s.deleteDuplicates(ListNode.create([1,1,1,2,3])))
print(s.deleteDuplicates(ListNode.create([1]*4+[2]*5)))
print(s.deleteDuplicates(ListNode.create([0]+[1]*4+[2]*5+[3])))
print(s.deleteDuplicates(ListNode.create([])))
