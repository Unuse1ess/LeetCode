/*
    Printing library for Leetcode written in C++.

    ** IMPORTANT **
    Do not use template, because this file is compiled to a DLL
    (the ELF loader cannot find the template symbol since the
    determined template type is not compiled)
*/

#include <iostream>
#include <vector>
#include "utils.hpp"

using namespace std;

ostream& operator<<(ostream& os, const vector<int>& v) {
    os << "[";
    for (size_t i = 0; i < v.size(); i++) {
        os << v[i] << ", ";
    }

    os << "\b\b]";

    return os;
}
