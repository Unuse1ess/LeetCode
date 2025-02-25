/*
 * @lc app=leetcode.cn id=450 lang=cpp
 *
 * [450] 删除二叉搜索树中的节点
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
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode** prev = searchBST(&root, key);
        if (!prev)
            return root;
        TreeNode* node = *prev;
        if (node->left == nullptr && node->right == nullptr) {
            *prev = nullptr;
            return root;
        }

        if (node->left) {
            TreeNode* rmost = node->left;
            while (rmost->right) {
                rmost = rmost->right;
            }

            rmost->right = node->right;
            (*prev) = node->left;
        } else {
            (*prev) = node->right;
        }
        return root;
    }

    TreeNode** searchBST(TreeNode** root, int val) {
        TreeNode* cur = *root;
        TreeNode** prev = root;

        while (cur) {
            if (cur->val < val) {
                prev = &(cur->right);
                cur = cur->right;
            } else if (cur->val > val) {
                prev = &(cur->left);
                cur = cur->left;
            } else {
                return prev;
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

    data = { "5", "3", "6", "2", "4", "null", "7" };
    root = TreeNode::create_tree(data);
    cout << s.deleteNode(root, 3) << endl;
    delete[] root;

    data = { "5", "3", "6", "2", "4", "null", "7" };
    root = TreeNode::create_tree(data);
    cout << s.deleteNode(root, 0) << endl;
    delete[] root;

    data = {};
    root = TreeNode::create_tree(data);
    cout << s.deleteNode(root, 0) << endl;
    delete[] root;

    data = { "5", "3", "6", "2", "4", "null", "7" };
    root = TreeNode::create_tree(data);
    cout << s.deleteNode(root, 5) << endl;
    delete[] root;

    data = { "5", "3", "6", "2", "4", "null", "7" };
    root = TreeNode::create_tree(data);
    cout << s.deleteNode(root, 4) << endl;
    delete[] root;

    /* [2] */
    data = { "1", "null", "2" };
    root = TreeNode::create_tree(data);
    cout << s.deleteNode(root, 1) << endl;
    delete[] root;
}