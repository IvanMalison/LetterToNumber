import solution


solution_function_to_test_value_map = {
	solution.get_partial_sums: [4, 6, 7, 1],
	solution.get_range_tuples: [3, 16, 17, 20],
	solution.get_ranges_from_range_tuples: [(10, 20), (30, 40), (161, 161)],
	solution.get_character_lists_from_number_lists: [range(26), range(26)],
	solution.get_letter_to_number_from_character_lists: [['A', 'B'], ['F', 'P'], ['D', 'C']]
}


def test_functions(functions_dict):
	for solution_function, input_value in solution_function_to_test_value_map.iteritems():
		solution_value = solution_function(input_value)
		actual_value = functions_dict[solution_function.func_name](input_value)

		print solution_function.func_name,
		if solution_value == actual_value:
			print "Suceeded"
		else:
			print "Failed"
			print "Expected Output: %s" % str(solution_value)
			print "Actual Output: %s" % str(actual_value)
