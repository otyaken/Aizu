# -*- coding utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A

def liner_search(num_list, key):
    num_list.append(key)
    idx = 0
    while num_list[idx] != key:
        idx += 1
    num_list.pop()
    if idx == len(num_list):
        return False
    return True

num_list_length = int(input())
num_list = list(map(int, input().split(' ')))
key_list_length = int(input())
key_list = list(map(int, input().split(' ')))

cnt = 0

for key in key_list:
    result = liner_search(num_list, key)
    if result == True:
        cnt += 1

print(cnt)
