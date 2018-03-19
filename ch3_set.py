import unittest
from collections import namedtuple

class TestSet(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #set('str') will split into {'s','t','r'}
    def test_set(self):
        value = set('abcde')
        expected = {'a', 'b', 'c', 'd', 'e'}

        self.assertEqual(expected, value)
    
    def test_set_remove_duplicate(self):
        value = set(['a', 'a', 'b', 'b'])

        expected = {'a','b'}
        
        self.assertEqual(expected, value)

    # using intersection or &
    def test_intersection(self):
        s = set(['a','b','c','d','e'])

        value = s.intersection({'a','g', 'h', 'b'})
        value2 = s & {'a','g', 'h', 'b'}

        expected = {'a', 'b'}

        self.assertEqual(expected, value)
        self.assertEqual(expected, value2)

    # using union or |
    def test_union(self):
        s = set(['a','b','c','d','e'])

        value = s.union({'a','g', 'h', 'b'})
        value2 = s | {'a','g', 'h', 'b'}

        expected = {'a', 'b','c','d','e','g', 'h'}

        self.assertEqual(expected, value)
        self.assertEqual(expected, value2)

    # using difference or -
    def test_difference(self):
        s = set(['a','b','c','d','e'])

        value = s.difference({'a','g', 'h', 'b'})
        value2 = s - {'a','g', 'h', 'b'}

        expected = {'c','d','e'}

        self.assertEqual(expected, value)
        self.assertEqual(expected, value2)

    # using symmetric_difference or ^
    def test__symmetric_difference(self):
        s = set(['a','b','c','d','e'])

        value = s.symmetric_difference({'a','g', 'h', 'b'})
        value2 = s ^ {'a','g', 'h', 'b'}

        expected = {'c','d','e','g','h'}

        self.assertEqual(expected, value)
        self.assertEqual(expected, value2)

    # using issubset or <=
    def test__issubset(self):
        s = set(['a','b','c','d','e'])

        value = s.issubset({'a','b','c','d','e','g', 'h'})
        value2 = s <= {'a','b','c','d','e','g', 'h'}

        expected = True

        self.assertEqual(expected, value)
        self.assertEqual(expected, value2)

    # using issubset or <=
    def test__issuperset(self):
        s = set(['a','b','c','d','e'])

        value = s.issuperset({'a','b','c'})
        value2 = s >= {'a','b','c'}

        expected = True

        self.assertEqual(expected, value)
        self.assertEqual(expected, value2)
    

if __name__ == "__main__":
    unittest.main()