#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
from typing import Optional, Iterable

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next : ListNode = None

    @classmethod
    def create_cycled_linked_list(cls, l: Iterable, pos: int) -> 'ListNode':
        if len(l) == 0:
            return None
        head = cls(l[0])
        cur = head
        target = None

        for i in range(1, len(l)):
            if i - 1 == pos:
                target = cur
            cur.next = cls(l[i])
            cur = cur.next

        cur.next = target if pos != len(l) - 1 else cur
        
        return head

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# @lc code=end

s = Solution()
print(s.hasCycle(ListNode.create_cycled_linked_list([3, 2, 0, -4], 1)))
print(s.hasCycle(ListNode.create_cycled_linked_list([1,2], 0)))
print(s.hasCycle(ListNode.create_cycled_linked_list([1], -1)))
print(s.hasCycle(ListNode.create_cycled_linked_list(range(10), -1)))
print(s.hasCycle(ListNode.create_cycled_linked_list(range(3), 2)))
print(s.hasCycle(None))
