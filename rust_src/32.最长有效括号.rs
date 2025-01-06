/*
 * @lc app=leetcode.cn id=32 lang=rust
 *
 * [32] 最长有效括号
 */

// @lc code=start
impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
		if s.len() < 2
		{
			return 0;
		}

		let mut s = s.as_bytes();
		let mut i = 0;
		let mut max = 0;

		while let Some(b')') = s.get(i)
		{
			i += 1;
		}

		s = &s[i..];

		let mut dp: Vec<usize> = Vec::with_capacity(s.len());

		// Initialize state
		for i in 0..s.len()
		{
			if s[i] == b'(' && Some(&b')') == s.get(i + 1)
			{
				dp.push(i + 1);
			}
			else
			{
				dp.push(i);
			}
		}
		
		loop
		{
			let mut changed = false;

			for i in 0..dp.len()
			{
				if dp[i] != i
				{
					if dp[i] + 1 < dp.len() && dp[i] + 1 != dp[dp[i] + 1]
					{
						let tmp = dp[i];

						dp[i] = dp[dp[i] + 1];
						dp[tmp + 1] = tmp + 1;
						changed = true;
					}
					if i != 0 && dp[i] + 1 < dp.len() && s[i - 1] == b'(' && s[dp[i] + 1] == b')'
					{
						dp[i - 1] = dp[i] + 1;
						dp[i] = i;
						changed = true;
					}
					if max < dp[i] - i
					{
						max = dp[i] - i;
					}
				}
			}
			if !changed
			{
				break;
			}
		}

		return if max == 0 { 0 } else { max + 1 } as i32; 
    }
}
// @lc code=end

