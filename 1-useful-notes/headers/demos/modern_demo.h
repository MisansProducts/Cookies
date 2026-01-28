#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <memory>
using namespace std;

inline void demonstrateModernCPP() {
	cout << "--- Modern C++ Features ---\n";
	
	// Smart pointers
	unique_ptr<int> uniquePtr = make_unique<int>(42);
	cout << "Unique pointer value: " << *uniquePtr << endl;
	
	shared_ptr<int> sharedPtr1 = make_shared<int>(100);
	shared_ptr<int> sharedPtr2 = sharedPtr1;
	cout << "Shared pointer value: " << *sharedPtr1;
	cout << "\nShared pointer use count: " << sharedPtr1.use_count() << endl;
	
	// Move semantics
	string str1 = "Hello";
	string str2 = move(str1);
	cout << "After move: str1='" << str1 << "', str2='" << str2 << "'" << endl;
	
	// Range-based for with auto
	vector<string> words = {"Modern", "C++", "Features"};
	cout << "Words: ";
	for (const auto& word : words) {
		cout << word << " ";
	}
	
	// nullptr instead of NULL
	int* nullPtr = nullptr;
	cout << "\nNull pointer is null: " << (nullPtr == nullptr) << endl;
	
	// Constexpr factorial function (declaration)
	constexpr int factorial(int n);
	cout << "Factorial of 5 (constexpr): " << factorial(5) << endl;
	
	// Initializer lists
	vector<int> initListVec = {1, 2, 3, 4, 5};
	cout << "Initializer list vector: ";
	for (int val : initListVec) cout << val << " ";
	
	// Auto return type deduction (C++14)
	auto addNumbers = [](auto a, auto b) { return a + b; };
	cout << "\nGeneric lambda addNumbers(3.5, 2.5): " << addNumbers(3.5, 2.5);
	
	// Range-based for with structured bindings (C++17 equivalent)
	cout << "\n\nVector of pairs with iteration:\n";
	vector<pair<string, int>> people = {{"Alice", 25}, {"Bob", 30}};
	for (const auto& person : people) {
		cout << person.first << " is " << person.second << " years old\n";
	}
	
	// Move semantics with vectors
	vector<string> source = {"item1", "item2", "item3"};
	vector<string> destination = move(source);
	
	cout << "\nMove semantics with vectors:\n";
	cout << "Destination size: " << destination.size() << endl;
	cout << "Source size after move: " << source.size() << endl;
	
	// Unique_ptr with custom deleter
	auto fileDeleter = [](FILE* f) { 
		if (f) fclose(f); 
		cout << "File closed via custom deleter\n";
	};
	
	// Demonstrate RAII
	cout << "\nRAII demonstration:\n";
	{
		unique_ptr<FILE, decltype(fileDeleter)> filePtr(fopen("test.txt", "r"), fileDeleter);
		if (filePtr) {
			cout << "File opened successfully\n";
		}
	} // filePtr automatically closes file here
	
	cout << "\n";
}

// Constexpr factorial function definition
constexpr int factorial(int n) {
	return n <= 1 ? 1 : n * factorial(n - 1);
}