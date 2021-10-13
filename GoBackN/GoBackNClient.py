import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	send_data=list()
	while(1):
		pkt=int(input("/nENTER NUMBER OF PACKETS(0 to exit):"))
		if(pkt==0):
			s.sendall("q".encode())
			s.close()
			exit(0)
		nack=100;
		resend=0;
		i=0
		while(i < pkt):
			if (resend==1):
				nack=100
				print("\n RESENDING PACKET ",i+1," :",send_data[i])
				opt=input(" ENTER 1 TO CONTINUE")
			else:
				print("\nENTER THE PACKET:",i+1)
				s_data=input()
				send_data.append(s_data)
			s.sendall(send_data[i].encode())
			recv_data=s.recv(1024)
			if(recv_data==b"NACK"):
				print("\nRECEIVED NEGATIVE ACKNOWLEDGEMENT")
				if(nack>i):
					nack=i
			if((i+1)>=pkt):
				resend=1
				i=nack
				continue
			i=i+1
		print("\nRETRANSMISSION COMPLETED");