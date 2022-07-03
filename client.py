import socket

IP = "192.168.56.107" #ip address of the server
PORT = 8888 #port number that used

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True: #ask user to enter the value

	# Python code for creating a GUI Tkinter calculator.
	# 1-import tkinter package
	from tkinter import *
	# 2-create a GUI user interface
	if __name__ == "__main__":
		giu_face = Tk() 
		# 3-set the background color for the GUI interface.
		giu_face.configure(background="red")
		# 4-set the title for GUI interface
		giu_face.title("Simple Calculator")
		# 5-set the size of the GUI window interface.
		giu_face.geometry("370x180")
		giu_face.mainloop()
		exp = ""
	# 6-Function to Update the exp in the Text Entry Box
	def pres(number):
		global exp
		# string concatenation
		exp = exp + str(number)
		# using set method to update the expression
		equation.set(exp)
	# 7-Code for Calculating Ultimate Expression
	def pres():
		try:
			global exp
	# 8-using eval function to calculate expression
	total_value = str(eval(exp))
		equation.set(total_value)
		exp = ""
		# using except block to handle generated errors
		except:
		equation.set(" error ")
		exp = ""
	# 9-Function for Clearing the Contents of the Calculator
	def clearng():
		global exp
		exp = ""
		equation.set("")
		equation = StrVar()
	# 10-Function for Creating the EntryBox for Typing the Text for Operation
	exp_field = Ent(gui, text_variable=equation)
	# 11-Using the Grid Method for Assigning the Widgets at their respective positions.
	exp_field.grid(columnspan = 5)
		equation.set("enter your value")
	# 12-create the Buttons and position them inside the window.

	bton1 = Button(giu_face, text =' 1 ', font="lucida 20 bold",
	command = lambda: input_val(1), height = 1, width = 7)
	bton1.grid(row = 2, column = 0, ipady = 4 , ipadx = 2)
	bton2 = Button(giu_face, text = ' 2 ', font="lucida 20 bold",
	command = lambda: input_val(2), height = 1, width = 7)
	bton2.grid(row = 2, column = 1, ipady = 4 , ipadx = 2)
	bton3 = Button(giu_face, text = ' 3 ', font="lucida 20 bold",
	command = lambda: input_val(3), height = 1, width = 7)
	bton3.grid(row = 2, column = 2, ipady = 4 , ipadx = 2)
	bton4 = Button(giu_face, text = ' 4 ', font="lucida 20 bold",
	command = lambda: input_val(4), height = 1, width = 7)
	bton4.grid(row = 3, column = 0, ipady = 4 , ipadx = 2)
	bton5 = Button(giu_face, text = ' 5 ', font="lucida 20 bold",
	command = lambda: input_val(5), height = 1, width = 7)
	bton5.grid(row = 3, column = 1, ipady = 4 , ipadx = 2)
	bton6 = Button(giu_face, text = ' 6 ', font="lucida 20 bold",
	command = lambda: input_val(6), height = 1, width = 7)
	bton6.grid(row = 3, column = 2, ipady = 4 , ipadx = 2)
	bton7 = Button(giu_face, text = ' 7 ', font="lucida 20 bold",,
	command = lambda: input_val(7), height = 1, width = 7)
	bton7.grid(row = 4, column = 0, ipady = 4 , ipadx = 2)	
	bton8 = Button(giu_face, text = ' 8 ', font="lucida 20 bold",
	command = lambda: input_val(8), height = 1, width = 7)
	bton8.grid(row = 4, column = 1, ipady = 4 , ipadx = 2)
	bton9 = Button(giu_face, text = ' 9 ', font="lucida 20 bold",
	command = lambda: input_val(9), height = 1, width = 7)
	bton9.grid(row = 4, column = 2, ipady = 4 , ipadx = 2)
	bton10 = Button(giu_face, text = ' 0 ', font="lucida 20 bold",
	command = lambda: input_val(0), height = 1, width = 7)
	bton10.grid(row = 5, column = 0, ipady = 4 , ipadx = 2)
	plus = Button(giu_face, text=' + ', font="lucida 20 bold",
	command = lambda: input_val("+"), height=1, width=7)
	plus.grid(row = 2, column = 3, ipady = 4 , ipadx = 2)
	minus = Button(giu_face, text = ' - ', font="lucida 20 bold",
	command = lambda: input_val("-"), height = 1, width = 7)
	minus.grid(row = 3, column = 3, ipady = 4 , ipadx = 2)
	multiply = Button(giu_face, text = ' * ', font="lucida 20 bold",
	command = lambda: input_val("*"), height = 1, width = 7)
	multiply.grid(row = 4, column = 3, ipady = 4 , ipadx = 2)
	divide = Button(giu_face, text=' / ', font="lucida 20 bold",
	command = lambda: input_val("/"), height = 1, width = 7)
	equal = Button(giu_face, text=' = ', font="lucida 20 bold",
	command = input_val, height = 1, width = 7)
	equal.grid(row = 5, column = 2, ipady = 4 , ipadx = 2)
	clearng = Button(giu_face, text = 'clearng', font="lucida 20 bold",
	command = clearng, height = 1, width = 7)
	clearng.grid(row = 5, column = '1', ipady = 4 , ipadx = 2)
	Decimal = Button(giu_face, text='.', font="lucida 20 bold",
	command = lambda: input_val('.'), height = 1, width = 7)
	Decimal.grid(row = 6, column = 0, ipady = 4 , ipadx = 2)
	giu_face.mainloop()
 
print('Connection Closed')
socket.close() #close all the socket
