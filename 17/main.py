# Problem 17: https://projecteuler.net/problem=17

NUMBERS = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

TENS = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

def numToWord(n):
    if n <= 19:
        return NUMBERS[n]
    else:
        strNum = str(n)
        if n < 100:
            # 20 - 99
            return TENS[int(strNum[0]) - 2] + ' ' + numToWord(int(strNum[1]))
        elif n < 1000:
            #100 - 999
            hundredPart = numToWord(int(strNum[0])) + ' hundred'
            tensPart = numToWord(int(strNum[1:]))
            if len(tensPart) <= 0:
                return hundredPart + ' and ' + tensPart
            else:
                return hundredPart
        elif n == 1000:
            return 'one thousand'

def main():
    totalLength = 0
    for i in range(1, 1001):
        number = numToWord(i)
        totalLength += len(number.replace(' ', ''))
        print number
    print totalLength

main()
