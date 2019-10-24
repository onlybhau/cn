import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name=socket.gethostname()
port=12122
sock.connect((host_name,port))
print("File Transfer")
sock.send("Hello Server")
print("Message From Server",sock.recv(1024))
print("File Download")
filename=raw_input("Enter The File Name-->")
sock.send(filename)
status=int(sock.recv(1024))
if(status==1):
	print(sock.recv(1024))
	sock.close()
else:
	data=sock.recv(1024)
	fo=open("a1.txt",'w')
	fo.write(data)
	fo.close()
	print("File Successfully Download")
	sock.close()
