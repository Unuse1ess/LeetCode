/*
 * @lc app=leetcode.cn id=104 lang=c
 *
 * [104] 二叉树的最大深度
 */
#include "utils.h"

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define max(a, b) ((a) > (b) ? (a) : (b))
int maxDepth(struct TreeNode* root) {
    int l = 0, r = 0;

    if (!root) return 0;

    if (root->left)
        l = maxDepth(root->left);
    if (root->right)
        r = maxDepth(root->right);
    return max(l, r) + 1;
}
// @lc code=end

void test() {
    char* arr1[] = { "3", "9", "20", "null", "null", "15", "7" };
    struct TreeNode* root = create_tree(arr1, 7);
    print_int(maxDepth(root));
    free(root);

    char* arr2[] = { "1", "null", "2" };
    root = create_tree(arr2, 3);
    print_int(maxDepth(root));
    free(root);

    char* arr3[] = { };
    root = create_tree(arr3, 0);
    print_int(maxDepth(root));
    free(root);
}