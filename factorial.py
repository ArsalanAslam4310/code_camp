def factor(value):
    fact = value
    for i in range(1,fact):
        fact = fact*i
    return fact


print(factor(7))
