#ifndef TEMPLATES_H
#define TEMPLATES_H

#include <iostream>
using namespace std;

// Template function
template <typename T>
T my_max(T a, T b) {
    return (a > b) ? a : b;
}

// Template class
template <typename T>
class Box {
private:
    T value;
    
public:
    // Constructor
    Box(T val) : value(val) {}
    
    // Getter
    T getValue() const {
        return value;
    }
    
    // Setter
    void setValue(T val) {
        value = val;
    }
    
    // Display method
    void display() const {
        cout << "Box contains: " << value << endl;
    }
    
    // Template method inside template class
    template <typename U>
    void addAndDisplay(U addend) {
        cout << "Value + addend: " << (value + addend) << endl;
    }
};

// Template specialization
template <>
class Box<bool> {
private:
    bool value;
    
public:
    Box(bool val) : value(val) {}
    
    bool getValue() const {
        return value;
    }
    
    void display() const {
        cout << "Boolean box contains: " << (value ? "true" : "false") << endl;
    }
};

// Template with multiple parameters
template <typename T, typename U>
class Pair {
private:
    T first;
    U second;
    
public:
    Pair(T f, U s) : first(f), second(s) {}
    
    T getFirst() const { return first; }
    U getSecond() const { return second; }
    
    void display() const {
        cout << "Pair: " << first << ", " << second << endl;
    }
};

#endif