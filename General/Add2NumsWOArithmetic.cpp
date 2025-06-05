/* The goal is to add two numbers without using any arithmetic operators. 
I have achieved this by making use of bitwise operators.
When you add two numbers, say 34 and 78, by completely ignoring the carry, you get 002. 
When you add the same two numbers by only considering the carry you get 110.
The sum of these two will give the actual sum which is 112.
Similarly in binary, you can do the same. The intersting pattern here is as follows:
The sum of two numbers result in 0 iff both the bits I am going to add are either 0 or 1. This is essentially XOR operation. 
The carry of two numbers result in 1 iff both the bits I am going to add are 1 but the thing to note here is that it is left shifted by 1 bit. 
This operation is AND of two numbers followed by leftshift by 1 bit. 
Implemented this logic in a recursive function.
*/

#include<iostream>
using namespace std;

int add(int x, int y)
{
	if(y==0)
		return x;
	int sum = (x ^ y);
	int carry = (x & y) << 1;
	return add(sum, carry);
}

int main(){
	cout<<"Enter the first number:";
	int x;
	cin>>x;
	cout<<"Enter the second number:";
	int y;
	cin>>y;
	
	//Adding the two numbers without any airthmetic operators. 
	cout<<"The sum is "<<add(x, y)<<endl;
	return 0;
}
	
