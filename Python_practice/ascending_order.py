def ascending_order():
    a = [1270, 1362, 1365, 1363, 1366, 1364]
    b = []
    while a:
        ascending = a[0]
        for i in a:
            if i > ascending:
                ascending = i
        b.append(ascending)
        a.remove(ascending)
    print(b)


def descending_order():
    a = [1270, 1362, 1365, 1363, 1366, 1364]
    b = []
    while a:
        descending = a[0]
        for i in a:
            if i < descending:
                descending = i
        b.append(descending)
        a.remove(descending)
    print(b)


if __name__ == '__main__':
    ascending_order()
    descending_order()
