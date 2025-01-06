/*
 * @lc app=leetcode.cn id=188 lang=rust
 *
 * [188] 买卖股票的最佳时机 IV
 */

/*
Please refer to [123] 买卖股票的最佳时机 III.
*/

// @lc code=start
impl Solution {
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
		use std::cmp::max;

		if k == 0 || prices.len() == 0
		{
			return 0;
		}

		let mut buy: Vec<i32> = vec![-prices[0]; k as usize];
		let mut sell: Vec<i32> = vec![0; k as usize];

		for v in prices.into_iter().skip(1)
		{
			// Try to buy at lowest point.
			buy[0] = max(buy[0], -v);
			// Try to sell at highest point.
			sell[0] = max(sell[0], v + buy[0]);
			
			for i in 1..k as usize
			{
				// Try to buy at lowest point base on previous income.
				buy[i] = max(buy[i], sell[i - 1] - v);
				// Try to sell at highest point base on previous income.
				sell[i] = max(sell[i], v + buy[i]);
			}
		}

		return sell[k as usize - 1];
    }
}
// @lc code=end

