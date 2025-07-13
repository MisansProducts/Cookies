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

#Print Result Function
def printResult(t: tuple[list[int], int, list[float]], label):
	sequence, max_sum, times = t
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
	
	# Plots the times
	plt.plot(times)
	plt.xlabel('Index')
	plt.ylabel('Time Elapsed')
	plt.title(label)
	plt.savefig(f"graphs/{label}.png")
	plt.close()
#Cubic Function
def cubic(l, start_time=time.time()):
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence
	times = []
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
		times.append(time.time() - start_time)
	return maxSequence, maxSum, times

#Quadratic Function
def quadratic(l, start_time=time.time()):
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence
	times = []
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
		times.append(time.time() - start_time)
	return maxSequence, maxSum, times

#Linear Function
def linear(l, start_time=time.time()):
	#Variables
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence
	currentSum = 0 #Current sum
	currentSequence = [] #Current sequence
	times = []
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
		times.append(time.time() - start_time)
	return maxSequence, maxSum, times

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
	printResult(response, "Cubic")
	print("Time elapsed:", cubicTime)

	print() #Spacer

	#Time complexity of O(N^2)
	start = time.time() #Gets starting time
	response = quadratic(myList)
	end = time.time() #Gets ending time
	quadraticTime = end - start
	print("-=-=-=Run time complexity of O(N^2)=-=-=-")
	printResult(response, "Quadratic")
	print("Time elapsed:", quadraticTime)

	print() #Spacer

	#Time complexity of O(N)
	start = time.time() #Gets starting time
	response = linear(myList)
	end = time.time() #Gets ending time
	linearTime = end - start
	print("-=-=-=Run time complexity of O(N)=-=-=-")
	printResult(response, "Linear")
	print("Time elapsed:", linearTime)

#======Execution Check======
if __name__ == '__main__':
	main()