/*
 * @lc app=leetcode.cn id=4 lang=rust
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
fn find_kth(mut v1: &[i32], mut v2: &[i32], mut k: usize) -> i32
{
	loop
	{
		let step = if k >> 1 == 0 { 1 } else { k >> 1 };
		let m = if step - 1 >= v1.len() { if v1.len() == 0 {0} else {v1.len() - 1} } else { step - 1 };
		let n = if step - 1 >= v2.len() { if v2.len() == 0 {0} else {v2.len() - 1} } else { step - 1 };

		match (v1.get(m), v2.get(n))
		{
			(Some(a), Some(b)) =>
			{
				if a < b
				{
					if k == 1
					{
						return *a;
					}
					v1 = &v1[(m + 1)..];
					k -= m + 1;
				}
				else
				{
					if k == 1
					{
						return *b;
					}
					v2 = &v2[(n + 1)..];
					k -= n + 1;
				}
			},
			(Some(_), None) =>
			{
				return *v1.get(k - 1).unwrap();
			},
			(None, Some(_)) =>
			{
				return *v2.get(k - 1).unwrap();
			},
			(None, None) =>
			{
				return 0;
			}
		}
	}
}


impl Solution{
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
		let l = nums1.len() + nums2.len();
		if l & 1 == 1
		{
			find_kth(&nums1[..], &nums2[..], (l >> 1) + 1) as f64
		}
		else
		{
			(find_kth(&nums1[..], &nums2[..], (l >> 1) + 1) as f64 +
			find_kth(&nums1[..], &nums2[..], l >> 1) as f64) / 2.0
		}
	}
}
// @lc code=end

/*
struct Mix<'a>
{
	it1: std::slice::Iter<'a, i32>,
	m: Option<&'a i32>,
	it2: std::slice::Iter<'a, i32>,
	n: Option<&'a i32>,
}

impl<'a> Mix<'a>
{
	pub fn new(nums1: &'a [i32], nums2: &'a [i32]) -> Self
	{
		let mut obj = Mix
		{
			it1: nums1.iter(),
			m: None,
			it2: nums2.iter(),
			n: None,
		};

		obj.m = obj.it1.next();
		obj.n = obj.it2.next();

		return obj;
	}

	pub fn smaller(m: Option<&'a i32>, n: Option<&'a i32>) -> bool
	{
		if m.is_none()
		{
			return false;
		}
		if n.is_none()
		{
			return true;
		}

		return m.unwrap() < n.unwrap();
	}
}

impl<'a> Iterator for Mix<'a>
{
	type Item = &'a i32;

	fn next(&mut self) -> Option<Self::Item>
	{
		let ret: Option<Self::Item>;

		if self.m.is_none() && self.n.is_none()
		{
			return None;
		}

		if Mix::smaller(self.n, self.m)
		{
			ret = self.n;
			self.n = self.it2.next();
		}
		else
		{
			ret = self.m;
			self.m = self.it1.next();
		}

		return ret;
	}
}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
		let t_len = nums1.len() + nums2.len();
		let odd = t_len & 1 == 1;
		let mid_pos = t_len >> 1;
		let mut i = 0;
		let mix = Mix::new(&nums1[..], &nums2[..]);
		let mut last_num = 0;

		for &num in mix
		{
			if i == mid_pos
			{
				if odd
				{
					return num as f64;
				}
				else
				{
					return (last_num as f64 + num as f64) / 2.0;
				}
			}
			i += 1;
			last_num = num;
		}

		return 0.0;
    }
}
*/
