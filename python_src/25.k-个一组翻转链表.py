#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Tuple[ListNode, ListNode]:
        head = ListNode(None, head)
        cur = head
        i = -1
        end = None
        while cur:
            i += 1
            if i == left:
                start = prev
                end = cur
            elif left < i <= right:
                fol = cur.next
                cur.next = prev
                prev = cur
                cur = fol

                if i == right or cur is None:
                    start.next.next = cur
                    start.next = prev
                    break
                else:
                    continue

            prev = cur
            cur = cur.next
        
        if cur is None and i != right:
            return self.reverseBetween(head.next, left, i)

        return head.next, end
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        head = ListNode(None, head)
        cur = head
        while cur:
            l, r = self.reverseBetween(cur.next, 1, k)
            cur.next = l
            cur = r
        return head.next
# @lc code=end

s = Solution()
print(s.reverseKGroup(ListNode.create([1,2,3,4,5]), 2))
print(s.reverseKGroup(ListNode.create([1,2,3,4,5]), 3))
print(s.reverseKGroup(ListNode.create([1,2,3,4,5]), 4))
print(s.reverseKGroup(ListNode.create(list(range(10))), 2))
print(s.reverseKGroup(ListNode.create(list(range(10))), 6))
