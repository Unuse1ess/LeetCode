/*
 * @lc app=leetcode.cn id=312 lang=rust
 *
 * [312] 戳气球
 */

/*
dp[i][j] = max{i < k < j | nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]} if j - i >= 2
dp[i][j] = 0 if j - i < 2

题目中的正向操作是从数组中选一个数进行删除操作，那么其反向操作是不断的往
[1,1]这个数组中间不断插入一个数。显然往数组前后插入1不影响最终结果。
以题目描述中所给例子，则
[1,3,1,5,8,1] --> [1,3,5,8,1] --> [1,3,8,1] --> [1,8,1] --> [1,1]
以[1,5,3,8]的顺序删除，那么其等价于
[1,3,1,5,8,1] <-- [1,3,5,8,1] <-- [1,3,8,1] <-- [1,8,1] <-- [1,1]
以[8,3,5,1]的顺序插入，不影响最终结果。

那么dp[i][j]就可以表示为开区间(i,j)内最优插入顺序下的硬币数。
*/


// @lc code=start
impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32
	{
		use std::cmp::max;

		let get = |i: usize| {
			if i == 0 || i == nums.len() + 1
			{
				1
			}
			else
			{
				nums[i - 1]
			}
		};

		let mut dp = vec![vec![0; nums.len() + 2]; nums.len() + 2];
		for (i, &v) in nums.iter().enumerate()
		{
			dp[i][i + 2] = v;
		}

		for diff in 3..=dp.len()
		{
			for i in 0..=dp.len() - diff
			{
				let mut res = i32::MIN;
				let j = i + diff - 1;
				for k in i + 1..j
				{
					res = max(res, get(i) * get(k) * get(j) + dp[i][k] + dp[k][j]);
				}
				dp[i][j] = res;
			}
		}

		return dp[0][nums.len() + 1];
	}
}
// @lc code=end

