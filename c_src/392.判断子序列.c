/*
 * @lc app=leetcode.cn id=392 lang=c
 *
 * [392] 判断子序列
 */
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "print_utils.h"

// @lc code=start
bool isSubsequence(char* s, char* t) {
    size_t slen = strlen(s), tlen = strlen(t);

    if (slen > tlen) {
        return false;
    }
    size_t i = 0, j = 0;
    while (i < slen && j < tlen) {
        if (s[i] == t[j]) {
            i++;
        }
        j++;
    }
    return i == slen;
}
// @lc code=end

void test() {
    print_bool(isSubsequence("abc", "ahbgdc"));
    print_bool(isSubsequence("axc", "ahbgdc"));
}