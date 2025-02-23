/*
    Printing library for Leetcode written in C.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "utils.h"

static char float_fstring[128] = "%.4f";
static char* bool_string[] = { "false", "true" };

struct TreeNode* create_tree(char** data, size_t N) {
    if (N == 0) return NULL;
    struct TreeNode* tree = (struct TreeNode*)malloc(sizeof(struct TreeNode) * N);
    struct TreeNode* root = tree;

    root->val = atoi(data[0]);
    root->left = root->right = NULL;

    for (size_t i = 1; i < N; i++) {
        if (strncmp(data[i], "null", 4)) {
            if (i & 1)
                tree[((i + 1) >> 1) - 1].left = &tree[i];
            else
                tree[((i + 1) >> 1) - 1].right = &tree[i];

            tree[i].val = atoi(data[i]);
            tree[i].left = tree[i].right = NULL;
        }
    }

    return root;
}

void print_tree(struct TreeNode* root) {
    static struct TreeNode* queue[128] = { NULL };

    size_t queue_l = 0, queue_r = 0;

    if (!root) {
        puts("[]");
        return;
    }

    queue[queue_r++] = root;
    while (queue_l < queue_r && queue_r < 128) {
        struct TreeNode* node = queue[queue_l++];
        if (node) {
            queue[queue_r++] = node->left;
            queue[queue_r++] = node->right;
        }
    }
    queue_l = 0;
    while (queue[queue_r] == NULL)
        queue_r--;

    printf("[");
    while (queue_l <= queue_r) {
        struct TreeNode* node = queue[queue_l++];
        if (node) {
            printf("%d, ", node->val);
        } else {
            printf("null, ");
        }
    }
    puts("\b\b]");
}


void set_float_fstring(char* __new_fstring) {
    strncpy(float_fstring, __new_fstring, 128);
}

void print_int(int val) {
    printf("%d\n", val);
}

void print_float(float val) {
    printf(float_fstring, val);
    printf("\n");
}

void print_bool(bool val) {
    puts(bool_string[(size_t)val]);
}

/* string type can be printed directly using puts */

void print_int_arr(int* arr, size_t N) {
    if (N == 0) {
        puts("[]\n");
    } else if (N == 1) {
        printf("[%d]\n", arr[0]);
    } else {
        printf("[%d", arr[0]);
        for (size_t i = 1; i < N; i++)
            printf(", %d", arr[i]);
        puts("]");
    }
}

void print_float_arr(int* arr, size_t N) {
    if (N == 0) {
        puts("[]\n");
    } else if (N == 1) {
        printf("[");
        printf(float_fstring, arr[0]);
        printf("]\n");
    } else {
        printf("[");
        printf(float_fstring, arr[0]);
        for (size_t i = 1; i < N; i++) {
            printf(", ");
            printf(float_fstring, arr[i]);
        }
        puts("]");
    }
}

void print_bool_arr(int* arr, size_t N) {
    if (N == 0) {
        puts("[]\n");
    } else if (N == 1) {
        printf("[%s]\n", bool_string[(size_t)arr[0]]);
    } else {
        printf("[%s", bool_string[(size_t)arr[0]]);
        for (size_t i = 1; i < N; i++)
            printf(", %s", bool_string[(size_t)arr[i]]);
        puts("]");
    }
}

void print_arr(void* data, size_t N, print_type_t t) {
    static void (*printer[])(int*, size_t) = { print_int_arr, print_float_arr, print_bool_arr };
    printer[(size_t)t](data, N);
}