/*
 * @lc app=leetcode.cn id=236 lang=cpp
 *
 * [236] 二叉树的最近公共祖先
 */
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include "utils.hpp"

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution0 {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> path, p_path, q_path;
        dfs(root, p, path, p_path);
        path.clear();
        dfs(root, q, path, q_path);

        size_t N = min(p_path.size(), q_path.size());
        size_t i = N - 1;
        for (; i >= 0; i--) {
            if (p_path[i] == q_path[i])
                break;
        }

        return p_path[i];
    }

    void dfs(TreeNode* root, TreeNode* t, vector<TreeNode*>& path, vector<TreeNode*>& res) {
        path.push_back(root);
        if (root->val == t->val) {
            res = path;
            return;
        }
        if (root->left)
            dfs(root->left, t, path, res);
        if (root->right)
            dfs(root->right, t, path, res);
        path.pop_back();
    }
};
// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        unordered_map<int, TreeNode*> parent;
        dfs(root, parent);
        parent[root->val] = nullptr;

        unordered_set<int> visited;
        TreeNode* tmp = p;
        while (tmp != nullptr) {
            visited.insert(tmp->val);
            tmp = parent[tmp->val];
        }
        tmp = q;
        while (visited.find(tmp->val) == visited.end()) {
            tmp = parent[tmp->val];
        }
        return tmp;
    }

    void dfs(TreeNode* root, unordered_map<int, TreeNode*>& parent) {
        if (root->left) {
            parent[root->left->val] = root;
            dfs(root->left, parent);
        }
        if (root->right) {
            parent[root->right->val] = root;
            dfs(root->right, parent);
        }
    }
};

// @lc code=end

void test() {
    Solution s;

    std::vector<const char*> data = { "3", "5", "1", "6", "2", "0", "8", "null", "null", "7", "4" };
    TreeNode* root = TreeNode::create_tree(data);
    TreeNode p = TreeNode(5), q = TreeNode(1);
    cout << s.lowestCommonAncestor(root, &p, &q) << endl;
    delete[] root;

    data = { "3", "5", "1", "6", "2", "0", "8", "null", "null", "7", "4" };
    root = TreeNode::create_tree(data);
    p = TreeNode(5);
    q = TreeNode(4);
    cout << s.lowestCommonAncestor(root, &p, &q) << endl;
    delete[] root;

    data = { "1", "2" };
    root = TreeNode::create_tree(data);
    p = TreeNode(1);
    q = TreeNode(2);
    cout << s.lowestCommonAncestor(root, &p, &q) << endl;
    delete[] root;
}