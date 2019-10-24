import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

host=socket.gethostname()
port=12411


s.bind((host,port))

s.listen(5)

clt,addr=s.accept()

print("Connected To Cilent ")
clt.send(bytes("\nSelect Operation \n1.File Transfer\n2.Arithmetic Operation"))
ch=clt.recv(1000)
ch=int(ch)
print(type(ch))
if ch == 2:
	clt.send(bytes("Enter Value of a and b"))
	a=clt.recv(1000)
	print(a)
	b=clt.recv(1000)
	print(b)
	clt.send(bytes("\nSelect Operation \n1.Addition\n2.Substraction"))
	ans=clt.recv(1000)
	print(ans)
	ans=int(ans)
	if ans == 1:
		ans=(int(a)+int(b))
	elif ans == 2:
		ans=(int(a)-int(b))
		
	clt.send(bytes(ans))
elif ch == 1:
	clt.send(bytes("Enter File Name :"))
	fnm=clt.recv(1000)
	fnm=str(fnm)
	
	fo = open(fnm,'r')
	data=fo.read()
	clt.send(bytes(data))
s.close()
