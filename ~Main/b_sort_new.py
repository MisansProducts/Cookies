def bSortNew(amount = 10, min = 0, max = 10):
	l = list(random.randint(min, max) for n in range(amount))
	print("List: ")
	print(*l)
	for i in range(len(l)):
		for j in range(len(l) - 1):
			if l[j] > l[j + 1]:
				temp = l[j]
				l[j] = l[j + 1]
				l[j + 1] = temp
	print("Sorted: ")
	print(*l)
