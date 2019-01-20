import unittest
from linked_list import List

class TestList(unittest.TestCase):

    def test_init(self):
        list_ = List(value=1, next_=List(value=2, next_=List(value=3)))

        self.assertEqual(list_.value, 1)
        self.assertEqual(list_.next_._value, 2)
        self.assertEqual(list_.next_.next_.value, 3) 
        self.assertEqual(list_.next_.next_.next_, None) 

    def test_append(self):
        list_ = List(value=1, next_=List(value=2, next_=List(value=3)))
        list_.append(4)

        self.assertEqual(list_.value, 1)
        self.assertEqual(list_.next_._value, 2)
        self.assertEqual(list_.next_.next_.value, 3) 
        self.assertEqual(list_.next_.next_.next_.value, 4) 

if __name__ == '__main__':
    unittest.main()