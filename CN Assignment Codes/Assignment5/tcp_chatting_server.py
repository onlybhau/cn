import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name=socket.gethostname()
port=12122

sock.bind((host_name,port))
sock.listen(1)
count=0
status=0
while count!=5:
	print('server is listening')
	conn,address=sock.accept()
	print("Address of Client ",address)
	print("Message From Client",conn.recv(1024))
	conn.send("Hello  Client")
	conn.close()
	count+=1
sock.close()
