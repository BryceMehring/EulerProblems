# https://projecteuler.net/problem=26

def main():
    largestNumber = 0
    for p in range(7, 1000, 2):
        if len(common.factors(p)) == 2:
            b = 10
            t = 0
            r = 1
            n = 0
            while True:
                t += 1
                x = r * b
                d = x / p
                r = x % p
                n = n * b + d

                if t == p - 1:
                    largestNumber = p

                if r == 1:
                    break

    print largestNumber

main()
