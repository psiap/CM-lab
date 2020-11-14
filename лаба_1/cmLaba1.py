from math import inf, pi


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nextSumWithoutFactorial(x, n):
    return ((-1) * (x ** 2) * (2 * n - 1)) / (n * (2 * n + 1))
def nextSum(x, n):
    return ((-1) ** n) * (x ** (2 * n + 1)) / (factorial(n) * (2 * n + 1))
def erf(x, withFact):
    collector = 0 if withFact else x
    current = 1 if withFact else x
    counter = 0 if withFact else 1
    while current != 0:
        current = nextSum(x, counter) if withFact else current * nextSumWithoutFactorial(x, counter)
        counter += 1
        collector += current
        return 2 / (pi ** (1 / 2)) * collector
print('Без вычисления факториала: \t', erf(3, False))
print('С вычислением факториала: \t', erf(3, True))
