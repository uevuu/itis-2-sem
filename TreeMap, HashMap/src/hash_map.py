"""Realisation of Linked list and HashMap"""


class Node:
    """class Node"""

    def __init__(self, data=None):
        # Информационная составляющая
        self.data = data
        # Ссылка на след узел
        self.next = None

    def __str__(self):
        return f'{self.data}'

    def positive_data(self):
        """checking that data >= 0"""
        if self.data >= 0:
            return True
        return False


class SingleList:
    """class Linked List"""

    def __init__(self):
        self.head = None
        self.end = None
        self.max_num = None
        self.sum = None
        self.lenth = 0

    def add_item(self, item):
        """add item"""
        item = Node(item)
        if self.head is None:
            self.head = item
        else:
            self.end.next = item
        self.end = item
        self.lenth += 1

    def list_len(self):
        """return length of linked list"""
        return self.lenth

    def print_list(self):
        """print linked list"""
        now_node = self.head
        while now_node is not None:
            print(now_node.data)
            now_node = now_node.next

    def list_sum(self):
        """return sum of all items in linked list"""
        now_node = self.head
        list_sum = None
        while now_node is not None:
            if isinstance(now_node.data, (int, float)):
                if list_sum is None:
                    list_sum = 0
                list_sum += now_node.data
            now_node = now_node.next
        return list_sum

    def find_max(self):
        """find max element in linked list"""
        now_node = self.head
        max_num = None
        while now_node is not None:
            if isinstance(now_node.data, (int, float)):
                if max_num is None:
                    max_num = -100000000000
                if now_node.data > max_num:
                    max_num = now_node.data
            now_node = now_node.next
        return max_num

    def has_otr(self):
        """checking for the presence of a negative element"""
        flag = True
        now_node = self.head
        while now_node is not None:
            if isinstance(now_node.data, (int, float)):
                if now_node.data < 0:
                    flag = False
            now_node = now_node.next
        if flag:
            return 'Не содержит отрицательных чисел'
        return 'Есть отрицательное(ые) число'

    def delete_by_id(self, item_id):
        """deleting an item by id"""
        now_id = 1
        now_node = self.head
        self.lenth -= 1
        prev_node = None
        while now_node is not None:
            if now_id == item_id:
                if prev_node is not None:
                    prev_node.next = now_node.next
                else:
                    self.head = now_node.next

            prev_node = now_node
            now_node = now_node.next
            now_id += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next


class HashMap:
    """class HashMap"""
    def __init__(self, _size=10):
        self._size = _size
        self._inner_list = [SingleList() for i in range(_size)]
        self._length = 0

    def __setitem__(self, key, value):
        hash_id = hash(key) % self._size
        for element in self._inner_list[hash_id]:
            if key == element[0]:
                element[1] = value
                break
        else:
            self._inner_list[hash_id].add_item([key, value])
            self._length += 1

        if self._length >= self._size * 0.8:
            self._size *= 2
            self._inner_list = self._inner_list + [SingleList() for i in range(self._size)]

    def __getitem__(self, key):
        hash_id = hash(key) % self._size
        for element in self._inner_list[hash_id]:
            if element[0] == key:
                return element[1]
        raise KeyError

    def __str__(self):
        print_s = ''
        for i in range(self._size):
            for j in self._inner_list[i]:
                print_s += str(j)
            print_s += '\n'
        return print_s

    def __len__(self):
        return self._length

    def __delitem__(self, key):
        hash_id = hash(key) % self._size
        if self._inner_list[hash_id] is not None:
            self._inner_list[hash_id] = SingleList()
            self._length -= 1

    def size(self):
        """return size of HashMap"""
        return self._size
