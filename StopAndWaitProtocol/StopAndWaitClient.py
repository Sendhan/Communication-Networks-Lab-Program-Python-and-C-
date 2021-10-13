import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while(1):
		print("\nEnter Message to server(q or Q to quit):")
		send_data= input()
		s.sendall(send_data.encode())
		if(send_data=="q" or send_data== "Q"):
		   s.close()
		   exit(0)
		while(1):
		   recv_data=s.recv(1024)
		   if(recv_data==b"q" or recv_data==b"Q"):
			   s.close()
			   exit(0)
		   elif(recv_data==b"timeout"):
			   print("\n ack is not received\n resend data=",send_data)
			   s.sendall(send_data.encode())
		   else:
			   print("\n RECEIVED ACK :",recv_data)
			   break