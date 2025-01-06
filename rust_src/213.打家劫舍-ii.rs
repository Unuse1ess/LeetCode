/*
 * @lc app=leetcode.cn id=213 lang=rust
 *
 * [213] 打家劫舍 II
 */

// @lc code=start
use std::cmp::max;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
		if nums.len() == 1
		{
			return nums[0];
		}
		if nums.len() == 2
		{
			return max(nums[0], nums[1]);
		}
		
		let a = Self::r(&nums[..(nums.len() - 1)]);
		let b = Self::r(&nums[1..]);
		
		return max(a, b);
	}
	
    pub fn r(nums: &[i32]) -> i32 {
		let mut it = nums.iter();

		let mut dp0 = *it.next().unwrap();
		let mut dp1 = *it.next().unwrap();

		dp1 = max(dp1, dp0);

		while let Some(&v) = it.next()
		{
			let tmp = max(dp0 + v, dp1);
			dp0 = dp1;
			dp1 = tmp;
		}

		return dp1;
	}
}
// @lc code=end

