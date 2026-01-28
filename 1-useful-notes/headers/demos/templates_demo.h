#pragma once
#include <iostream>
using namespace std;

#include "../templates.h"

inline void demonstrateTemplates() {
	cout << "--- Template Programming ---\n";
	
	// Template function
	cout << "Max of 3 and 7: " << my_max<int>(3, 7) << endl;
	cout << "Max of 3.14 and 2.71: " << my_max<double>(3.14, 2.71) << endl;
	cout << "Max of A and Z: " << my_max<char>('A', 'Z') << endl;
	
	// Template class
	Box<int> intBox(42);
	Box<string> stringBox("Template Box");
	Box<double> doubleBox(3.14159);
	
	cout << "Int box: " << intBox.getValue() << endl;
	cout << "String box: " << stringBox.getValue() << endl;
	cout << "Double box: " << doubleBox.getValue() << endl;
	
	// Template class methods
	intBox.display();
	stringBox.display();
	doubleBox.display();
	
	// Template method inside template class
	cout << "\nTemplate method examples:\n";
	intBox.addAndDisplay(8);
	stringBox.addAndDisplay(string(" is awesome"));
	
	// Template specialization
	Box<bool> boolBox(true);
	cout << "\nTemplate specialization:\n";
	boolBox.display();
	
	// Template with multiple parameters
	Pair<string, int> person("Alice", 25);
	Pair<double, char> measurement(3.14, 'p');
	
	cout << "\nTemplate with multiple parameters:\n";
	person.display();
	measurement.display();
	
	// Template function with different types
	cout << "\nTemplate function with different types:\n";
	cout << "Max string: " << my_max<string>("Hello", "World") << endl;
	
	// Template class with user-defined type
	struct Point {
		double x, y;
		Point(double x, double y) : x(x), y(y) {}
	};
	
	Box<Point> pointBox(Point(1.5, 2.5));
	cout << "Point box: (" << pointBox.getValue().x << ", " << pointBox.getValue().y << ")" << endl;
	
	cout << "\n";
}