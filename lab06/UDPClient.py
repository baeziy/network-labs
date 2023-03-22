# NAME: Muhammad Mustafa Kamal Malik
# Roll# 241610047

from socket import *
serverName = 'localhost'	# or 'hostname' 'IP address'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print("Received message from %s port %s"%(serverAddress[0],serverAddress[1]))
print(modifiedMessage.decode())
clientSocket.close()
