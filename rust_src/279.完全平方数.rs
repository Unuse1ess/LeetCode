/*
 * @lc app=leetcode.cn id=279 lang=rust
 *
 * [279] 完全平方数
 */

/*
Not so effective:
dp[i] = min{1 <= j <= i / 2 | dp[j] + dp[i - j]}

Much effective:
dp[i] = min{1 <= j <= sqrt(i) | 1 + dp[i - j * j]}

BFS:
Treat each perfect square number as a tree node.
*/

// @lc code=start
impl Solution {
    pub fn num_squares(n: i32) -> i32 {
		use std::cmp::min;

		let n = n as usize;
		let mut dp = vec![0; n + 1];

		dp[0] = 0;

		for i in 1..=n
		{
			let mut m = i32::MAX;
			let mut j = 1;

			while j * j <= i
			{
				m = min(m, dp[i - j * j]);
				j += 1;
			}

			dp[i] = 1 + m;
		}

		return dp[n];
    }
}
// @lc code=end

