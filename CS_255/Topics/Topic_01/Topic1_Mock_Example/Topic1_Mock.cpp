/*
 * Topic1_Mock.cpp
 *
 *  Created on: June 11, 2020
 *      Author: kamilla
 */

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
double average(double a, double b)
{
	//instead of writing body of the function just return
	//the value that matches return value (return type).
	// make the program work.
	//the body of this function you will write later.
	return 1;
}

void testYear(const string& inputFileName,const string& outputFileName)
{
	//it is void function, just mention that you call this function,
	//the body of this function you will write later.
	cout<<"inside testYear():Testing Year\n";
}
void testFile(int numberFile)
{
    const string& number        = to_string(numberFile);
    const string& inputFile     = "in"+number+".txt";
    const string& outputFile    = "out"+number+"_stub.txt";

    cout << "\n*** Testing file " << inputFile << " *** " << endl;
    testYear(inputFile, outputFile);
    cout << "\n*** OK ***\n";
    double a = 5;
    double b = 7;
    cout << "average between " << a << " and "
    	 << b << " is " << average(a,b) << endl;
}
int main()
{
try
{
	for (int i=1;i<=5;++i) testFile(i);
}

catch ( const exception& ex )
{
   cout << "Exception:" << ex.what() << "\n";
}
}
