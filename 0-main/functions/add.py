def add(n):
	z = 0
	for i in range(1, n + 1):
		x = input(f"Addend {i}: ")
		try:
			x = float(x)
			z += x
			if z % 1 == 0:
				z = int(z)
		except ValueError:
			return print("Error: Not a number.")
	print(f"Sum: {z}")
