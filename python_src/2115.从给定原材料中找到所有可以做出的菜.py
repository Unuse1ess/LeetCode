#
# @lc app=leetcode.cn id=2115 lang=python3
#
# [2115] 从给定原材料中找到所有可以做出的菜
#
from typing import *

# @lc code=start
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        make: Set[str] = set()
        skip: Set[int] = set()
        prev = 0

        while True:
            for i, ingr in enumerate(ingredients):
                if i in skip: continue
                if all(s in supplies or s in make for s in ingr):
                    make.add(recipes[i])
                    skip.add(i)
            if prev == len(make):
                break
            prev = len(make)
        return list(make)
        
# @lc code=end

s = Solution()
print(s.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
print(s.findAllRecipes(recipes = ["bread", "sandwich"], ingredients = [["yeast", "flour"], ["bread", "meat"]], supplies = ["yeast", "flour", "meat"]))
print(s.findAllRecipes(recipes = ["bread", "sandwich", "burger"], ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], supplies = ["yeast", "flour", "meat"]))
print(s.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"]))
