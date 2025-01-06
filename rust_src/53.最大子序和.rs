/*
 * @lc app=leetcode.cn id=53 lang=rust
 *
 * [53] 最大子序和
 */

// Transfer equation:
// dp[i][j] = max{dp[i][j - 1], dp[i + 1][j]}

// Inital state:
// dp[i][j] = nums[i] (i = j)

// @lc code=start
impl Solution {
    pub fn max_sub_array(mut nums: Vec<i32>) -> i32 {
		use std::cmp::max;

		let mut dp = nums.pop().unwrap();
		let mut res = dp;

		while let Some(v) = nums.pop()
		{
			dp = max(dp + v, v);
			res = max(res, dp);
		}

		return res;
    }
}
// @lc code=end

