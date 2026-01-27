from utils.input_validators import get_valid_int, get_valid_float

def car():
	order = get_valid_int(
		"What derivative order was the car traveling?\n"
		"1) Velocity (m/s)\n"
		"2) Acceleration (m/s^2)\n"
		"3) Jerk (m/s^3)\n"
		"4) Jounce (m/s^4)\n"
		"...\n"
		"n) n-th derivative (m/s^n)\n"
		"Order: ",
		min_val=1,
		parameter_name="Derivative order"
	)
	magnitude = get_valid_float("\nHow fast was the car traveling?\nMagnitude (meters): ", parameter_name="Magnitude")
	t = get_valid_float("\nHow long did the car travel for?\nTime (seconds): ", min_val=0, parameter_name="Time")
	
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
