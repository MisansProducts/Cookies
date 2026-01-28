# Useful Notes
> Cookies/1-useful-notes/

Comprehensive C++ Language Features Demonstration - showcasing various aspects of the C++ programming language from basics to modern features.

## Features Demonstrated

### Basic Types & Variables (`basics.cpp`)
- Fundamental data types (bool, char, int, float, double, string)
- Type inference with `auto` and `decltype`
- Arrays and range-based for loops
- Math functions from `<cmath>`

### Functions & Overloading (`functions.cpp`)
- Function templates and overloading
- Lambda expressions and `std::function`
- Function pointers
- Array manipulation functions

### Object-Oriented Programming (`oop.cpp`)
- Classes with constructors/destructors
- Operator overloading (+, -, ++, ==, !=, <, <<)
- Copy and move semantics
- Virtual functions and polymorphism
- Pure virtual functions and abstract classes
- Multiple inheritance

### STL Containers & Algorithms (`stl_demo.cpp`)
- `vector`, `map`, `set`, `list` containers
- Sorting algorithms with `std::sort`
- Search operations with `std::find`
- Accumulation with `std::accumulate`
- Range-based for loops with containers
- Pair operations and custom sorting

### Modern C++ Features (`modern.cpp`)
- Smart pointers (`unique_ptr`, `shared_ptr`)
- Move semantics and rvalue references
- `nullptr` instead of `NULL`
- `constexpr` functions
- Initializer lists
- Lambda expressions
- Generic lambdas (C++14)
- RAII demonstrations

### Template Programming (`templates_demo.cpp`)
- Function templates
- Class templates with specialization
- Template member functions
- Multiple template parameters
- User-defined type templates

### File I/O & Streams (`file_io.cpp`)
- File reading and writing
- String streams for parsing
- Stream manipulators
- Error handling for file operations
- Binary file operations
- File position operations

## Usage

1. Download and navigate to the directory for these files
2. Open the terminal and type `make`
3. Type `./output` to run the demonstration program
4. Type `make clean` to remove the compiled files

## Requirements

This program requires a C++14 compliant compiler. For Windows users, [MinGW](https://nuwen.net/mingw.html) is recommended. Install on the main drive and add it to the PATH.

## Header-Only File Structure

### Main Program
- `main.cpp` - Simple coordinator that includes all demonstration headers

### Demonstration Headers (`headers/demos/`)
- `basics_demo.h` - Basic types, variables, arrays, and math functions
- `functions_demo.h` - Function overloading, lambdas, and function pointers
- `oop_demo.h` - Object-oriented programming, operators, and polymorphism
- `stl_demo.h` - STL containers, algorithms, and data structures
- `modern_demo.h` - Modern C++11/14 features and best practices
- `templates_demo.h` - Template programming and specialization
- `io_demo.h` - File I/O, streams, and error handling

### Core Headers (`headers/`)
- `cookie.h` - Enhanced class with operator overloading and move semantics
- `virtual.h` - Virtual functions, polymorphism, and multiple inheritance
- `templates.h` - Template functions and classes

### Build & Documentation
- `Makefile` - Simplified single-file build configuration
- `test.txt` - Sample file for I/O demonstrations
- `README.md` - This documentation file

### Benefits of Header-Only Design
- **No intermediate build artifacts** - Only the final executable is created
- **Clean directory structure** - All code organized in headers
- **Fast compilation** - Single compilation unit
- **Better optimization** - Compiler sees all code together
- **Easy distribution** - Just include headers to use

The program runs through each feature category as inline functions in headers, providing clear output that demonstrates the concepts in action. Each header is focused on a specific area of C++ programming, making it easy to study and reference individual features.
