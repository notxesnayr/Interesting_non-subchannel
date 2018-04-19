def factorial_number(x):
    if x >= 0:
        if x == 1:
            return 1
        if x == 0:
            return 1
        else:
            return x * factorial_number(x-1)
    if x < 0:
        if x == -1:
            return -1
        else:
            return x * (factorial_number(x+1))
print(factorial_number(99))

