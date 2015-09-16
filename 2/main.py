# Problem 2: https://projecteuler.net/problem=2
def fibEvenTotal(maxValue):
    a = 1
    b = 2
    total = 0
    while a < maxValue:
        if a % 2 == 0:
            total += a
        b, a = a + b, b
    return total

def main():
    print fibEvenTotal(4000000)

main()
