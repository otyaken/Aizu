# -*- coding: utf-8 -*-

# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D


num = int(input())

max = -20000000000
min_value = int(input())

for i in range(0, num-1):
    num = int(input())
    if max < num - min_value:
        max = num - min_value
    if min_value > num:
        min_value = num

print(max)
