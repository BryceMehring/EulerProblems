# Problem 19: https://projecteuler.net/problem=19

daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def nextMonthStart(day, month, year):
    daysInMonth = daysPerMonth[month - 1]

    if month == 2 and isLeapYear(year):
        daysInMonth += 1

    total = daysInMonth + day
    if total % 7 != 0:
        total %= 7

    return total

def main():
    day = 3
    month = 1
    year = 1901
    sundayCounter = 0
    while year <= 2000:
        day = nextMonthStart(day, month, year)
        if day == 1:
            sundayCounter += 1

        month += 1
        if month >= 13:
            month = 1
            year += 1
    print sundayCounter

main()
