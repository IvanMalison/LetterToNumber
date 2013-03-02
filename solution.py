#!/usr/bin/env python
import util

# The ith entry of the following list contains the sum of the 0 to i-1th entries
# in starting value. We want to calculate these values because this will be the
# numeral associated with the first letter that maps to i on a phone dial pad.
def get_partial_sums(number_list):
	return [sum(number_list[:i]) for i in range(len(number_list)+1)]

# The end of the range of the ith number will be the start of the i+1th, thus
# we zip all the values together yielding tuples of the form
# (partial_sums[i], partial_sums[i+1]) for i < len(partial_sums) - 1
# in other words, this is equivalent to
# (partial_sums[i], partial_sums[i+1]) for i in range(len(partial_sums) - 1)
def get_range_tuples(increasing_list):
	return zip(increasing_list[:-1], increasing_list[1:])

# We use the range function to generate lists of the actual values to associate
# with each number. The expression below is just a fancy way of saying
# [range(start, end) for start, end in range_tuples] or more simply
# [range(range_tuple[0], range_tuple[1]) for range_tuple in range_tuples]
def get_ranges_from_range_tuples(range_tuples):
	return [range(*range_tuple) for range_tuple in range_tuples]

# Now we want to convert these numbers into actual characters.
# We will do this by using the map function, which applies a function to each
# element of an iterable and returns the resulting iterable. e.g.
# map(lambda x: x+1, [1,2,3]) == [2,3,4]
# In our case, we have a nested list, and the elements that we actually want to
# operate on are one level deeper. i.e. we have [[], [], [0, 1, 2], ...],
# and we want to produce [[], [], ['A', 'B', 'C'], ...]. This means that the
# function that we pass to map has to operate on lists. Since the numbers that
# we want to operate on are a level deeper, we perform a map inside of this of
# this function with the number -> character mapping (lambda char: chr(char+65))
# as the operator.
def get_character_lists_from_number_lists(number_lists):
	return map(
		lambda number_list: map(lambda char: chr(char+65), number_list),
		number_lists
	)

# The final step is to create the mapping between characters in each character list
# to the number that is the index of their containing list. We enumeare the
# character_lists to give us easy access to their respective indices. Then we
# iterate over these tuples, with another layer of iteration on each character
# list. Now we have access to the letter and the number, so we simply map the
# letter to the number.
def get_letter_to_number_from_character_lists(character_lists):
	return {
		letter: number
		for number, letters in enumerate(character_lists)
		for letter in letters
	}

generate_letter_to_number_with_prints = util.build_generate_letter_to_number_with_prints(vars())

if __name__ == '__main__':
	util.test_generate_letter_to_number_with_prints(
		generate_letter_to_number_with_prints
	)
