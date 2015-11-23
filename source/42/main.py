import math

def isTriangleNumber(n):
    sqrtValue = 0.25 + (2 * n)
    denominator = -1
    if sqrtValue >= 0:
        result = ((0.5 + math.sqrt(sqrtValue)) / denominator, (0.5 - math.sqrt(sqrtValue)) / denominator)
        if (result[0] > 0 and result[0].is_integer()) or (result[1] > 0 and result[1].is_integer()):
            return True
    return False

def main():
    with open('source/42/words.txt') as f:
        words = f.read().replace('"', '').split(',')
        triangleWordCounter = 0
        for word in words:
            total = 0
            for c in word:
                total += common.charToIndex(c)
            if isTriangleNumber(total):
                triangleWordCounter += 1

        print triangleWordCounter

main()
