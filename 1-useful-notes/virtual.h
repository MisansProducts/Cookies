#ifndef VIRTUAL_H
#define VIRTUAL_H

#include <iostream>
using namespace std;

//Base Class Definition
class Base {
    public:
        virtual void print() {
            cout << "Printed base class." << endl;
        }
        void show() {
            cout << "Showing base class." << endl;
        }
};

//Derived Class Definition
class Derived: public Base {
    public:
        void print() {
            cout << "Printed derived class." << endl;
        }
        void show() {
            cout << "Showing derived class." << endl;
        }
};

#endif