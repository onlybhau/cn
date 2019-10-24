import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name=socket.gethostname()
port=12122
sock.connect((host_name,port))
sock.send("Hello Server")
print("Message From Server",sock.recv(1024))
print 'Enter Your Choice :-'
print '\t1.sin'
print '\t2.cos'
print '\t3.tan'
choice=int(input("Enter choice--->"))
print("Choice",choice)
sock.send(str(choice))
if(choice==1):
	print("sin")
	no=input("Enter the No:-->")
	sock.send(str(no))
	print("result",sock.recv(1024))
if(choice==2):
	print("cos")
	no=input("Enter the No:-->")
	sock.send(str(no))
	print("result",sock.recv(1024))
if(choice==3):
	print("tan")
	no=input("Enter the No:-->")
	sock.send(str(no))
	print("result",sock.recv(1024))
sock.close()
