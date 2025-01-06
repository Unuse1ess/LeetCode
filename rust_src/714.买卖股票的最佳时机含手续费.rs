/*
 * @lc app=leetcode.cn id=714 lang=rust
 *
 * [714] 买卖股票的最佳时机含手续费
 */

/*
buy[i] = max{buy[i - 1], sell[i - 1] - prices[i] - fee}
sell[i] = max{sell[i - 1], buy[i] + prices[i]}

手续费在购买的时候扣除，这样卖出时就能体现出这个费用。其余的不变。
*/
// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
		use std::cmp::max;

		return prices.iter().skip(1).fold((-prices[0] - fee, 0), |(buy, sell), price| {
			(max(buy, sell - price - fee), max(sell, buy + price))
		}).1
    }
}
// @lc code=end

