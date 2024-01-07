import unittest
from WordSuggestionEngine import *

class TestMethods(unittest.TestCase):

    def test_count_words(self):

        data = {}

        self.assertEqual(0, count_words(data))
        insert(data, 'test')
        self.assertEqual(1, count_words(data))
        insert(data, 'testing')
        self.assertEqual(2, count_words(data))
        insert(data, 'doc')
        self.assertEqual(3, count_words(data))
        insert(data, 'docs')
        self.assertEqual(4, count_words(data))
        insert(data, 'document')
        self.assertEqual(5, count_words(data))
        insert(data, 'documenting')
        self.assertEqual(6, count_words(data))
    

    def test_contains(self):

        data = {}

        self.assertTrue(contains(data, ''))
        self.assertFalse(contains(data, 'try'))
        insert(data, 'tree')
        self.assertTrue(contains(data, ''))
        self.assertFalse(contains(data, 'try'))
        self.assertFalse(contains(data, 'tr'))
        self.assertFalse(contains(data, 'q'))
        self.assertTrue(contains(data, 'tree'))
        insert(data, 'trie')
        self.assertTrue(contains(data, ''))
        self.assertFalse(contains(data, 'try'))
        self.assertFalse(contains(data, 'q'))
        self.assertFalse(contains(data, 'tr'))
        self.assertTrue(contains(data, 'tree'))
        self.assertTrue(contains(data, 'trie'))
        insert(data, 'try')
        self.assertTrue(contains(data, ''))
        self.assertFalse(contains(data, 'tr'))
        self.assertTrue(contains(data, 'tree'))
        self.assertFalse(contains(data, 'q'))
        self.assertTrue(contains(data, 'trie'))
        self.assertTrue(contains(data, 'try'))
        insert(data, 'trying')
        self.assertTrue(contains(data, ''))
        self.assertFalse(contains(data, 'tr'))
        self.assertTrue(contains(data, 'tree'))
        self.assertFalse(contains(data, 'q'))
        self.assertTrue(contains(data, 'trie'))
        self.assertTrue(contains(data, 'try'))
        self.assertTrue(contains(data, 'trying'))
        self.assertFalse(contains(data, 'the'))

        data2 = {'a': [{'p': [{'p': [{'l': [{'e': [{'t': [{}, True], 's': [{}, True]}, True]},
                False]}, True]}, False], 'n': [{}, True]}, False], 'i': [{}, True],
                'o': [{'r': [{'a': [{'n': [{'g': [{'e': [{}, True]}, False]}, False]},
                False], 'i': [{'g': [{'i': [{'n': [{}, True]}, False]}, False]}, False]},
                True]}, False]}

        self.assertTrue(contains(data2, 'app'))
        self.assertTrue(contains(data2, 'apple'))

    
    def test_height(self):
       
        data = {}

        self.assertEqual(0, height(data))

        # docTest
        insert(data, 'test')
        self.assertEqual(4, height(data))
        insert(data, 'testing')
        self.assertEqual(7, height(data))
        insert(data, 'doc')
        self.assertEqual(7, height(data))
        insert(data, 'docs')
        self.assertEqual(7, height(data))
        insert(data, 'document')
        self.assertEqual(8, height(data))
        insert(data, 'documenting')
        self.assertEqual(11, height(data))

        data2 = {}
        insert(data2, 'a')

        self.assertEqual(1, height(data2))


    def test_count_from_prefix(self):

        data = {}

        self.assertEqual(0, count_from_prefix(data, ''))
        self.assertEqual(0, count_from_prefix(data, 'pro'))
        insert(data, 'python')
        self.assertEqual(1, count_from_prefix(data, ''))
        self.assertEqual(0, count_from_prefix(data, 'pro'))
        self.assertEqual(1, count_from_prefix(data, 'py'))
        insert(data, 'pro')
        self.assertEqual(2, count_from_prefix(data, ''))
        self.assertEqual(0, count_from_prefix(data, 'q'))
        self.assertEqual(0, count_from_prefix(data, 'pro'))
        insert(data, 'professionnal')
        self.assertEqual(3, count_from_prefix(data, ''))
        self.assertEqual(0, count_from_prefix(data, 'q'))
        self.assertEqual(1, count_from_prefix(data, 'pro'))
        insert(data, 'program')
        self.assertEqual(4, count_from_prefix(data, ''))
        self.assertEqual(0, count_from_prefix(data, 'q'))
        self.assertEqual(2, count_from_prefix(data, 'pro'))
        insert(data, 'programming')
        self.assertEqual(5, count_from_prefix(data, ''))
        self.assertEqual(0, count_from_prefix(data, 'q'))
        self.assertEqual(3, count_from_prefix(data, 'pro'))
        insert(data, 'programmer')
        self.assertEqual(6, count_from_prefix(data, ''))
        self.assertEqual(0, count_from_prefix(data, 'q'))
        self.assertEqual(4, count_from_prefix(data, 'pro'))
        insert(data, 'programmers')
        self.assertEqual(5, count_from_prefix(data, 'pro'))
        self.assertEqual(1, count_from_prefix(data, 'py'))
        self.assertEqual(3, count_from_prefix(data, 'program'))
        self.assertEqual(7, count_from_prefix(data, ''))


    def test_get_suggestions(self):

        data = {}
        
        self.assertEqual([], get_suggestions(data, ''))
        self.assertEqual([], get_suggestions(data, 'q'))
        insert(data, 'python')
        self.assertEqual(['python'], get_suggestions(data, ''))
        self.assertEqual([], get_suggestions(data, 'q'))
        self.assertEqual(['python'], get_suggestions(data, 'py'))
        insert(data, 'pro')
        self.assertEqual(['python', 'pro'], get_suggestions(data, ''))
        self.assertEqual([], get_suggestions(data, 'q'))
        self.assertEqual(['python'], get_suggestions(data, 'py'))
        self.assertEqual(['python','pro'], get_suggestions(data, 'p'))
        insert(data, 'professionnal')
        self.assertEqual(['python', 'pro', 'professionnal'], get_suggestions(data, ''))
        self.assertEqual([], get_suggestions(data, 'q'))
        self.assertEqual(['python'], get_suggestions(data, 'py'))
        self.assertEqual(['python','pro', 'professionnal'], get_suggestions(data, 'p'))
        insert(data, 'program')
        self.assertEqual(['python', 'pro', 'professionnal', 'program'], get_suggestions(data, ''))
        self.assertEqual([], get_suggestions(data, 'q'))
        self.assertEqual(['python'], get_suggestions(data, 'py'))
        self.assertEqual(['python','pro', 'professionnal', 'program'], get_suggestions(data, 'p'))        
        insert(data, 'programming')
        insert(data, 'programmer')
        insert(data, 'programmers')

        self.assertEqual(['program', 'programming', 'programmer', 'programmers'], get_suggestions(data, 'progr'))
        self.assertEqual(['programming', 'programmer', 'programmers'], get_suggestions(data, 'program'))
        self.assertEqual([], get_suggestions(data, 'programmers'))
        self.assertEqual(['python','pro', 'professionnal','program','programming', 'programmer','programmers'], get_suggestions(data, '')) 

if __name__ == '__main__':
    unittest.main()
