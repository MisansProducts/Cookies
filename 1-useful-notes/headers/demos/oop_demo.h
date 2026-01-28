#pragma once
#include <iostream>
#include <string>
using namespace std;

#include "../cookie.h"
#include "../virtual.h"

inline void demonstrateOOP() {
	cout << "--- Object-Oriented Programming ---\n";
	
	// Basic class usage
	Cookie myObject(14, 12);
	cout << "Initial Cookie object:\n";
	myObject.print();
	
	myObject.add(5);
	cout << "After add(5):\n";
	myObject.print();
	
	// Operator overloading
	Cookie cookie1(10, 20);
	Cookie cookie2(5, 15);
	Cookie cookie3 = cookie1 + cookie2;
	cout << "Cookie1 + Cookie2:\n";
	cookie3.print();
	
	// Copy constructor
	Cookie cookieCopy = cookie1;
	cout << "Copy of Cookie1:\n";
	cookieCopy.print();
	
	// Increment operators
	cout << "Pre-increment on Cookie2:\n";
	++cookie2;
	cookie2.print();
	
	cout << "Post-increment on Cookie2:\n";
	cookie2++;
	cookie2.print();
	
	// Comparison operators
	cout << "Cookie1 == Cookie3: " << (cookie1 == cookie3) << endl;
	cout << "Cookie1 < Cookie3: " << (cookie1 < cookie3) << endl;
	
	// Stream operator
	cout << "Stream output: " << cookie1 << endl;
	
	// Virtual functions and polymorphism
	cout << "\nVirtual functions:\n";
	Base *basePointer;
	Derived derived;
	basePointer = &derived;
	basePointer->print();
	basePointer->show();
	
	// Pure virtual functions
	Shape *circle = new Circle(5.0);
	Shape *rectangle = new Rectangle(4.0, 6.0);
	
	cout << "\nPure virtual functions:\n";
	circle->draw();
	cout << "Circle area: " << circle->area() << endl;
	
	rectangle->draw();
	cout << "Rectangle area: " << rectangle->area() << endl;
	
	delete circle;
	delete rectangle;
	
	// Multiple inheritance
	cout << "\nMultiple inheritance:\n";
	ColoredShape coloredRect("Rectangle", "red");
	coloredRect.draw();
	coloredRect.printInfo();
	
	// Structure with constructor
	struct employee {
		string name;
		int age;
		
		// Constructor
		employee(string n, int a) : name(n), age(a) {}
	};
	
	employee alex("Alex", 100);
	cout << "\nEmployee: " << alex.name << ", Age: " << alex.age << endl;
	
	cout << "\n";
}