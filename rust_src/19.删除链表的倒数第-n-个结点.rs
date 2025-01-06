/*
 * @lc app=leetcode.cn id=19 lang=rust
 *
 * [19] 删除链表的倒数第 N 个结点
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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
		let mut root = Some(Box::new(ListNode::new(0)));

		root.as_mut().unwrap().next = head;
		let mut end = root.as_ref().unwrap();

		for _ in 0..n
		{
			end = end.next.as_ref().unwrap();
		}
		
		let mut tmp = root.clone();
		let mut cur = tmp.as_mut().unwrap();
		
		while end.next.is_some()
		{
			end = end.next.as_ref().unwrap();
			cur = cur.next.as_mut().unwrap();
		}

		let node = cur.next.take().unwrap();
		cur.next = node.next;

		return tmp.unwrap().next;
    }
}
// @lc code=end

