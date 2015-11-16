import itertools

def tupleToInt(value):
    return reduce(lambda rst, d: rst * 10 + d, value)

def main():
    for index, value in enumerate(itertools.permutations(range(0, 10), 10)):
        if index + 1 == 1000000:
            print tupleToInt(value)
            break

main()
