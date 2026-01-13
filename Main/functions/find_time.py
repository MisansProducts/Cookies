def find_time():
	try:
		#Time Input
		time_input = list(input("Current Time (hh:mm AM/PM): ").replace(":", " ", -1).split())
		#Variables
		hours, minutes = int(time_input[0]), int(time_input[1])
		#Conversion
		if hours < 1 or hours > 12 or minutes < 0 or minutes > 59:
			raise ValueError
		if time_input[2].lower() == "pm" and hours < 12:
			hours += 12
		elif time_input[2].lower() == "am" and hours == 12:
			hours -= 12
		minutes += hours * 60
		#Time Passed Input
		hours_passed, minutes_passed = int(input("Hours Passed: ")), int(input("Minutes passed: "))
		#Conversion
		minutes_passed += hours_passed * 60
	except IndexError:
		return print("Error: Incorrect format.")
	except ValueError:
		return print("Error: Incorrect value(s).")
	#Calculation
	minutes_final = ((minutes + minutes_passed) % 1440) % 60
	hours_final = ((minutes + minutes_passed) % 1440) // 60
	#PM
	if hours_final > 12:
		print(f"The time is now {hours_final - 12}:{minutes_final:02d} PM.")
	elif hours_final == 12:
		print(f"The time is now {hours_final}:{minutes_final:02d} PM.")
	#AM
	elif hours_final > 0:
		print(f"The time is now {hours_final}:{minutes_final:02d} AM.")
	else:
		print(f"The time is now {hours_final + 12}:{minutes_final:02d} AM.")
