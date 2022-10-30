# Solution 1


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)



# Solution 2


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact
