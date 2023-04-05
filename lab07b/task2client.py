from socket import *

serverName = 'localhost'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
data = input('Enter your data: ')
clientSocket.send(data.encode())
encryptedData = clientSocket.recv(1024)
print("Encrypted data is: ", encryptedData.decode())
