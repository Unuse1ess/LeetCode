/*
 * @lc app=leetcode.cn id=357 lang=rust
 *
 * [357] 计算各个位数不同的数字个数
 */

/*
dp[i] = (dp[i - 1] - dp[i - 2]) * (10 - (i - 1)) + dp[i - 1]

在前一次不以0开头的组合的基础上往后加1位，再加上前一次的组合个数。
(dp[i - 1] - dp[i - 2])为前一位不以0开头的情况，即一定有i - 1位的情况，
后面可以组合(10 - (i - 1))个数。
*/

// @lc code=start
impl Solution {
    pub fn count_numbers_with_unique_digits(n: i32) -> i32 {
		let mut dp0 = 1;
		let mut dp1 = 10;

		if n == 0
		{
			return 1;
		}
		
		for i in 2..=n
		{
			let tmp = dp1;
			dp1 = (dp1 - dp0) * (11 - i) + dp1;
			dp0 = tmp;
		}

		return dp1;
    }
}
// @lc code=end

