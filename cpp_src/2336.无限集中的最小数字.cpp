/*
 * @lc app=leetcode.cn id=2336 lang=cpp
 *
 * [2336] 无限集中的最小数字
 */
#include "utils.hpp"

using namespace std;

namespace s0 {
    class SmallestInfiniteSet {
    public:
        SmallestInfiniteSet() {
            cur = 1;
            heap.emplace(2000);
        }

        int popSmallest() {
            int ret = heap.top();
            if (cur < ret) {
                ret = cur;
                cur++;
            } else {
                heap.pop();
            }
            removed.emplace(ret);
            return ret;
        }

        void addBack(int num) {
            if (removed.erase(num)) {
                heap.emplace(num);
            }
        }
    private:
        priority_queue<int, vector<int>, greater<int>> heap;
        unordered_set<int> removed;
        int cur;
    };
} // namespace s0

// @lc code=start
class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() {
        cur = 1;
        s.emplace(2000);
    }

    int popSmallest() {
        int ret = *s.begin();
        if (cur < ret) {
            ret = cur;
            cur++;
        } else {
            s.erase(ret);
            if (cur == ret) {
                cur++;
            }
        }
        return ret;
    }

    void addBack(int num) {
        s.emplace(num);
    }
private:
    set<int> s;
    int cur;
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */
// @lc code=end

vector<string>& invoker(vector<string>& methods, vector<vector<int>>& params, vector<string>& results) {
    SmallestInfiniteSet* obj;
    for (size_t i = 0; i < methods.size(); i++) {
        if (methods[i] == "SmallestInfiniteSet") {
            obj = new SmallestInfiniteSet();
            results.emplace_back("null");
        } else if (methods[i] == "addBack") {
            obj->addBack(params[i][0]);
            results.emplace_back("null");
        } else if (methods[i] == "popSmallest") {
            stringstream ss;
            ss << obj->popSmallest();
            results.emplace_back(ss.str());
        }
    }
    delete obj;
    return results;
}

void test() {
    vector<string> methods;
    vector<vector<int>> params;
    vector<string> results;

    SmallestInfiniteSet obj;
    methods = { "SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest" };
    params = { {}, { 2 }, {}, {}, {}, { 1 }, {}, {}, {} };

    cout << invoker(methods, params, results) << endl;
}
