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
	string var3 = "Hello world!";
	int var4 = -5;
	float var5 = 3.14f;
	double var6 = 3.14159;
	
	// Type inference (C++11)
	auto var7 = 42;
	decltype(var4) var8 = var4;

	const int LABEL_WIDTH_1 = 9;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "bool" << ": " << var1 << endl;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "char" << ": " << var2 << endl;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "string" << ": " << var3 << endl;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "int" << ": " << var4 << endl;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "float" << ": " << var5 << endl;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "double" << ": " << var6 << endl;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "auto" << ": " << var7 << endl;
	cout << left << setw(LABEL_WIDTH_1) << setfill(' ') << "decltype" << ": " << var8 << endl;
	
	// Arrays
	const unsigned int myArrayLength = 10;
	int myArray[myArrayLength] = {};
	
	const int LABEL_WIDTH_2 = 16;
	cout << left << setw(LABEL_WIDTH_2) << setfill(' ') << "Array" << ": ";
	for (unsigned int i = 0; i < myArrayLength; i++) {
		myArray[i] = i + 1;
		cout << myArray[i] << " ";
	}
	
	// Range-based for loop (C++11)
	cout << "\n" << left << setw(LABEL_WIDTH_2) << setfill(' ') << "Range-based for" << ": ";
	for (int val : myArray) {
		cout << val << " ";
	}
	
	// Math demonstration
	const int LABEL_WIDTH_3 = 10;
	cout << "\nMath functions:\n";
	cout << fixed << setprecision(10);
	cout << "\t" << left << setw(LABEL_WIDTH_3) << setfill(' ') << "sin(3.14)" << ": " << sin(3.14) << endl;
	cout << "\t" << left << setw(LABEL_WIDTH_3) << setfill(' ') << "cos(3.14)" << ": " << cos(3.14) << endl;
	cout << "\t" << left << setw(LABEL_WIDTH_3) << setfill(' ') << "sqrt(16)" << ": " << sqrt(16) << endl;
	cout << "\t" << left << setw(LABEL_WIDTH_3) << setfill(' ') << "pow(2, 3)" << ": " << pow(2, 3) << endl;
	
	cout << "\n";
}
