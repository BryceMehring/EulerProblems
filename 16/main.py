# Problem 16: https://projecteuler.net/problem=16

def main():
    total = 0
    for c in str(2 ** 1000):
        total += int(c)

    print total

main()
