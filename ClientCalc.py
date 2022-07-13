#client
import socket
import math
ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(2048)
print(Response)
while True:
    print("Option:   1-cm to m Conversion      2-m to cm Conversion    3-kg to pounds Conversion    4-pounds to kg Conversion   5-cm to feet Conversion    6-feet to cm Conversion   7-km to m Conversion   8-m to km Conversion  9-celcius to f Conversion 10-f to celcius Conversion 11-Addition Operation 12-Subtraction Operation 13-Multiplication Operation 14-Division Operation  15-Modulus Operation  16-Power Operation  17-exit\n")
    option = input('Enter Your Option: ')
    ClientSocket.send(str.encode(option))
    number = input('Enter number: ')
    ClientSocket.send(str.encode(number))
    if (option == '1'):
      print("cm to m Conversion")
    elif (option == '2'):
      print("m to cm Conversion")
    elif (option == '3'):
      print("kg to pounds Conversion")
    elif (option == '4'):
      print("pounds to kg Conversion")
    elif (option == '5'):
      print("cm to feet Conversion")
    elif (option == '6'):
      print("feet to cm Conversion")
    elif (option == '7'):
      print("km to m Conversion")
    elif (option == '8'):
      print("m to km Conversion")
    elif (option == '9'):
      print("celcius to f Conversion")
    elif (option == '10'):
      print("f to celcius Conversion")
    elif (option == '11'):
      print("Addition Operation")
    elif (option == '12'):
      print("Subtraction Operation")
    elif (option == '13'):
      print("Multiplication Operation")
    elif (option == '14'):
      print("Division Operation")
    elif (option == '15'):
      print("Modulus Operation")
    elif (option == '16'):
      print("Power Operation")
    elif (option == '17'):
      print("Bye!")
      ClientSocket.close()
    else:
      print("Invalid option. Try again!")
    result = ClientSocket.recv(2048)
    print("Result:",result.decode('utf-8'))
ClientSocket.close()
