# Problem 6: https://projecteuler.net/problem=6

def sumSquareDifference(n):
    sumOfSquares = sum([i ** 2 for i in range(1, n + 1)])
    squreOfSums = sum([i for i in range(1, n + 1)]) ** 2
    return squreOfSums - sumOfSquares

def main():
    print sumSquareDifference(100)

main()
