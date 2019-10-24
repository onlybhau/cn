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
msg="hii client"
udp_sock.sendto(bytes(msg,'utf-8'),Address_of_client) 


udp_sock.close()
