/*
 * @lc app=leetcode.cn id=399 lang=cpp
 *
 * [399] 除法求值
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, unordered_map<string, double>> graph;
        vector<double> ans;
        for (size_t i = 0; i < values.size(); i++) {
            graph[equations[i][0]][equations[i][1]] = values[i];
            graph[equations[i][1]][equations[i][0]] = 1. / values[i];
        }
        for (auto& query : queries) {
            double res = -1.;
            if (graph.contains(query[0]) && graph.contains(query[1])) {
                res = query[0] == query[1] ? 1. : bfs(graph, query[0], query[1]);
            }
            ans.emplace_back(res);
        }
        return ans;
    }

    double bfs(unordered_map<string, unordered_map<string, double>>& graph,
        const string& src, const string& target) {
        if (graph[src].contains(target))
            return graph[src][target];

        queue<string> q;
        unordered_set<string> visited;
        q.emplace(src);
        visited.emplace(src);
        while (q.size()) {
            auto& node = q.front();
            for (auto& t : graph[node]) {
                if (visited.find(t.first) == visited.end()) {
                    visited.emplace(t.first);
                    q.emplace(t.first);
                    auto val = t.second * graph[src][node];
                    graph[src].emplace(t.first, val);
                    graph[t.first].emplace(src, 1. / val);
                }
            }
            q.pop();
        }
        return graph[src].contains(target) ? graph[src][target] : -1.;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<vector<string>> equations;
    vector<double> values;
    vector<vector<string>> queries;

    equations = { {"a", "b"}, {"b", "c"} };
    values = { 2.0, 3.0 };
    queries = { {"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"} };
    cout << s.calcEquation(equations, values, queries) << endl;

    equations = { {"a", "b"}, {"b", "c"}, {"bc", "cd"} };
    values = { 1.5, 2.5, 5.0 };
    queries = { {"a", "c"}, {"c", "b"}, {"bc", "cd"}, {"cd", "bc"} };
    cout << s.calcEquation(equations, values, queries) << endl;

    equations = { {"a", "b"} };
    values = { 0.5 };
    queries = { {"a", "b"}, {"b", "a"}, {"a", "c"}, {"x", "y"} };
    cout << s.calcEquation(equations, values, queries) << endl;
}
