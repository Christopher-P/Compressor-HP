#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

void compress();

class Node {

};


int main() {
	
}

void compress() {
	string input;
	cout << "Hello World!" << endl;


	ifstream infile("small-data.txt");


	string line;
	while (getline(infile, line))
	{
		ifstream file("small-data.txt");
		if (file.is_open()) {
			string line;
			while (getline(file, line)) {
				// using printf() in all tests for consistency
				printf("%s", line.c_str());
			}
			file.close();
		}
	}

	cin >> input;
}