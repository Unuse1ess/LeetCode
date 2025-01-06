/*
 * @lc app=leetcode.cn id=9 lang=rust
 *
 * [9] 回文数
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
		if x < 0
		{
			return false;
		}
		let s = x.to_string();

		return s.chars().rev().collect::<String>() == s;
    }
}

// @lc code=end

