# Problem 11: https://projecteuler.net/problem=11

def loadGrid(inputFile):
    with open(inputFile) as f:
        grid = []
        for line in f:
            grid.append(line.split())
        return grid

def largestProductInGrid(grid):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    rows = len(grid)
    columns = len(grid[0])
    greatestProduct = 0
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            for d in directions:
                offsetX = x
                offsetY = y
                product = int(value)
                for i in range(3):
                    offsetX += d[0]
                    offsetY += d[1]
                    if 0 <= offsetX < rows and 0 <= offsetY < columns:
                        product *= int(grid[offsetY][offsetX])

                greatestProduct = max(greatestProduct, product)

    return greatestProduct

def main():
    grid = loadGrid('grid.txt')
    print largestProductInGrid(grid)


main()
