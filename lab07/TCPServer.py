from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')



def insertionSort(arr: list) -> list:
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr




while 1:
    connectionSocket, addr = serverSocket.accept()
    print(connectionSocket.getpeername())
    array = connectionSocket.recv(1024).decode()
    array = [int(x) for x in array.split(', ')]
    sorted_array = insertionSort(array)
    sorted_string = ', '.join(str(x) for x in sorted_array)
    connectionSocket.send(sorted_string.encode())
    connectionSocket.close()
