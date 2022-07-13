import socket

IP = "192.168.56.109" #ip address of the server
PORT = 8888 #port number that used

def main_menu(): #menu to display 
    print('\nWelcome to the conversion calculator!')
<<<<<<< HEAD
    print('Which function would you like to do?')
    print('1. Length Conversion') #cm to m , m to cm
    print('2. Weight Conversion') #kg to pounds , pounds to kg
    print('3. Height Conversion') #cm to feet , feet to cm 
    print('4. Distance Conversion') #km to m , m to km
    print('5. Temperature Conversion') #celcius to fahrenhait, fahrenhait to celcius
    print('6. Addition Operation') #addition
    print('7. Subtraction Operation') #substraction
    print('8. Multiplication Operation') #multiplication
    print('9. Division Operation') #division
    print('10. Modulus Operation') #modulus
    print('11. Power Operation') #power
=======
    print('Which conversion would you like to do?')
    print('1. Length') #cm to m , m to cm
    print('2. Weight') #kg to pounds , pounds to kg
    print('3. Height') #cm to feet , feet to cm
    print('4. Distance') #km to m , m to km
    print('5. Temperature') #celcius to fahrenhait, fahrenhait to celcius
>>>>>>> origin
    print('Enter E if you want to exit the calculator')
    print('Enter M if you want to return to the main menu')

def cm_m():
    cm=float(input('\nEnter a length in centimeter (cm): '))
    m= cm/100
    print('Length in centimeter (cm): {0}'.format(m))
    message = 'Conversion for length from cm to m for ' + str(cm) + ' is ' + str(m)
    print(\n'Message being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def m_cm():
    m=float(input('\nEnter a length in meter (m): '))
    cm= m*100
    print('Length in meter (m): {0}'.format(cm))
    message = 'Conversion for length from m to cm for ' + str(m) + ' is ' + str(cm)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def kg_pounds():
    kg=float(input('\nEnter a weight in kilogram (kg): '))
    pounds= kg*2.205
    print('Weight in pounds: {0}'.format(pounds))
    message = 'Conversion for weight from kg to pounds for ' + str(kg) + ' is ' + str(pounds)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def pounds_kg():
    pounds=float(input('\nEnter a weight in pounds (lb): '))
    kg= pounds/2.205
    print('Weight in kilogram (kg): {0}'.format(kg))
    message = 'Conversion for weight from pounds to kg for ' + str(pounds) + ' is ' + str(kg)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()
    
def cm_feet():
    cm=float(input('\nEnter a height in centimeter (cm): '))
    feet= cm/30.48
    print('Height in feet (ft): {0}'.format(feet))
    message = 'Conversion for height from cm to feet for ' + str(cm) + ' is ' + str(feet)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def feet_cm():
    feet=float(input('\nEnter a height in centimeter (cm): '))
    cm= feet*30.48
    print('Height in centimeter (cm): {0}'.format(cm))
    message = 'Conversion for height from feet to cm for ' + str(feet) + ' is ' + str(cm)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()
    
def km_m():
    km=float(input('\nEnter a distance in kilometer (km): '))
    m= km*1000
    print('Distance in meter (m): {0}'.format(m))
    message = 'Conversion for distance from km to m for ' + str(km) + ' is ' + str(m)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def m_km():
    m=float(input('\nEnter a distance in meter: '))
    km=m/1000
    print('Distance in kilometer (km): {0}'.format(km))
    message = 'Conversion for distance from m to km for ' + str(m) + ' is ' + str(km)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()
    
def celcius_F():
    celcius=float(input('\nEnter a temperature in celcius (°C): '))
    F= (celcius * 9/5) + 32
    print('Temperature in Fahrenheit (F): {0}'.format(F))
    message = 'Conversion for temperature from Fahrenheit to celcius for ' + str(celcius) + ' is ' + str(F)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def F_celcius():
    F=float(input('\nEnter a temperature in Fahrenheit (F): '))
    celcius= (F -32) * 5/9
    print('Temperature in celcius (°C): {0}'.format(celcius))
    message = 'Conversion for temperature from celcius to Fahrenheit for ' + str(F) + ' is ' + str(celcius)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def add():
    num1 = float(input('\nEnter the first number: '))
    num2 = float(input('\nEnter the second number: '))
    ans = num1 + num2
    message = 'The addition for ' + str(num1) + ' and ' + str(num2) + ' is ' + str(ans)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def sub():
    num1 = float(input('\nEnter the first number: '))
    num2 = float(input('\nEnter the second number: '))
    ans = num1 - num2
    message = 'The subtraction  for ' + str(num1) + ' and ' + str(num2) + ' is ' + str(ans)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def mul():
    num1 = float(input('\nEnter the first number: '))
    num2 = float(input('\nEnter the second number: '))
    ans = num1 * num2
    message = 'The multiplication  for ' + str(num1) + ' and ' + str(num2) + ' is ' + str(ans)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def div():
    num1 = float(input('\nEnter the first number: '))
    num2 = float(input('\nEnter the second number: '))
    ans = num1 / num2
    message = 'The division  for ' + str(num1) + ' and ' + str(num2) + ' is ' + str(ans)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def mod():
    num1 = float(input('\nEnter the first number: '))
    num2 = float(input('\nEnter the second number: '))
    ans = num1 % num2
    message = 'The modulus  for ' + str(num1) + ' and ' + str(num2) + ' is ' + str(ans)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()

def pow():
    num1 = float(input('\nEnter the first number: '))
    num2 = float(input('\nEnter the second number: '))
    ans = num1 ** num2
    message = 'The power of num  ' + str(num1) + ' and ' + str(num2) + ' is ' + str(ans)
    print('\nMessage being send to server: ' + '\n' + message + "\n")
    socket.sendto(message.encode('utf-8'), (IP, PORT))
    main_menu()


    
main_menu()

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True: #ask user to enter the value
    choice = input()
                                    

    if choice == '1':
        print('\nThis is length unit conversion')
        print('1. cm to m')
        print('2. m to cm')
        choice_length = input()
        
        if choice_length == '1':
            cm_m()
        if choice_length == '2':
            m_cm()
       
    elif choice == '2':
        print('\nThis is weight unit conversion')
        print('1. kg to pounds')
        print('2. pounds to kg')
        choice_weight = input()
        
        if choice_weight == '1':
            kg_pounds()
        if choice_weight == '2':
            pounds_kg()
            
    elif choice == '3':
        print('\nThis is height unit conversion')
        print('1. cm to feet')
        print('2. feet to cm')
        choice_height = input()
        
        if choice_height == '1':
            cm_m()
        if choice_height == '2':
            m_cm()
      
    elif choice == '4':
        print('\nThis is distance unit conversion')
        print('1. km to m')
        print('2. m to km')
        choice_distance = input()
        
        if choice_distance == '1':
            km_m()
        if choice_distance == '2':
            m_km()
       
    elif choice == '5':
        print('\nThis is temperature unit conversion')
        print('1. °C to F')
        print('2. F to °C ')
        choice_temp = input()
        
        if choice_temp == '1':
            celcius_F()
        if choice_temp == '2':
            F_celcius()

    elif choice == '6':
        print('\nThis is addition operation')
        add()
    
    elif choice == '7':
        print('\nThis is subtraction operation')
        sub()
   
    elif choice == '8':
        print('\nThis is multiplication operation')
        mul()

    elif choice == '9':
        print('\nThis is division operation')
        div()

    elif choice == '10':
        print('\nThis is modulus operation')
        mod()

    elif choice == '11':
        print('\nThis is power operation')
        pow()


    elif choice == 'M' or choice =='m':
        main_menu()
        
    elif choice == 'E' or choice == 'e':
        message = 'E' or 'e'
        print('\nMessage being send to server: ' + '\n' + message + "\n")
        socket.sendto(message.encode('utf-8'), (IP, PORT))
        break;
    
    else:
        print('\nWrong input, please enter the right input')
        main_menu()

                                          
print('Connection Closed')
socket.close() #close all the socket

