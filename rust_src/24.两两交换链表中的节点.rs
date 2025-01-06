/*
 * @lc app=leetcode.cn id=24 lang=rust
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		if head.as_ref().unwrap().next.is_none()
		{
			return head;
		}
		let mut root1 = Some(Box::new(ListNode::new(0)));
		root1.as_mut().unwrap().next = head;

		let mut root2 = root1.clone();

		let mut cur1 = root1.as_mut().unwrap();
		let mut cur2 = root2.as_ref().unwrap().next.as_ref().unwrap();

		while cur1.next.is_some() && cur2.next.is_some()
		{
			
		}

		None
    }
}
// @lc code=end

