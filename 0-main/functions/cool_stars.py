def cool_stars():
	try:
		d = int(input("Enter the height of the stars: "))
		if d < 1:
			print("Error: Height cannot be less than 1!")
			return True
	except ValueError as e:
		print(f"Error: {e}")
		return True
	except KeyboardInterrupt:
		print()
		return True
	
	for i in range(1, d * 2):
		if i <= d:
			print('*' * i)
		else:
			print('*' * ((d * 2) - i))
	return False
