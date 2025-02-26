/*
 * @lc app=leetcode.cn id=547 lang=cpp
 *
 * [547] 省份数量
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        size_t N = isConnected.size();
        bitset<256> visited;
        function<void(int)> dfs = [&](int node) {
            visited[node] = true;
            for (size_t i = 0; i < N; i++) {
                if (isConnected[node][i] == 1 && !visited[i]) {
                    dfs(i);
                }
            }
        };

        int ret = 0;
        for (size_t i = 0; i < N; i++) {
            if (!visited[i]) {
                dfs(i);
                ret++;
            }
        }

        return ret;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<vector<int>> input;

    input = { {1, 1, 0}, {1, 1, 0}, {0, 0, 1} };
    cout << s.findCircleNum(input) << endl;

    input = { {1, 0, 0}, {0, 1, 0}, {0, 0, 1} };
    cout << s.findCircleNum(input) << endl;
}
