/*
 * @lc app=leetcode.cn id=1 lang=rust
 *
 * [1] 两数之和
 */

// @lc code=start
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
		use std::collections::HashMap;

		/*
		使用HashMap保存遍历结果，消掉一层遍历。
		nums中元素作为key，其下标作为value
		*/
		let mut m: HashMap<i32, usize> = HashMap::new();

		for i in 0..nums.len()
		{
			if let Some(v) = m.get(&(target - nums[i]))
			{
				return vec![*v as i32, i as i32];
			}
			m.insert(nums[i], i);
		}

		return vec![];
    }
}
// @lc code=end

