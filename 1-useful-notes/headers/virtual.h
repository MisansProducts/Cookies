#ifndef VIRTUAL_H
#define VIRTUAL_H

#include <iostream>
#include <string>
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
        virtual ~Base() = default; // Virtual destructor
};

//Derived Class Definition
class Derived: public Base {
    public:
        void print() override { // Override specifier
            cout << "Printed derived class." << endl;
        }
        void show() {
            cout << "Showing derived class." << endl;
        }
};

// Abstract base class with pure virtual functions
class Shape {
protected:
    string name;
    
public:
    Shape(const string& n) : name(n) {}
    virtual ~Shape() = default;
    
    // Pure virtual functions
    virtual void draw() const = 0;
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    
    // Regular virtual function
    virtual void describe() const {
        cout << "This is a " << name << endl;
    }
    
    string getName() const { return name; }
};

// Circle class inheriting from Shape
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : Shape("Circle"), radius(r) {}
    
    void draw() const override {
        cout << "Drawing a circle with radius " << radius << endl;
    }
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * 3.14159 * radius;
    }
};

// Rectangle class inheriting from Shape
class Rectangle : public Shape {
private:
    double width;
    double height;
    
public:
    Rectangle(double w, double h) : Shape("Rectangle"), width(w), height(h) {}
    
    void draw() const override {
        cout << "Drawing a rectangle " << width << " x " << height << endl;
    }
    
    double area() const override {
        return width * height;
    }
    
    double perimeter() const override {
        return 2 * (width + height);
    }
};

// Multiple inheritance example
class Printable {
public:
    virtual void printInfo() = 0;
    virtual ~Printable() = default;
};

class ColoredShape : public Shape, public Printable {
private:
    string color;
    
public:
    ColoredShape(const string& shapeName, const string& col) 
        : Shape(shapeName), color(col) {}
    
    void draw() const override {
        cout << "Drawing a " << color << " " << name << endl;
    }
    
    double area() const override {
        return 0.0; // Base implementation
    }
    
    double perimeter() const override {
        return 0.0; // Base implementation
    }
    
    void printInfo() override {
        cout << "Color: " << color << ", Shape: " << name << endl;
    }
};

#endif