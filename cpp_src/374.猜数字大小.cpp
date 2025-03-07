/*
 * @lc app=leetcode.cn id=374 lang=cpp
 *
 * [374] 猜数字大小
 */
#include "utils.hpp"

using namespace std;

function<int(int)> guess;

/*
使用uint32_t，否则int表示下(l + r)会溢出。
*/

// @lc code=start
/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        uint32_t l = 0, r = n;
        while (l <= r) {
            uint32_t mid = (l + r) >> 1;
            int ret = guess(mid);
            if (ret == 1) {
                l = mid + 1;
            } else if (ret == -1) {
                r = mid - 1;
            } else {
                return mid;
            }
        }
        return 0;
    }
};
// @lc code=end

void make_guess(int num) {
    guess = [num](int n) {
        if (n == num)
            return 0;
        else if (n > num)
            return -1;
        else
            return 1;
    };
}

void test() {
    Solution s;

    make_guess(6);
    cout << s.guessNumber(10) << endl;

    make_guess(1);
    cout << s.guessNumber(1) << endl;

    make_guess(1);
    cout << s.guessNumber(2) << endl;

    make_guess(1702766719);
    cout << s.guessNumber(2126753390) << endl;
}