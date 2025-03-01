/*
 * @lc app=leetcode.cn id=1926 lang=cpp
 *
 * [1926] 迷宫中离入口最近的出口
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        static const vector<pair<int, int>> dir = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
        queue<tuple<int, int, int>> q({ { entrance[0], entrance[1], 0 } });
        int h = maze.size(), w = maze[0].size();

        while (q.size()) {
            auto& t = q.front();
            int x = get<0>(t), y = get<1>(t), step = get<2>(t);
            q.pop();

            if (x < 0 || x >= h || y < 0 || y >= w || maze[x][y] == '+') {
                continue;
            }
            if (step != 0 && (x == 0 || y == 0 || x == h - 1 || y == w - 1) && maze[x][y] == '.') {
                return step;
            }
            maze[x][y] = '+';

            for (auto& [dx, dy] : dir) {
                q.emplace(x + dx, y + dy, step + 1);
            }
        }
        return -1;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<vector<char>> maze;
    vector<int> entrance;

    maze = {
        {'+','+','.','+'},
        {'.','.','.','+'},
        {'+','+','+','.'}
    };
    entrance = { 1,2 };
    cout << s.nearestExit(maze, entrance) << endl;

    maze = {
        {'+','+','+'},
        {'.','.','.'},
        {'+','+','+'}
    };
    entrance = { 1,0 };
    cout << s.nearestExit(maze, entrance) << endl;

    maze = {
        {'.','+'}
    };
    entrance = { 0,0 };
    cout << s.nearestExit(maze, entrance) << endl;

    // -1
    maze = { {'.', '+', '.'} };
    entrance = { 0, 2 };
    cout << s.nearestExit(maze, entrance) << endl;
}