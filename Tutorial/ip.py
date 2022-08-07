import socket

def infoip():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)

	print("Hostname: " + host_name)
	print("IPv4 Address: " + host_ip)