# Problem 21: https://projecteuler.net/problem=21

def main():
    total = 0
    for a in range(1, 10000):
        b = sum(common.factors(a)) - a
        if a != b and b > 0:
            c = sum(common.factors(b)) - b
            if a == c:
                total += (a + b)

    print total / 2

main()
