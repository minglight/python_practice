import unittest
from collections import namedtuple

class TestDict(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_with_2elements_iterator(self):
        lot = [('a',1), ('b',2), ('c', 'mytoken')]
        lot2 = (['a',1], ['b',2], ['c', 'mytoken'])


        value = dict(lot)
        value2 = dict(lot2)


        expected = {'a':1, 'b':2, 'c':'mytoken'}

        self.assertEqual(expected, value)
        self.assertEqual(expected, value2)


    def test_override_by_key(self):
        
        d = {'a':1, 'b':2, 'c':'mytoken'}

        d['b'] = 3

        expected = 3

        self.assertEqual(expected, d['b'])

    def test_update_by_another_dict(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        add = {'e': 10.3, 'f': 'hahaha'}

        d.update(add)

        expected = {'a':1, 'b':2, 'c':'mytoken', 'e': 10.3, 'f': 'hahaha'}

        self.assertEqual(expected , d)

    def test_del_by_key(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        del d['c']

        expected = {'a':1, 'b':2}

        self.assertEqual(expected , d)

    def test_clear_to_empty(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        d.clear()

        expected = {}

        self.assertEqual(expected , d)

    def test_in_by_key(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        value = 'b' in d

        expected = True

        self.assertEqual(expected , value)


    def test_keys_not_list(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        value = d.keys()
        
        expected =  ['a','b','c']
        
        #dict_keys(['a', 'b', 'c'])
        self.assertNotIsInstance(value, list)

    def test_keys_to_list(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        value = list(d.keys())
        
        expected =  ['a','b','c']
        
        self.assertEqual(expected, value)

    def test_values(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        value = list(d.values())
        
        expected =  [1,2,'mytoken']
        
        self.assertEqual(expected, value)

    def test_items(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        for k,v in d.items():
            if k == 'b':
                expected = 2
                self.assertEqual(expected, v)

    def test_loop_default_only_keys(self):
        d = {'a':1, 'b':2, 'c':'mytoken'}

        keys = ['a','b','c']
        for k in d:
            expected = True
            self.assertEqual(expected, k in keys )
        
        

if __name__ == "__main__":
    unittest.main()