#pragma once
#include <iostream>
#include <string>
using namespace std;

#include "../cookie.h"
#include "../virtual.h"

inline void demonstrateOOP() {
	cout << "--- Object-Oriented Programming ---\n";

	// Default constructor
	cout << "cookie1:" << endl;
	Cookie cookie1;
	cookie1.print();
	cookie1.add(5);

	// Stream operator
	cout << "\tStream output: " << cookie1 << endl;

	// Parameterized constructor
	cout << "cookie2(1, 2):" << endl;
	Cookie cookie2(1, 2);
	cookie2.print();

	// Pre-increment and post-increment
	++cookie2;
	cookie2++;
	cookie2.print();

	// Operator overloading
	cout << "cookie3 = cookie1 + cookie2:" << endl;
	Cookie cookie3 = cookie1 + cookie2;
	cookie3.print();

	// Comparison
	cout << "\tCookie1 == Cookie3: " << ((cookie1 == cookie3) ? "True" : "False") << endl;
	cout << "\tCookie1 <  Cookie3: " << ((cookie1 < cookie3) ? "True" : "False") << endl;
	
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