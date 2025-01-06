/*
 * @lc app=leetcode.cn id=13 lang=rust
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
		let mut res = 0;
		let mut last = ' ';

		for c in s.chars().rev()
		{
			match c
			{
				'I' =>
				{
					if last == 'V' || last == 'X'
					{
						res -= 1;
					}
					else
					{
						res += 1;
					}
				}
				'X' =>
				{
					if last == 'L' || last == 'C'
					{
						res -= 10;
					}
					else
					{
						res += 10;
					}
				}
				'C' =>
				{
					if last == 'D' || last == 'M'
					{
						res -= 100;
					}
					else
					{
						res += 100;
					}
				}
				'V' => res += 5,
				'L' => res += 50,
				'D' => res += 500,
				'M' => res += 1000,
				_ => (),
			}

			last = c;
		}

		return res;
    }
}
// @lc code=end

