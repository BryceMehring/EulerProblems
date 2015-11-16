# Problem 1: https://projecteuler.net/problem=1


def main():
    total = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    print 'Sum of all the multiples of 3 or 5 below 1000:', total

main()
