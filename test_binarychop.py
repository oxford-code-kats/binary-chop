import unittest
from binarychop import chop, find_middle_idx

class TestBinaryChop(unittest.TestCase):

	def test_chop_empty_list(self):
		"""chop should return -1 if the search space
		is empty."""
		search_list = []
		target = 3
		expected_idx = -1
		idx = chop(target, search_list)
		self.assertEqual(expected_idx, idx)

	def test_chop_missing_element(self):
		"""chop should return -1 if element is missing from 
		search space"""
		search_list = [1]
		target = 3
		expected_idx = -1
		idx = chop(target, search_list)
		self.assertEqual(expected_idx, idx)

	def test_chop_with_matching_element(self):
		"""chop should return 0 if first element matches."""
		search_list = [1]
		target = 1
		expected_idx = 0
		idx = chop(target, search_list)
		self.assertEqual(expected_idx, idx)

	def test_middle_idx_for_single_item_list(self):
		search_list = [1]
		expected_idx = 0
		middle_idx = find_middle_idx(search_list)
		self.assertEqual(expected_idx, middle_idx)

	def test_middle_idx_for_odd_length_list(self):
		search_list = [1,1,1,1,1]
		expected_idx = 2
		middle_idx = find_middle_idx(search_list)
		self.assertEqual(expected_idx, middle_idx)

	def test_middle_idx_for_even_length_list(self):
		search_list = [1,1,1,1,1,1,1,1]
		expected_idx = 3
		middle_idx = find_middle_idx(search_list)
		self.assertEqual(expected_idx, middle_idx)

	def test_longer_list_search(self):
		search_list = [1, 3, 5, 7, 8]
		target = 4
		expected_idx = -1
		actual_idx = chop(target, search_list)
		self.assertEqual(expected_idx, actual_idx)


if __name__ == "__main__":
	unittest.main()