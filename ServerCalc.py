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
        option = s_sock.recv(2048)
        dec = option.decode()
        print("The option is", dec)
        if not option:
            break
        number = s_sock.recv(2048)
        inumber = int(number)
        print("The number is" , inumber)
        if (dec == '1'):
          cm=float(input('Enter a length in centimeter (cm): '))
          result = cm/100
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for cm to m:", result)
        elif (dec == '2'):
          m=float(input('Enter a length in meter (m): '))
          result = m*100
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result m to cm:", result)
        elif (dec == '3'):
          kg=float(input('Enter a weight in kilogram (kg): '))
          result = kg*2.205
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for kg to pounds:", result)
        elif (dec == '4'):
          pounds=float(input('Enter a weight in pounds (lb): '))
          result = pounds/2.205
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for pounds to kg:", result)
        elif (dec == '5'):
          cm=float(input('Enter a height in centimeter (cm): '))
          result = cm/30.48
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for cm to feet:", result)
        elif (dec == '6'):
          feet=float(input('Enter a height in feet: '))
          result = feet*30.48
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for feet to cm:", result)
        elif (dec == '7'):
          km=float(input('Enter a distance in kilometer (km): '))
          result = km*1000
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for km to m:", result)
        elif (dec == '8'):
          m=float(input('Enter a distance in meter: '))
          result =m/1000
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for m to km:", result)
        elif (dec == '9'):
          celcius=float(input('Enter a temperature in celcius (°C): '))
          result = (celcius * 9/5) + 32
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for celcius to f:", result)
        elif (dec == '10'):
          F=float(input('Enter a temperature in Fahrenheit (F): '))
          result = (F -32) * 5/9
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result for f to celcius:", result)
        elif (dec == '11'):
          a = str(input('A: '))
          b = str(input('B: '))
          result = a + b
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result is:", result)
        elif (dec == '12'):
          a = str(input('A: '))
          b = str(input('B: '))
          result = a - b
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result is:", result)
        elif (dec == '13'):
          a = str(input('A: '))
          b = str(input('B: '))
          result = a * b
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result is:", result)
        elif (dec == '14'):
          a = str(input('A: '))
          b = str(input('B: '))
          result = a / b
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result is:", result)
        elif (dec == '15'):
          a = str(input('A: '))
          b = str(input('B: '))
          result = a % b
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result is:", result)
        elif (dec == '16'):
          a = str(input('A: '))
          b = str(input('B: '))
          result = a ^ b
          s_sock.send(bytes(str(result), 'utf-8'))
          print("The result is:", result)
        elif (dec == '17'):
          s_sock.close()
          print("Client has been disconnected.")
        else:
          print("Invalid option. Try again!")
          s_sock.close()
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
