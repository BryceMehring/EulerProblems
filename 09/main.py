# Problem 9: https://projecteuler.net/problem=9
# a < b < c
# a ** 2 + b ** 2 == c ** 2
# a + b + c == 1000

def pythagoreanTriplet():
    for a in range(1, int(-500 * (2 ** 0.5 - 2))):
        b = 1000 * (a - 500) / (a - 1000)
        c = (-a**2 + 1000 * a - 500000) / (a - 1000)

        if a + b + c == 1000:
            return (a, b, c, a * b * c)

def main():
    print pythagoreanTriplet()

main()
