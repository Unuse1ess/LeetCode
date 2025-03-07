/*
 * @lc app=leetcode.cn id=2300 lang=cpp
 *
 * [2300] 咒语和药水的成功对数
 */
#include "utils.hpp"
using namespace std;

// 使用float会有精度损失导致WA。

// @lc code=start
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> ans(spells.size());
        sort(potions.begin(), potions.end());

        for (size_t i = 0; i < spells.size(); i++) {
            ans[i] = bi_search(potions, (uint64_t)ceil((double)success / (double)spells[i]));
        }

        return ans;
    }

    int bi_search(vector<int>& v, uint64_t target) {
        int l = 0, r = (int)v.size() - 1;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if ((uint64_t)v[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return (int)v.size() - l;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<int> spells;
    vector<int> potions;

    spells = { 5, 1, 3 }, potions = { 1, 2, 3, 4, 5 };
    cout << s.successfulPairs(spells, potions, 7) << endl;

    spells = { 3, 1, 2 }, potions = { 8, 5, 8 };
    cout << s.successfulPairs(spells, potions, 16) << endl;
}