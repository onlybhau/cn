import socket
import time
import math
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name=socket.gethostname()
port=12122

sock.bind((host_name,port))
sock.listen(1)
count=0
status=0
while count!=3:
	print('server is listening')
	conn,address=sock.accept()
	print("Address of Client ",address)
	print("Message From Client",conn.recv(1024))
	conn.send("Hello  Client")
	choice=int(conn.recv(1024))
	print("Choice",choice)
	if(choice==1):
		print("sin")
		no=int(conn.recv(1024))
		result=math.sin(math.radians(no))
		print('Result:-',result)
		conn.send(str(result))
	if(choice==2):
		print("cos")
		no=int(conn.recv(1024))
		result=math.cos(math.radians(no))
		print('Result:-',result)
		conn.send(str(result))
	if(choice==3):
		print("tan")
		no=int(conn.recv(1024))
		result=math.tan(math.radians(no))
		print('Result:-',result)
		conn.send(str(result))

	conn.close()
	count+=1
sock.close()
