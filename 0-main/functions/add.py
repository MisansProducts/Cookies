from utils.input_validators import get_valid_int, get_valid_float

def add():
	n = get_valid_int("Enter the number of numbers you want to add: ", min_val=1, parameter_name="Number of addends")

	z = 0
	for i in range(1, n + 1):
		x = get_valid_float(f"Addend {i}: ")
		z += x
		if z % 1 == 0:
			z = int(z)
	print(f"Sum: {z}")
