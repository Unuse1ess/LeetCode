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

/*
** IMPORTANT **
    Bugs founded and fixed in C++, and migrated from C++.
    Not tested in C.
*/
struct TreeNode* create_tree(char** data, size_t N) {
    /* Assume that the input size <= 128 */
    static struct TreeNode* queue[128] = { NULL };

    if (N == 0) return NULL;

    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode) * N);
    size_t queue_l = 0, queue_r = 0;

    queue[queue_r++] = root;
    root->val = atoi(data[0]);

    for (size_t i = 1; i < N; i += 2) {
        struct TreeNode* node = queue[queue_l++];
        if (strncmp(data[i], "null", 4)) {
            node->left = &root[i];
            root[i].val = atoi(data[i]);
        }
        if (i + 1 < N && strncmp(data[i + 1], "null", 4)) {
            node->right = &root[i + 1];
            root[i + 1].val = atoi(data[i + 1]);
        }

        if (node->left)
            queue[queue_r++] = node->left;
        if (node->right)
            queue[queue_r++] = node->right;
    }
    return root;
}

void print_tree(struct TreeNode* root) {
    /* Assume that the input size <= 128 */
    static struct TreeNode* queue[128] = { NULL };

    size_t queue_l = 0, queue_r = 0;

    if (!root) {
        puts("[]");
        return;
    }

    queue[queue_r++] = root;
    while (queue_l < queue_r) {
        struct TreeNode* node = queue[queue_l++];
        if (node) {
            queue[queue_r++] = node->left;
            queue[queue_r++] = node->right;
        }
    }
    queue_l = 0;
    queue_r--;
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