def find_time():
	try:
		time_input = list(input("Current Time (hh:mm AM/PM): ").replace(":", " ", -1).split())
		if len(time_input) != 3:
			raise IndexError
		
		hours, minutes, meridiem_indicator = int(time_input[0]), int(time_input[1]), time_input[2].lower()
		if hours < 1 or hours > 12:
			print("Error: Hours must be between 1 and 12!")
			return True
		if minutes < 0 or minutes > 59:
			print("Error: Minutes must be between 0 and 59!")
			return True
		if meridiem_indicator not in ("am", "pm"):
			raise ValueError(f"Incorrect meridiem indicator, {meridiem_indicator}. Use AM or PM.")
		
		hours_passed, minutes_passed = int(input("Hours Passed: ")), int(input("Minutes passed: "))
			# Negative hours/minutes can pass, but I am keeping that in because I think that is funny
	except IndexError as e:
		print(f"Error: Incorrect format.")
		return True
	except ValueError as e:
		print(f"Error: {e}")
		return True
	except KeyboardInterrupt:
		print()
		return True
	
	# Calculation
	if meridiem_indicator == "pm" and hours < 12:
		hours += 12
	elif meridiem_indicator == "am" and hours == 12:
		hours -= 12
	minutes += hours * 60
	minutes_passed += hours_passed * 60
	minutes_final = ((minutes + minutes_passed) % 1440) % 60
	hours_final = ((minutes + minutes_passed) % 1440) // 60

	# PM
	if hours_final > 12:
		print(f"The time is now {hours_final - 12}:{minutes_final:02d} PM.")
	elif hours_final == 12:
		print(f"The time is now {hours_final}:{minutes_final:02d} PM.")
	# AM
	elif hours_final > 0:
		print(f"The time is now {hours_final}:{minutes_final:02d} AM.")
	else:
		print(f"The time is now {hours_final + 12}:{minutes_final:02d} AM.")
	return False
