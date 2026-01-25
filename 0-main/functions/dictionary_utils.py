def d_dict():
	try:
		n = int(input("Enter the number of entries: "))
		if n < 1:
			print("Error: A dictionary cannot have less than 1 entry!")
			return True
	except ValueError as e:
		print(f"Error: {e}")
		return True
	except KeyboardInterrupt:
		print()
		return True
	
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
			return True
		except KeyboardInterrupt:
			print()
			return True
		
		key, values = l
		for value in values.split(', '):
			if value not in d:
				d[value] = []
			d[value].append(key)

	for i in sorted(d):
		print(i, "-", ", ".join(sorted(d[i])))
	return False
