
def fibonancci(n):
    if (n == 0) or (n == 1):
        return n
    else:
        return fibonancci(n - 1) + fibonancci(n - 2)

print(fibonancci(10))

