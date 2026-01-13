def car(degree, t, value):
	print(f"How far did a car travel if it was traveling at {value} m/s^{degree} for {t} seconds?")
	#Suppose (1/a)bc^d
	#Then b/a multiplies by c^d
	d = {} # Dictionary of coeffients b/a
	d[0] = value/degree # Initial coefficient b/a

	#Then introduce c^d
	p = d[0] * t ** degree # Distance Traveled

	#Loop through the degree with natural number i
	for i in range(1, degree):
		d[i] = d[i - 1]/(i) # This key is defined by the previous key (b/a)/i
		p = d[i] * t ** (degree) # New disntance traveled.
	
	print(f"The car traveled {p:.2f} meters.")
