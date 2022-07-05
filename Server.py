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

IP = "192.168.56.105" #ip address of the server
PORT = 8888 #port number that used

main_menu()

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket for ip and udp
socket.bind((IP, PORT)) #bind ip and port client

print('Server Listening At {}'.format(socket.getsockname()))

while True:
    option = input()

    if option == 'A' or option == 'a':
                                        print('This is Arithmetic calculation')
                                        print('Which operation would you like to do?')
                                        print('1. Addition')
                                        print('2. Subtraction')
                                        print('3. Multiplication')
                                        print('4. Division')
                                        print('5. Modulus')
                                        print('6. Power')
                                        print('Enter E if you want to exit the calculator')
                                        print('Enter M to return to the main calculator')
                                        insert = input()

                                        if insert == '1':
                                            a = str(input('A: '))
                                            b = str(input('B: '))
                                            add = a + b

                                        elif insert == '2':
                                            a = str(input('A: '))
                                            b = str(input('B: '))
                                            minus = a - b

                                        elif insert == '3':
                                            a = str(input('A: '))
                                            b = str(input('B: '))
                                            multiply = a * b

                                        elif insert == '4':
                                            a = str(input('A: '))
                                            b = str(input('B: '))
                                            divide = a / b

                                        elif insert == '5':
                                            a = str(input('A: '))
                                            b = str(input('B: '))
                                            modulus = a % b

                                        elif insert == '6':
                                            a = str(input('A: '))
                                            b = str(input('B: '))
                                            power = a ^ b

                                        elif insert == 'M' or insert =='m':
                                            main_menu()

                                        elif insert == 'E' or insert =='e':
                                            print('Exiting the calculator')
                                            break
                                        else:
                                            print('ERROR')

                                        socket.sendto(message.encode('utf-8'), (IP, PORT))
                                        data, address = socket.recvfrom(2048)
                                        text = data.decode('utf-8')
                                        print('Result received from server %s : %s ' % (address, text) + "\n")
    elif option == 'B' or option == 'b':
print('Connection Closed')
socket.close() #close all the socket
