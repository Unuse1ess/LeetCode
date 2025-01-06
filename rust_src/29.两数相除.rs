/*
 * @lc app=leetcode.cn id=29 lang=rust
 *
 * [29] 两数相除
 */

// @lc code=start
impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
		if dividend == i32::MIN && divisor == -1
		{
			return i32::MAX;
		}
		if divisor == 0
		{
			return i32::MAX;
		}

		return match (dividend < 0, divisor < 0)
		{
			(true, true) => Self::div(!(dividend) as u32 + 1, !(divisor) as u32 + 1) as i32,
			(true, false) => -(Self::div(!(dividend) as u32 + 1, divisor as u32) as i32),
			(false, true) => -(Self::div(dividend as u32, !(divisor) as u32 + 1) as i32),
			(false, false) => Self::div(dividend as u32, divisor as u32) as i32,
		};
	}

	pub fn div(mut a: u32, b: u32) -> u32
	{
		let b_len = Self::get_digit_num(b);
		let mut res = 0;

		while a >= b
		{
			let a_len = Self::get_digit_num(a);
			let mut diff = a_len - b_len;
			
			if a < (b << diff)
			{
				diff -= 1;
			}
			res |= 1 << diff;
			a -= b << diff;
		}
		
		return res;
	}
	pub fn get_digit_num(mut num: u32) -> u32
	{
		use std::num::Wrapping;
		let mut i = Wrapping(u32::MAX);

		while num > 0
		{
			num >>= 1;
			i += Wrapping(1); 
		}

		return i.0;
	}
}
// @lc code=end

