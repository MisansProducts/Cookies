import sys

#======Function Imports======
from functions.car import car
from functions.mult_p import mult_p
from functions.cool_stars import cool_stars
from functions.add import add
from functions.multiply import multiply
from functions.find_time import find_time
from functions.sort import b_sort, s_sort, i_sort
from functions.matrix_operations import max_matrix_indices
from functions.dictionary_utils import d_dict
from functions.projects import proj_1, proj_2, proj_3
from functions.grid_utils import rand_grid

from utils.input_validators import get_valid_int

def _exit():
	print("Goodbye world!")
	sys.exit(0)

#======Main======
def main():
	prompt = (
		"Please select an option from the list below or type 0 to exit.\n"
		"1) Car Problem\n\tCalculates the displacement of a car that is traveling at some derivative order with a flat magnitude over a length of time.\n"
		"2) Multiplicative persistence\n\tRepeatedly multiplies the digits of a number until a single digit is reached, then counts how many multiplication steps that took.\n"
		"3) Cool stars\n\tGenerates a pattern of stars given a maximum height.\n"
		"4) Add\n\tAdds a list of numbers together.\n"
		"5) Multiply\n\tMultiplies a list of numbers together.\n"
		"6) Find time elapsed\n\tCalculates the time on a clock from the given time and the time elapsed.\n"
		"7) Bubble sort\n\tUses bubble sort on a list of numbers.\n"
		"8) Selection sort\n\tUses selection sort on a list of numbers.\n"
		"9) Insertion sort\n\tUses insertion sort on a list of numbers.\n"
		"10) Matrix max indices\n\tFinds the coordinates of the largest number in a matrix.\n"
		"11) Reverse dictionary\n\tReverses keys and values in a dictionary.\n"
		"12) Project 1\n\tGets quotient and remainder using cookies.\n"
		"13) Project 2\n\tGets elapsed time.\n"
		"14) Project 3\n\tGets number of days between 2 dates.\n"
		"15) Random grid\n\tProduces a grid of random letters.\n"
		"Response: "
	)
	options = (
		_exit,
		car,
		mult_p,
		cool_stars,
		add,
		multiply,
		find_time,
		b_sort,
		s_sort,
		i_sort,
		max_matrix_indices,
		d_dict,
		proj_1,
		proj_2,
		proj_3,
		rand_grid
	)
	option = get_valid_int(prompt, min_val=0, max_val=len(options)-1, parameter_name="Response")
	print()
	return options[option]()

#======Execution Check======
if __name__ == "__main__":
	print("Hello world!")
	main()
