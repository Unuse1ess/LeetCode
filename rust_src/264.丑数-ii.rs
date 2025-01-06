/*
 * @lc app=leetcode.cn id=264 lang=rust
 *
 * [264] 丑数 II
 */

// dp[i] = min{dp[i2] * 2, dp[i3] * 3, dp[i5] * 5}

// @lc code=start
impl Solution
{
    pub fn nth_ugly_number(n: i32) -> i32
	{
		let mut dp = vec![1; n as usize];
		let mut a = 0;
		let mut b = 0;
		let mut c = 0;
		let mut i = 1;

		while i < n
		{
			let _a = dp[a] * 2;
			let _b = dp[b] * 3;
			let _c = dp[c] * 5;

			dp[i as usize] = if _a < _b && _a < _c
			{
				a += 1;
				_a
			}
			else if _b < _c
			{
				b += 1;
				_b
			}
			else
			{
				c += 1;
				_c
			};

			if dp[i as usize] == dp[i as usize - 1]
			{
				continue;
			}

			i += 1;
		}
		return dp[n as usize - 1];
    }
}
// @lc code=end

