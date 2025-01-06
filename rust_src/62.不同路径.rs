/*
 * @lc app=leetcode.cn id=62 lang=rust
 *
 * [62] 不同路径
 */

// @lc code=start
impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
		let mut dp0: Vec<i32> = vec![1; n as usize];

		for _ in 1..m as usize
		{
			let mut dp1: Vec<i32> = vec![1; n as usize];
			for j in 1..n as usize
			{
				dp1[j] = dp0[j] + dp1[j - 1];
			}
			dp0 = dp1;
		}
		return dp0[n as usize - 1];
    }
}
// @lc code=end

