/*
 * @lc app=leetcode.cn id=12 lang=rust
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
impl Solution {
    pub fn int_to_roman(num: i32) -> String {
		let mut i = num;
		let mut j = 0;
		let mut res = String::new();
		let arr = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
					["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
					["" , "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
					["", "M", "MM", "MMM", "", "", "", "", "", ""]];

		while i != 0
		{
			let digit = i % 10;
			i /= 10;
			res.insert_str(0, arr[j][digit as usize]);
			j += 1;
		}
		
		return res;
    }
}

// @lc code=end

