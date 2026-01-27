import sys

from utils.input_validators import get_valid_int

def d_dict():
	n = get_valid_int("Enter the number of entries: ", min_val=1, parameter_name="Number of entries")
	
	print("Define dictionary (Key - Value(s))")
	print("Format: key_1 - value_1, value_2, ..., value_n")
	d = {}
	for i in range(n):
		try:
			l = input(f"Entry {i + 1}: ").split(" - ")
			if len(l) != 2:
				raise IndexError
		except IndexError as e:
			print(f"Error: Incorrect format.")
			sys.exit(1)
		except KeyboardInterrupt:
			print()
			sys.exit(1)
		
		key, values = l
		for value in values.split(', '):
			if value not in d:
				d[value] = []
			d[value].append(key)

	for i in sorted(d):
		print(i, "-", ", ".join(sorted(d[i])))
