import socket
print('Client Server...')

soc=socket.socket()
server_host = input('Enter Server\'s IP address : ')
name = input('Enter Client\'s name : ')
port = 1234

soc.connect((server_host, port))
print("Connected...\n")

soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()

print('Connected to {}...'.format(server_name))
print('Enter [bye] to exit.')




operation = input('Enter +,-,*,/ : ')
soc.send(operation.encode())
a = input('Enter number 1 and 2 with comma : ')
soc.send(a.encode())

result=soc.recv(1024)
result=result.decode()
print('Result is : ',result)
soc.close()
