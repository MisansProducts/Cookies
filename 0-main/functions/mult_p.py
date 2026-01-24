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
	try:
		num = int(input("Enter a number: "))
		if num < 0:
			print("Error: Number cannot be negative!")
			return True
	except ValueError as e:
		print(f"Error: {e}")
		return True
	except KeyboardInterrupt:
		print()
		return True
	
	helper(num)
	return False
