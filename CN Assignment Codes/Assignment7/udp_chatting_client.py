import socket

serverAddressPort   = (socket.gethostname(),12345) # addressport of server

udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #create udp socket

udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # create socket reuseable
msg="Hiii  Server"

udp_sock.sendto(bytes(msg,'utf-8'),serverAddressPort) #message to client

server_message=udp_sock.recvfrom(1024) # message from server
print("Meaasge:",server_message[0],"Address:-",server_message[1])

udp_sock.close()


