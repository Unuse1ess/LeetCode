/*
 * @lc app=leetcode.cn id=199 lang=cpp
 *
 * [199] 二叉树的右视图
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
    vector<int> rightSideView(TreeNode* root) {
        if (!root) {
            return vector<int> {};
        }

        vector<int> ans;
        ans.push_back(root->val);

        queue<pair<TreeNode*, size_t>> q;
        q.push({ root, 0 });
        while (q.size()) {
            auto tmp = q.front();
            TreeNode* node = tmp.first;
            size_t level = tmp.second;
            q.pop();

            // prev_lvl = level;
            if (ans.size() == level) {
                ans.push_back(node->val);
            } else {
                ans[level] = node->val;
            }

            if (node->left) {
                q.push({ node->left, level + 1 });
            }
            if (node->right) {
                q.push({ node->right, level + 1 });
            }
        }
        return ans;
    }
};
// @lc code=end

void test() {
    Solution s;

    vector<const char*> data = { "1", "2", "3", "null", "5", "null", "4" };
    TreeNode* root = TreeNode::create_tree(data);
    cout << s.rightSideView(root) << endl;
    delete[] root;

    data = { "1", "2", "3", "4", "null", "null", "null", "5" };
    root = TreeNode::create_tree(data);
    cout << s.rightSideView(root) << endl;
    delete[] root;

    data = { "1", "null", "3" };
    root = TreeNode::create_tree(data);
    cout << s.rightSideView(root) << endl;
    delete[] root;

    data = {};
    root = TreeNode::create_tree(data);
    cout << s.rightSideView(root) << endl;
    delete[] root;
}