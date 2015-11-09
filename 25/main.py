def fibValue(length):
    a = 1
    b = 1
    index = 0
    while len(str(a)) != length:
        b, a = a + b, b
        index += 1
    return (index + 1, a)

def main():
    print fibValue(1000)

main()
