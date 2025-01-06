/*
 * @lc app=leetcode.cn id=22 lang=rust
 *
 * [22] 括号生成
 */

// @lc code=start
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
		let mut ans: Vec<Vec<String>> = Vec::with_capacity((n + 1) as usize);

		ans.push(vec![String::from("")]);
		ans.push(vec![String::from("()")]);

		if n < 2
		{
			return ans.remove(n as usize);
		}

		for i in 2..=n
		{
			let mut v = vec![];
			for j in 0..i
			{
				for s1 in &ans[j as usize]
				{
					for s2 in &ans[(i - j - 1) as usize]
					{
						let mut s = String::from("(");

						s.push_str(s1);
						s.push(')');
						s.push_str(s2);

						v.push(s);
					}
				}
			}
			ans.push(v);
		}

		return ans.remove(n as usize);
    }

}
// @lc code=end

