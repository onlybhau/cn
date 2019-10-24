import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name=socket.gethostname()
port=12122
sock.connect((host_name,port))
sock.send("Hello Server".unicode())
print("Message From Server",sock.recv(1024))
sock.close()
