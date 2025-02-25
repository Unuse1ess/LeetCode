/*
 * @lc app=leetcode.cn id=841 lang=cpp
 *
 * [841] 钥匙和房间
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        unordered_set<int> visited;
        queue<int> q({ 0 });

        while (q.size()) {
            int cur = q.front();
            q.pop();

            visited.emplace(cur);
            for (auto& i : rooms[cur]) {
                if (visited.find(i) == visited.end()) {
                    q.emplace(i);
                }
            }
        }

        return visited.size() == rooms.size();
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<vector<int>> rooms;

    rooms = { {1}, {2}, {3}, {} };
    cout << s.canVisitAllRooms(rooms) << endl;

    rooms = { {1, 3}, {3, 0, 1}, {2}, {0} };
    cout << s.canVisitAllRooms(rooms) << endl;
}
