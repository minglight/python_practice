import unittest

class TestList(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_slice(self):
        l = [1,2,3,4,5]
        sliced = l[1:3]

        expected = [2,3]

        self.assertEqual(expected, sliced)

    def test_append(self):
        l = [1,2,3,4,5]
        item = ['a', 'b']
        l.append(item)
        length = len(l)
        expected = 6
        self.assertEqual(expected, length)
        #append will append entire list into original one

    def test_extend(self):
        l = [1,2,3,4,5]
        item = ['a', 'b']
        l.extend(item)
        length = len(l)
        expected = 7
        self.assertEqual(expected, length)

    def test_insert(self):
        l = [1,2,3,4,5]
        l.insert(3,'a')
        
        expected = [1,2,3,'a',4,5]
        self.assertEqual(expected, l)

    # del with list[index]
    def test_delete(self):
        l = [1,2,3,4,5]
        del l[-1] 
        
        expected = [1,2,3,4]
        self.assertEqual(expected, l)

    # remove with item "value"
    def test_remove(self):
        l = [1,2,3,4,5]
        l.remove(3)
        
        expected = [1,2,4,5]
        self.assertEqual(expected, l)

    def test_join_int_list_TypeError(self):
        l = [1,2,3,4,5]

        try:
            s = ",".join(l)
        except Exception as e:
             #TypeError: sequence item 0: expected str instance, int found
            self.assertIsInstance(e, TypeError)
           
    def test_join_int_list(self):
        l = [1,2,3,4,5]
       
        s = ",".join([str(i) for i in l ])
        expected = "1,2,3,4,5"

        self.assertEqual(expected, s)

    def test_index(self):
        l = [1,2,3,4,5]
       
        idx = l.index(3)
        expected = 2

        self.assertEqual(expected, idx)

    def test_in(self):
        l = [1,2,3,4,5]
       
        value = 3 in l

        expected = True

        self.assertEqual(expected, value)

    def test_count(self):
        l = [1,2,3,4,5,1,2,3,2]
       
        value = l.count(2)
        
        expected = 3

        self.assertEqual(expected, value)

    def test_pop_with_index(self):
        l = [1,2,3,4,5]
       
        value = l.pop(2)
        
        expected = 3

        self.assertEqual(expected, value)

    def test_pop_without_index_take_last(self):
        l = [1,2,3,4,5]
       
        value = l.pop()
        
        expected = 5

        self.assertEqual(expected, value)

    def test_sort_change_original(self):
        l = [1,2,3,4,5]
       
        l.sort(reverse=True)
        
        expected = [5,4,3,2,1]
        self.assertEqual(expected, l)

    def test_sorted_copy_newone(self):
        l = [1,2,3,4,5]
       
        newOne = sorted(l,reverse=True)
        
        expected = [5,4,3,2,1]
        self.assertEqual(expected, newOne)


    '''
        3 ways of copy 
            - l.copy()
            - list(l)
            - l[:]
    '''
    def test_copy(self):
        l = [1,2,3,4,5]
       
        newOne = l.copy()
        newTwo = list(l)
        newThree = l[:]

        l[3] = 'a'

        
        expected = [1,2,3,4,5]
        self.assertEqual(expected, newOne)
        self.assertEqual(expected, newTwo)
        self.assertEqual(expected, newThree)

    #list('str') will split into ['s','t','r']
    def test_list(self):
        value = list('abcde')
        expected = ['a', 'b', 'c', 'd', 'e']

        self.assertEqual(expected, value)

if __name__ == "__main__":
    unittest.main()