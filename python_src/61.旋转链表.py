#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head

        node_list: List[ListNode] = []
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next
        cnt = len(node_list)
        k %= cnt
        idx = (cnt + cnt - k - 1) % cnt
        node_list[-1].next = node_list[0]
        node_list[idx].next = None
        return node_list[-k]

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head
        
        head = ListNode(None, head)
        l, r = head, head.next
        gap = 1
        while r.next and gap < k:
            gap += 1
            r = r.next
        if r.next:
            while r.next:
                l = l.next
                r = r.next
        else:
            k %= gap
            if k == 0: return head.next
        
        while gap > k:
            gap -= 1
            l = l.next
        
        r.next = head.next
        head.next = l.next
        l.next = None

        return head.next
# @lc code=end

s = Solution()
print(s.rotateRight(ListNode.create([1,2,3,4,5]), 2))
print(s.rotateRight(ListNode.create([0,1,2]), 4))
print(s.rotateRight(ListNode.create([0,1,2]), 0))
print(s.rotateRight(ListNode.create([1,2,3,4,5]), 7))
print(s.rotateRight(ListNode.create([1,2,3]), 3))
print(s.rotateRight(ListNode.create([1,2]), 3))
print(s.rotateRight(ListNode.create([1]), 1))
print(s.rotateRight(ListNode.create([]), 10))
