def strip_prefix_suffix():
    a = ' 12334 5678 vinod  '
    print(len(a))
    b = a.strip()
    print(len(b))
    print(b)


def remove_empty_spaces_str():
    a = ' 12334 5678 vinod  '
    b = ''
    for i in a:
        if i == ' ':
            pass
        else:
            b += i
    print(len(b))
    print(b)


def remove_empty_space_list():
    a = ['1', '', '3']
    b = []
    for i in a:
        if i == '': pass
            # i = '2'
            # b.append(i)
        else:
            b.append(i)
    print(b)


if __name__ == '__main__':
    strip_prefix_suffix()
    remove_empty_spaces_str()
    remove_empty_space_list()
