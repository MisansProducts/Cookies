import sys

def max_matrix_indices():
	try:
		dims = input("Enter the dimensions separated by a space (i.e., \"2 2\"): ").split()
		if len(dims) != 2:
			raise IndexError
		
		ROWS, COLS = [int(j) for j in dims]
		
		a = []
		for i in range(ROWS):
			row = input(f"Enter values (row {i + 1}): ").split()
			if len(row) != COLS:
				raise IndexError
			
			row = [int(j) for j in row]
			a.append(row)
	except IndexError as e:
		print(f"Error: Incorrect format.")
		sys.exit(1)
	except ValueError as e:
		print(f"Error: {e}")
		sys.exit(1)
	except KeyboardInterrupt:
		print()
		sys.exit(1)
	mx = -float("inf")
	ind = [0, 0]
	
	print("Matrix:")
	for ROWS, lst in enumerate(a):
		for COLS, val in enumerate(lst):
			print(val, end=' ')
			if val > mx:
				mx = val
				ind = [ROWS, COLS]
		print()

	print("Location of the first maximum point:", *ind)
