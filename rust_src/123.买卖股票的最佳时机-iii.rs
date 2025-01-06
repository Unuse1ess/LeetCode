/*
 * @lc app=leetcode.cn id=123 lang=rust
 *
 * [123] 买卖股票的最佳时机 III
 */

/*
在任意时刻有一下状态：
1）第一次购买了股票未出售
2）第一次购买了股票并要售，但未购买第二次
3）购买了第二次并未出售
4）购买了第二次并要出售

对于每天的情况，不管是第几次，总是尝试在最低点买入，最高点卖出。
第一次和第二次的区别在于第二次是基于第一次的结果。在不需要第二
次购买的情况下，可以把第二次看成当天买入卖出，收益为0。
因此对每一种状态设立一个变量，允许当天买入卖出两次。

当前最低买入开销
buy1[i] = max(buy[i - 1], -prices[i])

当前卖出收益
sell1[i] = max(sell1[i - 1], buy1 + prices[i])

当前第二次买入的最低开销
buy2[i] = max(buy[i - 1], sell1[i] - prices[i])

当前第二次卖出的最高收益
sell2[i] = max(sell2[i - 1], buy2 + prices[i])
*/
// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
		use std::cmp::max;

		let mut buy1 = -prices[0];
		let mut sell1 = 0;
		let mut buy2 = -prices[0];
		let mut sell2 = 0;

		for i in prices.into_iter().skip(1)
		{
			buy1 = max(buy1, -i);
			sell1 = max(sell1, buy1 + i);
			buy2 = max(buy2, sell1 - i);
			sell2 = max(sell2, buy2 + i);
		}

		return sell2;
    }
}
// @lc code=end

