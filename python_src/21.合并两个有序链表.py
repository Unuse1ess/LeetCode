#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import *

class ListNode:
    def __init__(self, val:int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self) -> str:
        return f'{self.val} -> {self.next}'

    @staticmethod
    def create_from_list(l: List[int]) -> Optional["ListNode"]:
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = ListNode(None)
        cur = head
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
                # cur.next = None
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
                # cur.next = None
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return head.next
# @lc code=end

s = Solution()
print(s.mergeTwoLists(ListNode.create_from_list([1,2,4]), ListNode.create_from_list([1,3,4])))
print(s.mergeTwoLists(ListNode.create_from_list([]), ListNode.create_from_list([])))
print(s.mergeTwoLists(ListNode.create_from_list([]), ListNode.create_from_list([0])))
print(s.mergeTwoLists(ListNode.create_from_list(range(0,10,2)), ListNode.create_from_list(range(1,10,2))))
