def add(value):
    a = value
    b = 3
    c = a + b
    print(c)
    return c


if __name__ == "__main__":
    if add(2) == 6:
        print('return success')
    else:
        print('return failed')
