/*
 * @lc app=leetcode.cn id=2 lang=rust
 *
 * [2] 两数相加
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
pub fn new_node(val: i32) -> Box<ListNode>
{
	return Box::new(ListNode::new(val));
}

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		let mut cur1 = l1.as_ref();
		let mut cur2 = l2.as_ref();
		let mut carry = 0;
		let mut res = Some(new_node(0));
		let mut cur = res.as_mut().unwrap();

		while cur1.is_some() && cur2.is_some()
		{
			let mut sum = carry + cur1.unwrap().val + cur2.unwrap().val;
			carry = 0;
			if sum >= 10
			{
				carry = 1;
				sum -= 10;
			}

			cur1 = cur1.unwrap().next.as_ref();
			cur2 = cur2.unwrap().next.as_ref();

			cur.next = Some(new_node(sum));
			cur = cur.next.as_mut().unwrap();
		}
		while cur1.is_some()
		{
			let mut sum = carry + cur1.as_ref().unwrap().val;
			carry = 0;
			if sum >= 10
			{
				carry = 1;
				sum -= 10;
			}

			cur.next = Some(new_node(sum));
			cur = cur.next.as_mut().unwrap();
			cur1 = cur1.unwrap().next.as_ref();
		}
		while cur2.is_some()
		{
			let mut sum = carry + cur2.as_ref().unwrap().val;
			carry = 0;
			if sum >= 10
			{
				carry = 1;
				sum -= 10;
			}

			cur.next = Some(new_node(sum));
			cur = cur.next.as_mut().unwrap();
			cur2 = cur2.unwrap().next.as_ref();
		}
		if carry == 1
		{
			cur.next = Some(new_node(1));
		}

		return res.unwrap().next;
    }
}
// @lc code=end

/*
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut result = None;
        let mut tail = &mut result;
        let mut t = (l1, l2, 0, 0); // (list1, list2, sum, carry)
        loop {
            t = match t {
                (None, None, _, 0) => break,
                (None, None, _, carry) => (None, None, carry, 0),
                (Some(list), None, _, carry) | (None, Some(list), _, carry) if list.val + carry >= 10 => {
                    (list.next, None, list.val + carry - 10, 1)
                }
                (Some(list), None, _, carry) | (None, Some(list), _, carry) => {
                    (list.next, None, list.val + carry, 0)
                }
                (Some(l1), Some(l2), _, carry) if l1.val + l2.val + carry >= 10 => {
                    (l1.next, l2.next, l1.val + l2.val + carry - 10, 1)
                }
                (Some(l1), Some(l2), _, carry) => {
                    (l1.next, l2.next, l1.val + l2.val + carry, 0)
                }
            };

            *tail = Some(Box::new(ListNode::new(t.2)));
            tail = &mut tail.as_mut().unwrap().next;
        }
        result
    }
}

作者：anonyuser
链接：https://leetcode-cn.com/problems/add-two-numbers/solution/rust-pattern-matching-xie-fa-by-anonyuse-kk10/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
