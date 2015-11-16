# Problem 10: https://projecteuler.net/problem=10

def sieve_of_erat(n):
    primes = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return [i for i, v in enumerate(primes) if v]

def summationOfPrimes(n):
    return sum(sieve_of_erat(n)) - 1

def main():
    print summationOfPrimes(2000000)

main()
