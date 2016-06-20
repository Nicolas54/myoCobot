from Tkinter import *

fenetre  = Tk()

def drawline():
	can.create_line(12,8,15,45, width="2", fill='blue')

champ_label = Label(fenetre, text="Test first fenetre!")

can = Canvas(fenetre, bg="black")
drawline()
can.pack()

champ_label.pack()

fenetre.mainloop()
