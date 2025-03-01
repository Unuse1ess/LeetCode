/*
 * @lc app=leetcode.cn id=994 lang=cpp
 *
 * [994] 腐烂的橘子
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        static const vector<pair<int, int>> dir = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
        queue<tuple<int, int, int>> q;
        const int h = grid.size(), w = grid[0].size();
        size_t fresh = 0;
        int ans = 0;

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (grid[i][j] == 2) {
                    q.emplace(i, j, 0);
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }
        while (q.size()) {
            auto& [x, y, step] = q.front();
            for (auto& [dx, dy] : dir) {
                int tx = x + dx, ty = y + dy;
                ans = step;
                if (tx >= 0 && tx < h && ty >= 0 && ty < w && grid[tx][ty] == 1) {
                    grid[tx][ty] = 2;
                    fresh--;
                    q.emplace(tx, ty, step + 1);
                }
            }

            q.pop();
        }
        return fresh ? -1 : ans;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<vector<int>> grid;

    grid = { {2,1,1},{1,1,0},{0,1,1} };
    cout << s.orangesRotting(grid) << endl;

    grid = { {2,1,1},{0,1,1},{1,0,1} };
    cout << s.orangesRotting(grid) << endl;

    grid = { {0,2} };
    cout << s.orangesRotting(grid) << endl;

    // 1
    grid = { {1, 2} };
    cout << s.orangesRotting(grid) << endl;
}