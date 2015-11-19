def main():
    total = 0
    for i in range(1, 10 ** 6):
        numberStr = str(i)
        binNumberStr = bin(i)[2:]
        if numberStr == numberStr[::-1] and binNumberStr == binNumberStr[::-1]:
            total += i
    print total

main()
