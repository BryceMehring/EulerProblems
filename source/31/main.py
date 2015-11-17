COIN_VALUE = [200, 100, 50, 20, 10, 5, 2, 1]
cache = {}

def coinSum(n, k):
    if (n, k) not in cache:
        if k < 1 or n < 0:
            cache[(n, k)] = 0
        elif n == 0:
            cache[(n, k)] = 1
        else:
            cache[(n, k)] = coinSum(n, k - 1) + coinSum(n - COIN_VALUE[k - 1], k)

    return cache[(n, k)]

def main():
    print coinSum(200, 8)

main()
