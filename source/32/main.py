def main():
    uniqueResults = set()
    for a in range(1, 9999):
        for b in range(1, 9999):
            product = a * b
            if product not in uniqueResults and common.isPandigital([a, b, product], 9):
                uniqueResults.add(product)
    print sum(uniqueResults)


main()
