import socket

serverAddressPort   = (socket.gethostname(),12345) # addressport of server

udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #create udp socket

udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # create socket reuseable

udp_sock.sendto("Hiii  Server",serverAddressPort) #message to client
	
server_message=udp_sock.recvfrom(1024) # message from server
print("Meaasge:",server_message[0],"Address:-",server_message[1])

filename=raw_input("Enter the filename--->")
udp_sock.sendto(filename,serverAddressPort) #message to client

status=udp_sock.recvfrom(1024) # message from server
if(int(status[0])==1):
	message=udp_sock.recvfrom(1024) # message from server	
	print(message[0])
else:
	message=udp_sock.recvfrom(1024) # message from server	
	fo=open("a1.txt",'w')
	fo.write(message[0])
	fo.close()
udp_sock.close()


