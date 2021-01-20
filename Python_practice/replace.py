def replace_remove_letter():
    a = 'sreevani'
    b = a.replace('e', '')
    print("Remove_Letters ::", b)


def replace_with_letter():
    a = 'sreevani'
    b = a.replace('vani', 'vinni')
    c = a.replace('e', 'v')
    print("Change_Letter ::", b)
    print("Change_Letters ::", c)


def replace_with_index_word():
    a = 'sreevani sreevani'
    a = a.replace('vani', 'heart', 1)
    print("Change_index_word_letters ::", a)


def real_example_behind_replace():
    string = 'sreevani'
    # Define your variables
    result = ''
    for i in string:
        if i == 'e':
            i = ''
        result += i
    print(result)


def real_example_behind_replace_1():
    string = list('sreevani sreevani')
    result = []
    for i in string:
        if i == 'e':
            i = ''
        result.append(i)
    print('test', result)
    print(''.join(result))


def real_example_behind_replace_2():
    lists = ['sreevani']
    list1 = []
    list2 = []
    for i in lists:
        for j in i:
            list1.append(j)
    for v in list1:
        if v == 'e':
            v = 'V'
            list2.append(v)
        else:
            list2.append(v)

    print(''.join(list2))
    make_list = ''.join(list2)
    li = list(make_list.split(" "))
    print(li)


def replace_int_value():
    a = 1233356
    b = ''
    for i in str(a):
        if i == '3':
            i = '4'
            b += i
        else:
            b += i
    print(int(b))


if __name__ == '__main__':
    # replace_remove_letter()
    # replace_with_letter()
    # replace_with_index_word()
    # real_example_behind_replace()
    # real_example_behind_replace_1()
    real_example_behind_replace_2()
    # replace_int_value()
