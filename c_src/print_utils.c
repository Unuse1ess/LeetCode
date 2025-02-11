/*
    Printing library for Leetcode written in C.
    This file is compiled with:
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "print_utils.h"

static char float_fstring[128] = "%.4f";
static char* bool_string[] = { "false", "true" };

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