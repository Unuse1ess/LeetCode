/*
 * @lc app=leetcode.cn id=375 lang=rust
 *
 * [375] 猜数字大小 II
 */

/*
dp[i][j] = min{(i + j) / 2 <= n <= j | n + max(dp[i][n - 1], dp[n + 1][j])},
Parts where i > j are useless.
Remove those useless cells, and shift used cells i - 1 forward.
*/
// @lc code=start
impl Solution {
	pub fn get_money_amount(num: i32) -> i32
	{
		use std::cmp::{max, min};

		let num = num as usize;

		let mut dp = Vec::with_capacity(num);

		for i in 1..=num
		{
			dp.push(vec![0; num - i + 2]);
		}

		for len in 2..=num
		{
			for i in 1..=num - len + 1
			{
				let mut res = usize::MAX;

				for j in i + (len - 1) / 2..i + len - 1
				{
					res = min(res, j + max(dp[i - 1][j - i], dp[j][i + len - 1 - j]));
				}

				dp[i - 1][len] = res;
			}
		}
		return dp[0][num] as i32;
	}
}
// @lc code=end


//fn p(a: &Vec<Vec<usize>>)
//{
//	let dis = 100;
//	for (i, row) in a.iter().enumerate()
//	{
//		if let Some(v) = row.get(i + dis)
//		{
//			println!("({}, {}) {}", i, i + dis, v);
//		}
//	}
//}

/*
impl Solution {
	pub fn get_money_amount(num: i32) -> i32
	{
		use std::cmp::{max, min};
		if num == 1
		{
			return 0;
		}

		let mut dp = vec![0; num as usize + 1];
		let mut selected_count = dp.clone();

		for i in 2..=num
		{
			let mut res = i32::MAX;

			for j in 1..=i
			{
				let left = dp[j as usize - 1];
				let right = dp[(i - j) as usize] + j * selected_count[(i - j) as usize];

				res = min(res, j + max(left, right));

				let tmp = j + max(left, right);
				res = if res < tmp
				{
					res
				}
				else
				{
					selected_count[i as usize] = selected_count[j as usize - 1] + 1;
					tmp
				};
			}
			dp[i as usize] = res;
		}

		//println!("dp: {:?}", dp);
		//println!("count: {:?}", selected_count);
		
		return dp[num as usize];
	}
}
*/