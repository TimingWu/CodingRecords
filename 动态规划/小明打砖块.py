# -*- coding: utf-8 -*-
# 小米20240312春招笔试
"""
题目描述：

小明在玩一个消除游戏。这个消除游戏有点特别。游戏中，你会得到n个一维排列的有各自颜色的砖块。

消除的时候，你有三种消除方案。你可以单消一个砖块，这样你可以得到a的得分；如果两个颜色一样的砖块在一起，你可以将这两个砖块一起消除获得b的得分；如果三个颜色一样的砖块在一期，你可以将这三个砖块一起消除获得c的得分。

消除后，被消除的砖块自动消失，被消除砖块的左右两端的砖块将在消除之后挨在一起。

小明想知道在最优策略下他能得到多少得分。

输入描述

第一行4个整数n，a，b，c，表示砖块数量，和一消/二消/三消的得分。

接下来一行n个整数，第i个整数si表示第i个砖块的颜色。

输出描述

输出最高得分

样例输入
8 1 3 7
3 1 3 1 3 2 2 3

样例输出
14

提示
1≤si≤n≤300，0≤a,b,c≤10000
"""
"""
思路：
区间dp
记忆化搜索：
    dfs[i][j]代表i到j内的得分
    消除左端点：dfs[i+1][j]+a
    消除右端点：dfs[i][j-1]+a
    左右端点相同消两个：dfs[i+1][j-1]+b
    消三个，枚举一个中间点k：dfs[i+1][k-1]+dfs[k+1][j-1]+c
"""

from functools import cache

n, a, b, c = map(int, input().split())
nums = [int(x) for x in input().split()]

# # 记忆化搜索
# @cache
# def dfs(i, j):
#     if i >= j:
#         return 0 if i > j else a
    
#     ans = max(dfs(i + 1, j), dfs(i, j - 1)) + a
#     if nums[i] == nums[j]:
#         ans = max(ans, dfs(i + 1, j - 1)+b)
    
#     for k in range(i+1, j):
#         if nums[i] == nums[k] == nums[j]: 
#             ans = max(dfs(i+1, k-1) + dfs(k+1, j-1) + c, ans)
    
#     return ans

# print(dfs(0, n - 1))

# 递推
def solution():
    f = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        f[i][i] = a
        for j in range(i+1, n):
            f[i][j] = max(f[i+1][j]+a,  f[i][j])
            f[i][j] = max(f[i][j-1]+a,  f[i][j])
            if nums[i] == nums[j]:
                f[i][j] = max(f[i+1][j-1]+b, f[i][j])
            for k in range(i+1, j):
                if nums[i] == nums[k] == nums[j]:
                    f[i][j] = max(f[i+1][k-1] + f[k+1][j-1] + c, f[i][j])
    print(f)
    return f[0][n-1]

print(solution())
