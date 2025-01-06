/*
 * @lc app=leetcode.cn id=63 lang=rust
 *
 * [63] 不同路径 II
 */

// @lc code=start
impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
		let m = obstacle_grid.len();
		let n = obstacle_grid[0].len();

		let mut dp0 = vec![1; n];

		for i in 0..obstacle_grid[0].len()
		{
			if obstacle_grid[0][i] == 1
			{
				for j in i..n
				{
					dp0[j] = 0;
				}
				break;
			}
		}

		(1..m).into_iter().for_each(|i|
		{
			let mut dp1 = vec![dp0[0]; n];
			if obstacle_grid[i][0] == 1
			{
				dp1[0] = 0;
			}
			
			(1..n).into_iter().for_each(|j|
			{
				if obstacle_grid[i][j] == 0
				{
					dp1[j] = dp0[j] + dp1[j - 1];
				}
				else
				{
					dp1[j] = 0;
				}
			});

			dp0 = dp1;
		});

		return dp0[n as usize - 1];
	}
}
// @lc code=end

