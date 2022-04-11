class Long:
    def __init__(self, number):
        self.list = self.num_to_list(number)

    def num_to_list(self, number):
        """Преобразует число в массив из цифр"""
        help_list = []
        curr = abs(number)
        while curr != 0:
            help_list.append(curr % 10)
            curr //= 10
        if number < 0:
            help_list.append('-')
        elif number == 0:
            help_list.append(0)
        return help_list[::-1]

    def __str__(self):
        return f'{self.list}'

    __repr__ = __str__

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __len__(self):
        return len(self.list)

    def __add__(self, other):
        if isinstance(other, int):
            other = Long(other)
        if isinstance(other, Long):
            if (other[0] == '-' and self.list[0] == '-') or (other[0] != '-' and self.list[0] != '-'):
                if other[0] == '-':
                    new_len = (max(len(self.list), len(other)))
                    other = [0] * (new_len - len(other) + 1) + other.list[1:]
                    now_long = [0] * (new_len - len(self.list) + 1) + self.list[1:]
                else:
                    new_len = (max(len(self.list), len(other)) + 1)
                    other = [0] * (new_len - len(other)) + other.list
                    now_long = [0] * (new_len - len(self.list)) + self.list
                new_long = []
                summ = 0
                for index in range(new_len - 1, -1, -1):
                    summ += other[index] + now_long[index]
                    new_long.append(summ % 10)
                    summ = summ // 10
                if new_long[-1] == 0:
                    del new_long[-1]
                if self.list[0] == '-':
                    new_long.append('-')
                return new_long[::-1]

    def __neg__(self):
        if self.list[0] == '-':
            del self.list[0]
        else:
            self.list = ['-'] + self.list

    def __eq__(self, other):
        if isinstance(other, int):
            other = Long(other)
        if len(other) != len(self.list):
            return False
        for i in range(len(other)):
            if other[i] != self.list[i]:
                return False
        return True

    __ne__ = __eq__

    def __lt__(self, other):
        """x < y"""
        if isinstance(other, int):
            other = Long(other)
        if other[0] == '-' and self.list[0] == '-':
            if len(self.list) != len(other):
                return len(self.list) > len(other)
            for i in range(len(other)):
                if self.list[i] != other[i]:
                    return self.list[i] > other[i]
            return False
        elif other[0] != '-' and self.list[0] != '-':
            if len(self.list) != len(other):
                return len(self.list) < len(other)
            for i in range(len(other)):
                if self.list[i] != other[i]:
                    return self.list[i] < other[i]
            return False

        elif other[0] != '-' and self.list[0] == '-':
            return False
        elif other[0] == '-' and self.list[0] != '-':
            return True
        return False
