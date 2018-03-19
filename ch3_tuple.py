import unittest
from collections import namedtuple

class TestTuple(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_slice(self):
        t = (1,2,3,4,5)
        
        value = t[1:3] 
        
        expected = (2,3)

        self.assertEqual(expected, value)

    def test_unpacking(self):
        t = (1,2,3,4,5)

        a,b,c,d,e = t

        expected = 3

        self.assertEqual(expected, c)
    
    
    def test_namedtuple(self):
        # from collections import namedtuple
        Person = namedtuple('Person', 'name age')
        ivan = Person(name='Ivan', age=30)

        expected = "Ivan"

        self.assertEqual(expected, ivan.name)

    #tuple('str') will split into ('s','t','r')
    def test_tuple(self):
        value = tuple('abcde')
        expected = ('a', 'b', 'c', 'd', 'e')

        self.assertEqual(expected, value)



if __name__ == "__main__":
    unittest.main()