def join_string():
    a = '123'
    b = '4'
    print(b.join(a))


def join_list_str():
    a = ['1', '2', '3']
    b = ''
    for i in a:
        b += i
    print(b)

    li = b.split(' ')
    print(li)


def join_list_int():
    a = [1, 2, 3]
    # b = ''
    print(''.join(a))


def example_join_string():
    a = '123'
    b = ''
    for i in a:
        if i in ['1', '2', '3']:
            b += i
            b += '4'
        else:
            b += i
    print(b)


def example_join_string_2():
    a = 123
    b = str(a)
    c = ''
    for i in b:
        if i in ['1', '2']:
            c += i
        elif i == '3':
            c += i
            c += '4'
    print(c)


if __name__ == '__main__':
    join_string()
    join_list_str()
    # join_list_int()
    # example_join_string()
    # example_join_string_2()
