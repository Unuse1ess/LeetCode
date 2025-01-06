/*
 * @lc app=leetcode.cn id=96 lang=rust
 *
 * [96] 不同的二叉搜索树
 */

// @lc code=start
impl Solution {
    pub fn num_trees(n: i32) -> i32 {
		let n = n as usize;
		let mut dp = vec![1; n + 1];

		// Solve sub question starting from 2,
		// and let i be the sub question.
		(2..=n).into_iter().for_each(|i| {
			dp[i] = 0;

			// The number of nodes at left or at right is [0, i - 1]
			// Let j be number of nodes at left,
			// then there will be i - 1 - j at right.
			(0..i).into_iter().for_each(|j| {
				dp[i] += dp[j] * dp[i - 1 - j];
			});
		});

		return dp[n as usize];
	}
}
// @lc code=end

