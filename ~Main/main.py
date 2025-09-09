#Made by Alex

#======Libraries======
import random

#======Functions======
#Multiply Function
def multiply(n):
	z = 1
	for i in range(1, n + 1):
		x = input(f"Factor {i}: ")
		try:
			x = float(x)
			z *= x
			if z % 1 == 0:
				z = int(z)
		except ValueError:
			return print("Error: Not a number.")
	print(f"Product: {z}")

#Find Time Function
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

#Bubble Sort Function
def b_sort():
	l = [s for s in input("Type list elements: ").split()]
	for i in range(len(l)):
		for j in range(len(l) - 1):
			if l[j] > l[j + 1]:
				temp = l[j]
				l[j] = l[j + 1]
				l[j + 1] = temp
	print(*l)

#Bubble Sort Function (New)
def bSortNew(amount = 10, min = 0, max = 10):
	l = list(random.randint(min, max) for n in range(amount))
	print("List: ")
	print(*l)
	for i in range(len(l)):
		for j in range(len(l) - 1):
			if l[j] > l[j + 1]:
				temp = l[j]
				l[j] = l[j + 1]
				l[j + 1] = temp
	print("Sorted: ")
	print(*l)

#Selection Sort Function
def s_sort():
	l = [s for s in input("Type list elements: ").split()]
	for i in range(len(l)):
		m = i
		for j in range(i + 1, len(l)):
			if l[j] < l[m]:
				m = j
		l[m], l[i] = l[i], l[m]
	print(*l)

#Insertion Sort Function
def i_sort():
	l = [s for s in input("Type list elements: ").split()]
	for i in range(len(l)):
		v = l[i]
		p = i
		while p > 0 and l[p - 1] > v:
			l[p] = l[p - 1]
			p = p - 1
		l[p] = v
	print(*l)

#First Max Matrix Indices Function
def max_matrix_indicies():
	ROWS, COLS = [int(j) for j in input("Dimensions: ").split()]
	a = [[int(j) for j in input("Enter values: ").split()] for i in range(ROWS)]

	mx = -float("inf")
	for ROWS, lst in enumerate(a):
		for COLS, val in enumerate(lst):
			if val > mx:
				mx = val
				ind = [ROWS,COLS]
	print("Location of the first maximum point:", *ind)

#Double Sided Dictionary Function
def d_dict():
	d = {}
	n = int(input("Amount of lines: "))
	for i in range(n):
		key, value = input("Define dictionary (Key - Value(s)): ").split(" - ")
		
		for i in value.split(', '):
			if i not in d:
				d[i] = []
			d[i].append(key)
	print(len(d))
	for i in sorted(d):
		print(i, "-", ", ".join(sorted(d[i])))

#Project 1 Idea
def proj_1():
	#Alex loves cookies! Given that Alex divided n cookies with m friends, find how many cookies Alex gave to each friend and if there are any leftovers. Print all the information in one summary sentence.
	#Example Input: 8, 3
	#Example Output: Alex divided 8 cookies into 3 equal groups, giving his friends 2 cookies each with 2 cookies leftover.
	n = int(input())
	m = int(input())
	quotient = n // m
	remainder = n % m
	print("Alex divided", n, "cookies into", m, "equal groups, giving his friends", quotient, "cookies each with", remainder, "cookies leftover.")

#Project 2 Idea
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

#Project 3 Idea
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

#Random Grid Function
def rand_grid():
	letters = "abcdefghijklmnopqrstuvwxyz"
	size = int(input("Grid size: "))
	grid = []
	for row in range(size):
		currentCol = []
		for col in range(size):
			currentCol.append(random.choice(letters))
		grid.append(currentCol)
	
	for row in range(size):
		for col in range(size):
			print(grid[row][col], end = ' ')
		print()

#======Main======
def main():
	prompt = [
		"1) myFunc(degree, t, value) - Calculates the displacement of some object over an initial exponent of velocity.",
		"2) multP(num, count = 0) - Calculates the multiplicative persistence of a number.",
		"3) cool_stars(d) - Generates a pattern of stars.",
		"4) add(n) - Adds a list of numbers together.",
		"5) multiply(n) - Multiplies a list of numbers together.",
		"6) find_time() - Calculates the time on a clock from the given time and the time elapsed.",
		"7) b_sort() - Bubble sort a list of numbers.",
		"8) bSortNew(amount = 10, min = 0, max = 10) - Bubble sort a random list of numbers.",
		"9) s_sort() - Selection sort a list of numbers.",
		"10) i_sort() - Insertion sort a list of numbers.",
		"11) max_matrix_indicies() - Finds the coordinates of the largest number in a matrix.",
		"12) d_dict() - Reverses keys and values in a dictionary data type.",
		"13) proj_1() - Gets quotient and remainder.",
		"14) proj_2() - Gets elapsed time.",
		"15) proj_3() - Unfinished.",
		"16) rand_grid() - Produces a grid of random letters."
	]
	inputFlag = True
	response = 0

	while (inputFlag):
		print("Please select an option from the list below.")
		print("Or, type 0 to exit.")
		for option in prompt:
			print(option)
		try:
			response = int(input("Response: "))
		except:
			print("Error. Response not an integer.")
		else:
			inputFlag = False
	
	if response == 0:
		return -1
	elif response == 1:
		myFunc(4, 4, 4)
	elif response == 2:
		multP(4, count = 0)
	elif response == 3:
		cool_stars(4)
	elif response == 4:
		add(4)
	elif response == 5:
		multiply(4)
	elif response == 6:
		find_time()
	elif response == 7:
		b_sort()
	elif response == 8:
		bSortNew()
	elif response == 9:
		s_sort()
	elif response == 10:
		i_sort()
	elif response == 11:
		max_matrix_indicies()
	elif response == 12:
		d_dict()
	elif response == 13:
		proj_1()
	elif response == 14:
		proj_2()
	elif response == 15:
		proj_3()
	elif response == 16:
		rand_grid()

#======Execution Check======
if __name__ == "__main__":
	print("Hello world!")
	while True:
		if main() == -1:
			break