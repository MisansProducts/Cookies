#ifndef COOKIE_H
#define COOKIE_H

#include <iostream>
using namespace std;

//Class Definition
class Cookie {
	private:
		int a;
		int b;
	public:
		// Constructors
		Cookie(int, int); // Constructor
		Cookie(); // Default constructor
		Cookie(const Cookie& other); // Copy constructor
		Cookie(Cookie&& other) noexcept; // Move constructor
		
		// Assignment operators
		Cookie& operator=(const Cookie& other); // Copy assignment
		Cookie& operator=(Cookie&& other) noexcept; // Move assignment
		
		// Arithmetic operators
		Cookie operator+(const Cookie& other) const;
		Cookie operator-(const Cookie& other) const;
		Cookie& operator++(); // Pre-increment
		Cookie operator++(int); // Post-increment
		
		// Comparison operators
		bool operator==(const Cookie& other) const;
		bool operator!=(const Cookie& other) const;
		bool operator<(const Cookie& other) const;
		
		// Stream operators
		friend ostream& operator<<(ostream& os, const Cookie& cookie);
		
		// Member functions
		void add(int);
		void print();
		int getA() const { return a; }
		int getB() const { return b; }
		void setA(int val) { a = val; }
		void setB(int val) { b = val; }
		
		// Destructor
		~Cookie() = default;
};

//Default Constructor
Cookie::Cookie() : a(0), b(0) {
	cout << "Default constructor called\n";
}

//Parameterized Constructor
Cookie::Cookie(int num1, int num2) : a(num1), b(num2) {
	cout << "Parameterized constructor called\n";
}

//Copy Constructor
Cookie::Cookie(const Cookie& other) : a(other.a), b(other.b) {
	cout << "Copy constructor called\n";
}

//Move Constructor
Cookie::Cookie(Cookie&& other) noexcept : a(other.a), b(other.b) {
	cout << "Move constructor called\n";
}

//Copy Assignment
Cookie& Cookie::operator=(const Cookie& other) {
	if (this != &other) {
		a = other.a;
		b = other.b;
		cout << "Copy assignment called\n";
	}
	return *this;
}

//Move Assignment
Cookie& Cookie::operator=(Cookie&& other) noexcept {
	if (this != &other) {
		a = other.a;
		b = other.b;
		cout << "Move assignment called\n";
	}
	return *this;
}

//Addition Operator
Cookie Cookie::operator+(const Cookie& other) const {
	return Cookie(a + other.a, b + other.b);
}

//Subtraction Operator
Cookie Cookie::operator-(const Cookie& other) const {
	return Cookie(a - other.a, b - other.b);
}

//Pre-increment Operator
Cookie& Cookie::operator++() {
	++a;
	++b;
	return *this;
}

//Post-increment Operator
Cookie Cookie::operator++(int) {
	Cookie temp = *this;
	++a;
	++b;
	return temp;
}

//Equality Operator
bool Cookie::operator==(const Cookie& other) const {
	return a == other.a && b == other.b;
}

//Inequality Operator
bool Cookie::operator!=(const Cookie& other) const {
	return !(*this == other);
}

//Less Than Operator
bool Cookie::operator<(const Cookie& other) const {
	return (a + b) < (other.a + other.b);
}

//Stream Output Operator
ostream& operator<<(ostream& os, const Cookie& cookie) {
	os << "Cookie(a=" << cookie.a << ", b=" << cookie.b << ")";
	return os;
}

//Add Function
void Cookie::add(int num) {
	a += num;
}

//Print Function
void Cookie::print() {
	cout << "a = " << a << endl;
	cout << "b = " << b << endl;
}

#endif