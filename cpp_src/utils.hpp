#pragma once

#include <vector>
#include <iostream>

std::ostream& operator<<(std::ostream& os, const std::vector<int>& v);

extern "C" {
    void test();
}

