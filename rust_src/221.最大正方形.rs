/*
 * @lc app=leetcode.cn id=221 lang=rust
 *
 * [221] 最大正方形
 */

// dp[i][j] = min{dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]} + 1 (matrix[i][j] == '1')
// dp[i][j] = 0 (matrix[i][j] == '0')

// @lc code=start
impl Solution {
    pub fn maximal_square(mut matrix: Vec<Vec<char>>) -> i32 {
		use std::cmp::{min, max};

		//let m = matrix.len();
		let n = matrix[0].len();

		let mut length = 0;

		matrix.iter_mut().for_each(|row| {
			row.iter_mut().for_each(|v| {
				*v = (*v as u8 - b'0') as char;
			});
		});

		let mut dp0 = vec!['\0'; n];
		
		while let Some(mut dp1) = matrix.pop()
		{
			for i in (0..n).rev()
			{
				if dp1[i] == '\0'
				{
					continue;
				}
				let a = if let Some(&v) = dp0.get(i + 1)
				{
					v
				}
				else
				{
					'\0'
				} as u8;
				let b = if let Some(&v) = dp1.get(i + 1)
				{
					v
				}
				else
				{
					'\0'
				} as u8;
				let res = min(min(dp0[i] as u8, a), b) + 1;
				length = max(length, res);
				dp1[i] = res as char;
			}
			dp0 = dp1;
		}

		return length as i32 * length as i32;
	}
}
// @lc code=end

// dp[i][j] = dp[i][j] + min{Surrounding(dp[i][j])}
/*
impl Solution {
    pub fn maximal_square(mut matrix: Vec<Vec<char>>) -> i32 {
		use std::cmp::max;

		let m = matrix.len();
		let n = matrix[0].len();
		let mut max_size: u8 = 0;

		matrix.iter_mut().for_each(|row| {
			row.iter_mut().for_each(|v| {
				*v = (*v as u8 - b'0') as char;
			});
		});


		loop
		{
			let mut changed = false;

			for i in 0..m
			{
				for j in 0..n
				{
					if matrix[i][j] != 0 as char
					//if matrix[i][j] == max_size as char
					{
						let res = Self::min_sur(&matrix, i, j);
						matrix[i][j] = (matrix[i][j] as u8 + res) as char;
						max_size = max(matrix[i][j] as u8, max_size);
						if res != 0
						{
							changed = true;
						}
					}
				}
			}
			if !changed
			{
				break;
			}
		}

		let res = max_size as i32;
		return res * res;
    }

	fn min_sur(dp: &Vec<Vec<char>>, x: usize, y: usize) -> u8
	{
		use std::cmp::min;

		let size = dp[x][y] as usize;

		let mut min_size = u8::MAX;
		// Check bottom row
		// dp[x + size][y..y + size]
		if let Some(row) = dp.get(x + size)
		{
			//for &i in row
			for i in y..y + size
			{
				min_size = min(row[i] as u8, min_size);
			}
		}
		else
		{
			return 0;
		}

		// Check right column
		// dp[x..x + size][size + 1]
		if let Some(_) = dp[0].get(y + size)
		{
			for i in x..x + size
			{
				min_size = min(min_size, dp[i][y + size] as u8);
			}
		}
		else
		{
			return 0;
		}

		return min(min_size, dp[x + size][y + size] as u8);
	}
}
*/

