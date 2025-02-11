/*
 * @lc app=leetcode.cn id=238 lang=c
 *
 * [238] 除自身以外数组的乘积
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "print_utils.h"

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* ret = (int*)malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;

    if (numsSize == 2) {
        ret[0] = nums[1];
        ret[1] = nums[0];
        return ret;
    }

    memcpy(ret, nums, numsSize * sizeof(int));

    for (size_t i = 1; i < numsSize; i++) {
        nums[i] *= nums[i - 1];
        ret[numsSize - i - 1] *= ret[numsSize - i];
    }

    ret[0] = ret[1];
    for (size_t i = 1; i < numsSize - 1; i++) {
        ret[i] = ret[i + 1] * nums[i - 1];
    }
    ret[numsSize - 1] = nums[numsSize - 2];
    return ret;
}
// @lc code=end

void test() {
    int* ret;
    int ret_num_size;

    int nums[] = { 1, 2, 3, 4 };
    print_arr(ret = productExceptSelf(nums, 4, &ret_num_size), 4, INT_TYPE);
    free(ret);

    int nums2[] = { -1, 1, 0, -3, 3 };
    print_arr(ret = productExceptSelf(nums2, 5, &ret_num_size), 5, INT_TYPE);
    free(ret);
}
