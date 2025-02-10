/*
 * @lc app=leetcode.cn id=334 lang=c
 *
 * [334] 递增的三元子序列
 */

#include <stdbool.h>

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

}