/*
 * @lc app=leetcode.cn id=700 lang=cpp
 *
 * [700] 二叉搜索树中的搜索
 */
#include "utils.hpp"

using namespace std;

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* cur = root;

        while (cur) {
            if (cur->val < val) {
                cur = cur->right;
            } else if (cur->val > val) {
                cur = cur->left;
            } else {
                return cur;
            }
        }
        return nullptr;
    }
};
// @lc code=end

void test() {
    Solution s;
    vector<const char*> data;
    TreeNode* root;

    data = { "4", "2", "7", "1", "3" };
    root = TreeNode::create_tree(data);
    cout << s.searchBST(root, 2) << endl;
    delete[] root;

    data = { "4", "2", "7", "1", "3" };
    root = TreeNode::create_tree(data);
    cout << s.searchBST(root, 5) << endl;
    delete[] root;
}
