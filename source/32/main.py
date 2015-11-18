def isPandigital(args, length):
    numberStr = None
    if type(args) == list:
        numberStr = reduce(lambda x, y: str(x) + str(y), args)
    elif type(args) == int:
        numberStr = str(args)

    if numberStr and length and len(numberStr) == length:
        for i in range(1, len(numberStr) + 1):
            if str(i) not in numberStr:
                return False

        return True

def main():
    uniqueResults = set()
    for a in range(1, 9999):
        for b in range(1, 9999):
            product = a * b
            if product not in uniqueResults and isPandigital([a, b, product], 9):
                uniqueResults.add(product)
    print sum(uniqueResults)


main()
