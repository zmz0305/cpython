import os
import string
import random

import unittest


class TestDictRandomTraverse(unittest.TestCase):
    def _to_str(self, d):
        s = ''
        for k in d:
            s = s + k
        return s

    def _item_to_str(self, d):
        s = ''
        for key, value in d.items():
            s = s + key
        return s

    def _generate_random_str(self, n):
        return ''.join(
            random.choice(string.ascii_uppercase + string.digits) \
            for _ in range(n))

    def setUp(self):
        # Test data
        self.dicts = [
            {},
            {'a': 0}, 
            {'a': 0 , 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        ]

        for d in self.dicts:
            for key in d:
                assert isinstance(key, str), \
                    "For the purpose of only testing traverse \
                    order by concat keys, keys must be in string type"
        
        

    def test_empty_dict(self):
        """
        Test empty dictionary
        """
        for d in self.dicts:
            if(len(d) == 0):
                for key in d:
                    print(d)
                    self.assertTrue(False)

    def test_random_correctness1(self):
        """
        Test if the randomized key set holds the same keys all the time.
        """
        os.environ['PY_SRAND'] = '1'
        for d in self.dicts:
            keys = set(d.keys())
            key_list = list(self._to_str(d))
            if(len(d) == 0):
                self.assertEqual(keys, set([]))
                self.assertEqual(key_list, [])
            if(len(d) == 1):
                self.assertEqual(keys, set(['a']))
                self.assertEqual(key_list, ['a'])
            if(len(d) == 5):
                self.assertEqual(keys, set(['a', 'b', 'c', 'd', 'e']))
                self.assertEqual(key_list, ['c', 'a', 'e', 'd', 'b'])
            

    def test_random_correctness2(self):
        os.environ['PY_SRAND'] = '2'
        for d in self.dicts:
            keys = set(d.keys())
            key_list = list(self._to_str(d))
            if(len(d) == 0):
                self.assertEqual(keys, set([]))
                self.assertEqual(key_list, [])
            if(len(d) == 1):
                self.assertEqual(keys, set(['a']))
                self.assertEqual(key_list, ['a'])
            if(len(d) == 5):
                self.assertEqual(keys, set(['a', 'b', 'c', 'd', 'e']))
                self.assertEqual(key_list, ['e', 'd', 'c', 'b', 'a'])

    def test_modify_in_loop1(self):
        """
        Test if modifying dictionary while looping will throw runtime 
        error should raise runtime error due to change of dictionary  
        length during traverse.
        """
        for d in self.dicts:
            if(len(d) > 1):
                with self.assertRaises(RuntimeError):
                    for key in d:
                        if(key == 'a'):
                            d.pop(key)
                with self.assertRaises(RuntimeError):
                    for key in d:
                        d['z'] = 1

    def test_modify_in_loop2(self):
        """
        Test when modifying but the dict length does not change. It 
        should not throw errors.
        """
        for d in self.dicts:
            if(len(d) != 0):
                for key in d:
                    if(key == 'a'):
                        d.pop(key)
                        d['z'] = 1
                    if(key == 'b'):
                        d.pop(key)
                        d['b'] = 1

    def test_modify_in_loop3(self):
        """
        Test when a key is deleted then add back into the dictionary,
        if the traverse order remains the same.
        """
        os.environ['PY_SRAND'] = '1'
        for d in self.dicts:
            if(len(d) == 5):
                key_list = list(d.keys())
                d.pop('a')
                d['a'] = 1
                self.assertEqual(key_list, ['c', 'a', 'e', 'd', 'b'])

    def test_modify_in_loop4(self):
        """
        Test when multiple keys are deleted then add back into the 
        dictionary, if the traverse order remains the same.
        """
        os.environ['PY_SRAND'] = '2'
        for d in self.dicts:
            if(len(d) == 5):
                key_list = list(d.keys())
                d.pop('b')
                d['b'] = 1
                d.pop('a')
                d.pop('c')
                d['a'] = 1
                d['c'] = 1
                self.assertEqual(key_list, ['e', 'd', 'c', 'b', 'a'])

    def test_long_dict(self):
        """
        Test both randomness and data integrity of a large dictionary
        """
        long_dict = {}
        for i in range(1000):
            long_dict[i] = 1
        for i in range(10):
            os.environ['PY_SRAND'] = '3'
            rand1 = long_dict.keys()
            rand1_list = list(rand1)
            os.environ['PY_SRAND'] = '4'
            rand2 = long_dict.keys()
            rand2_list = list(rand2)
            self.assertEqual(rand1, rand2)
            self.assertNotEqual(rand1_list, rand2_list)
        for i in range(1000):
            if(i % 3 == 0):
                long_dict.pop(i)
        for i in range(1000):
            if(i % 3 == 0):
                long_dict[str(i)] = 1
        for i in range(1000):
            if(i % 3 != 0):
                long_dict.pop(i)
        for i in range(1000):
            if(i % 3 != 0):
                long_dict[str(i)] = 1
        self.assertEqual(len(long_dict), 1000)
        for i in range(1000):
            self.assertTrue(str(i) in long_dict)
            long_dict.pop(str(i))
            long_dict[i] = 1
        self.assertEqual(rand2_list, list(long_dict.keys()))

if __name__ == '__main__':
    unittest.main()



