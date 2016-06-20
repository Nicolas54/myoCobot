from Tkinter import *

import math


fenetre = Tk()
x1=0
x2=10
y1=10
y2=10

check="all"

can = Canvas(fenetre, bg="black", height=1000, width=500)

def change():
	global check
	if (check == "all" or check == "hauteur"):
		check = "split"
	else:
		check = "all"

def changeH():
	global check
	if (check == "all" or check == "split"):
		check = "hauteur"
	else:
		check = "all"



buttonChange = Button(fenetre, text="change", command = change)
buttonHauteur = Button(fenetre, text="hauteur", command = changeH)

buttonChange.pack(side="left")
#buttonHauteur.pack(side="left")

can.pack()


def drawLineA(x1, coul, delta, change):
	global y1,y2
	z=10
	
	if(delta == 400):
		z=5

	if(delta !=450):

		x2 = delta - (x1/z)/2
		x1 = delta + (x1/z)/2
		
		print("x1 : " + str(x1))
		print("x2 : " + str(x2))
		
		if x1-x2 >5:
			can.create_line(y1,x1,y2,x2, width=1, fill=coul)
		if(change):
			#print myo.getPitch()
			y1+=1
			y2+=1
		if(y1>500):
			can.delete("all")
			y1=0
			y2=0
	else:
		x2 = delta - (x1*10) / 2
		x1 = delta + (x1*10) / 2
		can.create_line(y1,x1,y2,x2, width=2, fill="blue")
		y1+=1
		y2+=1	

def onUnlock():
	myo.unlock("hold")
	print "Deverouiller"

def onEMG(data, test):
	global check

	if(check == "hauteur"):
		drawLineA(myo.getPitch(), "red", 450, True)
		
	
	else:
		if(check == "all"):
			a=75
			b=175	
			c=275
			d=375
			e=475
			f=575
			g=675
			h=775
		else:
			a=400
			b=400
			c=400
			d=400
			e=400
			f=400
			g=400
			h=400

		drawLineA(data[0] , "white",a, False)
		drawLineA(data[1] , "green", b, False)
		drawLineA(data[2] , "white", c, False)
		drawLineA(data[3] , "blue", d, False)
		drawLineA(data[4] , "white", e, False)
		drawLineA(data[5] , "yellow", f, False)
		drawLineA(data[6] , "white", g, False)
		drawLineA(data[7] , "orange", h, True)

	if(data[0]<0):
		print "error point negatif"

def onPoseEdge(pose, edge):
	print("Etat " + pose + " & :" + edge)	
	if (pose == 'rest') and (edge == 'on'):
		print("Statut : activer") 
	
