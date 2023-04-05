from socket import *

serverName = 'localhost'
serverPort = 8000

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    arr = [12, 35, 67, 98, 101]
    print('Array is:', arr)
    el = input('Choose your num: ')
    arr_str = ','.join(str(x) for x in arr)
    clientSocket.send((str(el) + ';' + arr_str).encode())

    pos = clientSocket.recv(1024)
    if pos:
        pos = pos.decode()
        if pos != "-1":
            print(f"The index of {el} in the array is {pos}")
        else:
            print(f"{el} is not present in the array")
    else:
        print("Server did not respond")
except ConnectionRefusedError:
    print(f"Could not connect to server at {serverName}:{serverPort}")
finally:
    clientSocket.close()
