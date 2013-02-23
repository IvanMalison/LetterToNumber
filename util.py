import sys


# The number of letters associated with each number on a phone pad in order.
starting_value = [0, 0] + [3 for i in range(5)] + [4, 3, 4]

def compose(g, f):
	return lambda *args, **kwargs: g(f(*args, **kwargs))

def compose_functions(*args):
	return reduce(compose, args)

def print_incoming_value_with_label(label):
	def inner(value):
		print '%s: ' % label,
		print value
		return value
	return inner

def test_generate_letter_to_number_with_prints(
	generate_letter_to_number_with_prints
):
	expected_result = {
		'A': 2,
		'C': 2,
		'B': 2,
		'E': 3,
		'D': 3,
		'G': 4,
		'F': 3,
		'I': 4,
		'H': 4,
		'K': 5,
		'J': 5,
		'M': 6,
		'L': 5,
		'O': 6,
		'N': 6,
		'Q': 7,
		'P': 7,
		'S': 7,
		'R': 7,
		'U': 8,
		'T': 8,
		'W': 9,
		'V': 8,
		'Y': 9,
		'X': 9,
		'Z': 9
	}
	if expected_result == generate_letter_to_number_with_prints(starting_value):
		print "Success"
	else:
		print "Failure"

def build_generate_letter_to_number_with_prints(globals_dict):
	sys.modules[__name__].__dict__.update(globals_dict)
	return compose_functions(
		print_incoming_value_with_label('letter_to_number'),
		get_letter_to_number_from_character_lists,
		print_incoming_value_with_label('character_lists'),
		get_character_lists_from_number_lists,
		print_incoming_value_with_label('ranges'),
		get_ranges_from_range_tuples,
		print_incoming_value_with_label('range_tuples'),
		get_range_tuples,
		print_incoming_value_with_label('partial_sums'),
		get_partial_sums,
		print_incoming_value_with_label('starting_value'),
	)
