import socket
import operator
# convert the string operator
operators = {
            "+" : operator.add,
            "-" : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
            '%' : operator.mod,
            '^' : operator.xor,
            }

IP = "192.168.56.101"
PORT = 8888

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

print('Server Listening At {}'.format(socket.getsockname()))

while True:
    messageBytes, address = socket.recvfrom(2048)
    messageString = messageBytes.decode('utf-8')
    print('Received from client {} : {}'.format(address, messageString))

    messageString = messageString.split(", ")
    a = messageString[0]
    b = messageString[1]
    operator = messageString[2]

    if a == 'X' or b == 'X' or operator == 'X':
        break

    result = operators[operator](int(a), int(b))


    socket.sendto(str(result).encode(), address)


print('Connection Closed')
socket.close()