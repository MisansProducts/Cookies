#pragma once
#include <iostream>
#include <iomanip>
#include <vector>
#include <functional>
using namespace std;

// Function prototype
inline void multArr(int* arr, int size, int num);

// Overloaded functions
inline int add(int a, int b) {
	return a + b;
}

inline double add(double a, double b) {
	return a + b;
}

inline void demonstrateFunctions() {
	cout << "--- Functions & Overloading ---\n";
	
	// Array manipulation
	const unsigned int arrSize = 5;
	int testArray[arrSize] = {1, 2, 3, 4, 5};
	
	const int LABEL_WIDTH_1 = 29;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "Original array" << ": ";
	for (int val : testArray) cout << val << " ";
	cout << endl;
	
	multArr(testArray, arrSize, 2);
	
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "Multiplied by 2" << ": ";
	for (int val : testArray) cout << val << " ";
	
	// Function pointers and lambda expressions
	auto addLambda = [](int a, int b) { return a + b; };
	auto multiply = [](int a, int b) { return a * b; };
	
	cout << "\n" << left << setw(LABEL_WIDTH_1) << setfill(' ') << "Lambda add(3, 4)" << ": " << addLambda(3, 4);
	cout << "\n" << left << setw(LABEL_WIDTH_1) << setfill(' ') << "Lambda multiply(3, 4)" << ": " << multiply(3, 4);
	
	// std::function
	function<int(int, int)> operation = addLambda;
	cout << "\n" << left << setw(LABEL_WIDTH_1) << setfill(' ') << "std::function add(5, 3)" << ": " << operation(5, 3);
	
	operation = multiply;
	cout << "\n" << left << setw(LABEL_WIDTH_1) << setfill(' ') << "std::function multiply(5, 3)" << ": " << operation(5, 3);
	
	// Function overloading example
	const int LABEL_WIDTH_2 = 14;
	cout << "\nFunction overloading:\n";
	cout << "\t" << left << setw(LABEL_WIDTH_2) << setfill(' ') << "add(3, 4)" << ": " << add(3, 4) << endl;
	cout << "\t" << left << setw(LABEL_WIDTH_2) << setfill(' ') << "add(3.5, 4.5)" << ": " << add(3.5, 4.5) << endl;
	
	cout << "\n";
}

// Function definition
inline void multArr(int* arr, int size, int num) {
	for (int i = 0; i < size; i++) {
		arr[i] *= num;
	}
}
