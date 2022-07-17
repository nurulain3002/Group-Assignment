#client
import socket
import math
import sys

ClientSocket = socket.socket()
host = '192.168.56.106'
port = 8888

print('\nWaiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(2048)
print(Response.decode("utf-8"))


print(		"\t\t\t* *** *** *** OPERATION LIST *** **** *** *\t\t\t\n")

print("   ------------------------------------------------------------------------------")
print("   | [A]  cm to m Conversion")
print("   | [B]  m to cm Conversio")
print("   | [C]  kg to pounds Conversion")
print("   | [D]  pounds to kg Conversion")
print("   | [E]  cm to feet Conversion")
print("   | [F]  feet to cm Conversion")
print("   | [G]  km to m Conversion ")
print("   | [H]  m to km Conversion ")
print("   | [I]  celcius to f Conversion")
print("   | [J]  f to celcius Conversion")
print("   | [K]  Addition Operation")
print("   | [L]  Subtraction Operation")
print("   | [M]  Multiplication Operation")
print("   | [N]  Division Operation")
print("   | [O]  Modulus Operation")
print("   | [P]  Power Operation")
print("   -------------------------------------------------------------------------------")

while True:
    
    option = input('Enter Your Option or Type "EXIT" if you are done :\n ')
    

    if option == "A" or option == "B" or option == "C" or option == "D" or option == "E" or option == "F" or option == "G" or option == "H" or option == "I" or option == "J" or option == "K" or option == "L" or option == "M" or option == "N" or option == "O" or option == "P":
        number1 = '0'
        number2 = '0'
        Input =  option + ":" + number1 + ":" + number2
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(2048)
        print(Response.decode("utf-8"))

    elif option == "EXIT":
      print ("THANK YOU FOR USING THIS CONVERSION CALCULATOR\n")
      break

    else:
      print("WRONG INPUT, TRY AGAIN!!")
      ClientSocket.send(str.encode(input))
      Response = ClientSocket.recv(2048)
      print(Response.decode("utf-8"))
    
ClientSocket.close()
