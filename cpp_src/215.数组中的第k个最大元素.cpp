/*
 * @lc app=leetcode.cn id=215 lang=cpp
 *
 * [215] 数组中的第K个最大元素
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution0 {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, less<int>> q_max;
        priority_queue<int, vector<int>, greater<int>> q_min;

        q_min.emplace(nums[0]);

        for (size_t i = 1; i < nums.size(); i++) {
            int n = nums[i];
            if (n > q_min.top()) {
                q_min.emplace(n);
                if (q_min.size() > (size_t)k) {
                    q_max.emplace(q_min.top());
                    q_min.pop();
                }
            } else {
                q_max.emplace(n);
                if (q_min.size() < (size_t)k) {
                    q_min.emplace(q_max.top());
                    q_max.pop();
                }
            }
        }

        return q_min.top();
    }
};
class Solution1 {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> h_min;

        for (auto& n : nums) {
            h_min.emplace(n);
            if (h_min.size() > (size_t)k) {
                h_min.pop();
            }
        }
        return h_min.top();
    }
};
// @lc code=start
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        if (nums.size() == 1)
            return nums[0];
        uint32_t p[20001] = { 0 };
        uint32_t* _p = &p[10000];

        for (auto& n : nums) {
            _p[n]++;
        }
        int i = 10000;

        while (i >= -10000) {
            k -= _p[i];
            if (k <= 0) {
                return i;
            }
            i--;
        }
        return 0;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<int> nums;

    nums = { 3,2,1,5,6,4 };
    cout << s.findKthLargest(nums, 2) << endl;

    nums = { 3,2,3,1,2,4,5,5,6 };
    cout << s.findKthLargest(nums, 4) << endl;

    nums = { -12 };
    cout << s.findKthLargest(nums, 1) << endl;

    // 1
    nums = { 2, 1 };
    cout << s.findKthLargest(nums, 2) << endl;

    // 2
    nums = { 2, 1 };
    cout << s.findKthLargest(nums, 1) << endl;
}