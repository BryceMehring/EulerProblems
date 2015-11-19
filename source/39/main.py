import math

def rightTrianglePerimter(a, b):
    return a + b + math.sqrt(a * a + b * b)

def main():
    maxSolutions = 0
    maxIndex = 0
    for i in range(1, 1001):
        results = set()
        for a in range(1, i / 2):
            for b in range(1, i / 2):
                sides = (min(a, b), max(a, b))
                if sides not in results and rightTrianglePerimter(a, b) == i:
                    results.add(sides)
        if len(results) > maxSolutions:
            maxSolutions = len(results)
            maxIndex = i
        print i
    print maxIndex

main()
