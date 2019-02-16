# -*- coding utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

def print_result(sequence, swap_cnt):
    for i in range(0, len(sequence)):
        if i != 0:
            print(" ", end='')
        print(sequence[i], end='')
    print()
    print(swap_cnt)

def selection_sort(num_list, num_list_length):
    swap_cnt = 0
    for i in range(0, num_list_length):
        min_idx = num_list_length-1
        for j in range(num_list_length-2, i-1, -1):
            if num_list[min_idx] > num_list[j]:
                min_idx = j

        #スワップする必要があるかどうか調べる
        if num_list[i] != num_list[min_idx]:
            tmp = num_list[i]
            num_list[i] = num_list[min_idx]
            num_list[min_idx] = tmp
            swap_cnt += 1


    return swap_cnt

num_list_length = int(input())
num_list = list(map(int, input().split(' ')))
swap_cnt = selection_sort(num_list, num_list_length)
print_result(num_list, swap_cnt)
