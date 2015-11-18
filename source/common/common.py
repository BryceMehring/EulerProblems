def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def isPrime(n):
    return len(factors(n)) == 2

def sieve_of_erat(n):
    primes = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return [i for i, v in enumerate(primes) if v and i > 1]
