def  factorial(base) :
    if base == 0:
        return 1
    else:
        return base * factorial(base-1)
n = 4
print(factorial(n) )
