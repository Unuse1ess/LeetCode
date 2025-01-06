/*
 * @lc app=leetcode.cn id=416 lang=rust
 *
 * [416] 分割等和子集
 */

/*
dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]	if j >= nums[i]
		 = dp[i - 1][j]								if j < nums[i]

dp[i][j]表示nums[0]到nums[i]是否存在某几个数，其和为j。
若nums[i]小于j，那么可做两种选择:加上nums[i]或者不加。
由于每个数只能选择一次，每次只能用前面的结果来判断。即前
一次的某个结果加上nums[i]后显然是可能的组合，且保证了没有
重复使用。若和x已经存在于前一次的结果当中，那么显然当前区间
也是存在这种组合的。
*/

// @lc code=start
impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
		let (sum, max) = nums.iter().fold((0, usize::MIN), |(sum, max), &v| {
			(sum + v as usize, max.max(v as usize))
		});

		if sum & 1 == 1
		{
			return false;
		}
		
		let half = sum >> 1;
		if max > half
		{
			return false;
		}

		let mut dp0 = vec![false; half + 1];
		dp0[0] = true;
		dp0[nums[0] as usize] = true;

		for v in nums.into_iter().skip(1)
		{
			let mut dp1 = vec![false; half + 1];
			dp1[0] = true;

			for j in 1..=half
			{
				if j >= v as usize
				{
					dp1[j] = dp0[j] || dp0[j - v as usize];
				}
				else
				{
					dp1[j] = dp0[j];
				}
			}
			dp0 = dp1;
		}

		return dp0[half];
    }
}
// @lc code=end

