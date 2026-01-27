from utils.input_validators import get_valid_int

def helper(num, count=0):
	product = 1
	digits = [int(index) for index in str(num)]
	if len(digits) == 1:
		return print(f"Count: {count}")
	
	for i, digit in enumerate(digits):
		if i != len(digits) - 1:
			print(f"{digit} * ", end='')
		else:
			print(f"{digit} = ", end='')
		product *= digit
	count += 1
	print(product)
	helper(product, count)

def mult_p():
	num = get_valid_int("Enter a number: ", min_val=0)
	helper(num)
