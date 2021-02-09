

class testing:
    def __init__(self):
        self.dinesh = ''
        self.offer = ''

    def read_excel(self):
        """dinesh | offer
            a         c
            b         d
            c          e """
        self.dinesh = ['a', 'b', 'c']
        self.offer = ['c', 'd', 'e']

    def create_candidate(self, index):
        print(f'Row {index} |', self.dinesh[index], "|", self.offer[index])


Object = testing()
Object.read_excel()
Total_count = len(Object.dinesh)
print("Number of rows::", Total_count)
i = 0
for looping in range(0, Total_count):
    Object.create_candidate(i)
    i += 1
