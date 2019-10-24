import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name=socket.gethostname()
port=12121

sock.bind((host_name,port))
sock.listen(1)
count=0
while count!=5:
	conn,address=sock.accept()
	print("Address of Client ",address)
	print("Message From Client",conn.recv(1024))
	conn.send("Hello Client")
	approach=int(conn.recv(1024))
	m=int(conn.recv(1024))
	print(type(approach),type(m))
	if(approach==1):
		for i in range(0,2**m):
			print("Send frame ",i)
			conn.send(str(i))
			time.sleep(1)
		error=int(conn.recv(1024))
		print(" Error in Bit no",error)
		for i in range(error,2**m):
			print("Send frame ",i)
			conn.send(str(i))
			time.sleep(1)
	if(approach==2):
		for i in range(0,2**m):
			print("Send frame ",i)
			conn.send(str(i))
			time.sleep(1)
		error=int(conn.recv(1024))
		print(" Error in Bit no",error)
		print("Send frame ",error)
		conn.send(str(error))
		time.sleep(1)
	conn.close()	
	count+=1
sock.close()
