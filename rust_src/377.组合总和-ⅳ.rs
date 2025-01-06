/*
 * @lc app=leetcode.cn id=377 lang=rust
 *
 * [377] 组合总和 Ⅳ
 */

/*
dp[i] = sum{0 <= j < nums.len(), nums[j] <= i | dp[i - nums[j]]}
每次加起来的情况都是以nums[j]为首的情况。这样就考虑了顺序问题。
*/

// @lc code=start
impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
		let target = target as usize;
		let mut dp = vec![0; target + 1];

		dp[0] = 1;

		for i in 1..=target
		{
			for &num in &nums
			{
				if num <= i
				{
					dp[i] += dp[i - num as usize];
				}
			}
		}

		return dp[target as usize];
    }
}

// @lc code=end

