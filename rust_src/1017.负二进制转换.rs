/*
 * @lc app=leetcode.cn id=1017 lang=rust
 *
 * [1017] 负二进制转换
 */

// @lc code=start
impl Solution {
    pub fn base_neg2(mut n: i32) -> String {
		if n == 0
		{
			return String::from("0");
		}
		let mut res = Vec::new();
		while n != 0
		{
			let mut r = n % -2;
			if r == -1
			{
				r = 1;
				n -= 1;
			}
			res.push(r as u8 + b'0');
			n /= -2;
		}

		return String::from_utf8(res.into_iter().rev().collect()).unwrap();
	}
}

// @lc code=end

