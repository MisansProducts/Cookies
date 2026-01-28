//Made by Alex

//======Libraries======
#include <iostream>
using namespace std;

//======Header Files======
#include "headers/demos/basics_demo.h"
#include "headers/demos/functions_demo.h"
#include "headers/demos/oop_demo.h"
#include "headers/demos/stl_demo.h"
#include "headers/demos/modern_demo.h"
#include "headers/demos/templates_demo.h"
#include "headers/demos/io_demo.h"

//======Main======
int main() {
	cout << "=== C++ Language Features Demonstration ===\n\n";
	
	demonstrateBasics();
	demonstrateFunctions();
	demonstrateOOP();
	demonstrateSTL();
	demonstrateModernCPP();
	demonstrateTemplates();
	demonstrateFileIO();
	
	cout << "\n=== Demonstration Complete ===\n";
	return EXIT_SUCCESS;
}