# Problem 22: https://projecteuler.net/problem=22

def charToIndex(c):
    return ord(c) - 64

def main():
    with open('22/names.txt') as f:
        names = f.read()
        names = names.replace('"', '')
        nameArray = names.split(',')
        nameArray.sort()
        total = 0
        for i, name in enumerate(nameArray):
            nameTotal = 0
            for c in name:
                nameTotal += charToIndex(c)
            total += nameTotal * (i + 1)
        print total

main()
