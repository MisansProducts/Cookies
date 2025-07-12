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
		Cookie(int, int); //Constructor
		void add(int);
		void print();
};

//Constructor Definition
Cookie::Cookie(int num1, int num2) {
	a = num1;
	b = num2;
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