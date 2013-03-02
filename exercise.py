#!/usr/bin/env python
import util


def get_partial_sums(number_list):
	"""Return the partial sums of `number_list`.
	Note that the ith entry of the return value should contain the sum of the
	first i-1 values (the ith value is not included).

	Ex: get_partial_sums([2, 3, 4]) == [0, 2, 5, 9].
	"""
	return number_list

def get_range_tuples(increasing_list):
	"""Return a list whose ith entry of is the tuple
	(increasing_list[i], increasing_list[i+1]).

	Ex: get_range_tuples([1, 5, 7, 10]) == [(1, 5), (5, 7), (7, 10)]
	"""
	return increasing_list

def get_ranges_from_range_tuples(range_tuples):
	"""For each (start, end) entry in `range_tuples` there should be a
	corresponding list of integers starting at `start` and ending at `end` - 1.
	in the list that is the output of this function.
	Note:
	To get the list [1, 2, 3] from (1,4) you might use the function range(1, 4)
	Note that this would require you to expand the entries of the tuple.

	Ex: get_ranges_from_range_tuples([(3, 6), (6, 9)]) == [[3, 4, 5], [6, 7, 8]]
	"""
	return range_tuples

def get_character_lists_from_number_lists(number_lists):
	"""Return a list of lists of characters from a list of lists of integer
	values. The 0 should map to "A", 1 should map to "B" etc. The built in
	function chr converts integer values to characters. Note, however, that chr
	does not map 0 to A. This is because the ascci character code for "A" is 65.
	As you might imagine, 66 is the character code for "B", 67 the character code
	for "C" etc.

	get_character_lists_from_number_lists([[0, 1], [2,25]]) == [['A', 'B'], ['C', 'Z']]
	"""
	return number_lists

def get_letter_to_number_from_character_lists(character_lists):
	"""Given a list of lists of characters, return a mapping from the characters
	in each list to the index of the list in which the character appears.

	Ex: get_letter_to_number_from_character_lists([['A', 'B'], ['F', 'P'], ['D', 'C']]) == {'A': 0, 'B': 0, 'C': 2, 'D': 2, 'F': 1, 'P': 1}
	"""
	return character_lists


generate_letter_to_number_with_prints = util.build_generate_letter_to_number_with_prints(globals())


if __name__ == '__main__':
	functions_to_test = {
		func_name: func for func_name, func in vars().iteritems()
		if func_name[:4] == "get_"
	}
	import test
	test.test_functions(functions_to_test)
	generate_letter_to_number_with_prints(util.starting_value)
