# -*- coding utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

def bubble_sort(sequence, sequence_len):
    sort_cnt = 0
    for i in range(0, sequence_len):
        for j in range(sequence_len-1, i, -1):
            if sequence[j] < sequence[j-1]:
                tmp = sequence[j]
                sequence[j] = sequence[j-1]
                sequence[j-1] = tmp
                sort_cnt += 1
    return sort_cnt

def print_result(sequence, sort_cnt):
    for i in range(0, len(sequence)):
        if i != 0:
            print(" ", end='')
        print(sequence[i], end='')
    print()
    print(sort_cnt)

sequence_len = int(input())
sequence = list(map(int, input().split()))
sort_cnt= bubble_sort(sequence, sequence_len)
print_result(sequence, sort_cnt)
