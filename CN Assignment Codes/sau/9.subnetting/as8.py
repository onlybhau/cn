mask=[]
sbmsk=[]
ip=[]
nwid=[0,0,0,0]

print("Enter IP Address : ")
a=input()

ip=a.split('.')

for i in range(0,len(ip)):
	ip[i]=int(ip[i])
	
start=ip[3]

if ip[0] > 0 and ip[0]<=127 :
	print("IP Belongs to class A")
	mask=[255,0,0,0]
	print("Default Subnet Mask is : ")
	print(mask)
	
if ip[0] >= 127 and ip[0]<= 191 :
	print("IP Belongs to class B")
	mask=[255,255,0,0]
	print("Default Subnet Mask is : ")
	print(mask)
	
if ip[0] >= 192 and ip[0]<=223 :
	print("IP Belongs to class C")
	mask=[255,255,255,0]
	print("Default Subnet Mask is : ")
	print(mask)

i=0	
for i in range(0,3):
	nwid[i]=(ip[i] & mask[i])
	
	
print("Network Address is: ")	
print(nwid)


host=int(input("Enter No of Hosts"))

host=int(host)

start=int(ip[3])

total=start+host

z=0
while int(total)>0:
    z=z+1
    total=total/2
    
temp=32-z

print("range of IP is "+str(temp))
str1=""
temp=temp-24
while temp !=0:
    str1='1'+str1
    temp=temp-1
    
while len(str1)!=8:
    str1=str1+'0'
    
str1=int(str1,2)

print("subnet Mask is :255.255.255."+str(str1))
#print( str1)


    


#prrr
