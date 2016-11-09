#!/usr/bin/python3

def nValue(a0, q, n):
    return a0 * (q ** (n - 1))

def sum(a0, q, n):
    sum = 0
    for i in range(n):
        sum += nValue(a0, q, i+1)
        print(i, nValue(a0, q, i+1), sum)
    return sum

def sum2(a0, q, n):
    return a0 * ((q ** n) - 1) / (q - 1)

print(nValue(1, 2, 4))
print(sum(1,2,4))
print(sum2(1,2,4))
