primes = set(common.sieve_of_erat(10 ** 6))

def rotate(l,n):
    return l[-n:] + l[:-n]

def isCircularPrime(n):
    numberStr = str(n)
    for i in range(len(numberStr)):
        if int(rotate(numberStr, i)) not in primes:
            return False

    return True

def main():
    count = 0
    for prime in primes:
        if isCircularPrime(prime):
            print prime
            count += 1

    print count

main()
