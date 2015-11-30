import socket, sys
import time

dest = ('<broadcast>', 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
while 1:
	s.sendto("Hello from me", dest)
	time.sleep(1)