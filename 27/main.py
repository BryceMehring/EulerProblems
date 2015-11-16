#https://projecteuler.net/problem=27

def quadtraticPrimeListLenth(a, b):
    n = 0
    while True:
        y = n ** 2 + (a * n) + b
        if y < 1 or not common.isPrime(y):
            break
        n += 1
    return dict(n=n, coefficents=(a, b))

def main():
    largestN = 0
    largestResult = None
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            result = quadtraticPrimeListLenth(a, b)
            if result['n'] > largestN:
                largestN = result['n']
                largestResult = result

    print largestResult['n'], largestResult['coefficents'][0], largestResult['coefficents'][1], largestResult['coefficents'][0] * largestResult['coefficents'][1]

main()
