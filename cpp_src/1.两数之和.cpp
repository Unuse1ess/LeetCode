/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */
#include <iostream>
#include <vector>
#include <unordered_map>

#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;
        unordered_map<int, int> map;

        for (auto n : nums) {
            auto it = map.find(n);
            if (it == map.end()) {
                map.insert({ target - n, i });
            } else {
                return vector<int> {it->second, i};
            }
            i++;
        }

        return vector<int> {0, 1};
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<int> nums = { 2, 7, 11, 15 };
    cout << s.twoSum(nums, 9) << endl;

    nums = { 3, 2, 4 };
    cout << s.twoSum(nums, 6) << endl;

    nums = { 3, 3 };
    cout << s.twoSum(nums, 6) << endl;
}
