#pragma once
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
using namespace std;

inline void demonstrateFileIO() {
	cout << "--- File I/O & Streams ---\n";
	
	// Writing to file
	ofstream outFile("example.txt");
	if (outFile.is_open()) {
		outFile << "Hello, C++!\n";
		outFile << "File I/O demonstration\n";
		outFile << "Line 3\n";
		outFile.close();
		cout << "Successfully wrote to example.txt\n";
	} else {
		cout << "Failed to open example.txt for writing\n";
	}
	
	// Reading from file
	ifstream inFile("example.txt");
	if (inFile.is_open()) {
		string line;
		cout << "File contents:\n";
		while (getline(inFile, line)) {
			cout << line << endl;
		}
		inFile.close();
	} else {
		cout << "Failed to open example.txt for reading\n";
	}
	
	// String streams
	string data = "123 456 789";
	istringstream iss(data);
	int a, b, c;
	iss >> a >> b >> c;
	cout << "Parsed numbers: " << a << ", " << b << ", " << c << endl;
	
	// Stream manipulation
	cout << "\nStream manipulation:\n";
	cout << "Fixed precision: " << fixed << setprecision(2) << 3.14159 << endl;
	cout << "Scientific: " << scientific << 3.14159 << endl;
	cout << "Hexadecimal: " << hex << 255 << endl;
	cout << "Octal: " << oct << 255 << endl;
	
	// Reset to decimal
	cout << dec;
	
	// Try to read original test.txt if it exists
	ifstream testFile("test.txt");
	if (testFile.is_open()) {
		cout << "\nOriginal test.txt content:\n";
		string line;
		while (getline(testFile, line)) {
			istringstream iss(line);
			string str;
			while (iss >> str) {
				cout << str << " ";
			}
			cout << endl;
		}
		testFile.close();
	} else {
		cout << "\ntest.txt not found (this is expected if file doesn't exist)\n";
	}
	
	// Binary file operations
	cout << "\nBinary file operations:\n";
	ofstream binOut("binary.dat", ios::binary);
	if (binOut.is_open()) {
		int numbers[] = {1, 2, 3, 4, 5};
		binOut.write(reinterpret_cast<char*>(numbers), sizeof(numbers));
		binOut.close();
		cout << "Wrote binary data to binary.dat\n";
	}
	
	ifstream binIn("binary.dat", ios::binary);
	if (binIn.is_open()) {
		int readNumbers[5];
		binIn.read(reinterpret_cast<char*>(readNumbers), sizeof(readNumbers));
		binIn.close();
		cout << "Read from binary file: ";
		for (int i = 0; i < 5; i++) {
			cout << readNumbers[i] << " ";
		}
		cout << endl;
	}
	
	// String stream examples
	cout << "\nString stream examples:\n";
	ostringstream oss;
	oss << "The answer is " << 42;
	string result = oss.str();
	cout << "String stream output: " << result << endl;
	
	// Error handling with streams
	cout << "\nError handling demonstration:\n";
	ifstream errorFile("nonexistent.txt");
	if (!errorFile) {
		cout << "Failed to open nonexistent.txt (expected)\n";
		if (errorFile.fail()) {
			cout << "Stream is in fail state\n";
		}
	}
	
	// File position operations
	cout << "\nFile position operations:\n";
	ofstream posFile("position.txt");
	if (posFile.is_open()) {
		posFile << "Hello";
		streampos pos = posFile.tellp();
		cout << "Current position: " << pos << endl;
		posFile << ", World!";
		posFile.close();
	}
	
	cout << "\n";
}