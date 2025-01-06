/*
 * @lc app=leetcode.cn id=343 lang=rust
 *
 * [343] 整数拆分
 */

/*
Mathemetic:
Divid `n` into as many `x`s as possible.
Let f(x) be the maximal product.
f(x) = x^(n/x)
The result is 3.
*/

// @lc code=start
impl Solution {
    pub fn integer_break(n: i32) -> i32 {
		match n
		{
			2 | 3 => n - 1,
			n =>
			{
				let q = n / 3;

				match n % 3
				{
					0 => i32::pow(3, q as u32),
					1 => i32::pow(3, q as u32 - 1) * 4,
					2 => i32::pow(3, q as u32) * 2,
					_ => 0,
				}
			}
		}
    }
}
// @lc code=end

/*
// dp[i] = max{1 <= j < i | j * max{dp[i - j], i - j}}
impl Solution {
    pub fn integer_break(n: i32) -> i32 {
		use std::cmp::max;

		let n = n as usize;
		let mut dp = vec![1; n + 1];

		for i in 2..=n
		{
			for j in 1..i
			{
				dp[i] = max(dp[i], j * max(dp[i - j], i - j));
			}
		}

		return dp[n] as i32;
    }
}
*/
