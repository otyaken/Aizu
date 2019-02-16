# -*- coding utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B

stack = []
operator = ["+", "-", "*"]
statement = input().split(' ')
for i in statement:
    if i not in operator:
        stack.append(i)
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(str(eval(b + i + a)))
print(stack.pop())
