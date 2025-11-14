def func_compute(n):
    return lambda x: x * n

result = func_compute(2)
print("Double the number of 15 =", result(15))