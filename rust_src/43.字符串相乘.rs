/*
 * @lc app=leetcode.cn id=43 lang=rust
 *
 * [43] 字符串相乘
 */

// @lc code=start
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
		let mut mid: Vec<Vec<u8>> = Vec::new();

		for c1 in num1.as_bytes().iter().rev()
		{
			if *c1 == b'0'
			{
				mid.push(vec![0]);
				continue;
			}

			let mut res = Vec::new();
			let mut carry = 0;
			let mut prod;
			
			for c2 in num2.as_bytes().iter().rev()
			{
				prod = (c1 - b'0') * (c2 - b'0') + carry;
				//println!("{} * {} + {} = {}", *c2 as char, *c1 as char, carry, prod);
				if prod > 9
				{
					carry = prod / 10;
					prod %= 10;
				}
				else
				{
					carry = 0;
				}
				res.push(prod);
			}

			if carry != 0
			{
				res.push(carry);
			}

			//println!("{:?}", res);
			mid.push(res);
		}
		
		return String::from_utf8(Self::add(mid)).unwrap();
    }

	fn add(nums: Vec<Vec<u8>>) -> Vec<u8>
	{
		let mut i = 0;
		let mut res = nums[0].clone();

		//println!("{:?}", nums);

		for m in nums.iter().skip(1)
		{
			//println!("{:?}", res);
			i += 1;

			if *m == vec![0]
			{
				continue;
			}

			let mut j = i;
			let mut carry = 0;

			for n in m
			{
				while j >= res.len()
				{
					res.push(0);
				}

				let mut sum = n + res[j] + carry;
				//println!("{}+{}+{}={}", n, res[j], carry, sum);

				if sum > 9
				{
					carry = 1;
					sum -= 10;
				}
				else
				{
					carry = 0;
				}

				res[j] = sum;
				j += 1;
			}

			if carry != 0
			{
				res.push(1);
			}
		}
		
		return res.into_iter().rev().map(|v| { v + b'0' }).collect();
	}
}
// @lc code=end

