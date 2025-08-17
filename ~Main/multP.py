#Multiplicative Persistence
def multP(num, count = 0):
	product = 1
	digits = [int(index) for index in str(num)]
	for element in digits:
		product *= element
	if len(digits) == 1:
		return print(f"Count: {count}")
	count += 1
	print(product)
	multP(product, count)