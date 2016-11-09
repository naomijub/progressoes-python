#!/usr/bin/python3

def nvalue(a1, q, n):
    return a1 * (q ** (n - 1))

def sum(a1, q, n):
    sum = 0
    for i in range(n):
        sum += nvalue(a1, q, i+1)
        print(i, nvalue(a1, q, i+1), sum)
    return sum

def sum2(a1, q, n):
    return a1 * ((q ** n) - 1) / (q - 1)

print(nvalue(1, 2, 4))
print(sum(1,2,4))
print(sum2(1,2,4))
