# Problem 3: https://projecteuler.net/problem=3
# TODO: this could be cleaned up and checked for correctness even though it gives the correct answer
import math

# http://stackoverflow.com/a/2489519
def IsSquare(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def FermatFactor(N):
    if N % 2 == 0:
        return None

    a = math.ceil(math.sqrt(N))
    b2 = a * a - N

    if a <= 1:
        return None

    while IsSquare(b2) == False:
        a += 1
        b2 = a*a - N
    return a - math.sqrt(b2), a + math.sqrt(b2)

def largestPrimeFactor(N):
    result = FermatFactor(N)
    if (result != None):
        if result[0] == 1 or result[1] == 1:
            return N

        A = largestPrimeFactor(result[0])
        B = largestPrimeFactor(result[1])

        return max(A, B)

def main():
    print largestPrimeFactor(600851475143)

main()
