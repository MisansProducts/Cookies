#Made by Alex

#======Libraries======
import random

#======Functions======
def myFunc(degree, t, value):
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

#Cool Stars Function
def cool_stars(d):
  for i in range(1, d * 2):
    if i <= d:
      print('*' * i)
    else:
      print('*' * ((d * 2) - i))

#Add Function
def add(n):
	z = 0
	for i in range(1, n + 1):
		x = input(f"Addend {i}: ")
		try:
			x = float(x)
			z += x
			if z % 1 == 0:
				z = int(z)
		except ValueError:
			return print("Error: Not a number.")
	print(f"Sum: {z}")

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
	initial = int(input())
	final = int(input())

#======Main======
def main():
	print("Hello world!")

#======Execution Check======
if __name__ == "__main__":
	main()