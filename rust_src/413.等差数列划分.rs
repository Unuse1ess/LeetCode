/*
 * @lc app=leetcode.cn id=413 lang=rust
 *
 * [413] 等差数列划分
 */

/*
len[i] = len[i - 1] + 1 if nums[i] - nums[i - 1] = nums[i - 1] - nums[i - 2]
		 2				if nums[i] - nums[i - 1] != nums[i - 1] - nums[i - 2]
dp[i] = dp[i - 1] + len[i] - 2

[1..n]的长度至少为3的连续子序列（包括自身）个数为1 + 2 + ... + (n - 2)。
在遍历nums时，统计长度至少为3的等差子序列最长的长度。
经观察可得每次当前的等差子序列长度增加1时，当前子序列的等差子序列个数为上
一次的结果减2。
*/

// @lc code=start
impl Solution {
    pub fn number_of_arithmetic_slices(mut nums: Vec<i32>) -> i32 {
		if nums.len() < 3
		{
			return 0;
		}

		let mut diff = nums[1] - nums[0];
		let mut res = 0;
		let mut idx = 0;

		nums[0] = 2;

		for i in 2..nums.len()
		{
			if diff != nums[i] - nums[i - 1]
			{
				if nums[idx] > 2
				{
					idx += 1;
					nums[idx] = 2;
				}
				diff = nums[i] - nums[i - 1];
			}
			else
			{
				nums[idx] += 1;
				res += nums[idx] - 2;
			}
		}

		return res;
    }
}
// @lc code=end

