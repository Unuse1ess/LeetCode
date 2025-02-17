#
# @lc app=leetcode.cn id=2095 lang=python3
#
# [2095] 删除链表的中间节点
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        head = ListNode(0, head)
        p1, p2 = head, head

        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        
        p1.next = p1.next.next

        return head.next
        
# @lc code=end

s = Solution()
print(s.deleteMiddle(ListNode.create([1,3,4,7,1,2,6])))
print(s.deleteMiddle(ListNode.create([1, 2, 3, 4])))
print(s.deleteMiddle(ListNode.create([2,1])))
