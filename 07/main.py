# Problem 7: https://projecteuler.net/problem=7

def isPrime(n):
    if (n % 2 == 0 and n != 2) or (n == 2):
        return n == 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def nthPrime(n):
    counter = 2
    primeCounter = 1
    while True:
        if isPrime(counter):
            if primeCounter >= n:
                break
            primeCounter += 1
        counter += 1
    return counter

def main():
    print nthPrime(10001)

main()
