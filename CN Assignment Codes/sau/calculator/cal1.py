import  socket

soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))

print('\nHostname : ',host_name, '\nIP Address : ({})'.format(ip))
name = input('\nEnter Server Name : ')
soc.listen(1)
print('\nWaiting for incoming connections...')


connection, addr = soc.accept()

client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' is connected...')

connection.send(name.encode())




operation = connection.recv(1024)
operation = operation.decode()
a = connection.recv(1024)
a = a.decode()
temp=a.split(',')
print(temp)
a=int(temp[0])
b=int(temp[1])
if(operation == '+'):
	result=a+b
elif(operation == '-'):
	result=a-b
elif(operation == '*'):
	result=a*b
else:
	result=a/b
result=str(result)
connection.send(result.encode())
connection.close()
