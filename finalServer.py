import socket #import all socket

IP = "192.168.56.105" #ip address of server
PORT = 8888 #port that used

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket for ip address and udp
socket.bind((IP, PORT)) #bind with ip and port client

print('Server Listening At {}'.format(socket.getsockname())) #get client ip and port

while True: #while loop
    messageBytes, address = socket.recvfrom(2048) #receive from client
    messageString = messageBytes.decode('utf-8') #decode bytes to string
    print('Received from client {} : {}'.format(address, messageString)) #print message in string from client
    print('\n')
    print(messageString)

    if messageString == 'E' or messageString == 'e': #when client choose to exit
        break

print('Connection Closed')
socket.close() #close all the socket

