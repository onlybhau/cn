import socket

udp_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)# create udp socket

udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # create socket reusable

host_name=socket.gethostname() #get host name 
port=12345	#port no

udp_sock.bind((host_name,port)) #bind IP and port no to each other

print("UDP server up and listening")

client_message=udp_sock.recvfrom(1024) # message from client
Address_of_client=client_message[1] # store client Address
print("Meaasge:",client_message[0],"Address:-",client_message[1]) 

#message to client
udp_sock.sendto("Hiii  Cilent",Address_of_client) 
status=0
filename=udp_sock.recvfrom(1024)
try:
	fo=open(filename[0],'r')
except IOError:
	print("File Does Not Exist")
	status=1

udp_sock.sendto(str(status),Address_of_client)
if(status==1):
	udp_sock.sendto(" File Does Not Exists",Address_of_client) 
else:
	udp_sock.sendto(fo.read(),Address_of_client) 
fo.close()
udp_sock.close()
