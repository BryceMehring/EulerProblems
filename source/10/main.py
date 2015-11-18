# Problem 10: https://projecteuler.net/problem=10

def summationOfPrimes(n):
    return sum(common.sieve_of_erat(n))

def main():
    print summationOfPrimes(2000000)

main()
