# Problem 12: https://projecteuler.net/problem=12

def nthTriangularNumber(n):
    return n * (n + 1) / 2

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def highlyDivisibleTriangularNumber(divisors):
    i = 1
    factorList = []
    while len(factorList) <= divisors:
        triNumber = nthTriangularNumber(i)
        factorList = factors(triNumber)
        i += 1
    return triNumber

def main():
    print highlyDivisibleTriangularNumber(500)

main()
