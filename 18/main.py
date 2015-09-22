# Problem 18: https://projecteuler.net/problem=18

def left(i, depth):
    return i + depth + 1

def right(i, depth):
    return i + depth + 2

def maximumPathSum(numbers, index = 0, depth = 0):
    leftIndex = left(index, depth)
    rightIndex = right(index, depth)
    maxValue = 0

    if leftIndex < len(numbers):
        maxValue = maximumPathSum(numbers, leftIndex, depth + 1)

    if rightIndex < len(numbers):
        maxValue = max(maximumPathSum(numbers, rightIndex, depth + 1), maxValue)

    return maxValue + numbers[index]

def main():
    numbers = []
    with open('triangle.txt') as f:
        for line in f:
            for number in line.split():
                numbers.append(int(number))

    print maximumPathSum(numbers)
    
main()
