def main():
    primes = common.sieve_of_erat(10000000)
    for prime in primes:
        if common.isPandigital(prime, len(str(prime))):
            largestPrime = prime
    print largestPrime

main()
