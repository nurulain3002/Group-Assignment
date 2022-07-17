#server
import socket
import sys
import time
import errno
import math
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        #calculation
        try:
            opt, num1, num2 = data.split(":")
            option = str(opt)
            number1 = int(num1)
            number2 =  int(num2)

            if (option[0] == 'A'):
              option = "cm to m Conversion"
              number1 = float(input('Enter a length in centimeter (cm): '))
              result = number1/100
            elif (option[0] == 'B'):
              option = "m to cm Conversion"
              number1=float(input('Enter a length in meter (m): '))
              result = number1*100
            elif (option[0] == 'C'):
              option = "kg to pounds Conversion"
              number1=float(input('Enter a weight in kilogram (kg): '))
              result = number1*2.205
            elif (option[0] == 'D'):
              option = "pounds to kg Conversion"
              number1=float(input('Enter a weight in pounds (lb): '))
              result = number1/2.205
            elif (option[0] == 'E'):
              option = "cm to feet Conversion"
              number1=float(input('Enter a height in centimeter (cm): '))
              result = number1/30.48
            elif (option[0] == 'F'):
              option = "feet to cm Conversion"
              number1=float(input('Enter a height in feet: '))
              result = number1*30.48
            elif (option[0] == 'G'):
              option = "km to m Conversion"
              number1=float(input('Enter a distance in kilometer (km): '))
              result = number1*1000
            elif (option[0] == 'H'):
              option = "m to km Conversion"
              number1=float(input('Enter a distance in meter: '))
              result =number1/1000
            elif (option[0] == 'I'):
              option = "celcius to f Conversion"
              number1=float(input('Enter a temperature in celcius (°C): '))
              result = (number1 * 9/5) + 32
            elif (option[0] == 'J'):
              option = "f to celcius Conversion"
              number1=float(input('Enter a temperature in Fahrenheit (F): '))
              result = (number1 -32) * 5/9
            elif (option[0] == 'K'):
              option = "Addition Operation"
              number1 = str(input('A: '))
              number2 = str(input('B: '))
              result = number1 + number2
            elif (option[0] == 'L'):
              option = "Subtraction Operation"
              number1 = str(input('A: '))
              number2 = str(input('B: '))
              result = number1 - number2
            elif (option[0] == 'M'):
              option = "Multiplication Operation"
              number1 = str(input('A: '))
              number2 = str(input('B: '))
              result = number1 * number2
            elif (option[0] == 'N'):
              option = "Division Operation"
              number1 = str(input('A: '))
              number2 = str(input('B: '))
              result = number1 / number2
            elif (option[0] == 'O'):
              option = "Modulus Operation"
              number1 = str(input('A: '))
              number2 = str(input('B: '))
              result = number1 % number2
            elif (option[0] == 'P'):
              option = "Power Operation"
              number1 = str(input('A: '))
              number2 = str(input('B: '))
              result = number1 ^ number2
            else:
              print("Invalid option. Try again!")

            sendtoClient = (str(option) + int(number)+ "\nThe answer is:" + str(result))
            print(sendtoClient)
            print ('DATA RECEIVED :')
            #break

        except:
            print ("Client Disconnected")
            s_sock.send(str("Client Disconnected"))
            break

        if not data:
            break

        s_sock.send(str.encode(str(sendtoClient)))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()


            except socket.error:

                print('got a socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
           s.close()
