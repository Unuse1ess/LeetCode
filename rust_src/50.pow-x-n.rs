/*
 * @lc app=leetcode.cn id=50 lang=rust
 *
 * [50] Pow(x, n)
 */

// @lc code=start
impl Solution {
    pub fn my_pow(mut x: f64, mut n: i32) -> f64 {
		if n == 0
		{
			return 1.0;
		}

		if x == 1.0 || x == 0.0
		{
			return x;
		}
		if x == -1.0
		{
			return if n & 1 == 1 { -1.0 } else { 1.0 };
		}

		if n < -100
		{
			return 0.0;
		}

		if n < 0
		{
			x = 1.0 / x;
			n = -n;
		}

		let mut res = 1.0;
		
		while n != 0
		{
			if n & 1 == 1
			{
				res *= x;
			}
			x *= x;
			n >>= 1;
		}

		return res;
    }
}
// @lc code=end

