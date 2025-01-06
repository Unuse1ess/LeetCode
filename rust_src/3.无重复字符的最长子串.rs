/*
 * @lc app=leetcode.cn id=3 lang=rust
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
		use std::collections::HashMap;
		
		let mut set: HashMap<char, usize> = HashMap::new();
		let mut len = 0;

		for (i, c) in s.chars().enumerate()
		{
			if set.contains_key(&c)
			{
				let idx = *set.get(&c).unwrap();
				set.retain(|_k, v| *v > idx);
			}
			set.insert(c, i);
			if set.len() > len
			{
				len = set.len();
			}
		}

		return len as i32;
    }
}
// @lc code=end

