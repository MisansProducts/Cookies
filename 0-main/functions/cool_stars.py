from utils.input_validators import get_valid_int

def cool_stars():
	d = get_valid_int("Enter the height of the stars: ", min_val=1, parameter_name="Height")
	
	for i in range(1, d * 2):
		if i <= d:
			print('*' * i)
		else:
			print('*' * ((d * 2) - i))
