from decimal import *

def isCuriousFraction(a, b):
    if a >= b:
        return False

    strA = str(a)
    strB = str(b)

    if len(strA) != 2 or len(strB) != 2:
        return False
    if b == 0 or int(strB[0]) == 0 or int(strB[1]) == 0:
        return False
    if strA[0] != strB[1] and strA[1] != strB[0]:
        return False

    fraction = a / float(b)

    return fraction == (int(strA[0]) / float(strB[1])) or fraction == (int(strA[1]) / float(strB[0]))

def main():
    product = Decimal(1)
    for a in range(10, 100):
        for b in range(10, 100):
            if isCuriousFraction(a, b):
                product *= (Decimal(a) / Decimal(b))

    result = Decimal(1) / product
    print('{0:f}'.format(result))

main()
