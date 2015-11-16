# Problem 13: https://projecteuler.net/problem=13

def main():
    with open('source/13/big_numbers.txt') as f:
        total = 0
        for line in f:
            total += int(line)
        print str(total)[:10]

main()
