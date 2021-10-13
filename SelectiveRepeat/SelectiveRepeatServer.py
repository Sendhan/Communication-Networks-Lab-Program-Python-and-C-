import socket 

HOST = '127.0.0.1' # Standard loopback interface address (localhost) 
PORT = 65432 # Port to listen on (non-privileged ports are > 1023) 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT)) 
	s.listen() 
	conn, addr = s.accept() 
	with conn: 
		print('Connected by', addr) 
		while True:
			recv_data=conn.recv(1024) 
			if(recv_data==b"q"): 
				s.close() 
				exit(0) 
			else: 
				print("\n1.SEND ACK\n2.DO NOT SEND ACK\n")  
				opt=input("Enter Option:\n") 
				if(opt=="1"): 
					send_data="ACK" 
					print("\n RECEIVED DATA=",recv_data ) 
					i=input("Enter 1 to continue:\n") 
				else:
					send_data="NACK"
					conn.sendall(send_data.encode()) 