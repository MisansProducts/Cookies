//Made by Alex

//======Libraries======
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
using namespace std;

//======Header Files======
#include "cookie.h"
#include "virtual.h"

//======Structures======
struct employee {
	string name;
	int age;
};

//======Function Prototypes======
void multArr(int*, int, int);

//======Main======
int main() {
	cout << "Hello world!" << endl;

	//Variables 1-6
	bool var1 = true;
	char var2 = 'a';
	string var3 = "cookie75";
	int var4 = -6;
	float var5 = 3.14;
	double var6 = 3.14159;

	//Array variables
	const unsigned int myArrayLength = 10; //Length of array
	int myArray[myArrayLength] = {}; //Array declaration

	//Loops through array
	for (unsigned int i = 0; i < myArrayLength; i++) {
		myArray[i] = i + 1; //Sets array at index to i + 1
		cout << myArray[i]; //Prints number
		if (i < myArrayLength - 1) {
			cout << "," << setfill(' ') << setw(4) << right; //Formatting
		}
	}

	cout << endl; //Formatting

	//Math
	cout << fixed << setprecision(10);
	cout << "The sine of pi radians is " << sin(var5);
	cout << ", " << sin(var6) << "..." << endl;
	cout << "Should be 0.\n";

	cout << endl; //Formatting
	
	//Opens files with getline() and a space delimiter per line
	ifstream myFile;
	myFile.open("test.txt");
	string line;
	while (getline(myFile, line)) {
		istringstream iss(line);
		string str;
		while (iss >> str) {
			cout << str << " ";
		}
		cout << endl;
	}
	
	myFile.close(); //Closes file
	
	if (myFile.is_open()) {
		cout << "My file is open.\n";
	}
	else {
		cout << "My file is closed.\n";
	}

	cout << endl; //Formatting

	int var3Copy = 0;
	
	//Loops through string
	for (unsigned int i = 0; i < var3.length(); i++) {
		if (isalpha(var3[i])) {
			var3[i] = '0';
		}
	}

	var3Copy = stoi(var3); //Converts string to integer
	
	//User input
	int response = 0;
	int sum = 0;
	bool inputErrorFlag = false;
	cout << "Enter 2 numbers to add together." << endl;
	do {
		inputErrorFlag = false;
		cout << "Number 1: ";
		cin >> response;
		if (cin.fail()) {
			cin.clear(); //Clears input flag
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			cout << "Error! Please try again." << endl;
			inputErrorFlag = true;
		}
	} while (inputErrorFlag);
	sum += response;
	do {
		inputErrorFlag = false;
		cout << "Number 2: ";
		cin >> response;
		if (cin.fail()) {
			cin.clear(); //Clears input flag
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			cout << "Error! Please try again." << endl;
			inputErrorFlag = true;
		}
	} while (inputErrorFlag);
	sum += response;
	cout << "The sum is " << sum << endl;

	cout << endl; //Formatting

	//Structure stuff
	employee alex;
	alex.name = "Alex";
	alex.age = 100;

	//Function stuff
	multArr(myArray, myArrayLength, var3Copy);

	//Class stuff
	Cookie myObject(14, 12);
	myObject.print();
	myObject.add(var4);
	myObject.print();

	cout << endl; //Formatting

	//Virtual functions are declared within a base class and are overridden by a derived class
	Base *basePointer;
	Derived derived;
	basePointer = &derived;
	basePointer->print();
	basePointer->show();

	return EXIT_SUCCESS;
}

//======Function Definitions======
void multArr(int* arr, int size, int num) {
	for (unsigned int i = 0; i < size; i++) {
		arr[i] *= num;
	}
}