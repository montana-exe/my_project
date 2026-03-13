def sum_odd_numbers(n):
    s = 0
    for i in range(n+1):
        if i % 2 == 1:
            s += i
    return s

print(sum_odd_numbers(5))
