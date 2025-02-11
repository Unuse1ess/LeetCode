/*
 * @lc app=leetcode.cn id=334 lang=java
 *
 * [334] 递增的三元子序列
 */

// @lc code=start
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int N = nums.length;

        if (N < 3) {
            return false;
        }
        int a = 0, b = 0;
        for (int i = 1; i < N; i++) {
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
}
// @lc code=end

class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.increasingTriplet(new int[] { 1, 2, 3, 4, 5 }));
        System.out.println(s.increasingTriplet(new int[] { 5, 4, 3, 2, 1 }));
        System.out.println(s.increasingTriplet(new int[] { 2, 1, 5, 0, 4, 6 }));
    }
}