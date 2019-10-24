import socket 



while True:
	choice=int(input('Enter your choice :\n1.GetHostName\n2.URL -> IP\n'))
	if choice==1:
		hostname=socket.gethostname()
		print('HostName : ',hostname)
	elif choice==2:
		URL=input('Enter the URL :')
		IP=socket.gethostbyname(URL)
		print('IP address : ',IP)
	wh=int(input('Continue?(1|0)'))
	if wh==0:
		break
