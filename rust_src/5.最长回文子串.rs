/*
 * @lc app=leetcode.cn id=5 lang=rust
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (34.54%)
 * Likes:    3796
 * Dislikes: 0
 * Total Accepted:    631.4K
 * Total Submissions: 1.8M
 * Testcase Example:  '"babad"'
 *
 * 给你一个字符串 s，找到 s 中最长的回文子串。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "cbbd"
 * 输出："bb"
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：s = "a"
 * 输出："a"
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：s = "ac"
 * 输出："a"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * s 仅由数字和英文字母（大写和/或小写）组成
 * 
 * 
 */

// @lc code=start
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
		if s.len() <= 1
		{
			return s;
		}

		let arr = Self::insert_byte(s.as_bytes());
		let (mut last_idx, mut last) = (0, arr[0]);
		let (mut cur_idx, mut cur) = (1, arr[1]);

		let mut start = 0;
		let mut end = 1;
		let mut i = 1;

		loop
		{
			i += 1;

			if i == arr.len()
			{
				break;
			}
			let c = arr[i];
			if c == last
			{
				let ret = Self::check(&arr, last_idx, i);
				if ret.1 - ret.0 > end - start
				{
					start = ret.0;
					end = ret.1;
				}
			} 
			else if c == cur
			{
				let ret = Self::check(&arr, cur_idx, i);
				if ret.1 - ret.0 > end - start
				{
					start = ret.0;
					end = ret.1;
				}
			}

			last = cur;
			cur = c;

			cur_idx += 1;
			last_idx += 1;
		}
		
		if start != 0
		{
			start = start >> 1;
		}
		if end != 0
		{
			end = (end - 1) >> 1;
		}

		return String::from(&s[start..end]);
    }

	pub fn insert_byte(s: &[u8]) -> Vec<u8>
	{
		let mut v: Vec<u8> = Vec::with_capacity(2 * s.len() + 1);
		v.push(b'_');

		for &c in s
		{
			v.push(c);
			v.push(b'_');
		}

		return v;
	}

	pub fn check(s: &[u8], mut left: usize, mut right: usize) -> (usize, usize)
	{
		while s[left] == s[right]
		{
			if left == 0
			{
				return (left, right + 1);
			}
			if right == s.len() - 1
			{
				return (left, right + 1);
			}

			left -= 1;
			right += 1;
		}

		return (left + 1, right);
	}
}
// @lc code=end

