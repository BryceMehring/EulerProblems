def main():
    digits = ''.join(map(lambda x: str(x), range(1000000)))
    product = 1
    for i in range(7):
        product *= int(digits[10 ** i])

    print product

main()
