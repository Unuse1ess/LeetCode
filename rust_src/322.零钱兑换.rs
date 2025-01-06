/*
 * @lc app=leetcode.cn id=322 lang=rust
 *
 * [322] 零钱兑换
 */

/*
dp[i] = min{0 <= j <= coins.len()| dp[i - coins[j]] + 1} if i >= coins[j] 
*/

// @lc code=start
impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
		use std::cmp::min;

		let amount = amount as usize;
		let mut dp = Vec::with_capacity(amount + 1);

		dp.push(Some(0));
		
		for i in 1..=amount
		{
			let mut res = i32::MAX;

			for &coin in &coins
			{
				if coin <= i as i32
				{
					if let Some(v) = dp[i - coin as usize]
					{
						res = min(res, v + 1);
					}
				}
			}
			dp.push(if res == i32::MAX { None } else { Some(res) });
		}

		//println!("{:?}", dp);

		return dp[amount].unwrap_or(-1);
	}
}

// @lc code=end
