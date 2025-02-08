/*
    ComPile and Run
    Compile and run program for LeetCode written in C/C++.
*/
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include<dlfcn.h>
#include <stdio.h>

int main(int argc, char** argv) {
    if (argc == 1) {
        puts("No input files.");
        return 1;
    }

    /* Compile */

    char* gcc_argv[] = { "/usr/bin/gcc", "-fsanitize=address", "-Wall", "-g", "-fPIC", "-shared", argv[1], "-o", "./solution.so", NULL };
    pid_t pid = fork();

    if (!pid) {
        execvp(gcc_argv[0], gcc_argv);
        puts("gcc invoke failed.");
        return 1;
    }

    waitpid(pid, NULL, 0);

    /* Run */

    void* handle = NULL;
    void (*test)();
    char* error;

    if ((handle = dlopen("./solution.so", RTLD_LAZY)) == NULL) {
        puts("dlopen() error.");
        return 1;
    }

    test = dlsym(handle, "test");
    if ((error = dlerror()) != NULL) {
        puts("dlsym() error.");
        return 1;
    }

    test();
    dlclose(handle);

    return 0;
}