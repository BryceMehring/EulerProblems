# https://projecteuler.net/problem=28

gridSize = 5

def printGrid(numbers):
    for line in numbers:
        print line

def calculateDiagTotals(grid):
    stepOptions = [
        {'i': 0, 'j': 0, 'stepI': 1, 'stepJ': 1},
        {'i': len(grid) - 1, 'j': 0, 'stepI': -1, 'stepJ': 1}
    ]
    total = 0
    for option in stepOptions:
        i, j, stepI, stepJ = option['i'], option['j'], option['stepI'], option['stepJ']
        while i < len(grid) and j < len(grid):
            total += grid[i][j]
            i += stepI
            j += stepJ

    return total - 1

def generateNumberSpiralGrid(gridSize):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    numbers = [[0]*gridSize for i in range(gridSize)]
    pos = {0: gridSize / 2, 1: gridSize / 2}
    i = 1
    length = 0
    while i <= (gridSize * gridSize):
        for index, direction in enumerate(directions):
            if index == 0 or index == 2:
                length += 1

            lengthCounter = length
            while lengthCounter > 0 and pos[1] < len(numbers) and pos[0] < len(numbers):
                numbers[pos[1]][pos[0]] = i
                pos[0] += direction[0]
                pos[1] += direction[1]
                lengthCounter -= 1
                i += 1
    return numbers


def main():

    numberSpiralGrid = generateNumberSpiralGrid(1001)
    #printGrid(numberSpiralGrid)
    total = calculateDiagTotals(numberSpiralGrid)
    print "Total: ", total

main()
