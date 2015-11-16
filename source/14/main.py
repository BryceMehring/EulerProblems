# Problem 14: https://projecteuler.net/problem=14

def collatzSequenceLength(n):
    length = 1
    while(n != 1):
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def main():
    maxLength = 0
    maxNumber = 0
    for i in range(1, 1000000):
        length = collatzSequenceLength(i)
        if length > maxLength:
            maxLength = length
            maxNumber = i
    print maxNumber, maxLength

main()
