
import math
IP_address = input("Enter the IP address : ")
No_of_subnets = int(input("Enter the desired no. of subnets : "))
id_list = IP_address.split('/')

#calculating subnet id length
length_of_subnet_id = int((int(id_list[1]) + math.log(No_of_subnets,2)))

#calculating no of ohsts per subnet
No_of_hosts_per_subnet = int(math.pow(2,(32-length_of_subnet_id)))

host_bits = (32-length_of_subnet_id)
a = host_bits

octects = id_list[0].split('.')
while(a > 8):
    a = a - 8

number = 1
if host_bits > 16 and host_bits <= 24:
    x = int(octects[1]) + int(math.pow(2,a))
    while(No_of_subnets):
        print ("Subnet ",number,' : ','.'.join(octects))
        octects[1] = str(int(octects[1]) + x)
        No_of_subnets = No_of_subnets - 1
        number = number + 1
elif host_bits > 8 and host_bits <= 16:
    x = int(octects[2]) + int(math.pow(2,a))
    while(No_of_subnets):
        print ("Subnet ",number,' : ','.'.join(octects))
        octects[2] = str(int(octects[2]) + x)
        No_of_subnets = No_of_subnets - 1
        number = number + 1
elif host_bits > 0 and host_bits <= 8:
    x = int(octects[3]) + int(math.pow(2,a))
    while(No_of_subnets):
        print ("Subnet ",number,' : ','.'.join(octects))
        octects[3] = str(int(octects[3]) + x)
        No_of_subnets = No_of_subnets - 1
        number = number + 1
print("\nNo. of hosts in each subnet : ",No_of_hosts_per_subnet)
