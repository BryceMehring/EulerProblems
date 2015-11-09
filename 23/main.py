# Problem 23: https://projecteuler.net/problem=23

def abundantSums(multiples, total):
    for value in multiples:
        for secondValue in multiples:
            if value + secondValue == total:
                return (value, secondValue)

    return False

def main():
    abundantNumbers = set()
    for i in range(12, 28124):
        total = sum(common.factors(i)) - i
        if total > i:
            abundantNumbers.add(i)

    total = 0
    for i in range(1, 28124):
        multiples = []
        for j in range(12, i - 1):
            if j in abundantNumbers:
                multiples.append(j)

        if not abundantSums(multiples, i):
            total += i

    print total

main()
