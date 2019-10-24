import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name=socket.gethostname()
port=12121
sock.connect((host_name,port))
sock.send("Hello Server")
print("Message From Server",sock.recv(1024))
approach = int(input("Enter 1 for GoBack N or 2 for SelectiveRepeat : "))
sock.send(str(approach))
m = int(input("Enter the value for m : "))
sock.send(str(m))

if(approach==1):
	print(" By Go Back N Protocol")
	for i in range(0,2**m):
		print(" Received Frame Are:-",sock.recv(1024))
		time.sleep(1)
	error = int(input("Enter Error Frame NO: "))
	sock.send(str(error))
	for i in range(error,2**m):
		print(" Received Frame Are:-",sock.recv(1024))
		time.sleep(1)
if(approach==2):
	print("Selective Repeat")
	for i in range(0,2**m):
		print(" Received Frame Are:-",sock.recv(1024))
		time.sleep(1)
	error = int(input("Enter Error Frame NO: "))
	sock.send(str(error))
	print(" Received Frame Are:-",sock.recv(1024))
	time.sleep(1)

sock.close()
