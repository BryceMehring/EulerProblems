# Problem 12: https://projecteuler.net/problem=12

def nthTriangularNumber(n):
    return n * (n + 1) / 2

def highlyDivisibleTriangularNumber(divisors):
    i = 1
    factorList = []
    while len(factorList) <= divisors:
        triNumber = nthTriangularNumber(i)
        factorList = common.factors(triNumber)
        i += 1
    return triNumber

def main():
    print highlyDivisibleTriangularNumber(500)

main()
