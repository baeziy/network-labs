from socket import *

serverPort = 8080
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print('The server is ready to receive...')

def encrypt(text, shift):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif (char == ' '):
            result += ' '
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
 
    return result


while True:
    connectionSocket, addr = serverSocket.accept()
    data = connectionSocket.recv(1024).decode()
    connectionSocket.send(encrypt(data, 3).encode())
    connectionSocket.close()
