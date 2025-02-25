#pragma once

#include <vector>
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
