/*
 * @lc app=leetcode.cn id=64 lang=rust
 *
 * [64] 最小路径和
 */

// dp[i][j] = min{dp[i - 1][j], dp[i][j - 1]} + grid[i][j]

// @lc code=start
impl Solution {
    pub fn min_path_sum(mut grid: Vec<Vec<i32>>) -> i32 {
		let m = grid.len();
		let n = grid[0].len();

		if m < 1 || n < 1
		{
			return 0;
		}
		
		for i in 1..n
		{
			grid[0][i] += grid[0][i - 1];
		}
		
		for i in 1..m
		{
			grid[i][0] += grid[i - 1][0];
			for j in 1..n
			{
				grid[i][j] += std::cmp::min(grid[i - 1][j], grid[i][j - 1]);
			}
		}

		return grid[m - 1][n - 1];
    }
}
// @lc code=end

