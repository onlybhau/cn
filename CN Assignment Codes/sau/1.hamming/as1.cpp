#include<iostream>
using namespace std;

int main()
{
	int d[10],r[10];
	int j,p1,p2,p3,p4;
	
	cout<<"\nenter 1st data bit=";
	cin>>d[3];
	cout<<"\nenter 2nd data bit=";
	cin>>d[5];
	cout<<"\nenter 3rd data bit=";
	cin>>d[6];
	cout<<"\nenter 4th data bit=";
	cin>>d[7];
	
	d[1]=d[3] xor d[5] xor d[7];
	d[2]=d[3] xor d[6] xor d[7];
	d[4]=d[5] xor d[6] xor d[7];
	
	cout<<"Data Bits send from sender Are : ";
	
	for(int i=1;i<8;i++)
		cout<<d[i];
		
	cout<<"\nEnter Bites Recived at Recivers side ";
	for(int i=1;i<8;i++)
		cin>>d[i];
		
	cout<<"Recived Bits Are : ";
	
	for(int i=1;i<8;i++)
		cout<<d[i];
		
	p1=d[1] xor d[3] xor d[5] xor d[7];
	p2=d[2] xor d[3] xor d[6] xor d[7];
	p3=d[4] xor d[5] xor d[6] xor d[7];
	
	int p=(p1*1)+(p2*2)+(p3*4);
	cout<<"\n"<<p<<"th bit is changed";
	
	if(d[p]==0)
		d[p]=1;
	else if(d[p]==1)
		d[p]=0;
		h
	cout<<"\n\nCorrected Hamming Code is :"	;
	for(int i=1;i<8;i++)
		cout<<d[i];
		
	cout<<"\n";
	return 0;
} 
