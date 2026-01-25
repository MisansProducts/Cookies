def add():
	try:
		n = int(input("Enter the number of numbers you want to add: "))
		if n < 1:
			print("Error: There must be at least 1 number to add with!")
			return True
	except ValueError as e:
		print(f"Error: {e}")
		return True
	except KeyboardInterrupt:
		print()
		return True
	
	z = 0
	for i in range(1, n + 1):
		try:
			x = float(input(f"Addend {i}: "))
		except ValueError as e:
			print(f"Error: {e}")
			return True
		except KeyboardInterrupt:
			print()
			return True
		z += x
		if z % 1 == 0:
			z = int(z)
	print(f"Sum: {z}")
	return False
