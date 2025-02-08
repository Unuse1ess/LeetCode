/*
 * @lc app=leetcode.cn id=151 lang=c
 *
 * [151] 反转字符串中的单词
 */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/*
static char ret[100002];
char* reverseWords(char* s) {
    int N = strlen(s);
    int pos = 0;

    while (N > 0 && s[N - 1] == ' ') {
        N--;
    }

    while (N > 0) {
        int r = N;
        while (N > 0 && s[N - 1] != ' ') {
            N--;
        }
        int cnt = r - N;

        memcpy(&ret[pos], &s[N], cnt);

        pos += cnt;
        ret[pos++] = ' ';

        while (N > 0 && s[N - 1] == ' ') {
            N--;
        }
    }
    ret[--pos] = 0;

    return ret;
}
*/

// @lc code=start
void rev_ptr(char* l, char* r) {
    char tmp;
    while (l < r) {
        tmp = *r;
        *r = *l;
        *l = tmp;
        r--; l++;
    }
}

char* reverseWords(char* s) {
    size_t N = strlen(s);
    while (s[N - 1] == ' ') {
        N--;
    }
    while (*s == ' ') {
        s++;
        N--;
    }

    rev_ptr(s, &s[N - 1]);

    size_t r = 0;
    size_t l = 0;
    while (r < N) {
        int word_len = 0;
        while (s[r] != ' ' && s[r] != 0) {
            r++;
            word_len++;
        }
        if (word_len) {
            rev_ptr(&s[l], &s[r - 1]);
            l += word_len + 1;
            while (s[r] == ' ') r++;
        }
    }
    s[l - 1] = 0;
    return s;
}
// @lc code=end

void _strcpy(char** _in, char* src) {
    *_in = (char*)malloc(strlen(src) + 1);
    strcpy(*_in, src);
}
void test() {
    char* inputs;

    _strcpy(&inputs, "the sky is blue");
    puts(reverseWords(inputs));
    free(inputs);
    _strcpy(&inputs, "  hello world  ");
    puts(reverseWords(inputs));
    free(inputs);
    _strcpy(&inputs, "a good   example");
    puts(reverseWords(inputs));
    free(inputs);
}
