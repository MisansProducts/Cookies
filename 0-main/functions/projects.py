def proj_1():
	#Alex loves cookies! Given that Alex divided n cookies with m friends, find how many cookies Alex gave to each friend and if there are any leftovers. Print all the information in one summary sentence.
	#Example Input: 8, 3
	#Example Output: Alex divided 8 cookies into 3 equal groups, giving his friends 2 cookies each with 2 cookies leftover.
	n = int(input())
	m = int(input())
	quotient = n // m
	remainder = n % m
	print("Alex divided", n, "cookies into", m, "equal groups, giving his friends", quotient, "cookies each with", remainder, "cookies leftover.")

def proj_2():
	#Alex wants to know how much time is left before his alarm goes off (on a 24-hour clock). You are given the initial time and the alarm's time without a colon separator (hhmm). Find out how much time is left before the alarm goes off.
	#Example Input: 1330, 2330
	#Example Output: 10 hours and 0 minutes left.
	initial_time = int(input())
	final_time = int(input())
	
	initial_minutes = (1440 + (60 * (initial_time % 10000 // 100) + (initial_time % 100)))
	final_minutes = (1440 + (60 * (final_time % 10000 // 100) + (final_time % 100)))
	
	elapsed_hours = ((final_minutes - initial_minutes) % 1440) // 60
	elapsed_minutes = ((final_minutes - initial_minutes) % 1440) % 60

	print(elapsed_hours, "hours and", elapsed_minutes, "minutes left.")

def proj_3():
	#Alex wants to convert his integer dates to mm/dd. Using the 2019 Julian Calendar
	#Jan, March, May, Jul, Aug, Oct, Dec = 31
	#Apr, Jun, Sep, Nov = 30
	#Feb = 28
	#Given an initial integer and a final integer, calculate the initial date, the final date, and how many days are between the two dates.
	initial = int(input("Initial date number between 1-365: "))
	final = int(input("Final date number between 1-365: "))
	
	# Define the months and their days in order
	months = [
        ("January", 31),
        ("February", 28),
        ("March", 31),
        ("April", 30),
        ("May", 31),
        ("June", 30),
        ("July", 31),
        ("August", 31),
        ("September", 30),
        ("October", 31),
        ("November", 30),
        ("December", 31)
    ]

	def day_to_date(day_num):
		if day_num < 1 or day_num > 365:
			return "Invalid day number"
		
		remaining_days = day_num
		for i, (month, days_in_month) in enumerate(months):
			if remaining_days <= days_in_month:
				month_num = i + 1
				day = remaining_days
				return f"{month_num:02d}/{day:02d}"
			remaining_days -= days_in_month

	initial_date = day_to_date(initial)
	final_date = day_to_date(final)
	
	if initial_date == "Invalid day number" or final_date == "Invalid day number":
		print("Invalid day number")
		return
	
	days_between = final - initial
	
	print(f"Initial date: {initial_date}")
	print(f"Final date: {final_date}")
	print(f"Days between: {days_between}")
