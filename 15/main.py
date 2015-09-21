# Problem 15: https://projecteuler.net/problem=15
import math

def countLatticePaths(w, h):
    return math.factorial(w + h) / (math.factorial(w) ** 2)

def main():
    print countLatticePaths(20, 20)

main()
