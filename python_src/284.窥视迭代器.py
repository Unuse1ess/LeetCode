#
# @lc app=leetcode.cn id=284 lang=python3
#
# [284] 窥视迭代器
#
from typing import List, Optional

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.p = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.p < len(self.nums)
    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.p += 1
        return self.nums[self.p - 1]

# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it: Iterator = iterator
        self.next_val: Optional[int] = self.it.next() if self.it.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_val

    def next(self):
        """
        :rtype: int
        """
        ret = self.next_val
        self.next_val = self.it.next() if self.it.hasNext() else None
        return ret
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_val is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

    instance: Optional["PeekingIterator"] = None

    @staticmethod
    def PeekingIterator_(nums: List[int]):
        PeekingIterator.instance = PeekingIterator(iterator=nums)

    next_ = lambda *args: PeekingIterator.instance.next(*args)
    hasNext_ = lambda *args: PeekingIterator.instance.hasNext(*args)
    peek_ = lambda *args: PeekingIterator.instance.peek(*args)

def run(methods, params):
    print([
        getattr(PeekingIterator, m)(*p) for m, p in zip(map(lambda x: x + "_", methods), params)
    ])

run(["PeekingIterator", "next", "peek", "next", "next", "hasNext"],
    [[Iterator([1,2,3])], [], [], [], [], []])