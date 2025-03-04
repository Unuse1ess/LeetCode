/*
 * @lc app=leetcode.cn id=2542 lang=cpp
 *
 * [2542] 最大子序列的分数
 */
#include "utils.hpp"

using namespace std;

class Solution0 {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        const size_t N = nums1.size();
        vector<int> idx(N);
        priority_queue<int, vector<int>, greater<int>> heap;
        for (size_t i = 0; i < N; i++) {
            idx[i] = i;
        }
        sort(idx.begin(), idx.end(), [&](int& a, int& b) {
            return nums2[a] > nums2[b];
        });
        long long s = 0;
        for (int i = 0; i < k; i++) {
            s += nums1[idx[i]];
            heap.emplace(nums1[idx[i]]);
        }
        long long ans = s * nums2[idx[k - 1]];

        // cout << idx << endl;
        for (size_t i = k; i < N; i++) {
            if (nums1[idx[i]] > heap.top()) {
                s += nums1[idx[i]] - heap.top();
                heap.pop();
                heap.emplace(nums1[idx[i]]);
                long long tmp = s * nums2[idx[i]];
                if (tmp > ans) {
                    ans = tmp;
                }
            }
        }

        return ans;
    }
};

// @lc code=start
class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        const size_t N = nums1.size();
        vector<pair<int, int>> pairs;
        priority_queue<int, vector<int>, greater<int>> heap;

        for (size_t i = 0; i < N; i++) {
            pairs.emplace_back(nums1[i], nums2[i]);
        }

        sort(pairs.begin(), pairs.end(), [](pair<int, int>& a, pair<int, int>& b) {
            return a.second > b.second;
        });

        long long s = 0;
        for (int i = 0; i < k; i++) {
            s += pairs[i].first;
            heap.emplace(pairs[i].first);
        }
        long long ans = s * pairs[k - 1].second;
        const int& tp = heap.top();
        for (size_t i = k; i < N; i++) {
            if (pairs[i].first > tp) {
                s += pairs[i].first - tp;
                heap.pop();
                heap.emplace(pairs[i].first);
                long long tmp = s * pairs[i].second;
                if (tmp > ans) {
                    ans = tmp;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<int> nums1, nums2;

    // 12
    nums1 = { 1,3,3,2 };
    nums2 = { 2,1,3,4 };
    cout << s.maxScore(nums1, nums2, 3) << endl;

    // 30
    nums1 = { 4,2,3,1,1 };
    nums2 = { 7,5,10,9,6 };
    cout << s.maxScore(nums1, nums2, 1) << endl;

    // 168
    nums1 = { 2,1,14,12 };
    nums2 = { 11,7,13,6 };
    cout << s.maxScore(nums1, nums2, 3) << endl;
}
