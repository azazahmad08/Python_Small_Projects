#Take socket as input
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)