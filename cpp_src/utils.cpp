/*
    Printing library for Leetcode written in C++.

    ** IMPORTANT **
    Do not use template, because this file is compiled to a DLL
    (the ELF loader cannot find the template symbol since the
    determined template type is not compiled)
*/

#include <cstring>
#include "utils.hpp"

using namespace std;


ostream& operator<<(ostream& os, const vector<int>& v) {
    if (v.size() == 0) {
        return os << "[]";
    }
    os << "[";
    for (size_t i = 0; i < v.size(); i++) {
        os << v[i] << ", ";
    }

    os << "\b\b]";

    return os;
}

TreeNode* TreeNode::create_tree(vector<const char*>& data) {
    if (data.size() == 0) {
        return nullptr;
    }
    TreeNode* root = new TreeNode[data.size()];
    queue<TreeNode*> q;
    q.push(root);
    root->val = atoi(data[0]);

    for (size_t i = 1; i < data.size(); i += 2) {
        TreeNode* node = q.front();
        q.pop();

        if (strncmp(data[i], "null", 4)) {
            node->left = &root[i];
            root[i].val = atoi(data[i]);
        }
        if (i + 1 < data.size() && strncmp(data[i + 1], "null", 4)) {
            node->right = &root[i + 1];
            root[i + 1].val = atoi(data[i + 1]);
        }

        if (node->left)
            q.push(node->left);
        if (node->right)
            q.push(node->right);
    }

    return root;
}

TreeNode::TreeNode() {
    this->val = 0;
    this->left = this->right = nullptr;
}

TreeNode::TreeNode(int x) {
    this->val = x;
    this->left = this->right = nullptr;
}

ostream& operator<<(ostream& os, const TreeNode* root) {
    /* Assume that the input size <= 128 */
    static const TreeNode* queue[128] = { nullptr };

    size_t queue_l = 0, queue_r = 0;

    if (!root) {
        return os << "[]";
    }

    queue[queue_r++] = root;
    while (queue_l < queue_r) {
        const TreeNode* node = queue[queue_l++];
        if (node) {
            queue[queue_r++] = node->left;
            queue[queue_r++] = node->right;
        }
    }
    queue_l = 0;
    queue_r--;
    while (queue[queue_r] == nullptr)
        queue_r--;

    os << "[";
    while (queue_l <= queue_r) {
        const TreeNode* node = queue[queue_l++];
        if (node) {
            os << node->val << ", ";
        } else {
            os << "null, ";
        }
    }
    os << "\b\b]";

    return os;
}
