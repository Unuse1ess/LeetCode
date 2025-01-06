/*
 * @lc app=leetcode.cn id=198 lang=rust
 *
 * [198] 打家劫舍
 */


// 若选择偷，i + 2与i中间隔着i + 1，不触发警报。
// 若选择不偷，即便i + 1选择偷了，i也不触发警报。
// 选择两者中收益大的即可。

// dp[i] = max{dp[i + 1], dp[i + 2] + nums[i]}

// @lc code=start
impl Solution {
    pub fn rob(mut nums: Vec<i32>) -> i32 {
		use std::cmp::max;

		if nums.len() == 1
		{
			return nums[0];
		}
		if nums.len() == 2
		{
			return max(nums[0], nums[1]);
		}

		let mut dp0 = nums.pop().unwrap();
		let mut dp1 = max(nums.pop().unwrap(), dp0);

		while let Some(v) = nums.pop()
		{
			let dp2 = max(dp0 + v, dp1);
			dp0 = dp1;
			dp1 = dp2;
		}
		
		return dp1;
    }
}
// @lc code=end

/*
use std::collections::HashMap;
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
		let mut cache: HashMap<&[i32], i32> = HashMap::new();
		return Self::r(&nums[..], &mut cache);
    }
	pub fn r<'a>(nums: &'a [i32], cache: &mut HashMap<&'a [i32], i32>) -> i32
	{
		use std::cmp::max;

		if nums.len() == 1
		{
			return nums[0]
		}
		if nums.len() == 2
		{
			return max(nums[0], nums[1]);
		}

		if let Some(&v) = cache.get(nums)
		{
			return v;
		}
		
		let mut res = 0;

		for i in 0..nums.len()
		{
			let tmp;
			if i == 0 || i == 1
			{
				tmp = nums[i] + Self::r(&nums[i + 2..], cache);
			}
			else if i == nums.len() - 2 || i == nums.len() - 1
			{
				tmp = nums[i] + Self::r(&nums[..i - 1], cache);
			}
			else
			{
				tmp = nums[i] + Self::r(&nums[..i - 1], cache) + Self::r(&nums[i + 2..], cache);
			}
			res = max(res, tmp);
		}

		cache.insert(nums, res);
		
		return res;
	}
}
*/
