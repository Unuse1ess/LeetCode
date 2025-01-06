/*
 * @lc app=leetcode.cn id=121 lang=rust
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
		use std::cmp::{min, max};

		let mut dp = 0;
		let mut buy = prices[0];

		for i in prices
		{
			buy = min(buy, i);
			dp = max(dp, i - buy);
		}

		return dp;
    }
}
// @lc code=end
/*
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
		use std::cmp::max;

		let mut diff = 0;

		for i in 0..prices.len()
		{
			for j in i + 1..prices.len()
			{
				diff = max(diff, prices[j] - prices[i]);
			}
		}
		return diff;
    }
}
*/
