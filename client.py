import socket 

IP = "192.168.56.105" #ip address of the server
PORT = 8888 #port number that used

print('Welcome to the simple calculator! \n - Press X if you want to exit \n - Insert the values of A and B and then the operation you want to make')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True: #ask user to enter the value 

    print('Please enter the value for A')
    a = input()

    print('Please enter the value for B')
    b = input()

    print('Please enter the arithmetic operation')
    operator = input()



    message = a +', '+b+', '+operator
    print('Message being send to server: ' + message + "\n")

    socket.sendto(message.encode('utf-8'), (IP, PORT))
    if a == 'X' or b == 'X' or operator == 'X':
        break

    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print('Result received from server %s : %s ' % (address, text) + "\n")

print('Connection Closed')
socket.close() #close all the socket
