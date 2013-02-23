#!/usr/bin/env python
import util

def get_partial_sums(number_list):
	return number_list

def get_range_tuples(increasing_list):
	return increasing_list

def get_ranges_from_range_tuples(range_tuples):
	return range_tuples

def get_character_lists_from_number_lists(number_lists):
	return number_lists

def get_letter_to_number_from_character_lists(character_lists):
	return character_lists

generate_letter_to_number_with_prints = util.build_generate_letter_to_number_with_prints(globals())

if __name__ == '__main__':
	util.test_generate_letter_to_number_with_prints(
		generate_letter_to_number_with_prints
	)
