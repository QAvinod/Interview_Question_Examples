def add(value1, value2):
    a = value1
    b = value2
    c = a + b
    print(c)
    return c


if __name__ == "__main__":
    if add(2, 4) == 6:
        print('return success')
    else:
        print('return failed')
