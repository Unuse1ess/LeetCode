/*
 * @lc app=leetcode.cn id=120 lang=rust
 *
 * [120] 三角形最小路径和
 */

// From bottom to top
// dp[i][j] = min{dp[i + 1][j], dp[i + 1][j + 1]} + triangle[i][j]

// @lc code=start
impl Solution {
    pub fn minimum_total(mut triangle: Vec<Vec<i32>>) -> i32 {
		use std::cmp::min;

		let mut dp0 = triangle.pop().unwrap();

		while let Some(mut dp1) = triangle.pop()
		{
			for j in 0..dp1.len()
			{
				dp1[j] += min(dp0[j], dp0[j + 1]);
			}

			dp0 = dp1;
		}

		return dp0[0];
    }
}
// @lc code=end

/*
// From top to bottom
// dp[i][j] = min{dp[i - 1][j], dp[i - 1][j - 1]} + triangle[i][j]

impl Solution {
    pub fn minimum_total(mut triangle: Vec<Vec<i32>>) -> i32 {
		use std::cmp::min;

		let m = triangle.len();

		for i in 1..m
		{
			triangle[i][0] += triangle[i - 1][0];
			triangle[i][i] += triangle[i - 1][i - 1];
			for j in 1..i
			{
				triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1]);
			}
		}

		return triangle.pop().unwrap().into_iter().fold(i32::MAX, |m, v| { min(m, v)});
    }
}
*/
