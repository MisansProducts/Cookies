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
	prompt = (
		"Please select an option from the list below or type 0 to exit.\n"
		"1) Car Problem\n\tCalculates the displacement of a car that is traveling at some derivative order with a flat magnitude over a length of time.\n"
		"2) Multiplicative persistence\n\tRepeatedly multiplies the digits of a number until a single digit is reached, then counts how many multiplication steps that took.\n"
		"3) cool_stars(d) - Generates a pattern of stars.\n"
		"4) add(n) - Adds a list of numbers together.\n"
		"5) multiply(n) - Multiplies a list of numbers together.\n"
		"6) find_time() - Calculates the time on a clock from the given time and the time elapsed.\n"
		"7) b_sort() - Bubble sort a list of numbers.\n"
		"8) s_sort() - Selection sort a list of numbers.\n"
		"9) i_sort() - Insertion sort a list of numbers.\n"
		"10) max_matrix_indicies() - Finds the coordinates of the largest number in a matrix.\n"
		"11) d_dict() - Reverses keys and values in a dictionary data type.\n"
		"12) proj_1() - Gets quotient and remainder.\n"
		"13) proj_2() - Gets elapsed time.\n"
		"14) proj_3() - Unfinished.\n"
		"15) rand_grid() - Produces a grid of random letters.\n"
		"Response: "
	)
	options = (
		car,
		mult_p,
		cool_stars,
		add,
		multiply,
		find_time,
		b_sort,
		s_sort,
		i_sort,
		max_matrix_indicies,
		d_dict,
		proj_1,
		proj_2,
		proj_3,
		rand_grid
	)
	option = 0
	N = len(options)

	# Input sanitization
	try:
		option = int(input(prompt))
		if option < 0 or option > N:
			print(f"Error: Response must be between 0 and {N}!")
			return True
	except ValueError as e:
		print(f"Error: {e}")
		return True
	except KeyboardInterrupt:
		print()
		return True
	
	if option == 0:
		return False
	
	return options[option - 1]()

#======Execution Check======
if __name__ == "__main__":
	print("Hello world!")
	main()
