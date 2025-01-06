#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from typing import *
from operator import *
from collections import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next
    
    def __str__(self):
        return f"({self.val})->{self.next}"

    __repr__ = __str__

    @staticmethod
    def create(nums: List[int]) -> Optional['ListNode']:
        head = ListNode()
        cur = head
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next

class Solution0:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        cur = head
        tmp: List[ListNode] = []
        while cur:
            tmp.append(cur)
            cur = cur.next
        tmp.sort(key=attrgetter("val"))
            
        for i in range(1, len(tmp)):
            tmp[i - 1].next = tmp[i]
        tmp[-1].next = None

        return tmp[0]

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Tuple[ListNode, ListNode]:
        if list1 is None:
            tmp = list2
            while tmp.next:
                tmp = tmp.next
            return list2, tmp
        if list2 is None:
            tmp = list1
            while tmp.next:
                tmp = tmp.next
            return list1, tmp

        head = ListNode(None)
        cur = head
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        tmp = cur

        if list1:
            tmp = list1
            while tmp.next:
                tmp = tmp.next
            cur.next = list1
        if list2:
            tmp = list2
            while tmp.next:
                tmp = tmp.next
            cur.next = list2
        return head.next, tmp
    
    def split_list(self, head: ListNode, k: int) -> Tuple[ListNode, Optional[ListNode], int]:
        head = ListNode(0, head)
        cur = head
        i = 0
        while i < k and cur.next:
            i += 1
            cur = cur.next
        
        c_next = cur.next
        cur.next = None

        return head.next, c_next, i

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        k = 1
        head = ListNode(0, head)
        while k < cnt:
            i = 0
            cur = head.next
            prev = head
            while i < cnt:
                op1, cur, j = self.split_list(cur, k)
                i += j
                if cur:
                    op2, cur, j = self.split_list(cur, k)
                    i += j
                    prev.next, tmp = self.mergeTwoLists(op1, op2)
                    tmp.next = cur
                    prev = tmp
                
            k <<= 1
        return head.next
# @lc code=end

s = Solution()
print(s.sortList(ListNode.create([4,2,1,3])))
print(s.sortList(ListNode.create([-1,5,3,4,0])))
print(s.sortList(ListNode.create([-1,5,2,-2,-3,3])))
print(s.sortList(ListNode.create([6,-1,5,2,-2,-3,3,-6])))
print(s.sortList(ListNode.create([])))
