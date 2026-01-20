#Made by Alex

#======Libraries======
import random

#======Function Imports======
from functions.car import car
from functions.mult_p import mult_p
from functions.cool_stars import cool_stars
from functions.add import add
from functions.multiply import multiply
from functions.find_time import find_time
from functions.sort import b_sort, s_sort, i_sort
from functions.matrix_operations import max_matrix_indicies
from functions.dictionary_utils import d_dict
from functions.projects import proj_1, proj_2, proj_3
from functions.grid_utils import rand_grid

#======Main======
def main():
	prompt = [
		"1) car(degree, t, value) - Calculates the displacement of some object over an initial exponent of velocity.",
		"2) mult_p(num, count = 0) - Calculates the multiplicative persistence of a number.",
		"3) cool_stars(d) - Generates a pattern of stars.",
		"4) add(n) - Adds a list of numbers together.",
		"5) multiply(n) - Multiplies a list of numbers together.",
		"6) find_time() - Calculates the time on a clock from the given time and the time elapsed.",
		"7) b_sort() - Bubble sort a list of numbers.",
		"8) s_sort() - Selection sort a list of numbers.",
		"9) i_sort() - Insertion sort a list of numbers.",
		"10) max_matrix_indicies() - Finds the coordinates of the largest number in a matrix.",
		"11) d_dict() - Reverses keys and values in a dictionary data type.",
		"12) proj_1() - Gets quotient and remainder.",
		"13) proj_2() - Gets elapsed time.",
		"14) proj_3() - Unfinished.",
		"15) rand_grid() - Produces a grid of random letters."
	]
	inputFlag = True
	response = 0

	while (inputFlag):
		print("Please select an option from the list below.")
		print("Or, type 0 to exit.")
		for option in prompt:
			print(option)
		try:
			response = int(input("Response: "))
		except:
			print("Error. Response not an integer.")
		else:
			inputFlag = False
	
	if response == 0:
		return -1
	elif response == 1:
		car(4, 4, 4)
	elif response == 2:
		mult_p(4, count = 0)
	elif response == 3:
		cool_stars(4)
	elif response == 4:
		add(4)
	elif response == 5:
		multiply(4)
	elif response == 6:
		find_time()
	elif response == 7:
		b_sort()
	elif response == 8:
		s_sort()
	elif response == 9:
		i_sort()
	elif response == 10:
		max_matrix_indicies()
	elif response == 11:
		d_dict()
	elif response == 12:
		proj_1()
	elif response == 13:
		proj_2()
	elif response == 14:
		proj_3()
	elif response == 15:
		rand_grid()

#======Execution Check======
if __name__ == "__main__":
	print("Hello world!")
	while True:
		if main() == -1:
			break
