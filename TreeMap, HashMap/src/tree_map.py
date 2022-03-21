class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class TreeMap:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __setitem__(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._add_leaf(key, value, self.root)
        self.size += 1

    def _add_leaf(self, key, value, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._add_leaf(key, value, node.left)

        elif key == node.key:
            node.value = value
        else:
            if node.right is not None:
                self._add_leaf(key, value, node.right)
            else:
                node.right = Node(key, value)

    def __getitem__(self, key):
        if self.root is None:
            raise KeyError
        else:
            node = self._get(key, self.root)
            if node is not None:
                return node.value
        raise KeyError

    def _get(self, key, node):
        if key < node.key:
            return self._get(key, node.left)
        elif key > node.key:
            return self._get(key, node.right)
        elif node.key == key:
            return node
        else:
            return None

    @staticmethod
    def find_left_node(node):
        if node.left is not None:
            return TreeMap.find_left_node(node.left)
        return node

    def __delitem__(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            raise KeyError
        elif key > node.key:
            result = self._delete(node.right, key)
            node.right = result
            return node
        elif key < node.key:
            result = self._delete(node.left, key)
            node.left = result
            return node
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is not None and node.right is None:
                return node.left
            elif node.left is None and node.right is not None:
                return node.right
            else:
                min_node = TreeMap.find_left_node(node.right)
                node.key, node.value = min_node.key, min_node.value
                node.right = self._delete(node.right, min_node.key)
                return node
