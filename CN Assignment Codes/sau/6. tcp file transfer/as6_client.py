import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

host=socket.gethostname()
port=12411



s.connect((host,port))
print(s.recv(1000))
ch=raw_input("Your Choice : ")
s.send(bytes(ch))
ch=int(ch)
if ch == 2:
	print(s.recv(1000))
	ch=raw_input("Enter Value of A :")
	s.send(bytes(ch))
	ch=raw_input("Enter Value of B :")
	s.send(bytes(ch))
	print(s.recv(1000))
	ch=raw_input("Your Choice : ")
	s.send(bytes(ch))
	print("Answer is :")
	print(s.recv(1000))

if	ch == 1:
	 print(s.recv(1000))
	 fnm=raw_input("Enter File Name :")
	 s.send(bytes(fnm))
	 
	 fin = open("recived.txt",'w')
	 fo=s.recv(1000)
	 fin.write(fo)
s.close()
