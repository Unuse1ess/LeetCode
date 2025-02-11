/*
 * @lc app=leetcode.cn id=11 lang=c
 *
 * [11] 盛最多水的容器
 */
#include <math.h>
#include "print_utils.h"

// @lc code=start
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
int maxArea(int* height, int heightSize) {
    size_t l = 0, r = heightSize - 1;
    int area = min(height[l], height[r]) * (r - l);

    while (l < r) {
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
        area = max(area, (r - l) * min(height[r], height[l]));
    }
    return area;
}
// @lc code=end

void test() {
    static int arr[] = { 1,8,6,2,5,4,8,3,7 };
    print_int(maxArea(arr, 9));

    static int arr2[] = { 1,1 };
    print_int(maxArea(arr2, 2));
}