# -*- coding: utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A

def output_result(num_list, num_list_length):
    for i in range(0, num_list_length):
        if i > 0:
             print(" ", end='')
        print(num_list[i], end='')
    print()

def insertion_sort(num_list, num_list_length):
    for i in range(1, num_list_length):
        v = num_list[i]
        j = i
        while v < num_list[j-1] and j > 0:
            num_list[j] = num_list[j-1]
            j -= 1
        num_list[j] = v
        output_result(num_list, num_list_length)

num_list = []
num_list_length = int(input())

num_list_str = input().split(' ')
num_list = list(map(int, num_list_str))

output_result(num_list, num_list_length)
insertion_sort(num_list, num_list_length)
