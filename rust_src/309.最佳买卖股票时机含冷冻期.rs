/*
 * @lc app=leetcode.cn id=309 lang=rust
 *
 * [309] 最佳买卖股票时机含冷冻期
 */


/*
buy[i] = max{buy[i - 1], sell[i - 2] - prices[i]}
sell[i] = max{sell[i - 1], buy[i] + prices[i]}
*/

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
		use std::cmp::max;

		return match prices.len()
		{
			0 | 1 => 0,
			2 => max(0, prices[1] - prices[0]),
			_ =>
			{
				let mut buy = max(-prices[0], -prices[1]);
				let mut sell0 = 0;
				let mut sell1 = max(sell0, prices[1] + buy);
		
				for v in prices.into_iter().skip(2)
				{
					buy = max(buy, sell0 - v);
					sell0 = sell1;
					sell1 = max(sell0, buy + v);
				}

				sell1
			},
		};
    }
}
// @lc code=end

