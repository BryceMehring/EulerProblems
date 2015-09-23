# Problem 20: https://projecteuler.net/problem=20
import math

def main():
    number = str(math.factorial(100))
    total = 0
    for c in number:
        total += int(c)
    print total

main()
