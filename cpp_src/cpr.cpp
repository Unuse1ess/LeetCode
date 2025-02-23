/*
    ComPile and Run
    Compile and run program for LeetCode written in C++.

    This file is compiled with:

        g++ -std=c++23 -fsanitize=address -O2 cpr.cpp -o cpr
*/
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <dlfcn.h>
#include <cstdio>

int main(int argc, char** argv) {
    if (argc == 1) {
        puts("No input files.");
        return 1;
    }

    /* Compile */

    const char* gcc_argv[] = { "/usr/bin/g++", "-std=c++23", "-fsanitize=address", "-Wall", "-g", "-fPIC", "-shared", "utils.cpp", argv[1], "-o", "/dev/shm/solution.so", NULL };
    int status;
    pid_t pid = fork();

    if (!pid) {
        execvp(gcc_argv[0], reinterpret_cast<char* const*>(reinterpret_cast<void*>(gcc_argv)));
        puts("gcc invoke failed.");
        return 1;
    }

    waitpid(pid, &status, 0);
    if ((!WIFEXITED(status)) || WEXITSTATUS(status) != 0) {
        puts("gcc compile failed.");
        return 1;
    }

    /* Run */

    void* handle = NULL;
    void (*test)();
    char* error;

    if ((handle = dlopen("/dev/shm/solution.so", RTLD_LAZY)) == NULL) {
        puts("dlopen() error.");
        return 1;
    }

    test = reinterpret_cast<void(*)()> (dlsym(handle, "test"));
    if ((error = dlerror()) != NULL) {
        puts("dlsym() error.");
        puts(error);
        dlclose(handle);
        return 1;
    }

    test();
    dlclose(handle);

    return 0;
}