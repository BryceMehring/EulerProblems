import math

def isCuriousNumber(n):
    total = 0
    for c in str(n):
        total += math.factorial(int(c))
        if total > n:
            break

    return total == n

def main():
    total = 0
    for i in range(3, 50000):
        if isCuriousNumber(i):
            total += i

    print total

main()
