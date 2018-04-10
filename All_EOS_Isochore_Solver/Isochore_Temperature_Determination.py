#Author: Mark Corrigan
#Email : mark.corrigan1994@googlemail.com
#For Master of Physics Project at the University of Edinburgh

#
from tkinter import *
from EOS_iso_therm import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

#These arrays are so that I can cater for all the different eos's by simply appending the params to them.
isoparams1 = []
isoparams2 = []
thermparams1 = []
thermparams2 = []



##################################
#This is used to select the element
##################################
#Sets up a tkinter window
master = Tk()

#Title for the window
Label(master, text="Isochore Crossing Point Finder - MPhys Project",font='Helvetica 14 bold').grid(row=0)


#Labelling the materials - these labela are used in the graph and various windows
Label(master, text="Please enter a name for Material 1").grid(row=1,column=0)
Label(master, text="Please enter a name for Material 2").grid(row=2,column=0)

#Text box for the first material
mat1=StringVar(None)
mat1=Entry(master,width=20)
mat1.grid(row=1,column=1)

#Text Box for the second material
mat2 = StringVar(None)
mat2 = Entry(master,width=20)
mat2.grid(row=2,column=1)

#various checkbuttons that are made use of later on using if statements to save/show graphs
#note the .grid method snaps everything to a grid where you can specify the row or column of the box
var1 = IntVar()
Checkbutton(master, text="Tick if you want to plot all isochore-crossing graphs", variable=var1).grid(row=3)
var2 = IntVar()
Checkbutton(master, text="Tick if you want plots to be saved", variable=var2).grid(row=4)
var3 = IntVar()
Checkbutton(master, text="Tick if you want plots to be shown", variable=var3).grid(row=5)

#this little method defines an ok button that allows the window to close
def ok():
    master.quit()
    
       
#This sets the ok button to snap to the grid
button1 = Button(master, text="OK", command=ok).grid(row=9)

#This runs this window
master.mainloop()












##################
#This section allows the selection of the Equations of State that I want to use
#################

#Setting up a tkinter window
master = Tk()

#Labelling the boxes with the appropriate names, taking the material names from the entries earlier
#not using a value for a column puts them in the left hand side
Label(master, text="Isothermal EOS for "+mat1.get()).grid(row=0)
Label(master, text="Thermal EOS for "+mat1.get()).grid(row=1)
Label(master, text="Isothermal EOS for "+mat2.get()).grid(row=2)
Label(master, text="Thermal EOS for "+mat2.get()).grid(row=3)

#setting the selection for the isothermal eos for the first material
iso_eos1 = StringVar(master)
#Below is the default value of 'please select' 
iso_eos1.set("Please Select")
iso1 = OptionMenu(master, iso_eos1,"Holzapfel AP2","Birch-Murnaghan (3rd Order)","Vinet")
#here is the first place in which the column is implemented allowing it to snap to the right hand side of the window
iso1.grid(row=0,column=1)

#setting the selection for the thermal eos for the first material
therm_eos1 = StringVar(master)
therm_eos1.set("Please Select")
therm1 = OptionMenu(master, therm_eos1,"Thermal Pressure EOS","Mie-Grüneisen-Debye EOS","Constant αKT")
therm1.grid(row=1,column=1)


#setting the isothermal eos for the second material
iso_eos2 = StringVar(master)
iso_eos2.set("Please Select")
iso2 = OptionMenu(master, iso_eos2,"Holzapfel AP2","Birch-Murnaghan (3rd Order)","Vinet")
iso2.grid(row=2,column=1)

#setting the thermal eos for the second material
therm_eos2 = StringVar(master)
therm_eos2.set("Please Select")
therm2 = OptionMenu(master, therm_eos2,"Thermal Pressure EOS","Mie-Grüneisen-Debye EOS","Constant αKT")
therm2.grid(row=3,column=1)


#defining and setting the ok button
def ok():
    master.quit()
button1 = Button(master, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

#running this window
master.mainloop( )














###
#This whole next section is dedicated to the input of parameters, using a set of if statements to decide which parameters are relevant to which EOS
#######
'''
############
# Material 1
#############
'''
## Isothermal EOS

if iso_eos1.get() == "Holzapfel AP2":


#BASIC GUI FOR ENTERING PARAMS
	#Setting up a tkinter window
	app = Tk()
	#Labels for the parameters for AP2
	Label(app, text=mat1.get()+" - Holzapfel AP2",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Atomic Number (Z)").grid(row=1)
	Label(app, text="Number of atoms in a chemical formula (n)").grid(row=2)
	Label(app, text="Molar volume under standard conditions (Vo) Jbar^-1").grid(row=3)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko (kbar)").grid(row=4)
	Label(app, text="Pressure derivative of isothermalbulk modulus under standard conditions (K')").grid(row=5)
	
	#Set of text boxes for the parameters for AP2
	z1=StringVar(None)
	z1=Entry(app,width=10)
	z1.grid(row=1,column=1)

	n1=StringVar(None)
	n1=Entry(app,width=10)
	n1.grid(row=2,column=1)

	Vo1=StringVar(None)
	Vo1=Entry(app,width=10)
	Vo1.grid(row=3,column=1)

	Ko1=StringVar(None)
	Ko1=Entry(app,width=10)
	Ko1.grid(row=4,column=1)

	Kk1=StringVar(None)
	Kk1=Entry(app,width=10)
	Kk1.grid(row=5,column=1)
	#making an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	
	#running the window
	app.mainloop()

	#appending all the parameters to a list
	isoparams1.append(float(z1.get()))
	isoparams1.append(float(n1.get()))
	isoparams1.append(float(Vo1.get()))
	isoparams1.append(float(Ko1.get()))
	isoparams1.append(float(Kk1.get()))

elif iso_eos1.get() == "Birch-Murnaghan (3rd Order)":

	#setting up the window for the birch murnaghan 3rd order	
	app = Tk()
	#putting a title and label for the parameters
	Label(app, text=mat1.get()+" - Birch-Murnaghan (3rd Order)",font='Helvetica 14 bold').grid(row=0)

	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko").grid(row=2)
	Label(app, text="Pressure derivative of isothermal bulk modulus under standard conditions (K')").grid(row=3)

	#making text boxes for the parameters, they snap to the columns and rows specified using the .grid method
	Vo1=StringVar(None)
	Vo1=Entry(app,width=10)
	Vo1.grid(row=1,column=1)

	Ko1=StringVar(None)
	Ko1=Entry(app,width=10)
	Ko1.grid(row=2,column=1)

	Kk1=StringVar(None)
	Kk1=Entry(app,width=10)
	Kk1.grid(row=3,column=1)
	#making an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)
	#running this window
	app.mainloop()

	#appending the three parameters to a file
	isoparams1.append(float(Ko1.get()))
	isoparams1.append(float(Vo1.get()))
	isoparams1.append(float(Kk1.get()))

elif iso_eos1.get() == "Vinet":
	#setting up the window
	app = Tk()
	
	#labelling the window and the parameters
	Label(app, text=mat1.get()+" - Vinet",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko").grid(row=2)
	Label(app, text="Pressure derivative of isothermal bulk modulus under standard conditions (K')").grid(row=3)

	#setting up text boxes for the data, setting the column =1 so as they are on the right hand side of the window
	Vo1=StringVar(None)
	Vo1=Entry(app,width=10)
	Vo1.grid(row=1,column=1)

	Ko1=StringVar(None)
	Ko1=Entry(app,width=10)
	Ko1.grid(row=2,column=1)

	Kk1=StringVar(None)
	Kk1=Entry(app,width=10)
	Kk1.grid(row=3,column=1)

	#defining an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	#running this window
	app.mainloop()

	#Appending this all to an array that is used in calculating values later
	isoparams1.append(float(Ko1.get()))
	isoparams1.append(float(Vo1.get()))
	isoparams1.append(float(Kk1.get()))


#################
## Thermal EOS ##
#################
#Now doing the same as above except this time fot eht thermal equations of state
#################

if therm_eos1.get() == "Thermal Pressure EOS":
	#setting up the windows
	app = Tk()
	#labelling the window and setting up labels for the parameters
	Label(app, text=mat1.get()+" - Thermal Pressure EOS",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Thermal expansion coefficient K^(-1) (αo)").grid(row=2)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko").grid(row=3)
	Label(app, text="First derivative of isothermal bulk modulus with respect to temperature").grid(row=4)
	Label(app, text="Second Derivative of pressure with respect to Temperature, holding V constant").grid(row=5)

	#setting up text boxes for the various parameters, making sure they are snapped to the right hand side of the window by using column=1
	Vo_th1=StringVar(None)
	Vo_th1=Entry(app,width=10)
	Vo_th1.grid(row=1,column=1)

	ao1=StringVar(None)
	ao1=Entry(app,width=10)
	ao1.grid(row=2,column=1)

	Ko_th1=StringVar(None)
	Ko_th1=Entry(app,width=10)
	Ko_th1.grid(row=3,column=1)

	db_th1=StringVar(None)
	db_th1=Entry(app,width=10)
	db_th1.grid(row=4,column=1)

	d2p1=StringVar(None)
	d2p1=Entry(app,width=10)
	d2p1.grid(row=5,column=1)


	#defining and using an ok button to quit the window when needs be
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	#this part runs the window
	app.mainloop()
	
	#appending all of the parameters to an array which will be used later = note all the inputs are strings so need to be converted
	thermparams1.append(float(ao1.get()))
	thermparams1.append(float(Vo_th1.get()))
	thermparams1.append(float(Ko_th1.get()))
	thermparams1.append(float(db_th1.get()))
	thermparams1.append(float(d2p1.get()))

elif therm_eos1.get() == "Mie-Grüneisen-Debye EOS":
	
	#setting up this window
	app = Tk()
	#labelling the window and all of the parameters needed for this EOS
	Label(app, text=mat1.get()+" - Mie-Grüneisen-Debye EOS",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Number of atoms in a  formula unit (n)").grid(row=2)
	Label(app, text="Debye Temperature (θ)").grid(row=3)
	Label(app, text="q - dimensionless parameter").grid(row=4)
	Label(app, text="γ0 - Scaling constant for Grüneisen  parameter").grid(row=5)
	Label(app, text= "Number of atoms in the unit cell").grid(row=6)

	#Setting up text boxes for the parameters being used, snapping them to the right hand side of the window

	Vo_th1=StringVar(None)
	Vo_th1=Entry(app,width=10)
	Vo_th1.grid(row=1,column=1)

	n1=StringVar(None)
	n1=Entry(app,width=10)
	n1.grid(row=2,column=1)

	thta1=StringVar(None)
	thta1=Entry(app,width=10)
	thta1.grid(row=3,column=1)

	q1=StringVar(None)
	q1=Entry(app,width=10)
	q1.grid(row=4,column=1)

	gam0_1=StringVar(None)
	gam0_1=Entry(app,width=10)
	gam0_1.grid(row=5,column=1)

	unit1=StringVar(None)
	unit1=Entry(app,width=10)
	unit1.grid(row=6,column=1)
	
	#setting up an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=8,column=1,sticky=W,pady=4)
	
	#running this window
	app.mainloop()

	#appending all of these parameters to a list
	thermparams1.append(float(Vo_th1.get()))
	thermparams1.append(float(n1.get()))
	thermparams1.append(float(thta1.get()))
	thermparams1.append(float(q1.get()))
	thermparams1.append(float(gam0_1.get()))
	thermparams1.append(float(unit1.get()))


elif therm_eos1.get() == "Constant αKT":

	#This window is again defined using tkinter
	app = Tk()

	#Setting up the labels and title for the window
	Label(app, text=mat1.get()+" - Constant αKT",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Constant αKT").grid(row=1)
	
	#setting up a text box for the parameter
	akt1=StringVar(None)
	akt1=Entry(app,width=10)
	akt1.grid(row=1,column=1)

	#defining and setting an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)
	
	#running this window
	app.mainloop()

	#Appending this to a list
	thermparams1.append(float(akt1.get()))











###
#Now have to define the parameters for the isothermal and thermal equations of state for the second material in the system
###


#########
# Material 2
#########

## Isothermal EOS ##

if iso_eos2.get() == "Holzapfel AP2":

#BASIC GUI FOR ENTERING PARAMS

	#Setting up a tkinter window
	app = Tk()
	#Setting up labels for the window and all the parameters (snapped left in the window)
	Label(app, text=mat2.get()+" - Holzapfel AP2",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Atomic Number (Z)").grid(row=1)
	Label(app, text="Number of atoms in a chemical formula (n)").grid(row=2)
	Label(app, text="Molar volume under standard conditions (Vo) Jbar^-1").grid(row=3)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko (kbar)").grid(row=4)
	Label(app, text="Pressure derivative of isothermalbulk modulus under standard conditions (K')").grid(row=5)
	
	#Setting up text boxes for all the the different parameters
	z2=StringVar(None)
	z2=Entry(app,width=10)
	z2.grid(row=1,column=1)

	n2=StringVar(None)
	n2=Entry(app,width=10)
	n2.grid(row=2,column=1)

	Vo2=StringVar(None)
	Vo2=Entry(app,width=10)
	Vo2.grid(row=3,column=1)

	Ko2=StringVar(None)
	Ko2=Entry(app,width=10)
	Ko2.grid(row=4,column=1)

	Kk2=StringVar(None)
	Kk2=Entry(app,width=10)
	Kk2.grid(row=5,column=1)

	#Defining and setting an ok button for the bottom of the window
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	#running the window
	app.mainloop()


	#Appending all of these to a list
	isoparams2.append(float(z2.get()))
	isoparams2.append(float(n2.get()))
	isoparams2.append(float(Vo2.get()))
	isoparams2.append(float(Ko2.get()))
	isoparams2.append(float(Kk2.get()))


elif iso_eos2.get() == "Birch-Murnaghan (3rd Order)":
	

	#Setting up a window here to input all of these parameters
	app = Tk()
	#Labelling this window and then labelling all of the parameters needed
	Label(app, text=mat2.get()+" - Birch-Murnaghan (3rd Order)",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko").grid(row=2)
	Label(app, text="Pressure derivative of isothermal bulk modulus under standard conditions (K')").grid(row=3)

	#Setting up text boxes for the input of all of the different parameters
	Vo2=StringVar(None)
	Vo2=Entry(app,width=10)
	Vo2.grid(row=1,column=1)

	Ko2=StringVar(None)
	Ko2=Entry(app,width=10)
	Ko2.grid(row=2,column=1)

	Kk2=StringVar(None)
	Kk2=Entry(app,width=10)
	Kk2.grid(row=3,column=1)


	#Defining and setting an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	#Running this window
	app.mainloop()

	#appending all of these parameters to the correct list
	isoparams2.append(float(Ko2.get()))
	isoparams2.append(float(Vo2.get()))
	isoparams2.append(float(Kk2.get()))

elif iso_eos2.get() == "Vinet":
	
	#Setting up a window in tkinter
	app = Tk()
	
	#Labelling the window and the parameters needed for this set, snapping them to the left hand side of the window
	Label(app, text=mat2.get()+" - Vinet",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko").grid(row=2)
	Label(app, text="Pressure derivative of isothermal bulk modulus under standard conditions (K')").grid(row=3)

	#Setting a text-box for each of the parameters
	Vo2=StringVar(None)
	Vo2=Entry(app,width=10)
	Vo2.grid(row=1,column=1)

	Ko2=StringVar(None)
	Ko2=Entry(app,width=10)
	Ko2.grid(row=2,column=1)

	Kk2=StringVar(None)
	Kk2=Entry(app,width=10)
	Kk2.grid(row=3,column=1)

	#Defining and setting an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	#Running this window
	app.mainloop()

	#appending these parameters to a list
	isoparams2.append(float(Ko2.get()))
	isoparams2.append(float(Vo2.get()))
	isoparams2.append(float(Kk2.get()))

##Thermal EOS ####

if therm_eos2.get() == "Thermal Pressure EOS":
	
	#Setting up a window for all of this to work in
	app = Tk()
	#Labelling the window and the parameters used
	Label(app, text=mat2.get()+" - Thermal Pressure EOS",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Thermal expansion coefficient K^(-1) (αo)").grid(row=2)
	Label(app, text="Isothermal bulk modulus under standard conditions Ko").grid(row=3)
	Label(app, text="First Derivative of the Bulk Modulus with respect to Temperature").grid(row=4)
	Label(app, text="Second Derivative of pressure with respect to Temperature, holding V constant").grid(row=5)

	#Setting text boxes for the parameters
	Vo_th2=StringVar(None)
	Vo_th2=Entry(app,width=10)
	Vo_th2.grid(row=1,column=1)

	ao2=StringVar(None)
	ao2=Entry(app,width=10)
	ao2.grid(row=2,column=1)

	Ko_th2=StringVar(None)
	Ko_th2=Entry(app,width=10)
	Ko_th2.grid(row=3,column=1)

	db_th2=StringVar(None)
	db_th2=Entry(app,width=10)
	db_th2.grid(row=4,column=1)

	d2p2=StringVar(None)
	d2p2=Entry(app,width=10)
	d2p2.grid(row=5,column=1)


	#This defines and sets an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	#This runs the window
	app.mainloop()

	#Appending all of these parameters to a file
	thermparams2.append(float(ao2.get()))
	thermparams2.append(float(Vo_th2.get()))
	thermparams2.append(float(Ko_th2.get()))
	thermparams2.append(float(db_th2.get()))
	thermparams2.append(float(d2p2.get()))

elif therm_eos2.get() == "Mie-Grüneisen-Debye EOS":
	
	#Setting up a window
	app = Tk()
	#Setting up labels for the window and for the parameters
	Label(app, text=mat2.get()+" - Mie-Grüneisen-Debye EOS",font='Helvetica 14 bold').grid(row=0)
	Label(app, text="Zero Pressure Volume (Vo)").grid(row=1)
	Label(app, text="Number of atoms in a  formula unit (n)").grid(row=2)
	Label(app, text="Debye Temperature (θ)").grid(row=3)
	Label(app, text="q - dimensionless parameter").grid(row=4)
	Label(app, text="γ0 - Scaling constant for Grüneisen  parameter").grid(row=5)
	Label(app,text="Number of atoms in the unit cell").grid(row=6)


	#Setting up textboxes for the parameters, snapping them to the RHS of the window
	Vo_th2=StringVar(None)
	Vo_th2=Entry(app,width=10)
	Vo_th2.grid(row=1,column=1)

	n2=StringVar(None)
	n2=Entry(app,width=10)
	n2.grid(row=2,column=1)

	thta2=StringVar(None)
	thta2=Entry(app,width=10)
	thta2.grid(row=3,column=1)

	q2=StringVar(None)
	q2=Entry(app,width=10)
	q2.grid(row=4,column=1)


	gam0_2=StringVar(None)
	gam0_2=Entry(app,width=10)
	gam0_2.grid(row=5,column=1)

	unit2 = StringVar(None)
	unit2 = Entry(app,width=10)
	unit2.grid(row=6,column = 1)

	#Defining and setting an ok button that will close the window
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)

	#Running this window
	app.mainloop()

	#Appending all of these parameters to a list that can be used
	thermparams2.append(float(Vo_th2.get()))
	thermparams2.append(float(n2.get()))
	thermparams2.append(float(thta2.get()))
	thermparams2.append(float(q2.get()))
	thermparams2.append(float(gam0_2.get()))
	thermparams2.append(float(unit2.get()))

elif therm_eos2.get() == "Constant αKT":

	#Setting up this window in tkinter 	
	app = Tk()
	
	#labelling the parameter
	Label(app, text="Constant αKT").grid(row=0)

	#Taking the input for the parameter
	akt2=StringVar(None)
	akt2=Entry(app,width=10)
	akt2.grid(row=0,column=1)

	#Defining and setting an ok button
	def ok():
		app.quit()
	button1 = Button(app, text="OK", command=ok).grid(row=7,column=1,sticky=W,pady=4)


	#running the window
	app.mainloop()
	
	#Appending the parameter to a file
	thermparams2.append(float(akt2.get()))


















###
#This litte part allows for the import of the volumes used in the determination of the crossing point. It pops up a little file browser window that allows for the selection of any file. Text files are needed
###

app = Tk()
app.filename1 =  filedialog.askopenfilename(title = "Please select the volumes for"+ mat1.get())
app.filename2 = filedialog.askopenfilename(title = "Please select the volumes for "+ mat2.get())


######
#The method above only returns the location of the files, this needs then to be used to return the files themselves
#####

#opening the first file, reading each line as a value
with open(app.filename1) as f:
    vol1 = f.readlines()
#converting all of the volumes to floats s they are inputted as strings
for i in range(len(vol1)):
	vol1[i] = float(vol1[i])
#converting the list to a numpy array for faster and easier processing
vol1 = np.array(vol1)

#opening the second file, reading each line as a value
with open(app.filename2) as f:
    vol2 = f.readlines()
#converting all of the values to a float as they are read in as a string
for i in range(len(vol2)):
	vol2[i] = float(vol2[i])
#converting the listto a numpy array for faster and easier processing
vol2 = np.array(vol2)












##########################################################
#Inputting the errors - This section allows for user input of errors if need be
##########################################################

#This sets up the tkinter window for input of user errors
error = Tk()

#Labelling the window and the drop down menu
Label(error, text="Error Analysis",font='Helvetica 14 bold').grid(row=0)
Label(error, text="Please select").grid(row=2)

#defining the drop down menu with the type of error needed
error_type = StringVar(error)
error_type.set("--") # initial value
option_err = OptionMenu(error, error_type,"No errors needed","Errors are constant","Errors are variable").grid(row=2,column=1)

#defining the ok button to close this window
def ok1():
    error.quit()
Button(error, text='OK', command=ok1).grid(row=6, column=0, sticky=W, pady=4)
error.mainloop()


#if the user has selected 'errprs' are constant then this window pops up. This error is prevalent in some static experiments - Notably in Dewaele's 'Equations of State of 6 Metals above 94GPa' where she states the uncertainty on each volume as 0.01 angstroms^3/atom
if error_type.get() == "Errors are constant":

	#This window is defined here, again a tkinter window
	constant = Tk()
	#Labelling the window and the text boxes
	Label(constant,text="Enter constant errors",font='Helvetica 14 bold').grid(row=0)
	Label(constant, text="Enter the error for "+ mat1.get()).grid(row=1)
	Label(constant, text="Enter the error for "+ mat2.get()).grid(row=2)
	#making the text boxes and snapping them to the grid

	err0 = Entry(constant)
	err1 = Entry(constant)
	err0.grid(row=1, column=1)
	err1.grid(row=2, column =1)
	#defining an ok button to close this window when needs be
	def ok1():
		constant.quit()
	Button(constant, text='OK', command=ok1).grid(row=6, column=0, sticky=W, pady=4)


	#running this window
	constant.mainloop()

	#if the error is constant then when calculating the error (Using the method in the report from Squires-Practical Physics) we need the error for every volume in the list of volumes - hence here I create an empty list the same length as the list of volumes and then fill it with the constant error for each material as specified in the window.
	errlst0 = np.zeros(len(vol1))
	errlst1 = np.zeros(len(vol1))
	errlst0 = [float(err0.get()) for i in range(len(vol1))]
	errlst1 = [float(err1.get()) for i in range(len(vol1))]


#The second option that was the errors are variable for each volume - this is seen for example in Litasov's Equation of state of Molybdenum where there is an error quoted on each measurement

if error_type.get() == "Errors are variable":

	#In this case we need to import a file which has the errors on the values. This uses the same system as the the import of the volume data in the first instance where the tkinter window opens a file browser for the error on each material

	rooterror1 = Tk()
	rooterror1.filename = filedialog.askopenfilename(title = "Select Errors for "+ mat1.get())

	rooterror2 = Tk()
	rooterror2.filename = filedialog.askopenfilename(title = "Select Errors for "+ mat2.get())


	#again the above method only returns the location of the files, so they actually need to be imported. The program imports the file line by line, converts them to a float and then finally to a numpy array for easy use
	with open(rooterror1.filename) as f:
		errlst0 = f.readlines()
		errlst0=np.array([float(errlst0[i]) for i in range(len(errlst0))])

	with open(rooterror2.filename) as g:
		errlst1 = g.readlines()
		errlst1=np.array([float(errlst1[i]) for i in range(len(errlst1))])


#This section below is slightly long-winded but is necessary as it allows a conversion from the selection of the isothermal and thermal Equations of state from earlier to a string which is the name of the method in EOS_iso_therm and hence allows the calculation of pressure

if iso_eos1.get() =="Holzapfel AP2":
	iso1='AP2'
elif iso_eos1.get() == "Birch-Murnaghan (3rd Order)":
	iso1 = 'BM3'
elif iso_eos1.get() == "Vinet":
	iso1 = 'Vinet'

if iso_eos2.get() =="Holzapfel AP2":
	iso2='AP2'
elif iso_eos2.get() == "Birch-Murnaghan (3rd Order)":
	iso2 = 'BM3'
elif iso_eos2.get() == "Vinet":
	iso2 = 'Vinet'

if therm_eos1.get() == "Thermal Pressure EOS":
	therm1 = 'thermal_Pressure'
elif therm_eos1.get() == "Mie-Grüneisen-Debye EOS":
	therm1 = 'Mie_gruinisen'
elif therm_eos1.get() ==  "Constant αKT":
	therm1 = 'simple'

if therm_eos2.get() == "Thermal Pressure EOS":
	therm2 = 'thermal_Pressure'
elif therm_eos2.get() == "Mie-Grüneisen-Debye EOS":
	therm2 = 'Mie_gruinisen'
elif therm_eos2.get() ==  "Constant αKT":
	therm2 = 'simple'







##This set of if statements allows the calculation of the errors using the squires method as described in the report. If the user has selected that there are are errors in the data then we need a set of volumes which are the original volume added to the error. Otherwise we set this to the original volume and it will not be used further

if error_type.get() != "No errors needed":
	volerr0 = vol1+errlst0
	volerr1 = vol2+errlst1
if error_type.get() == "No errors needed":
	volerr0 = vol1
	volerr1 = vol2




#This function calls the temperature guess method which can return the guesses for temperature and the values of the error bars used in the plots - these are redundant if there are no errors selected

temp_guess,y1_error,y2_error = temp().temp_guess_fcn(vol1,vol2,isoparams1,isoparams2,thermparams1,thermparams2,iso1,iso2,therm1,therm2,error_type.get(),volerr0,volerr1)



#### Here the program outputs the estimates for the temperatur to the terminal (finally...) ###

print('The estimates for the temperature are \n')

print(temp_guess)






#If the user has selected some sort of error then we have to calculate the uncertainties in the measurements

if error_type.get() != "No errors needed":
	#I calculate the temperature using the volume with the error included for the first set of volumes, where the second and third outputs are redundant in this case but have to still be named hence 'na' and 'na1'
	error1,na,na1 = temp().temp_guess_fcn(volerr0,vol2,isoparams1,isoparams2,thermparams1,thermparams2,iso1,iso2,therm1,therm2,error_type.get(),volerr0,volerr1)

	#I calculate the temp here for the volume with the error included for the second set of volumes where again the second and third outputs are redundant, but still have to be named hence 'na' and 'na1'
	error2,na,na1 = temp().temp_guess_fcn(vol1,volerr1,isoparams1,isoparams2,thermparams1,thermparams2,iso1,iso2,therm1,therm2,error_type.get(),volerr0,volerr1)

	#Calculating the error due to the error on the first set of volumes
	error_due1 = (np.array(temp_guess)-np.array(error1))

	#Calculating the error due to the error on the second set of volumes
	error_due2 = (np.array(temp_guess)-np.array(error2))

	#combining the errors in quadrature and taking the square root
	error_tot = np.sqrt(error_due1**2+error_due2**2)

	#Printing these errors out to the terminal
	print('\n\n\n'+'The uncertainties on these measurements are: ')
	print(list(error_tot))








#This section is only run if the user is interested in the graphs of the isochores


if var1.get() == 1:
###################################################
#Linear Regression
##################################################

	#the getattr function allows for the calling of a function using a string, you can't just call it normally. So below what is happening is I am essentially calling isothermal().iso1 and renaming it p_iso1 where iso1 will be the isothermal equation of state for the first material. This is repeated for the other 3 equations of state

	p_iso1 = getattr(isothermal(),iso1)
	p_iso2 = getattr(isothermal(),iso2)
	p_therm1 = getattr(thermal(),therm1)
	p_therm2 = getattr(thermal(),therm2)




	#When I am plotting the graphs I need to centre them around the discovered temperature, this results in a recalculation of the pressures around the crossing point. The empty arrays y1 and y2 hold this data
	y1=[]
	y2 = []

	# I also need to plot the data over a specified temperature range - this is held (unsurprisingly) in the 'temp_range' array
	temp_range =[]

	#iterating over the whole list of volumes
	for i in range(len(vol1)):
	
		#The temperature range which I decided to plot everything is +/- half of the temperature guess in 20K increments
		temp_range.append(range(int(temp_guess[i]-(temp_guess[i]/2)-10),int(temp_guess[i]+(temp_guess[i]/2)+10),20))

		#Initialise the arrays which hold the list of pressures for a given volume, they are zero'd every loop.
		P_tot_0 = np.zeros(len(temp_range[i]))
		P_tot_1 = np.zeros(len(temp_range[i]))

			
	
		#############################################################
		#Material1
		############################################################


		#Calculating the isothermal pressure for the current volume in the loop, using the set of parameters the user has chosen
		Px_0 = p_iso1(vol1[i],isoparams1)
		

		#Calculating the thermal pressure over the total range of temperature that is going to be plotted
		for j in range(len(temp_range[i])):
			#pthermal
			Pthermal_0 = p_therm1(temp_range[i][j],vol1[i],thermparams1)

			#Adding the current total pressure to the list, this happens for the range of temperatures
			P_tot_0[j] = Px_0+Pthermal_0

		#This list of pressures is then appended as an element in the y1 list
		y1.append(P_tot_0)

		##################################################################
		#Material2
		#############################################################

		#Calculating the isothermal pressures for the current volume in the loop for the second material using the set of parameters that the user has chosen
		Px_1 = p_iso2(vol2[i],isoparams2)

		#Calculating the thermal pressure over the total range of temperatures that is going to be plotted for material 2
		for j in range(len(temp_range[i])):

			
			#Thermal Pressure
			Pthermal_1 = p_therm2(temp_range[i][j],vol2[i],thermparams2)
			#Adding the current total pressure to the list, this happens for the range of temperatures
			P_tot_1[j] = Px_1+Pthermal_1

		#This list of pressures is then appended to an element in the y2 list
		y2.append(P_tot_1)



	#Plotting the results
	

	#we do this for the list of volumes

	for i in range(len(vol1)):

		#Againg plotting in the range +/- half the estimated temperature
		x=range(int(temp_guess[i]-(temp_guess[i]/2)-10),int(temp_guess[i]+(temp_guess[i]/2)+10),20)

		#The program has to differentiate between plots with and without error bars
		if error_type.get() != "No errors needed":
			
			#For the plots with error bars this method allows them to look ok on the graph, whilst also plotting the points
			(_, caps0, _) = plt.errorbar(x,y1[i],marker='x',label = mat1.get()+' data', color = 'blue',yerr = y1_error[i], capsize=5, elinewidth=1)
			for cap in caps0:
			    cap.set_color('blue')
			    cap.set_markeredgewidth(1)


			(_, caps1, _) = plt.errorbar(x,y2[i],marker='x',label = mat2.get()+' data', color = 'red',yerr = y2_error[i], capsize=5, elinewidth=1)


			for cap in caps1:
			    cap.set_color('red')
			    cap.set_markeredgewidth(1)
			

		#If no errors are selected then this 'else' statement comes into effect, essentially plotting the same thing as above just without error bars
		else:
			plt.errorbar(x,y1[i],marker='x',label = mat1.get()+' data', color = 'blue')
			plt.errorbar(x,y2[i],marker = 'x',label = mat2.get()+' data',color = 'red' )
		plt.title('Plot of P vs T of '+ mat1.get()+ ' and '+ mat2.get()+ ', V'+r'$_{'+str(mat1.get())+'}$'+'='+str(vol1[i])[:-1]+ ' (Å/at)'+', V'+r'$_{'+str(mat2.get())+'}$'+'='+str(vol2[i])[:-1]+ ' (Å/at)')
		




		#If there are errors then the plot specifies where they cross in text in the graph and the error in this value
		if error_type.get() != "No errors needed":
			plt.text(min(x), max(y1[i]),'Lines cross at T= '+str(temp_guess[i])[0:8]+r'$\pm$'+str(error_tot[i])[0:8]+' K')

		#Otherwise it just specifies where they cross
		else:
			plt.text(min(x), max(y1[i]),'Lines cross at T= '+str(temp_guess[i])[0:8]+' K')

		
		#Location 4 for the legend it bottom right
		plt.legend(loc=4)
		#Labeling the axes
		plt.ylabel("Pressure/GPa")
		plt.xlabel("Temperature/K")	

		#If the user has ticked to see the graphs then they are shown using this if statement
		if var3.get() ==1:
			plt.show()

		#If the user has ticket to save the graphs then this if statement is used. Where they are labelled appropriately
		if var2.get() ==1:
			plt.savefig(mat1.get()+mat2.get()+str((vol1[i]))[:-1]+str((vol2[i]))[:-1]+"_Temperature.pdf")

		plt.close()





