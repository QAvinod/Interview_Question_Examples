list = ['1', '3']
list.append('2')
print(list)

tuple = ('1', '2')
print(tuple)

"""Duplicate values will be ignored:"""
set = {"apple", "banana", "cherry", "apple"}
set.update()
print(set)

dict = {'a': 1, 'b': 1}
dict['mynewkey'] = 'mynewvalue'
print(dict)


for i in list:
    print(f'list - {i}')

for j in tuple:
    print(f'tuple - {j}')

for k in set:
    print(f'set - {k}')

for m in dict:
    print(f'dict - {m}')
