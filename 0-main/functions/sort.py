def b_sort():
	try:
		l = input("Type a list elements separated by spaces (i.e., \"1 2 3\"): ").split()
	except KeyboardInterrupt:
		print()
		return True
	
	for i in range(len(l)):
		for j in range(len(l) - 1):
			if l[j] > l[j + 1]:
				temp = l[j]
				l[j] = l[j + 1]
				l[j + 1] = temp
	print(*l)
	return False

def s_sort():
	try:
		l = input("Type a list elements separated by spaces (i.e., \"1 2 3\"): ").split()
	except KeyboardInterrupt:
		print()
		return True
	
	for i in range(len(l)):
		m = i
		for j in range(i + 1, len(l)):
			if l[j] < l[m]:
				m = j
		l[m], l[i] = l[i], l[m]
	print(*l)
	return False

def i_sort():
	try:
		l = input("Type a list elements separated by spaces (i.e., \"1 2 3\"): ").split()
	except KeyboardInterrupt:
		print()
		return True
	
	for i in range(len(l)):
		v = l[i]
		p = i
		while p > 0 and l[p - 1] > v:
			l[p] = l[p - 1]
			p = p - 1
		l[p] = v
	print(*l)
	return False
