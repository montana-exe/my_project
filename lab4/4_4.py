from functools import reduce

n = 5
nums = list(range(1, n + 1))

factorial = reduce(lambda x, y: x * y, nums)

print(f"{n}! =", factorial)
