primes = set(common.sieve_of_erat(10 ** 6))

def isTruncatablePrime(prime):
        primeStr = str(prime)
        for i in range(1, len(primeStr)):
            if int(primeStr[i:]) not in primes or int(primeStr[:(len(primeStr) - i)]) not in primes:
                return False
        return True

def main():
    total = 0
    for prime in primes:
        if prime > 7 and isTruncatablePrime(prime):
            total += prime
    print total

main()
