#!/usr/bin/python3

def sum(a1, step, n):
    sum = 0
    for i in range(n):
        sum += a1 + (step * i)
    return sum

def nvalue(a1, step, n):
    return a1 + ((n - 1) * step)


print(nvalue(1,1,10))
print(sum(1,1,10))
