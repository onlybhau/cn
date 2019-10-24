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
print("File Transfer")
while count!=2:
	print('server is listening')
	conn,address=sock.accept()
	print("Address of Client ",address)
	print("Message From Client",conn.recv(1024))
	conn.send("Hello  Client")
	filename=conn.recv(1024)
	try:
		fo = open(filename,'r')
	except IOError:
		status=1
	conn.send(str(status))
	if(status==1):
		print(" File Not Found")
		conn.send("File Not Found")
	else:
		conn.send(fo.read())
		print("File Successfully Transfer")
	conn.close()
	count+=1
sock.close()
