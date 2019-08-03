from tkinter import *
from tkinter import ttk
from pynput.mouse import Controller

import pyautogui as pag
class MyApp:
	def __init__(self, parent):
		self.myparent = parent
		#--------Main Frame-------#
		self.mainframe = Frame(self.myparent)
		self.mainframe.pack()
		#--------   Label --------#
		self.xlabel = Label(self.mainframe,
                                    text = 'x 좌표',
                                    width = 10)
		self.xlabel.grid(row=1, column=1)

		self.ylabel = Label(self.mainframe,
                                    text = 'y 좌표',
                                    width = 10)
		self.ylabel.grid(row=2, column=1)
		#--------   Entry --------#
		self.entry = Entry(self.mainframe,
				   width = 15)
		self.entry.grid(row=1, column=2)

		self.entry2 = Entry(self.mainframe,
                                    width = 15)
		self.entry2.grid(row=2, column =2)
		
		#--------   Button -------#
		self.button = Button(self.mainframe,
				     text = 'start',
				     command = self.clicked)
		self.button.grid(row=2, column = 3)
	def clicked(self):
		self.x = Controller().position[0]
		self.y = Controller().position[1]
		
		self.entry.delete(0,"end")
		self.entry2.delete(0,"end")

		self.entry.insert(0,str(self.x))
		self.entry2.insert(0,str(self.y))

if __name__ == '__main__':
	root = Tk()
	myapp = MyApp(root)
	root.mainloop()
