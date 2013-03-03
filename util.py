import sys


# The number of letters associated with each number on a phone pad in order.
starting_value = [0, 0] + [3 for i in range(5)] + [4, 3, 4]
BAR = "----------------------------------------------------------------------------------------------------"


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
