import socket
import time

dest = ('<broadcast>',5000)
sx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sx.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sx.bind(('10.20.4.255',5000))

while True:
	data, addr = sx.recvfrom(1024) # buffer size is 1024 bytes
	print data