/*
 * @lc app=leetcode.cn id=152 lang=rust
 *
 * [152] 乘积最大子数组
 */

/*
pos[i] = max{pos[i - 1] * nums[i], neg[i - 1] * nums[i], nums[i]}
neg[i] = min{neg[i - 1] * nums[i], pos[i - 1] * nums[i], nums[i]}
*/

// @lc code=start

impl Solution {
    pub fn max_product(mut nums: Vec<i32>) -> i32 {
		use std::cmp::{max, min};

		let tmp = nums.pop().unwrap();
		let mut pos = tmp;
		let mut neg = tmp;
		let mut res = tmp;

		while let Some(v) = nums.pop()
		{
			let pos0 = pos;
			pos = max(v, max(pos * v, neg * v));
			neg = min(v, min(pos0 * v, neg * v));

			res = max(res, pos);
		}

		return res;
    }
}
// @lc code=end

