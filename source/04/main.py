def main():
    largestNumber = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            product = a * b
            productStr = str(product)
            if productStr == productStr[::-1]:
                largestNumber = max(largestNumber, product)
    print largestNumber

main()
