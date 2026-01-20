def max_matrix_indicies():
	ROWS, COLS = [int(j) for j in input("Dimensions: ").split()]
	a = [[int(j) for j in input("Enter values: ").split()] for i in range(ROWS)]

	mx = -float("inf")
	for ROWS, lst in enumerate(a):
		for COLS, val in enumerate(lst):
			if val > mx:
				mx = val
				ind = [ROWS,COLS]
	print("Location of the first maximum point:", *ind)
