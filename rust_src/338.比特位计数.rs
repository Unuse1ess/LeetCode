/*
 * @lc app=leetcode.cn id=338 lang=rust
 *
 * [338] 比特位计数
 */

// @lc code=start
impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
		let mut res = vec![0; n as usize + 1];
		let mut bit = 0;
		let mut mask = 0;

		(1..=n as usize).into_iter().for_each(|i| {
			if i & (i - 1) == 0
			{
				mask = (1 << bit) - 1;
				bit += 1;
			}

			res[i] = 1 + res[i & mask];
		});

		return res;
    }
}
// @lc code=end

