def d_dict():
	d = {}
	n = int(input("Amount of lines: "))
	for i in range(n):
		key, value = input("Define dictionary (Key - Value(s)): ").split(" - ")
		
		for i in value.split(', '):
			if i not in d:
				d[i] = []
			d[i].append(key)
	print(len(d))
	for i in sorted(d):
		print(i, "-", ", ".join(sorted(d[i])))
