#pragma once
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <string>
using namespace std;

inline void demonstrateSTL() {
	cout << "--- STL Containers & Algorithms ---\n";
	
	// Vector
	vector<int> vec = {5, 2, 8, 1, 9, 3};
	cout << "Vector: ";
	for (int val : vec) cout << val << " ";
	
	sort(vec.begin(), vec.end());
	cout << "\nSorted: ";
	for (int val : vec) cout << val << " ";
	
	// Reverse vector
	reverse(vec.begin(), vec.end());
	cout << "\nReversed: ";
	for (int val : vec) cout << val << " ";
	
	// Map
	map<string, int> ages;
	ages["Alice"] = 25;
	ages["Bob"] = 30;
	ages["Charlie"] = 35;
	
	cout << "\n\nMap ages:\n";
	for (const auto& pair : ages) {
		cout << pair.first << ": " << pair.second << endl;
	}
	
	// Set
	set<int> uniqueNumbers = {1, 2, 3, 2, 1, 4, 5, 3};
	cout << "\nSet (unique numbers): ";
	for (int val : uniqueNumbers) cout << val << " ";
	
	// Algorithms
	vector<int> numbers = {10, 20, 30, 40, 50};
	auto found = find(numbers.begin(), numbers.end(), 30);
	if (found != numbers.end()) {
		cout << "\nFound 30 at position: " << distance(numbers.begin(), found);
	}
	
	int sum = accumulate(numbers.begin(), numbers.end(), 0);
	cout << "\nSum of numbers: " << sum;
	
	// Count occurrences
	vector<int> data = {1, 2, 3, 2, 1, 2, 4, 5};
	int countTwos = count(data.begin(), data.end(), 2);
	cout << "\nCount of 2s in data: " << countTwos;
	
	// Transform algorithm
	vector<int> squares;
	transform(numbers.begin(), numbers.end(), back_inserter(squares), 
			  [](int x) { return x * x; });
	cout << "\nSquares: ";
	for (int val : squares) cout << val << " ";
	
	// List
	list<string> stringList = {"First", "Second", "Third"};
	cout << "\n\nList: ";
	for (const auto& item : stringList) cout << item << " ";
	
	// List operations
	stringList.push_front("Zero");
	stringList.push_back("Fourth");
	cout << "\nList after push_front/push_back: ";
	for (const auto& item : stringList) cout << item << " ";
	
	// Pair operations
	vector<pair<string, int>> pairs = {
		{"Apple", 5},
		{"Banana", 3},
		{"Orange", 8}
	};
	
	cout << "\n\nVector of pairs:\n";
	for (const auto& p : pairs) {
		cout << p.first << ": " << p.second << endl;
	}
	
	// Sort pairs by second element
	sort(pairs.begin(), pairs.end(), 
		 [](const pair<string, int>& a, const pair<string, int>& b) {
			 return a.second < b.second;
		 });
	
	cout << "Sorted by value:\n";
	for (const auto& p : pairs) {
		cout << p.first << ": " << p.second << endl;
	}
	
	cout << "\n";
}