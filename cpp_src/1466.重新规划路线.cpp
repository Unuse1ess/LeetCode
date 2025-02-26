/*
 * @lc app=leetcode.cn id=1466 lang=cpp
 *
 * [1466] 重新规划路线
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        queue<int> q({ 0 });
        vector < vector<pair<int, bool>>> graph(n);
        vector<bool> visited(n, false);
        int ans = 0;

        for (auto& edge : connections) {
            graph[edge[0]].emplace_back(edge[1], true);
            graph[edge[1]].emplace_back(edge[0], false);
        }

        while (q.size()) {
            auto node = q.front();
            q.pop();
            visited[node] = true;

            for (auto& i : graph[node]) {
                if (!visited[i.first]) {
                    q.emplace(i.first);
                    if (i.second)
                        ans++;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<vector<int>> input;

    input = {
        {0,1},
        {1,3},
        {2,3},
        {4,0},
        {4,5},
    };
    cout << s.minReorder(6, input) << endl;

    input = {
        {1,0},
        {1,2},
        {3,2},
        {3,4},
    };
    cout << s.minReorder(5, input) << endl;

    input = {
        {1,0},
        {2,0},
    };
    cout << s.minReorder(3, input) << endl;

    // 0
    input = { {1,2},{2,0} };
    cout << s.minReorder(3, input) << endl;
}
