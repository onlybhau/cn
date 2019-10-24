import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0) # get instance

host=socket.gethostname() # get the hostname
port=12429 # initiate port no above 1000


s.bind((host,port)) # bind host address and port together

s.listen(5) # configure how many client the server can listen simultaneously

conn,addr=s.accept() # accept new connection


while True:
	# receive data stream. it won't accept data packet greater than 1000 bytes
	a=conn.recv(1000)
	print("\nMessage Recived :- "+a)
	if a == 'bye':
		break
	m=raw_input("Enter Message : ")
	conn.send(bytes(m))
	
	
s.close()
