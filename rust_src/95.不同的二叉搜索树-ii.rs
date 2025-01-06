/*
 * @lc app=leetcode.cn id=95 lang=rust
 *
 * [95] 不同的二叉搜索树 II
 */

// @lc code=start
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn generate_trees(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
		return Self::gen(1, n);
    }

	// Generate result [start, start + num - 1]
	fn gen(start: i32, num: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>>
	{
		if num == 0
		{
			return vec![None];
		}

		if num == 1
		{
			return vec![new_tree(start)];
		}

		let mut res = Vec::new();

		// Let i be root node's value
		for i in start..start + num
		{
			let left = Self::gen(start, i - start);
			let right = Self::gen(i + 1, num - 1 - (i - start));

			for p in left
			{
				for q in &right
				{
					let mut root = TreeNode::new(i);

					root.left = p.clone();
					root.right = q.clone();
					res.push(Some(Rc::new(RefCell::new(root))));
				}
			}
		}

		return res;
	}
}

#[inline]
fn new_tree(val: i32) -> Option<Rc<RefCell<TreeNode>>>
{
	Some(Rc::new(RefCell::new(TreeNode::new(val))))
}
// @lc code=end

