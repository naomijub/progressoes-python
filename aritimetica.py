def soma(a0, step, n):
    sum = 0
    for i in range(n):
        sum += a0 + (step * i)
    return sum
