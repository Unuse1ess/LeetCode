#pragma once

#include <cmath>
#include <sstream>
#include <cstdint>
#include <algorithm>
#include <functional>
#include <vector>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <deque>
#include <bitset>
#include <memory>
#include <iostream>

struct TreeNode {
public:

    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode();
    TreeNode(int x);

    static TreeNode* create_tree(std::vector<const char*>& data);
};

std::ostream& operator<<(std::ostream& os, const TreeNode* root);

template<typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& v) {
    if (v.size() == 0) {
        return os << "[]";
    }
    os << "[";
    for (size_t i = 0; i < v.size(); i++) {
        os << v[i] << ", ";
    }

    return os << "\b\b]";
}

template<typename T1, typename T2 = T1>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
    return os << "(" << p.first << ", " << p.second << ")";
}

extern "C" {
    void test();
}
