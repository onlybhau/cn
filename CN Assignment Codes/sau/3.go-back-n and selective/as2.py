import time
print("Enter Value of m");
m=input()
n=(2**m)-1;

def gobackn():

	print("\n\nSimulation Using Go Back N Sliding Window Protocol :\n\n")

	for i in range(n):
		print("Sending Frame  :"+str(i))
		time.sleep(1)
		
	fno=input("\n\nEnter Frame Number Which having Error :")
	for i in range(fno,n):
		print("Resending Frame : "+str(i))
		time.sleep(1)
		
def selrep():

	print("\n\nSimulation Using Selctive Repeat Sliding Window Protocol :\n\n")

	for i in range(n):
		print("Sending Frame  :"+str(i))
		time.sleep(1)
		
	fno=input("\n\nEnter Frame Number Which having Error :")
	print("Resending Frame : "+str(fno))
	time.sleep(1)
	

while True:
	print("\nSelect Protocol :")
	print("\n1.Go Back N\n2.Selctive Repeat\n3.Exit")
	ch=input("Enter Your Choice :")
	if ch == 1:
		gobackn()
	elif ch == 2:
		selrep()
	elif ch == 3:
		break
