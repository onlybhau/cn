import socket 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0) # instantiate

host=socket.gethostname() # as both code is running on same pc
port=12429 # socket server port number

s.connect((host,port)) # connect to the server

while True:
	m=raw_input("Enter Message : ")
	s.send(bytes(m)) # send message
	if m == 'bye': # if client send bye message then close the connection.
		break
	print("\nMessage Recived :-"+ s.recv(1000)) # receive response

s.close()
