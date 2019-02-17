# -*- coding utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B

def binary_search(num_list, key):
    left = 0
    right = len(num_list)
    while left < right:
        mid = int((left + rigth) / 2)
        if num_list[mid] == key:
            return True
        elif key < num_list[mid]:
            right = mid
        else:
            left = mid + 1
    return False

num_list_length = int(input())
num_list = list(map(int, input().split(' ')))
key_list_length = int(input())
key_list = list(map(int, input().split(' ')))

cnt = 0

for key in key_list:
    result = binary_search(num_list, key)
    if result == True:
        cnt += 1

print(cnt)
