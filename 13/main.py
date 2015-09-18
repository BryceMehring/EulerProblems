# Problem 13: https://projecteuler.net/problem=13

def main():
    with open('big_numbers.txt') as f:
        total = 0
        for line in f:
            total += int(line)
        print str(total)[:10]

main()
