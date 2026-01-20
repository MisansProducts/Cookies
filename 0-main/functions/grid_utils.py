import random

def rand_grid():
	letters = "abcdefghijklmnopqrstuvwxyz"
	size = int(input("Grid size: "))
	grid = []
	for row in range(size):
		currentCol = []
		for col in range(size):
			currentCol.append(random.choice(letters))
		grid.append(currentCol)
	
	for row in range(size):
		for col in range(size):
			print(grid[row][col], end = ' ')
		print()
