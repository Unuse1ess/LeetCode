#pragma once

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
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
std::ostream& operator<<(std::ostream& os, const TreeNode* _root);


extern "C" {
    void test();
}
