/*
code file, functionality goes here
*/
#include <string>
#include <iostream>

using namespace std;

int Multi(int val, int mul)
{
	// returns the value of both ins multiplied together
	int index;
	int out_val = 0;
	for( index = 0 ; index < mul; index++ )
		{
			out_val += val;
		}
	return out_val;
}

void main()
{
    string str("Hello Worlds!");
	int i_val = Multi(5,5);
	int i_val2 = Multi(2,6);
	cout << str << endl;
	cout << str << endl;
	cout << i_val << endl;
	cout << i_val2 << endl;
	cout << str << endl;
}

