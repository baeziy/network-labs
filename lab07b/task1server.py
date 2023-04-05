from socket import *

serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print('The server is ready to receive...')

def bSearch(data: list, n: int) -> int:
    low = 0  
    high = len(data) - 1  
    mid = 0  
  
    while low <= high:  
        mid = (high + low) // 2  
        if data[mid] < n:  
            low = mid + 1  
        elif data[mid] > n:  
            high = mid - 1  
        else:  
            return mid  
    return -1  

while True:
    connectionSocket, addr = serverSocket.accept()
    data = connectionSocket.recv(1024).decode()
    n, listt = data.split(';')
    arr = list(map(int, listt.split(',')))
    connectionSocket.send(str(bSearch(arr, int(n))).encode())
    connectionSocket.close()
