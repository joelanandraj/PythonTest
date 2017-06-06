import Bsearch
import unittest

class test_Bsearch(unittest.TestCase):
   

    
    def test_for_Element_in_the_middle(self):
        '''Testing whether the element is present in middle'''
        actual=Bsearch.Bsearch([5,4,1,2,7],4)
        expected="The Element is found in the position 2"
        self.assertEqual(expected,actual)

    def test_for_Element_present_anywhere_in_list(self):
        actual=Bsearch.Bsearch([5,4,1,2,7],2)
        expected="The Element is found in the position 1"
        self.assertEqual(expected,actual)

    def test_for_Element_present_anywhere_in_list2(self):
        actual=Bsearch.Bsearch([5,4,1,2,7,14,22,55,11,10],7)
        expected="The Element is found in the position 4"
        self.assertEqual(expected,actual)

    def test_for_Element_present_anywhere_in_list3(self):
        actual=Bsearch.Bsearch([1,2,3,4,5,6,7,8],1)
        expected="The Element is found in the position 0"
        self.assertEqual(expected,actual)

    def test_for_Element_present_Anywhere_in_the_list4(self):
        actual=Bsearch.Bsearch([8],8)
        expected="The Element is found in the position 0"
        self.assertEqual(expected,actual)
    
    def test_for_char_Element_present_in_the_list5(self):
        actual=Bsearch.Bsearch(['a','b','c','d'],'c')
        expected="The Element is found in the position 2"
        self.assertEqual(expected,actual)

    def test_for_Element_not_Present_in_the_list(self):
        actual=Bsearch.Bsearch([5,4,3,1,18,10,9],12)
        expected="The Element is not present in the list"
        self.assertEqual(expected,actual)
    
    def test_for_Empty_List(self):
        actual=Bsearch.Bsearch([])
        expected="The list is Empty"
        self.assertEqual(expected,actual)
    

if __name__ == '__main__':
    unittest.main()
