/*
 * @lc app=leetcode.cn id=300 lang=rust
 *
 * [300] 最长递增子序列
 */

/*
时间复杂度为O(n^2)的动态规划解法：
dp[i] = max{j∈[0, i], nums[i] > nums[j] | 1 + dp[j]}

dp[i]表示以nums[i]为子序列最后一个元素的情况下子序列的长度。
初始状态为1，意思是每个元素本身是长度为1的子序列。
只要每次从以前的结果当中选出子序列小于nums[i]、长度最大的来+1，那么当前结果就是
以nums[i]结尾最长的长度，显然nums[i]是子序列里最大的数，且是最后一个数。

进阶：
如果需要给出最长上升的子序列，则dp[i]需要记录以nums[i]结尾的最长递增子序列，
当nums[i]比之前的某个nums[j]大时，复制dp[j]到暂时的序列，并往其结尾附加
nums[i]，选取长度最长的那个赋到dp[i]。


时间复杂度为O(nlogn)的动态规划解法：
nums[i] > dp[len]:
	dp[len + 1] = nums[i]
	len = len + 1
nums[i] < dp[len]:
	dp[pos] = nums[i]，其中pos满足dp[pos] < nums[i] < dp[pos + 1]

dp[i]表示以i为长度的子序列最后面的元素。len表示当前最大子序列长度。
若nums[i]比当前子序列最后的元素（即dp[len],也是最大的）还要大，那么可以扩充子序列，
把nums[i]加入其后。由此可以推出dp是递增的，可以对其使用二分搜索。
若nums[i]比dp[len]小，那么替换最小的比nums[i]大的那个数，使对应的子序列以尽可能
缓地上升。
*/
// @lc code=start
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
		if nums.len() == 1
		{
			return 1;
		}

		let mut dp: Vec<i32> = Vec::with_capacity(nums.len());
		let mut len = 0;

		dp.push(nums[0]);

		for v in nums.into_iter().skip(1)
		{
			if v > dp[len]
			{
				len += 1;
				dp.push(v);
			}
			else
			{
				if v <= dp[0]
				{
					dp[0] = v;
					continue;
				}
				let pos = Self::bin_search(&dp[..], v);
				dp[pos + 1] = v;
			}
		}
		
		return len as i32 + 1;
    }
	fn bin_search(arr: &[i32], v: i32) -> usize
	{
		let mut left = 0;
		let mut right = arr.len();

		loop
		{
			if right - left == 1
			{
				break;
			}

			let mid = (left + right) >> 1;

			if arr[mid] > v
			{
				right = mid;
			}
			else if arr[mid] < v
			{
				left = mid;
			}
			else
			{
				left = mid - 1;
				right = mid;
			}
		}
		return left;
	}
}
// @lc code=end

/*
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
		use std::cmp::max;

		if nums.len() == 0
		{
			return 0;
		}

		let mut dp = vec![1; nums.len()];
		let mut res = 1;

		for i in 1..nums.len()
		{
			for j in 0..i
			{
				if nums[j] < nums[i]
				{
					dp[i] = max(dp[i], dp[j] + 1);
				}
			}
			res = max(res, dp[i]);
		}

		return res;
    }
}
*/