# NAME: Muhammad Mustafa Kamal Malik
# Roll# 241610047

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")


def findVal(char: str) -> str:
    myDict = {
        ('A', 'B', 'C'): "2",
        ('D', 'E', 'F'): "3",
        ('G', 'H', 'I'): "4",
        ('J', 'K', 'L'): "5",
        ('M', 'N', 'O'): "6",
        ('P', 'Q', 'R', 'S'): "7",
        ('T', 'U', 'V'): "8",
        ('W', 'X', 'Y', 'Z'): "9"
    }

    for key, value in myDict.items():
        if char in key:
            return value
    return char

def loopMessage(message: str) -> str:

    newMsg = ''
    for char in message:
        if char == ' ':
            newMsg += '1'
            continue
        elif char == '-':
            continue
        retVal = findVal(char)
        if retVal == None:
            continue
        newMsg += retVal

    return newMsg


while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    # print("Message received from %s port %s"%(clientAddress[0],clientAddress[1]))
    modifiedMessage = loopMessage(message.decode().upper())
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
