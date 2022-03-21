import unittest
from src.hash_map import HashMap
from src.tree_map import TreeMap


class TestMap(unittest.TestCase):
    def setUp(self) -> None:
        self.hash_map = HashMap()
        self.tree_map = TreeMap()
        self.hash_map[1] = 19
        self.hash_map['Nikita'] = 'people'
        self.tree_map[4] = 13

    def test_get(self):
        self.assertEqual(self.hash_map[1], 19)
        self.assertEqual(self.hash_map['Nikita'], 'people')
        self.assertEqual(self.tree_map[4], 13)

    def test_key_error(self):
        with self.assertRaises(KeyError):
            i = self.hash_map[100000]

    def test_replace(self):
        self.hash_map[1] = 20
        self.assertEqual(self.hash_map[1], 20)
        self.assertNotEqual(self.hash_map[1], 19)


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap()
        self.hash_map[1] = 3
        self.hash_map[5] = 'kuku'

    def test_increase(self):
        # размер должен увеличиться
        self.hash_map[6] = 'wfwfw'
        self.hash_map['rere'] = 3
        self.assertEqual(self.hash_map.size(), 10)

    def test_not_increase(self):
        # размер не должен увеличиться
        self.hash_map = HashMap(100)
        self.hash_map[1] = 1
        self.hash_map[2] = 2
        self.hash_map[3] = 3
        self.hash_map[4] = 4
        self.hash_map[5] = 5
        self.assertEqual(self.hash_map.size(), 100)

    def test_length(self):
        self.hash_map[6] = 'wfwfw'
        self.hash_map['rere'] = 3
        self.assertEqual(len(self.hash_map), 4)

    def test_delete(self):
        del self.hash_map[5]
        self.assertEqual(len(self.hash_map), 1)

    def test_fake_delete(self):
        # хэш мапа не поменяется после удаленеи элемента, которого не было
        hash_map_was = self.hash_map
        del self.hash_map[1234]
        self.assertEqual(self.hash_map, hash_map_was)


class TestTreeMap(unittest.TestCase):
    def setUp(self):
        self.tree_map = TreeMap()

    def test_root_none(self):
        self.assertEqual(self.tree_map.root, None)

    def test_size(self):
        self.tree_map[1] = 12
        self.tree_map[45] = 34
        self.assertEqual(self.tree_map.size, 2)

    def test_replace(self):
        self.tree_map[1] = 1
        self.tree_map[2] = 45
        self.tree_map[56] = 34
        self.tree_map[2] = 100
        self.assertEqual(self.tree_map[2], 100)
        self.assertNotEqual(self.tree_map[2], 45)

    def test_replace_root_is_none(self):
        # дерево меняется
        self.tree_map = TreeMap()
        self.tree_map[1] = 100
        self.assertNotEqual(self.tree_map.root, None)

    def test_tree_delete_node(self):
        # можно задать со значением не None
        self.tree_map = TreeMap(6)
        self.assertNotEqual(self.tree_map.root, None)



if __name__ == '__main__':
    unittest.main()
