from socket import *
serverName = 'localhost'
serverPort = 80
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
arr = [12,35,67,98,101]
print('Array is: ', arr)
el = int(input('Choose your num: '))
clientSocket.send(el.encode())
pos = clientSocket.recv(1024)
print ('From Server:', pos.decode())
clientSocket.close()
