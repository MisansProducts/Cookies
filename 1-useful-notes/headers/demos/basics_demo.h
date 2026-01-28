#pragma once
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

inline void demonstrateBasics() {
	cout << "--- Basic Types & Variables ---\n";
	
	// Basic types
	bool var1 = true;
	char var2 = 'a';
	string var3 = "cookie75";
	int var4 = -6;
	float var5 = 3.14f;
	double var6 = 3.14159;
	
	// Type inference (C++11)
	auto autoInt = 42;
	decltype(var4) decltypeInt = var4;
	
	cout << "bool: " << var1 << endl;
	cout << "char: " << var2 << endl;
	cout << "string: " << var3 << endl;
	cout << "int: " << var4 << endl;
	cout << "float: " << var5 << endl;
	cout << "double: " << var6 << endl;
	cout << "auto int: " << autoInt << endl;
	cout << "decltype int: " << decltypeInt << endl;
	
	// Arrays
	const unsigned int myArrayLength = 10;
	int myArray[myArrayLength] = {};
	
	cout << "Array: ";
	for (unsigned int i = 0; i < myArrayLength; i++) {
		myArray[i] = i + 1;
		cout << myArray[i];
		if (i < myArrayLength - 1) {
			cout << ", ";
		}
	}
	
	// Range-based for loop (C++11)
	cout << "\nRange-based for: ";
	for (int val : myArray) {
		cout << val << " ";
	}
	
	// Math demonstration
	cout << "\n\nMath functions:\n";
	cout << fixed << setprecision(10);
	cout << "sin(3.14): " << sin(3.14) << endl;
	cout << "cos(3.14): " << cos(3.14) << endl;
	cout << "sqrt(16): " << sqrt(16) << endl;
	cout << "pow(2, 3): " << pow(2, 3) << endl;
	
	cout << "\n";
}