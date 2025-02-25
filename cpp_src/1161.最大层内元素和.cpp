/*
 * @lc app=leetcode.cn id=1161 lang=cpp
 *
 * [1161] 最大层内元素和
 */
#include "utils.hpp"

using namespace std;

class Solution0 {
public:
    int maxLevelSum(TreeNode* root) {
        int sum = -100000, max_sum = -100000, level = 1;
        queue<pair<TreeNode*, int>> q;

        int prev_lvl = 0;
        q.push({ root, 1 });
        while (q.size()) {
            auto tmp = q.front();
            q.pop();

            TreeNode* node = tmp.first;
            int cur_level = tmp.second;

            if (prev_lvl != cur_level) {
                if (sum > max_sum) {
                    max_sum = sum;
                    level = prev_lvl;
                }
                sum = 0;
            }
            sum += node->val;

            if (node->left)
                q.push({ node->left, cur_level + 1 });
            if (node->right)
                q.push({ node->right, cur_level + 1 });

            prev_lvl = cur_level;
        }
        if (sum > max_sum) {
            max_sum = sum;
            level = prev_lvl;
        }

        return level;
    }
};

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
    int maxLevelSum(TreeNode* root) {
        vector<int> d_sum;

        function<void(TreeNode*, size_t)> dfs = [&](TreeNode* root, size_t depth) {
            if (depth == d_sum.size()) {
                d_sum.push_back(root->val);
            } else {
                d_sum[depth] += root->val;
            }

            if (root->left)
                dfs(root->left, depth + 1);
            if (root->right)
                dfs(root->right, depth + 1);
        };
        dfs(root, 0);
        return 1 + (max_element(d_sum.begin(), d_sum.end()) - d_sum.begin());
    }

};
// @lc code=end

void test() {
    Solution s;

    vector<const char*> data = { "1", "7", "0", "7", "-8", "null", "null" };
    TreeNode* root = TreeNode::create_tree(data);
    cout << s.maxLevelSum(root) << endl;
    delete[] root;

    data = { "989", "null", "10250", "98693", "-89366", "null", "null", "null", "-32127" };
    root = TreeNode::create_tree(data);
    cout << s.maxLevelSum(root) << endl;
    delete[] root;

    data = { "1" };
    root = TreeNode::create_tree(data);
    cout << s.maxLevelSum(root) << endl;
    delete[] root;

    /* 3 */
    data = { "-100","-200","-300","-20","-5","-10","null" };
    root = TreeNode::create_tree(data);
    cout << s.maxLevelSum(root) << endl;
    delete[] root;
}