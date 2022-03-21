class Node(object):
    def __init__(self, data=None):
        # Информационная составляющая
        self.data = data
        # Ссылка на след узел
        self.next = None


class SingleList:
    def __init__(self):
        self.head = None
        self.end = None
        self.max_num = None
        self.sum = None
        self.lenth = 0

    def add_item(self, item):
        item = Node(item)
        if self.head is None:
            self.head = item
        else:
            self.end.next = item
        self.end = item
        self.lenth += 1

    def list_len(self):
        return self.lenth

    def print_list(self):
        now_node = self.head
        while now_node is not None:
            print(now_node.data)
            now_node = now_node.next

    def list_sum(self):
        now_node = self.head
        s = None
        while now_node is not None:
            if isinstance(now_node.data, int) or isinstance(now_node.data, float):
                if s is None:
                    s = 0
                s += now_node.data
            now_node = now_node.next
        return s

    def find_max(self):
        now_node = self.head
        max_num = None
        while now_node is not None:
            if isinstance(now_node.data, int) or isinstance(now_node.data, float):
                if max_num is None:
                    max_num = -100000000000
                if now_node.data > max_num:
                    max_num = now_node.data
            now_node = now_node.next
        return max_num

    def has_otr(self):
        flag = True
        now_node = self.head
        while now_node is not None:
            if isinstance(now_node.data, int) or isinstance(now_node.data, float):
                if now_node.data < 0:
                    flag = False
            now_node = now_node.next
        if flag:
            return f'Не содержит отрицательных чисел'
        return f'Есть отрицательное(ые) число'

    def delete_by_id(self, item_id):
        now_id = 1
        now_node = self.head
        self.lenth -= 1
        prev_node = None
        while now_node is not None:
            if now_id == item_id:
                # если хотим удлать элемент который уже встречался, то заменим на prev_node.data == item
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
        s = ''
        k = 0
        for i in range(self._size):
            for j in self._inner_list[i]:
                s += str(j)
            s += '\n'
        return s

    def __len__(self):
        return self._length

    def __delitem__(self, key):
        hash_id = hash(key) % self._size
        if self._inner_list[hash_id] is not None:
            self._inner_list[hash_id] = SingleList()
            self._length -= 1

    def size(self):
        return self._size

