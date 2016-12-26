import unittest
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

	def setUp(self):
		self.dicts = [
			{},
			{'a': 0}, 
			{'a': 0 , 'b': 1, 'c': 2, 'd': 3, 'e': 4}
		]

		for d in self.dicts:
			for key in d:
				assert isinstance(key, str), "For the purpose of only testing traverse order, keys must be in string type"

	def test_empty_dict(self):
		for d in self.dicts:
			if(len(d) == 0):
				for key in d:
					print(d)
					self.assertTrue(False)

	def test_random_correctness(self):
		for d in self.dicts:
			keys = set(d.keys())
			key_list = list(self.toStr(d)).sort()
			for i in range(10):
				self.assertEqual(set(d.keys()), keys)
			for i in range(10):
				cur_str = self.toStr(d)
				# print(cur_str)
				self.assertEqual(list(self.toStr(d)).sort(), key_list)

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

	def test_modify_in_loop(self):
		for d in self.dicts:
			if(len(d) != 0):
				with self.assertRaises(RuntimeError):
					for key in d:
						if(key == 'a'):
							d.pop(key)


if __name__ == '__main__':
	unittest.main()



