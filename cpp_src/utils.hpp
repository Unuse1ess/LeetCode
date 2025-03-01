#pragma once

#include <cstdint>
#include <algorithm>
#include <functional>
#include <vector>
#include <unordered_map>
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


std::ostream& operator<<(std::ostream& os, const std::vector<int>& v);
std::ostream& operator<<(std::ostream& os, const std::vector<double>& v);
std::ostream& operator<<(std::ostream& os, const TreeNode* root);


extern "C" {
    void test();
}
