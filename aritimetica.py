#!/usr/bin/python3

def sum(a0, step, n):
    sum = 0
    for i in range(n):
        sum += a0 + (step * i)
    return sum

def nValue(a0, step, n):
    return a0 + ((n - 1) * step)


print(nValue(1,1,10))
print(sum(1,1,10))
