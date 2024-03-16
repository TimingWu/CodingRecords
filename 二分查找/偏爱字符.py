# -*- coding: utf-8 -*-
# 小米20240312春招笔试
"""
题目描述：

小李天生偏爱一些字符，对于一个字符串，他总是想把字符串中的字符变成他偏爱的那些字符。如果字符串中某个字符不是他所偏爱的字符，称为非偏爱字符，那么他会将该非偏爱字符替换为字符串中距离该字符最近的一个偏爱的字符。这里的距离定义即为字符在字符串中的对应下标之差的绝对值。如果有不止一个偏爱的字符距离非偏爱字符最近，那么小李会选择最左边的那个偏爱字符来替换该非偏爱字符，这样就保证了替换后的字符串是唯一的。小李的所有替换操作是同时进行的。

假定小李有m个偏爱的字符，依次为c1,c2...cm，当小李看到一个长度为n的字符串s时，请你输出小李在进行全部替换操作后形成的字符串。

输入描述

第一行输入两个正整数n，m。

接下来一行输入m个字符c1,c2...cm，每两个字符之间用空格隔开，表示小李偏爱的字符。

接下来一行输入一个字符串s。

1≤n≤100000，1≤m≤26，保证题目中所有的字符均为大写字符，小李偏爱的字符互不相同，且偏爱字符至少出现一次。

输出描述

输出一行字符串，表示小李将给定的字符串s替换后形成的字符串。

样例输入
12 4
Z G B A
ZQWEGRTBYAAI

样例输出
ZZZGGGBBBAAA

提示
字符Q为非偏爱字符，且偏爱字符Z距离它最近，所以替换成Z；同理E距离G最近，替换成G；
对于字符W，偏爱字符Z和G与其距离相同，所以替换为左边的Z；
.......
对于字符 I ，右边没有偏爱字符，左边第一个偏爱字符是A，所以替换成字符A。
同一个偏爱字符可能会在字符串中出现多次。
"""

"""
思路：二分查找+模拟
先把偏爱字符在数组中的下标记录下来，存放进新数组，然后遍历原数组，遇到非偏爱字符再去记录中进行二分查找。找到小于当前下标的最大值，和大于当前下标的最小值，选取相对距离最小的进行替换
"""
import bisect
from math import inf

n, m = map(int, input().split())
love = [s for s in input().split()]
string = [s for s in input()]
love = set(love)

love_idx = [] 
for i,c in enumerate(string):
    if c in love:
        love_idx.append(i)

for i,c in enumerate(string):
    if c not in love:
        l = bisect.bisect_left(love_idx, i) - 1
        r = bisect.bisect_left(love_idx, i)
        # i - l 和 r - i作比较
        l = love_idx[l] if l != -1 else -inf
        r = love_idx[r] if r != len(love_idx) else inf

        if i - l <= r - i:
            string[i] = string[l]
        else:
            string[i] = string[r]

print("".join(string))
