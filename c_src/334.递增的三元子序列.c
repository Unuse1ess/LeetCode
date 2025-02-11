/*
 * @lc app=leetcode.cn id=334 lang=c
 *
 * [334] 递增的三元子序列
 */

#include <stdbool.h>
#include "print_utils.h"

// @lc code=start
bool increasingTriplet(int* nums, int numsSize) {
    if (numsSize < 3) {
        return false;
    }
    int a = 0, b = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] <= nums[a]) {
            a = i;
        } else if (b == 0) {
            b = i;
        } else if (nums[i] > nums[b]) {
            return true;
        } else if (nums[i] < nums[b]) {
            b = i;
        }
    }
    return false;
}
// @lc code=end

void test() {
    int nums1[] = { 1, 2, 3, 4, 5 };
    print_bool(increasingTriplet(nums1, 5));

    int nums2[] = { 5, 4, 3, 2, 1 };
    print_bool(increasingTriplet(nums2, 5));

    int nums3[] = { 2, 1, 5, 0, 4, 6 };
    print_bool(increasingTriplet(nums3, 6));
}