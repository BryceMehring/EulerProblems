# Problem 8: https://projecteuler.net/problem=8

def largestAdjacentProduct(bigNumber, length):
    bigestProduct = 0
    bigestProducts = []
    for i in range(length, len(bigNumber), 1):
        product = 1
        productRange = []

        for j in range(i - length, i):
            digit = int(bigNumber[j])
            product *= digit
            productRange.append(digit)

        if product > bigestProduct:
            bigestProduct = product
            bigestProducts = productRange

    return {
        'product': bigestProduct,
        'products': bigestProducts
    }

def main():
    with open('big_number.txt') as f:
        bigNumber = f.read()
        print largestAdjacentProduct(bigNumber, 13)

main()
