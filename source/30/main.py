def isDigitPowerSum(number, power):
    numberStr = str(number)
    total = 0
    for c in numberStr:
        total += int(c) ** power
    return total == number

def main():
    numbers = []
    power = 5
    for i in range(2, (9 ** power) * power + 1):
        if isDigitPowerSum(i, power):
            numbers.append(i)

    print sum(numbers)

main()
