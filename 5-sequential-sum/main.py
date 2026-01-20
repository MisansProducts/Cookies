#Made by Alex

#======Libraries======
import random
import time
import copy

import matplotlib.pyplot as plt

#======Functions======
#List Generator Function
def genList(size):
	l = [] #Initializes empty list

	#Populates list with random integers
	for i in range(size):
		l.append(random.randint(-size, size))
	
	#Returns populated list
	return l

def test_runtimes(l):
	sizes = [i for i in range(len(l))]
	cubic_times = []
	quadratic_times = []
	linear_times = []

	for size in sizes:
		start = time.time()
		cubic(l[:size])
		cubic_times.append(time.time() - start)

		start = time.time()
		quadratic(l[:size])
		quadratic_times.append(time.time() - start)

		start = time.time()
		linear(l[:size])
		linear_times.append(time.time() - start)

	# Plots results
	plt.plot(sizes, cubic_times, label="Cubic O(n³)")
	plt.plot(sizes, quadratic_times, label="Quadratic O(n²)")
	plt.plot(sizes, linear_times, label="Linear O(n)")
	plt.xlabel("Input Size (n)")
	plt.ylabel("Execution Time (seconds)")
	plt.title("Runtime Complexity")
	plt.legend()
	plt.grid(True)
	plt.savefig("graphs/runtime_comparison.png")
	plt.show()

#Print Result Function
def printResult(t: tuple[list[int], int]):
	sequence, max_sum = t
	N = len(sequence)

	#List contains more than 1 number
	if N > 1:
		#Loops through the list of numbers (not the last)
		for i in range(N - 1):
			s = f"({sequence[i]})" if sequence[i] < 0 else str(sequence[i])
			print(s, end = " + ")
		#Prints last number
		print(sequence[-1], end = " = ") #This number will always be positive
	#Prints max sum
	print(max_sum, "is the largest contiguous sum")

#Cubic Function
def cubic(l):
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence
	#Loops through list (starting index)
	for i in range(len(l)):
		#Loops through list (ending index)
		for j in range(i, len(l)):
			#Resets current sum and current sequence list
			currentSum = 0
			currentSequence = []

			#Loops through range
			for k in range(i, j + 1):
				currentSum += l[k] #Sums numbers
				currentSequence.append(l[k]) #Appends numbers to sequence list
			
			#Comparison
			if currentSum >= maxSum:
				maxSum = currentSum
				maxSequence = copy.deepcopy(currentSequence)
	return maxSequence, maxSum

#Quadratic Function
def quadratic(l):
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence
	#Loops through list (starting index)
	for i in range(len(l)):
		#Resets current sum and current sequence list
		currentSum = 0
		currentSequence = []

		#Loops through list
		for j in range(i, len(l)):
			currentSum += l[j] #Sums numbers
			currentSequence.append(l[j]) #Appends numbers to sequence list

			#Comparison
			if currentSum >= maxSum:
				maxSum = currentSum
				maxSequence = copy.deepcopy(currentSequence)
	return maxSequence, maxSum

#Linear Function
def linear(l):
	#Variables
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence
	currentSum = 0 #Current sum
	currentSequence = [] #Current sequence
	#Loops through list
	for i in range(len(l)):
		currentSum += l[i] #Sums numbers
		currentSequence.append(l[i]) #Appends numbers to sequence list

		#Comparison
		if currentSum >= maxSum:
			maxSum = currentSum
			maxSequence = copy.deepcopy(currentSequence)
		elif currentSum < 0:
			currentSum = 0
			currentSequence = []
	return maxSequence, maxSum

#======Main======
def main():
	#Enter Input Loop
	while True:
		#List length input
		try:
			#Prompt
			listLength = float(input("Please enter the list size: "))

			#Bad inputs
			if listLength < 0:
				raise Exception("List size cannot be negative!")
			elif listLength == 0:
				raise Exception("List size must be greater than 0!")
			elif listLength.is_integer() == False:
				raise Exception("List size cannot be floating point values.")
		#Error handling (general)
		except ValueError:
			print("The list size must be a natural number.\n")
		#Error handling (specific)
		except Exception as specificError:
			print(specificError, end = "\n\n")
		#Exit Input Loop
		else:
			listLength = int(listLength)
			print() #Spacer
			break
	
	#Generates a list of random integers of size listLength
	myList = genList(listLength)

	#Prints list
	print("LIST:")
	for i in range(listLength - 1):
		print(myList[i], end = ", ")
	print(myList[-1], end = "\n\n")

	#Gets the largest contiguous sum
	#Time complexity of O(N^3)
	start = time.time() #Gets starting time
	response = cubic(myList)
	end = time.time() #Gets ending time
	cubicTime = end - start
	print("-=-=-=Run time complexity of O(N^3)=-=-=-")
	printResult(response)
	print("Time elapsed:", cubicTime)

	print() #Spacer

	#Time complexity of O(N^2)
	start = time.time() #Gets starting time
	response = quadratic(myList)
	end = time.time() #Gets ending time
	quadraticTime = end - start
	print("-=-=-=Run time complexity of O(N^2)=-=-=-")
	printResult(response)
	print("Time elapsed:", quadraticTime)

	print() #Spacer

	#Time complexity of O(N)
	start = time.time() #Gets starting time
	response = linear(myList)
	end = time.time() #Gets ending time
	linearTime = end - start
	print("-=-=-=Run time complexity of O(N)=-=-=-")
	printResult(response)
	print("Time elapsed:", linearTime)

	test_runtimes(myList)

#======Execution Check======
if __name__ == '__main__':
	main()