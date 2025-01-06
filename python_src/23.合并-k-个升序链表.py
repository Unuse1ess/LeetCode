#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"
    
    __repr__ = __str__

    @staticmethod
    def create(l: Iterable[int]) -> "ListNode":
        head = ListNode()
        cur = head
        for n in l:
            cur.next = ListNode(n)
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0: return None
        lists: Dict[int, Optional[ListNode]] = {i: node for i, node in enumerate(lists)}
        step = 1
        while step < k:
            i = 0
            # while True:
                # if i < k:
                #     op1 = lists[i]
                # else:
                #     break
                # if i + step < k:
                #     op2 = lists[i + step]
                #     lists[i] = self.mergeTwoLists(op1, op2)
                #     i += step << 1
                # else:
                #     break
            while i < k:
                op1 = lists.get(i)
                op2 = lists.get(i + step)
                lists[i] = self.mergeTwoLists(op1, op2)
                i += step << 1

            step <<= 1
        return lists[0]
        
# @lc code=end

s = Solution()
print(s.mergeKLists([ListNode.create([1,4,5]), ListNode.create([1,3,4]), ListNode.create([2,6])]))
print(s.mergeKLists([ListNode.create([])]))
print(s.mergeKLists([]))
