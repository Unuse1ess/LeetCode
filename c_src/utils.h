#ifndef PRINT_UTILS_H
#define PRINT_UTILS_H

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef enum {
    INT_TYPE = 0,
    FLOAT_TYPE = 1,
    BOOL_TYPE = 2,
    TREENODE_TYPE = 3,
} print_type_t;

struct TreeNode* create_tree(char** data, size_t N);
void print_tree(struct TreeNode* root);

void print_int(int val);
void print_float(float val);
void print_bool(bool val);

void print_int_arr(int* arr, size_t N);
void print_float_arr(int* arr, size_t N);
void print_bool_arr(int* arr, size_t N);

void print_arr(void* data, size_t N, print_type_t t);

#endif