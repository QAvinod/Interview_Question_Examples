def reverse_str():
    a = 'sreevani'
    reverse = ''
    for i in a:
        reverse = i + reverse
    print(reverse)


def half_str_reverse():
    a = 'sreevani'
    b = ''
    c = ''
    for i in a:
        if i in ['s', 'r', 'e']:
            b += i
        else:
            c = i + c
    print(b+c)


def half_reverse_with_list():
    lists = ['sreevani']
    string = ''
    normal_string = ''
    reverse_string = ''
    for i in lists:
        string += i
    for i in string:
        if i in ['s', 'r', 'e']:
            normal_string += i
        else:
            reverse_string = i + reverse_string

    add_string = normal_string + reverse_string
    make_list = add_string.split(" ")

    # print(lists)
    # print(string)
    # print(add_string)
    print(make_list)


def string_index_change_reverse():
    lists = ['sreevani']
    string = ''
    string_1 = ''
    string_2 = ''
    for i in lists:
        string += i
    for i in string:
        if i in ['s', 'r', 'e']:
            string_1 += i
        else:
            string_2 += i

    add_string = string_2 + string_1
    make_list = add_string.split(' ')

    # print(lists)
    # print(string)
    # print(string_1)
    # print(string_2)
    # print(add_string)
    print(make_list)


if __name__ == '__main__':
    # reverse_str()
    half_str_reverse()
    half_reverse_with_list()
    # string_index_change_reverse()
