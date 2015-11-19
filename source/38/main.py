def numberRangeProduct(n, numberRange):
    concat = ""
    for i in range(1, numberRange + 1):
        concat += str(i * n)

    return int(concat)

def getPandigitalMultiple(n):
    i = 2
    while True:
        number = numberRangeProduct(n, i)
        if common.isPandigital(number, 9):
            return (True, number)
        if number > 999999999:
            break

        i += 1

    return False

def main():
    maxNumber = 0
    for i in range(1, 10000):
        number = getPandigitalMultiple(i)
        if number:
            maxNumber = max(maxNumber, number[1])

    print maxNumber

main()
