# Problem 5: https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallestMultiple(minNum, maxNum):
    smallestNumber = 2
    while True:
        isValidMultiple = True
        for i in range(maxNum, minNum - 1, -1):
            if smallestNumber % i != 0:
                isValidMultiple = False
                break

        if isValidMultiple:
            return smallestNumber

        smallestNumber += 2

def main():
    print smallestMultiple(2, 10)
main()
