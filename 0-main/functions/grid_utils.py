import random

from utils.input_validators import get_valid_int

def rand_grid():
	size = get_valid_int("Grid size: ", min_val=1, parameter_name="Grid size")
	
	letters = "abcdefghijklmnopqrstuvwxyz"
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
