/*
 * @lc app=leetcode.cn id=70 lang=rust
 *
 * [70] 爬楼梯
 */

// @lc code=start
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
		if n == 1
		{
			return 1;
		}
		if n == 2
		{
			return 2;
		}

		let mut dp0 = 1;
		let mut dp1 = 2;

		for i in 2..n
		{
			dp1 = dp1 + dp0;
			dp0 = dp1 - dp0;
		}

		return dp1;
    }
}
// @lc code=end

