import socket

IP = "192.168.56.105"
PORT = 8888

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

print('Server Listening At {}'.format(socket.getsockname()))

while True:
    messageBytes, address = socket.recvfrom(2048)
    messageString = messageBytes.decode('utf-8')
    print('Received from client {} : {}'.format(address, messageString))
    print('\n')
    print(messageString)
    
    if messageString == 'E' or messageString == 'e':
        break

print('Connection Closed')
socket.close()

