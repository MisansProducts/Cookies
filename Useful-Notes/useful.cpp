/* Header! */
// #include <iostream>
// #include <iomanip>
// #include <cmath>
// #include <limits>
// #include <string>
// #include <fstream>
// #include <sstream>
// #include <vector>
// #include <algorithm>
// using namespace std;

/* Opens files with getline() and a space delimiter per line */
// ifstream myFile = "lol.txt";
// string line;
// while (getline(myFile, line)) {
// 	istringstream iss(line);
// 	string str;
// 	while (iss >> str) {
// 		//Code goes here!
// 	}
// }

/* Clear input flag on error */
// if (cin.fail()) {
// 	cin.clear(); //Clears input flag
// 	cin.ignore(numeric_limits<streamsize>::max(), '\n');
// 	cout << "Error!" << endl;
// }

/* Deletes trailing 0's in string */
// str.erase(str.find_last_not_of('0') + 1, std::string::npos);

/* Calculates the size of an array */
// int size = sizeof(arr)/sizeof(arr[0]);

/* Pass array by reference */
// void foo(string* arr, int size) {
// 	//Code goes here!
// }

/* Converts strings to lowercase */
// void caseFoldString(string& str) {
// 	for (unsigned int i = 0; i < str.size(); i++) {
// 		str[i] = tolower(str[i]);
// 	}
// }

/* How to use vector elements as variables */
// struct structure {
// 	string object;
// 	int value;
// 	//Other stuff
// };
// vector<structure> list;
// list.push_back(structure());

/* How to use header guards */
// #ifndef HEADER_GUARD
// #define HEADER_GUARD
// //Code goes here! <3
// #endif

/* Object composition */
// class method {
// 	public:
// 		method(); //Constructor
// };
// class base {
// 	private:
// 		method object;
// 	public:
// 		base(); //Constructor
// };
// method::method() {
// 	//Method Definition
// }
// base::base(): object() {
// 	//Base Definition
// }

/* Object inheritance */
// class base {
// 	public:
// 		base(); //Constructor
// };
// class derived: public base {
// 	public:
// 		derived(); //Constructor
// };
// base::base() {
// 	//Base Definition
// }
// derived::derived(): base() {
// 	//Derived Definition
// }

/* Dynamically allocate 2D array */
// int** arr = new int*[numRows];
// for (int row = 0; row < numRows; row++) {
// 	board[row] = new int[numCols]; //Initializes a row full of pointers
// }

/* Dynamically deallocate 2D array */
// for (int row = 0; row < numRows; row++) {
// 	delete[] arr[row]; //Deletes each row
// }
// delete[] arr; //Deletes array

/* Pointer arithmetic for arrays */
// for (int *ptr = arr; ptr < arr + size - 1; i++) {
// 	*ptr = //Something
// }

/* Operator overloading */
// void someClass::operator+(someClass x) {
// 	//Code to redefine addition of two objects as a function
// }

/* Class template */
// template <class T>
// class someClass {
// 	private:
// 		T variable;
// 	public:
// 		someClass(); //Constructor
// }

// template <class T>
// someClass<T>::someClass() {
// 	//Constructor Definition
// }