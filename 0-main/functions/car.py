def car():
	try:
		order = int(
			input(
				"\nWhat derivative order was the car traveling?\n"
				"1) Velocity (m/s)\n"
				"2) Acceleration (m/s^2)\n"
				"3) Jerk (m/s^3)\n"
				"4) Jounce (m/s^4)\n"
				"...\n"
				"n) n-th derivative (m/s^n)\n"
				"Order: "
			)
		)
		if order < 1:
			print("Error: Derivative order cannot be less than 1!")
			return True
		
		magnitude = float(input("\nHow fast was the car traveling?\nMagnitude (meters): "))

		t = float(input("\nHow long did the car travel for?\nTime (seconds): "))
		if t < 0:
			print("Error: Time cannot be less than 0!")
			return True
	except ValueError as e:
		print(f"Error: {e}")
		return True
	except KeyboardInterrupt:
		print()
		return True
	
	print(f"\nHow far did a car travel if it was traveling at {magnitude} m/s^{order} for {t} seconds?")

	# Assuming the car's n-th derivative of position is constant with zero initial conditions,
	# Then x(t) = (k / n!) * t^n
	
	# Start at k / n
	coeffs = [magnitude/order]

	# Divide by 1, ..., n-1 to get (k / n!)
	for i in range(1, order):
		coeffs.append(coeffs[i-1] / i)
	
	# Displacement from the constant n-th derivative term
	p = coeffs[-1] * t ** order
	
	print(f"The car traveled {p:.2f} meters.")
	return False
