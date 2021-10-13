import socket

HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	send_data = list()
	nack = list()
	while 1:
		pkt = int(input("\nENTER NUMBER OF PACKETS (0 to exit) : "))
		if pkt == 0:
			s.sendall("q".encode())
			s.close()
			exit(0)
		for i in range(0, pkt):
			nack.append(0)
			resend = 0
		i = 0
		while i < pkt:
			if resend == 1:
				if nack[i] == 1:
					nack[i] = 0
					print("\nRESENDING PACKET ", i + 1, " : ", send_data[i])
					opt = input("ENTER 1 TO CONTINUE")
					s.sendall(send_data[i].encode())
					recv_data = s.recv(1024)
					if recv_data == b"NACK":
						print("\nRECEIVED NEGATIVE ACKNOWLEDGEMENT")
						nack[i] = 1
					else:
						print("\nReceived Acknowledgement")
						opt = int(input("\nEnter 1 to continue"))
					if (i + 1) >= pkt:
						break
			else:
				print("\nENTER THE PACKET : ", i + 1)
				s_data = input()
				send_data.append(s_data)
				s.sendall(send_data[i].encode())
				recv_data = s.recv(1024)
				if recv_data == b"NACK":
					print("\nRECEIVED NEGATIVE ACKNOWLEDGEMENT")
					nack[i] = 1
				else:
					print("Received Acknowledgement")
				if (i + 1) >= pkt:
					resend = 1
					i = 1
					continue
			i = i + 1
		print("\nRETRANSMISSION COMPLETED")
