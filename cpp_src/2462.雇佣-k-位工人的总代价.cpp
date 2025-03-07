/*
 * @lc app=leetcode.cn id=2462 lang=cpp
 *
 * [2462] 雇佣 K 位工人的总代价
 */
#include "utils.hpp"
using namespace std;

// @lc code=start
class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        priority_queue<int, vector<int>, greater<int>> heap1, heap2;

        int l = 0, r = costs.size() - 1;
        int cnt = 0;
        long long ans = 0;
        do {
            int tmp = candidates - (int)heap1.size();
            for (int i = 0; i < tmp && l <= r; i++, l++) {
                heap1.emplace(costs[l]);
            }

            tmp = candidates - (int)heap2.size();
            for (int i = 0; i < tmp && l <= r; i++, r--) {
                heap2.emplace(costs[r]);
            }
            int a = 200000, b = 200000, cost;
            if (heap1.size()) {
                a = heap1.top();
            }
            if (heap2.size()) {
                b = heap2.top();
            }

            if (a <= b) {
                cost = a;
                heap1.pop();
            } else {
                cost = b;
                heap2.pop();
            }

            ans += cost;
            cnt++;
        } while (cnt < k);
        return ans;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<int> costs;

    costs = { 17,12,10,2,7,2,11,20,8 };
    cout << s.totalCost(costs, 3, 4) << endl;

    costs = { 1,2,4,1 };
    cout << s.totalCost(costs, 3, 3) << endl;

    // 526
    costs = { 57,33,26,76,14,67,24,90,72,37,30 };
    cout << s.totalCost(costs, 11, 2) << endl;
}
