import unittest
import string
import random
class TestStringMethods(unittest.TestCase):
	def toStr(self, d):
		s = ''
		for k in d:
			s = s + k
		return s

	def itemToStr(self, d):
		s = ''
		for key, value in d.items():
			s = s + key
		return s

	def generate_random_str(self, n):
		return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

	def setUp(self):
		# test data
		self.dicts = [
			{},
			{'a': 0}, 
			{'a': 0 , 'b': 1, 'c': 2, 'd': 3, 'e': 4}
		]

		for d in self.dicts:
			for key in d:
				assert isinstance(key, str), "For the purpose of only testing traverse order by concat keys, keys must be in string type"
		
		

	# test empty dictionary
	def test_empty_dict(self):
		for d in self.dicts:
			if(len(d) == 0):
				for key in d:
					print(d)
					self.assertTrue(False)

	# test if the randomized key set holds the same keys all the time, e.g. test correctness
	def test_random_correctness(self):
		for d in self.dicts:
			keys = set(d.keys())
			key_list = sorted(list(self.toStr(d)))
			if(len(d) == 0):
				self.assertEqual(keys, set([]))
				self.assertEqual(key_list, [])
			if(len(d) == 1):
				self.assertEqual(keys, set(['a']))
				self.assertEqual(key_list, ['a'])
			if(len(d) == 5):
				self.assertEqual(keys, set(['a', 'b', 'c', 'd', 'e']))
				self.assertEqual(key_list, ['a', 'b', 'c', 'd', 'e'])
			for i in range(10):
				self.assertEqual(set(d.keys()), keys)
			for i in range(10):
				cur_str = self.toStr(d)
				# print(cur_str)
				self.assertEqual(sorted(list(self.toStr(d))), key_list)

	# test if traverse order is non-deterministic
	def test_ifrandom(self):
		for d in self.dicts:
			if(len(d) >= 2):
				found_diff = False
				prev_str = self.toStr(d)
				for i in range(5):
					found_diff = self.toStr(d) != prev_str
					if found_diff:
						break
				self.assertTrue(found_diff)

	# test if modifying dictionary while looping will throw runtime error
	def test_modify_in_loop(self):
		for d in self.dicts:
			if(len(d) != 0):
				with self.assertRaises(RuntimeError):
					for key in d:
						if(key == 'a'):
							d.pop(key)

	# test a large dictionary. If code is correct, buy lottery when this test failed.
	def test_long_dict(self):
		long_dict = {}
		for i in range(100000):
			long_dict[self.generate_random_str(5)] = 1
		for i in range(10):
			self.assertEqual(long_dict.keys(), long_dict.keys())
			self.assertNotEqual(list(long_dict.keys()), list(long_dict.keys()))

if __name__ == '__main__':
	unittest.main()



