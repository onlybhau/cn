#include<iostream>
using namespace std;
int main()
{
	int sender[7]={0};
	int receiver[7]={0};
	
	//Accept The Data Field Of Hamming Code 
	printf("Enter the Data Bits Of Hamming Code :_");
	cin>>sender[7]>>sender[6]>>sender[5]>>sender[3];
	printf("\n");
	// Calculate the Parity Bit of that Data bit 
	sender[1]=(sender[3]+sender[5]+sender[7])%2;
	sender[2]=(sender[3]+sender[6]+sender[7])%2;
	sender[4]=(sender[5]+sender[6]+sender[7])%2;
	
	
	printf("Enter the Data Bits Of Hamming Code :_");
	// Display Hamming Code 
	for(int i=7;i>0;i--)
	{
 		printf("%d ",sender[i]);	
	}
	printf("\n");
	printf("Enter the Received Hamming Code :_");
	cin>>receiver[7]>>receiver[6]>>receiver[5]>>receiver[4]>>receiver[3];
	cin>>receiver[2]>>receiver[1];
	printf("Received Hamming Code :_");
	for(int i=7;i>0;i--)
	{
 		printf("%d ",receiver[i]);	
	}
	printf("\n");
	int e1=(receiver[1]+receiver[3]+receiver[5]+receiver[7])%2;
	int e2=(receiver[2]+receiver[3]+receiver[6]+receiver[7])%2;
	int e3=(receiver[4]+receiver[5]+receiver[6]+receiver[7])%2;
	int bit=(e1+e2*2+e3*4);
	printf("\n");
	printf(" Error Bit No Is :- %d",bit);	
	
	receiver[bit]=!(receiver[bit]);
	printf("\n");
	printf("Corrected Hamming Code :_");
	for(int i=7;i>0;i--)
	{
 		printf("%d ",receiver[i]);	
	}

return 0;
}
