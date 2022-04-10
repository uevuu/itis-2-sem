"""tests for BaseMap, HashMap, TreeMap"""
import unittest
from src.maps.hash_map import HashMap
from src.maps.tree_map import TreeMap


# from src.maps.base_map import BaseMap
# from test import mapping_tests


class TestMap(unittest.TestCase):
    """General tests"""

    def setUp(self) -> None:
        self.hash_map = HashMap()
        self.tree_map = TreeMap()
        self.hash_map[1] = 19
        self.hash_map['Nikita'] = 'people'
        self.tree_map[4] = 13

    def test_get(self):
        """get tests"""
        self.assertEqual(self.hash_map[1], 19)
        self.assertEqual(self.hash_map['Nikita'], 'people')
        self.assertEqual(self.tree_map[4], 13)

    def test_key_error(self):
        """tests key error"""
        with self.assertRaises(KeyError):
            i = self.hash_map[100000]
            del i

    def test_replace(self):
        """tests replace"""
        self.hash_map[1] = 20
        self.assertEqual(self.hash_map[1], 20)
        self.assertNotEqual(self.hash_map[1], 19)


class TestHashMap(unittest.TestCase):
    """Tests only for HashMap"""

    def setUp(self):
        self.hash_map = HashMap()
        self.hash_map[1] = 3
        self.hash_map[5] = 'kuku'

    def test_increase(self):
        """tests increase"""
        self.hash_map[6] = 'wfwfw'
        self.hash_map['rere'] = 3
        self.assertEqual(self.hash_map.size(), 10)

    def test_not_increase(self):
        """tests not increase"""
        self.hash_map = HashMap(100)
        self.hash_map[1] = 1
        self.hash_map[2] = 2
        self.hash_map[3] = 3
        self.hash_map[4] = 4
        self.hash_map[5] = 5
        self.assertEqual(self.hash_map.size(), 100)

    def test_length(self):
        """tests length"""
        self.hash_map[6] = 'wfwfw'
        self.hash_map['rere'] = 3
        self.assertEqual(len(self.hash_map), 4)

    def test_delete(self):
        """tests delete"""
        del self.hash_map[5]
        self.assertEqual(len(self.hash_map), 1)

    def test_fake_delete(self):
        """tests fake delete"""
        hash_map_was = self.hash_map
        del self.hash_map[1234]
        self.assertEqual(self.hash_map, hash_map_was)


class TestTreeMap(unittest.TestCase):
    """"Tests only for TreeMap"""

    def setUp(self):
        self.tree_map = TreeMap()

    def test_root_none(self):
        """tests root is none"""
        self.assertEqual(self.tree_map.root, None)

    def test_size(self):
        """tests size"""
        self.tree_map[1] = 12
        self.tree_map[45] = 34
        self.assertEqual(self.tree_map.size, 2)

    def test_replace(self):
        """tests replace"""
        self.tree_map[1] = 1
        self.tree_map[2] = 45
        self.tree_map[56] = 34
        self.tree_map[2] = 100
        self.assertEqual(self.tree_map[2], 100)
        self.assertNotEqual(self.tree_map[2], 45)

    def test_replace_root_is_none(self):
        """tests where replaced root == none"""
        self.tree_map = TreeMap()
        self.tree_map[1] = 100
        self.assertNotEqual(self.tree_map.root, None)

    def test_tree_delete_node(self):
        """tests where root is not None"""
        self.tree_map = TreeMap(6)
        self.assertNotEqual(self.tree_map.root, None)


# class GeneralMappingTests(mapping_tests.BasicTestMappingProtocol):
#     """
#     mocked test_read
#     """
#     type2test = HashMap
#
#     def test_read(self):
#         # Test for read only operations on mapping
#         p = self._empty_mapping()
#         p1 = dict(p)  # workaround for singleton objects
#         d = self._full_mapping(self.reference)
#         if d is p:
#             p = p1
#         # Indexing
#         for key, value in self.reference.items():
#             self.assertEqual(d[key], value)
#         knownkey = list(self.other.keys())[0]
#         self.assertRaises(KeyError, lambda: d[knownkey])
#         # len
#         self.assertEqual(len(p), 0)
#         self.assertEqual(len(d), len(self.reference))
#         # __contains__
#         for k in self.reference:
#             self.assertIn(k, d)
#         for k in self.other:
#             self.assertNotIn(k, d)
#         # cmp
#         self.assertEqual(p, p)
#         self.assertEqual(d, d)
#         self.assertNotEqual(p, d)
#         self.assertNotEqual(d, p)
#         # bool
#         if p: self.fail("Empty mapping must compare to False")
#         if not d: self.fail("Full mapping must compare to True")
#
#         # keys(), items(), iterkeys() ...
#         def check_iterandlist(iter, lst, ref):
#             self.assertTrue(hasattr(iter, '__next__'))
#             self.assertTrue(hasattr(iter, '__iter__'))
#             x = list(iter)
#             self.assertTrue(set(x) == set(lst) == set(ref))
#
#         check_iterandlist(iter(d.keys()), list(d.keys()),
#                           self.reference.keys())
#         check_iterandlist(iter(d.keys()), list(d.keys()), self.reference.keys())
#         check_iterandlist(iter(d.values()), list(d.values()),
#                           self.reference.values())
#         check_iterandlist(iter(d.items()), list(d.items()),
#                           self.reference.items())
#         # get
#         key, value = next(iter(d.items()))
#         knownkey, knownvalue = next(iter(self.other.items()))
#         self.assertEqual(d.get(key, knownvalue), value)
#         self.assertEqual(d.get(knownkey, knownvalue), knownvalue)
#         self.assertNotIn(knownkey, d)


if __name__ == '__main__':
    unittest.main()
