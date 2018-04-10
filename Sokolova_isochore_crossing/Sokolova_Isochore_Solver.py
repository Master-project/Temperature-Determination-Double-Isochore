#####
#Author - Mark Corrigan
#Email - mark.corrigan1994@googlemail.com
#MPhys Project 2017/18
#####

#Importing all of the packages needed to run this program

from EoSeqns import EoSeqns
import math
from tkinter import * 
from tkinter import filedialog
import pandas as pd
import numpy as np
import sys 
import matplotlib.pyplot as plt


#Uo,n,Vo,Ko,kk,QE1,m1,QE2,m2,δ,t,ao,eo,m,g,co,с2,Z,temp_0 and number of atoms in unit cell is the order of the data in the following arrays

#The data for these values is taken from the Spreadsheets provided by sokolova et al (DOI : 10.1016/j.cageo.2016.06.002)

#Explanations of the values and their names is also available in this paper


#Ag
Ag=[0,1,1.025,1000,6.15,115,1.5,199,1.5,0.178,2.21,0,22.1,0,0.19,3.75,0.98,47,298.15,4]

#Al
Al=[0,1,0.998,728,4.51,381,1.5,202,1.5,-0.242,-0.958,0,64.1,0,0.33,1.97,0.3,13,298.15,4]


#Au
Au=[0,1,1.0215,1670,5.9,179.5,1.5,83,1.5,0.134,0.087,0,0,0,0,4.1,0.25,79,298.15,4]


#Diamond (C)
C=[1290,1,0.34141,4415,3.9,684,0.564,1561,2.436,-0.506,1.085,0,0,0,0,0.66,0.68,6,298.15,8]

#Copper 
Cu=[0,1,0.7112,1335,5.32,296,1.5,169,1.5,-0.07,1.401,0,27.7,0,2.18,3.26,0.22,29,298.15,4]

#Periclase MgO
MgO=[0,2,1.1248,1603,4.1,748,3,401,3,-0.235,0.301,-17.4,0,4.95,0,1.75,-0.1,10.34,298.15,4]

#Mo
Mo=[0,1,0.9369,2600,4.2,353,1.5,222,1.5,-0.802,-0.791,0,143.2,0,2.66,2.75,-0.95,42,298.15,2]


#Nb
Nb=[0,1,1.0828,1705,3.65,134,1.5,302,1.5,-0.326,-0.763,0,115.9,0,0.9,2.89,-1.92,41,298.15,2]

#Pt 
Pt=[0,1,0.9091,2750,5.35,177,1.5,143,1.5,0.167,-0.343,0,80.6,0,0.06,3.78,-0.25,78,298.15,4]


#Ta
Ta=[0,1,1.0861,1910,3.83,254,1.5,101,1.5,-0.101,-0.148,0,82.3,0,0.12,3.74,-2.49,73,298.15,2]

#W
Tung=[0,1,0.9552,3080,4.12,172,1.5,309,1.5,-0.686,-0.591,0,100.1,0,2.77,3.49,-1.81,74,298.15,2]


############
#This is used to select the first material
############

#setting up the tkinter window
master = Tk()

#labelling the window
Label(master, text="Select two different materials to compare",font='Helvetica 14 bold').grid(row=0)
Label(master, text="Material 1").grid(row=1)
Label(master, text="Material 2").grid(row=2)

#initialising various tick boxes for use later
var1 = IntVar()
Checkbutton(master, text="Tick if you want to plot all isochore-crossing graphs", variable=var1).grid(row=3)
var2 = IntVar()
Checkbutton(master, text="Tick if you want plots to be saved", variable=var2).grid(row=4)
var3 = IntVar()
Checkbutton(master, text="Tick if you want plots to be shown", variable=var3).grid(row=5)


#setting initial null values for the materials
inmat = StringVar(master)
inmat.set("--") # initial value
inmat1 = StringVar(master)
inmat1.set("--") # initial value

#giving a list of materials available
option = OptionMenu(master, inmat,"Ag","Al","Au","C","Cu","MgO","Mo","Nb","Pt","Ta","W","Custom Parameters").grid(row=1,column=1)

option2 = OptionMenu(master, inmat1,"Ag","Al","Au","C","Cu","MgO","Mo","Nb","Pt","Ta","W","Custom Parameters").grid(row=2,column=1)

#defining an ok button which can close the window when necessary
def ok():
    master.quit()
       
#fitting the ok button to the window
button1 = Button(master, text="OK", command=ok).grid(row=9)

#running the window
master.mainloop()

###############
#The next few lines of code allow the user to open files which contain the volumes used in the determination of temperature (given in angstroms^3 per atom)
################


root1 = Tk()
root1.filename = filedialog.askopenfilename(title = "Select Volumes for "+str(inmat.get()))

root2 = Tk()
root2.filename = filedialog.askopenfilename(title = "Select Volumes for "+str(inmat1.get()))

####
#Once these have been seelcted they are processed by the program and inputted into arrays
###


with open(root1.filename) as f:
    vol0 = f.readlines()
    vol0 = [float(vol0[i]) for i in range(len(vol0))]
    vol0 = np.array(vol0)

with open(root2.filename) as g:
    vol1 = g.readlines()
    vol1=[float(vol1[i]) for i in range(len(vol1))]
    vol1 = np.array(vol1)





#This program also allows the user to input errors into the measurements if needed, these again are implemented using Tkinter and need to be given in angstroms^3 per atom


#defining the tkinter window
error = Tk()

#titling the window and the dropdown menu
Label(error, text="Error Analysis",font='Helvetica 14 bold').grid(row=0)
Label(error, text="Please select").grid(row=2)

#giving the options for the user
error_type = StringVar(error)
error_type.set("--") # initial value
option_err = OptionMenu(error, error_type,"No errors needed","Errors are constant","Errors are variable").grid(row=2,column=1)

#defining an ok button that can be used to close the window
def ok1():
    error.quit()

#placing the ok button on the window
Button(error, text='OK', command=ok1).grid(row=6, column=0, sticky=W, pady=4)

#running the window
error.mainloop()


#if the errors are constant for both materials then the user can simply imput them into a window which is opened if the proper condition is satisfied
if error_type.get() == "Errors are constant":

	#this is the window used to enter errors
	constant = Tk()
	Label(constant,text="Enter constant errors",font='Helvetica 14 bold').grid(row=0)
	Label(constant, text="Enter the error for " +inmat.get()).grid(row=1)
	Label(constant, text="Enter the error for " +inmat1.get()).grid(row=2)

	err0 = Entry(constant)
	err1 = Entry(constant)	
	#the boxes are snapped to a grid
	err0.grid(row=1, column=1)
	err1.grid(row=2, column =1)

	#defining an ok button to close the window when needed
	def ok1():
		constant.quit()

	#Setting the ok button to the correct place in the window
	Button(constant, text='OK', command=ok1).grid(row=6, column=0, sticky=W, pady=4)


	#Running the window
	constant.mainloop()

	#making and filling the lists of errors
	errlst0 = np.zeros(len(vol0))
	errlst1 = np.zeros(len(vol0))
	errlst0 = [float(err0.get()) for i in range(len(vol0))]
	errlst1 = [float(err1.get()) for i in range(len(vol0))]

#if the Errors are specified as variable then the user can select a file which will have a list of errors in it, again these errors will be given in angstroms^3 per atom

if error_type.get() == "Errors are variable":

	#They are selected using a tkinter standard dialog box

	rooterror1 = Tk()
	rooterror1.filename = filedialog.askopenfilename(title = "Select Errors for "+str(inmat.get()))

	rooterror2 = Tk()
	rooterror2.filename = filedialog.askopenfilename(title = "Select Errors for "+str(inmat1.get()))

	#They are then analysed and made into arrays of errors so as they can be used later

	with open(rooterror1.filename) as f:
		errlst0 = f.readlines()
		errlst0=np.array([float(errlst0[i]) for i in range(len(errlst0))])

	with open(rooterror2.filename) as g:
		errlst1 = g.readlines()
		errlst1=np.array([float(errlst1[i]) for i in range(len(errlst1))])
		

###########################################
#This section deals with sorting what is needed for material 1
########################################

#This while loop allows the user to select the first material from the list of materials given in the sokolova spreadsheets or a custom material

test1=1
custtest= 0
while test1==1:


	if inmat.get() == 'Ag':
		material_0 =Ag
		test1=2
	elif inmat.get() == 'Al':
		material_0 =Al
		test1=2
	elif inmat.get() =='Au':
		material_0 =Au
		test1=2
	elif inmat.get() =='C':
		material_0 =C
		test1=2
	elif inmat.get() =='Cu':
		material_0 =Cu
		test1=2
	elif inmat.get() =='MgO':
		material_0 = MgO
		test1=2
	elif inmat.get() =='Mo':
		material_0 = Mo
		test1=2
	elif inmat.get() =='Nb':
		material_0 = Nb
		test1=2
	elif inmat.get() =='Pt':
		material_0 = Pt
		test1=2
	elif inmat.get() =='Ta':
		material_0 = Ta
		test1=2
	elif inmat.get() =='W':
		material_0 = Tung
		test1=2
	elif inmat.get() =='Custom Parameters':
		material_0= custom
		custtest = 1
		test1 = 2






###########################
# If there is a custom material needed for material_1 then the if statement below is triggered and the user has to enter in all of the parameters needed for a given material.
###########################

#custom inputs
if custtest == 1:


	master2 = Tk()
	Label(master2, text="The reference energy (Jmol^-1), Uo ").grid(row=0)
	Label(master2, text="Number of atoms in a chemical formula, n").grid(row=1)
	Label(master2, text="Molar volume under standard conditions  (Jbar^-1), Vo").grid(row=2)
	Label(master2, text="Isothermal bulk modulus under standard conditions (kbar), Ko").grid(row=3)
	Label(master2, text="Pressure derivative of isothermal bulk modulus under standard conditions, equal K',kk").grid(row=4)
	Label(master2, text="The Einstein characteristic temperature, equal Θ_01 (K), QE1").grid(row=5)
	Label(master2, text="The Einstein number, m1").grid(row=6)
	Label(master2, text="The Einstein characteristic temperature, equal Θ_02 (K), QE2").grid(row=7)
	Label(master2, text="The Einstein number, m2").grid(row=8)
	Label(master2, text="Additive normalizing constant, δ").grid(row=9)
	Label(master2, text="Generalized Grüneisen parameter, t").grid(row=10)
	Label(master2, text="Intrinsic anharmonicity parameter (10^-6 K^-1), ao").grid(row=11)
	Label(master2, text="Free electrons parameter (10^-6 K^-1),eo").grid(row=12)
	Label(master2, text="Anharmonic analogue of the Grüneisen parameter, m").grid(row=13)
	Label(master2, text="Electronic analogue of the Grüneisen parameter, g").grid(row=14)
	Label(master2, text="Parameter of the Holzapfel EoS, co").grid(row=15)
	Label(master2, text="Parameter of the Holzapfel EoS, c2").grid(row=16)
	Label(master2, text="Temperature of the reference isotherm (K),To").grid(row=17)
	Label(master2, text="Atomic number, Z").grid(row=18)
	Label(master2, text="Number of atoms in unit cell").grid(row=19)


	Uo = Entry(master2)
	n = Entry(master2)
	Vo = Entry(master2)
	Ko = Entry(master2)
	kk = Entry(master2)
	QE1 = Entry(master2)
	m1 = Entry(master2)
	QE2 = Entry(master2)
	m2 = Entry(master2)
	delta = Entry(master2)
	t = Entry(master2)
	ao = Entry(master2)
	eo = Entry(master2)
	m = Entry(master2)
	g = Entry(master2)
	co = Entry(master2)
	c2 = Entry(master2)
	To = Entry(master2)
	Z = Entry(master2)
	atom = Entry(master2)



	Uo.grid(row=0, column=1)
	n.grid(row=1, column=1)
	Vo.grid(row=2, column=1)
	Ko.grid(row=3, column=1)
	kk.grid(row=4, column=1)
	QE1.grid(row=5, column=1)
	m1.grid(row=6, column=1)
	QE2.grid(row=7, column=1)
	m2.grid(row=8, column=1)
	delta.grid(row=9, column=1)
	t.grid(row=10, column=1)
	ao.grid(row=11, column=1)
	eo.grid(row=12, column=1)
	m.grid(row=13, column=1)
	g.grid(row=14, column=1)
	co.grid(row=15, column=1)
	c2.grid(row=16, column=1)
	To.grid(row=17, column=1)
	Z.grid(row=18, column=1)
	atom.grid(row=19,column=1)


	#This defines an ok button to close the window
	def ok2():
		master2.quit()
	


	#This ok button is then attached to the window
	Button(master2, text='OK', command=ok).grid(row=20, column=0, sticky=E, pady=4)

	#The tkinter window is run using this loop
	master2.mainloop()


	#These values are then appended to a list for use later if needed
	material_0.append(float(Uo.get()))
	material_0.append(float(n.get()))
	material_0.append(float(Vo.get()))
	material_0.append(float(Ko.get()))
	material_0.append(float(kk.get()))
	material_0.append(float(QE1.get()))
	material_0.append(float(m1.get()))
	material_0.append(float(QE2.get()))
	material_0.append(float(m2.get()))
	material_0.append(float(delta.get()))
	material_0.append(float(t.get()))
	material_0.append(float(ao.get()))
	material_0.append(float(eo.get()))
	material_0.append(float(m.get()))
	material_0.append(float(g.get()))
	material_0.append(float(co.get()))
	material_0.append(float(c2.get()))
	material_0.append(float(Z.get()))
	material_0.append(float(To.get()))
	material_0.append(float(atom.get()))


#####################################################
#Now to do the same preparation for the second element.
#####################################################

##This while loop allows for the selection of materials for the second material from the list of materials given in the sokolova spreadsheets
test1=1
custtest= 0
while test1==1:

	if inmat1.get() == 'Ag':
		material_1 =Ag
		test1=2
	elif inmat1.get() == 'Al':
		material_1 =Al
		test1=2
	elif inmat1.get() =='Au':
		material_1 =Au
		test1=2
	elif inmat1.get() =='C':
		material_1 =C
		test1=2
	elif inmat1.get() =='Cu':
		material_1 =Cu
		test1=2
	elif inmat1.get() =='MgO':
		material_1 = MgO
		test1=2
	elif inmat1.get() =='Mo':
		material_1 = Mo
		test1=2
	elif inmat1.get() =='Nb':
		material_1 = Nb
		test1=2
	elif inmat1.get() =='Pt':
		material_1 = Pt
		test1=2
	elif inmat1.get() =='Ta':
		material_1 = Ta
		test1=2
	elif inmat1.get() =='W':
		material_1 = Tung
		test1=2
	elif inmat1.get() =='Custom Parameters':
		material_1= custom
		custtest = 1
		test1 = 2


########################
# If a custom material is selected for the second material then one needs to input all of the parameters associated with this material so as it can be used
#########################

#custom inputs
if custtest == 1:


	master2 = Tk()
	Label(master2, text="The reference energy (Jmol^-1), Uo ").grid(row=0)
	Label(master2, text="Number of atoms in a chemical formula, n").grid(row=1)
	Label(master2, text="Molar volume under standard conditions  (Jbar^-1), Vo").grid(row=2)
	Label(master2, text="Isothermal bulk modulus under standard conditions (kbar), Ko").grid(row=3)
	Label(master2, text="Pressure derivative of isothermal bulk modulus under standard conditions, equal K',kk").grid(row=4)
	Label(master2, text="The Einstein characteristic temperature, equal Θ_01 (K), QE1").grid(row=5)
	Label(master2, text="The Einstein number, m1").grid(row=6)
	Label(master2, text="The Einstein characteristic temperature, equal Θ_02 (K), QE2").grid(row=7)
	Label(master2, text="The Einstein number, m2").grid(row=8)
	Label(master2, text="Additive normalizing constant, δ").grid(row=9)
	Label(master2, text="Generalized Grüneisen parameter, t").grid(row=10)
	Label(master2, text="Intrinsic anharmonicity parameter (10^-6 K^-1), ao").grid(row=11)
	Label(master2, text="Free electrons parameter (10^-6 K^-1),eo").grid(row=12)
	Label(master2, text="Anharmonic analogue of the Grüneisen parameter, m").grid(row=13)
	Label(master2, text="Electronic analogue of the Grüneisen parameter, g").grid(row=14)
	Label(master2, text="Parameter of the Holzapfel EoS, co").grid(row=15)
	Label(master2, text="Parameter of the Holzapfel EoS, c2").grid(row=16)
	Label(master2, text="Temperature of the reference isotherm (K),To").grid(row=17)
	Label(master2, text="Atomic number, Z").grid(row=18)
	Label(master2, text="Number of atoms in unit cell").grid(row=19)


	Uo = Entry(master2)
	n = Entry(master2)
	Vo = Entry(master2)
	Ko = Entry(master2)
	kk = Entry(master2)
	QE1 = Entry(master2)
	m1 = Entry(master2)
	QE2 = Entry(master2)
	m2 = Entry(master2)
	delta = Entry(master2)
	t = Entry(master2)
	ao = Entry(master2)
	eo = Entry(master2)
	m = Entry(master2)
	g = Entry(master2)
	co = Entry(master2)
	c2 = Entry(master2)
	To = Entry(master2)
	Z = Entry(master2)
	atom = Entry(master2)


	#snapping the boxes to a grid
	Uo.grid(row=0, column=1)
	n.grid(row=1, column=1)
	Vo.grid(row=2, column=1)
	Ko.grid(row=3, column=1)
	kk.grid(row=4, column=1)
	QE1.grid(row=5, column=1)
	m1.grid(row=6, column=1)
	QE2.grid(row=7, column=1)
	m2.grid(row=8, column=1)
	delta.grid(row=9, column=1)
	t.grid(row=10, column=1)
	ao.grid(row=11, column=1)
	eo.grid(row=12, column=1)
	m.grid(row=13, column=1)
	g.grid(row=14, column=1)
	co.grid(row=15, column=1)
	c2.grid(row=16, column=1)
	To.grid(row=17, column=1)
	Z.grid(row=18, column=1)
	atom.grid(row=19,column=1)


	#defining an ok button so as the window can be closed
	def ok2():
		master2.quit()
	


	#snapping the button to the window 
	Button(master2, text='OK', command=ok).grid(row=20, column=0, sticky=E, pady=4)


	#running the window
	master2.mainloop()


	#Appending all of the values inputted to a list - note that they need to be made into floats as tkinter inputs strings as standard.

	material_1.append(float(Uo.get()))
	material_1.append(float(n.get()))
	material_1.append(float(Vo.get()))
	material_1.append(float(Ko.get()))
	material_1.append(float(kk.get()))
	material_1.append(float(QE1.get()))
	material_1.append(float(m1.get()))
	material_1.append(float(QE2.get()))
	material_1.append(float(m2.get()))
	material_1.append(float(delta.get()))
	material_1.append(float(t.get()))
	material_1.append(float(ao.get()))
	material_1.append(float(eo.get()))
	material_1.append(float(m.get()))
	material_1.append(float(g.get()))
	material_1.append(float(co.get()))
	material_1.append(float(c2.get()))
	material_1.append(float(Z.get()))
	material_1.append(float(To.get()))
	material_1.append(float(atom.get()))


###############################################################################
#Now that all of the data has been entered for these materials one can start to determine the temperature
###############################################################################


#This is the temperature determination algorithm that is given in Appendix A of the report

#It takes in the volume lists of material 1 and 2 and also the parameter lists of material 1 and material 2

def temp_guess_fcn(vol0,vol1,material_0,material_1):
	
	#The temperature guess for each pair of volumes is initialy set to 100K
	temp_guess = np.ones(len(vol1))
	temp_guess = [100 for i in range(len(vol1))]
	
	#Looping over the whole set of volumes in the dataset one can determine the temperature

	for i in range(len(vol1)):
		#setting the initial temperature step to be 150
		step = 150
		value= 100000
		counter =0

		#the algorithm iterates a maximum of 10,000 times
		while counter<10000:
			
		#############################################################
		#Material1
		############################################################

			#For material 1 we determine the pressure at the current temperature guess using the methods provided in sokolova and the parameters given for the material earlier.
			
			#vcmol
			fcnvcmol_0 = float(vol0[i])*6.02214/10
	
			#V Jbar**(-1)
			fcnvjbar_0 = fcnvcmol_0/ 10
	

			#fcnx
			fcnx_0 = fcnvjbar_0/material_0[2]
	
			#exp
			fcnexp_0= math.exp(EoSeqns().I_gamV(material_0[1],material_0[17],fcnx_0,material_0[2],material_0[3],material_0[4],material_0[9],material_0[10],0))
	

			#pthermal
			pthermal_0 = EoSeqns().Pth(material_0[1],material_0[17],material_0[2],material_0[3],material_0[4],material_0	[18],fcnx_0,fcnexp_0,fcnvjbar_0,1,1,0,1,1,0,material_0[5],material_0[6],material_0[7],material_0[8],temp_guess[i],material_0[9],0,material_0[10],material_0[11],material_0[13],material_0[14],material_0[12])
	
			#Px
			Px_0 = EoSeqns().P(material_0[17],material_0[1],fcnx_0,material_0[2],material_0[3],material_0[4])

			#Ptot
			P_tot_0 = Px_0+pthermal_0


			##################################################################
			#Material2
			#############################################################

			#For material 2 we determine the pressure at the current temperature guess using the methods provided in sokolova and the parameters given for the material earlier.
			
			
			#vcmol
			fcnvcmol_1 = float(vol1[i])*6.02214/10
	
			#V Jbar**(-1)
			fcnvjbar_1 = fcnvcmol_1/ 10
	

			#fcnx
			fcnx_1 = fcnvjbar_1/material_1[2]
	
			#exp
			fcnexp_1= math.exp(EoSeqns().I_gamV(material_1[1],material_1[17],fcnx_1,material_1[2],material_1[3],material_1[4],material_1[9],material_1[10],0))
	

			#pthermal
			pthermal_1 = EoSeqns().Pth(material_1[1],material_1[17],material_1[2],material_1[3],material_1[4],material_1	[18],fcnx_1,fcnexp_1,fcnvjbar_1,1,1,0,1,1,0,material_1[5],material_1[6],material_1[7],material_1[8],temp_guess[i],material_1[9],0,material_1[10],material_1[11],material_1[13],material_1[14],material_1[12])
	
			#Px
			Px_1 = EoSeqns().P(material_1[17],material_1[1],fcnx_1,material_1[2],material_1[3],material_1[4])

			#Ptot
			P_tot_1 = Px_1+pthermal_1
			

			#setting value_old for comparison
			value_old = value

			#adding one to the counter
			counter = counter+1
			

			#determining the comparison value as the difference between two pressures at the current temperature			
			value = abs(P_tot_1-P_tot_0)

			#if the value is less than a certain threshold then we use the current temperature and break out of the loop
			if value<0.0000001:
				
				break

			#If the current value is less than the previous value then we add the step on and therefore change the temperature guess
			if value<value_old:
				temp_guess[i]=temp_guess[i]+step

			#If the current value is greater than the previous value then we find the negative of the step and add half of it on.
			#This helps find the minimum

			else:
				step = -step/2
				temp_guess[i]= temp_guess[i]+step

			#The loop is then ran again until a value for temperature at each set of volumes is found
			
	return(temp_guess)


#running the above fucntion to determine the temperatures
temp_list = temp_guess_fcn( vol0, vol1, material_0,material_1)


#printing the estimates of temperature to the screen
print('\n\n\n\n')
print('The estimates for the temperature are:')
print(temp_list)


#If the user has said that there is going to be an error associated with the data at hand then we have to determine this error
if error_type.get() != "No errors needed":

	#The error is determined using a method as specified in Squires - Practical Physics

	#We define a volume which is the sum of the original volume and its associated error
	volerr0 = vol0+errlst0
	volerr1 = vol1+errlst1

	#The temperature is then calculcated for these new errors
	error1 = temp_guess_fcn(volerr0,vol1,material_0,material_1)
	error2 = temp_guess_fcn(vol0,volerr1,material_0,material_1)
	
	#This is then subtracted from the original temperature estimate to find the error due to vol1 and error due to vol2
	error_due1 = (np.array(temp_list)-np.array(error1))
	error_due2 = (np.array(temp_list)-np.array(error2))
	
	#These errors are then added in quadrature and printed to the terminal
	error_tot = np.sqrt(error_due1**2+error_due2**2)
	print('\n\n\n'+'The uncertainties on these measurements are: ')
	print(list(error_tot))
#print(error1,error2)






#This is only used if the end user is interested in isochore graphs


if var1.get() == 1:
	#lists initialised for use later
	y1=[]
	y2 = []
	y1_error=[]
	y2_error=[]
	temp_range =[]

	#this is looped over every volume in the intial list
	for i in range(len(vol1)):
		
		#we plot the graphs for the temperature guess +/- 1/2 temperature guess in 20 K increments
		temp_range.append(range(int(temp_list[i]-(temp_list[i]/2)-10),int(temp_list[i]+(temp_list[i]/2)+10),20))
		P_tot_0 = np.zeros(len(temp_range[i]))
		P_tot_1 = np.zeros(len(temp_range[i]))

				
		
		#############################################################
		#I calculate the pressure over the range for material 1
		############################################################

		#vcmol
		fcnvcmol_0 = float(vol0[i])*6.02214/10
		#V Jbar**(-1)
		fcnvjbar_0 = fcnvcmol_0/ 10
		#fcnx
		fcnx_0 = fcnvjbar_0/material_0[2]
		#exp
		fcnexp_0= math.exp(EoSeqns().I_gamV(material_0[1],material_0[17],fcnx_0,material_0[2],material_0[3],material_0[4],material_0[9],material_0[10],0))
		#Px
		Px_0 = EoSeqns().P(material_0[17],material_0[1],fcnx_0,material_0[2],material_0[3],material_0[4])
		for j in range(len(temp_range[i])):
				#pthermal
			pthermal_0 = EoSeqns().Pth(material_0[1],material_0[17],material_0[2],material_0[3],material_0[4],material_0	[18],fcnx_0,fcnexp_0,fcnvjbar_0,1,1,0,1,1,0,material_0[5],material_0[6],material_0[7],material_0[8],temp_range[i][j],material_0[9],0,material_0[10],material_0[11],material_0[13],material_0[14],material_0[12])
				#Ptot
			P_tot_0[j] = Px_0+pthermal_0

		y1.append(P_tot_0)

		##################################################################
		#I calculate the pressure over the range for material 2
		#############################################################
		#vcmol
		fcnvcmol_1 = float(vol1[i])*6.02214/10
		#V Jbar**(-1)
		fcnvjbar_1 = fcnvcmol_1/ 10
		#fcnx
		fcnx_1 = fcnvjbar_1/material_1[2]
		#exp
		fcnexp_1= math.exp(EoSeqns().I_gamV(material_1[1],material_1[17],fcnx_1,material_1[2],material_1[3],material_1[4],material_1[9],material_1[10],0))
		#Px
		Px_1 = EoSeqns().P(material_1[17],material_1[1],fcnx_1,material_1[2],material_1[3],material_1[4])
		for j in range(len(temp_range[i])):			
			#pthermal
			pthermal_1 = EoSeqns().Pth(material_1[1],material_1[17],material_1[2],material_1[3],material_1[4],material_1	[18],fcnx_1,fcnexp_1,fcnvjbar_1,1,1,0,1,1,0,material_1[5],material_1[6],material_1[7],material_1[8],temp_range[i][j],material_1[9],0,material_1[10],material_1[11],material_1[13],material_1[14],material_1[12])
			#Ptot
			P_tot_1[j] = Px_1+pthermal_1
		y2.append(P_tot_1)


		if error_type.get() != "No errors needed":
			P_tot_0_error = np.zeros(len(temp_range[i]))
			P_tot_1_error = np.zeros(len(temp_range[i]))
			

			##################################################################
			#Determining the uncertainty on Material 1
			##################################################################
			#This is the same as before only I calculate the pressure with the given volume, adding on the uncertainty, then take the pressure from this new pressure to find the uncertainty

			#vcmol
			fcnvcmol_0_error = float(volerr0[i])*6.02214/10
			#V Jbar**(-1)
			fcnvjbar_0_error = fcnvcmol_0_error/ 10
			#fcnx
			fcnx_0_error = fcnvjbar_0_error/material_0[2]
			#exp
			fcnexp_0_error= math.exp(EoSeqns().I_gamV(material_0[1],material_0[17],fcnx_0_error,material_0[2],material_0[3],material_0[4],material_0[9],material_0[10],0))
			#Px
			Px_0_error = EoSeqns().P(material_0[17],material_0[1],fcnx_0_error,material_0[2],material_0[3],material_0[4])
			for j in range(len(temp_range[i])):
					#pthermal
				pthermal_0_error = EoSeqns().Pth(material_0[1],material_0[17],material_0[2],material_0[3],material_0[4],material_0	[18],fcnx_0_error,fcnexp_0_error,fcnvjbar_0_error,1,1,0,1,1,0,material_0[5],material_0[6],material_0[7],material_0[8],temp_range[i][j],material_0[9],0,material_0[10],material_0[11],material_0[13],material_0[14],material_0[12])
					#Ptot
				P_tot_0_error[j] = Px_0_error+pthermal_0_error

			y1_error.append(P_tot_0_error-P_tot_0)


			##################################################################################
			#Uncertainty on Material 2
			##################################################################################

			#vcmol
			fcnvcmol_1_error = float(volerr1[i])*6.02214/10
			#V Jbar**(-1)
			fcnvjbar_1_error = fcnvcmol_1_error/ 10
			#fcnx
			fcnx_1_error = fcnvjbar_1_error/material_1[2]
			#exp
			fcnexp_1_error= math.exp(EoSeqns().I_gamV(material_1[1],material_1[17],fcnx_1_error,material_1[2],material_1[3],material_1[4],material_1[9],material_1[10],0))
			#Px
			Px_1_error = EoSeqns().P(material_1[17],material_1[1],fcnx_1_error,material_1[2],material_1[3],material_1[4])
			for j in range(len(temp_range[i])):			
				#pthermal
				pthermal_1_error = EoSeqns().Pth(material_1[1],material_1[17],material_1[2],material_1[3],material_1[4],material_1	[18],fcnx_1_error,fcnexp_1_error,fcnvjbar_1_error,1,1,0,1,1,0,material_1[5],material_1[6],material_1[7],material_1[8],temp_range[i][j],material_1[9],0,material_1[10],material_1[11],material_1[13],material_1[14],material_1[12])
				#Ptot
				P_tot_1_error[j] = Px_1_error+pthermal_1_error
			y2_error.append(P_tot_1_error-P_tot_1)




	#due to the fact that sokolova outputs values in bars the pressure is divided by 10,000 to get GPa
	###Plot the results
	y1= [y1[i]/10000 for i in range(len(y1))]
	y2= [y2[i]/10000 for i in range(len(y2))]


	#If we have errorbars then I also need to divide these by 10,000 so I can get these in GPa
	if error_type.get != "No errors needed":
		y1_error= [y1_error[i]/10000 for i in range(len(y1_error))]
		y2_error= [y2_error[i]/10000 for i in range(len(y2_error))]
	

	#Plotting all 
	for i in range(len(vol0)):
		x=temp_range[i]
		#different for with and without errors
		if error_type.get != "No errors needed":
			#this is a method of including error bars
			(_, caps0, _) = plt.errorbar(x,y1[i],marker='x',label = inmat.get()+' data', color = 'blue',yerr = y1_error[i], capsize=5, elinewidth=1)
			for cap in caps0:
			    cap.set_color('blue')
			    cap.set_markeredgewidth(1)

			#material 1
			(_, caps1, _) = plt.errorbar(x,y2[i],marker='x',label = inmat.get()+' data', color = 'red',yerr = y2_error[i], capsize=5, elinewidth=1)


			for cap in caps1:
			    cap.set_color('red')
			    cap.set_markeredgewidth(1)
		#If we have no error then it is simple to plot the results
		else:
			plt.errorbar(x,y1[i],marker='x',label = inmat.get()+' data', color = 'blue')
			plt.errorbar(x,y2[i],marker = 'x',label = inmat1.get()+' data',color = 'red' )
		plt.title('Plot of P vs T of '+ inmat.get()+ ' and '+ inmat1.get()+ ', V'+r'$_{'+str(inmat.get())+'}$'+'='+str(vol0[i])[:-1]+ ' (Å/at)'+', V'+r'$_{'+str(inmat1.get())+'}$'+'='+str(vol1[i])[:-1]+ ' (Å/at)')
		
		#placing a label on the graph of where the lines cross
		if error_type.get != "No errors needed":
			plt.text(min(x), max(y1[i]),'Lines cross at T= '+str(temp_list[i])[0:8]+r'$\pm$'+str(error_tot[i])[0:8]+' K')

		else:
			plt.text(min(x), max(y1[i]),'Lines cross at T= '+str(temp_list[i])[0:8]+' K')

		#Adding a legend and labels	
		plt.legend(loc=4)
		plt.ylabel("Pressure/GPa")
		plt.xlabel("Temperature/K")

		#Showing/Saving depending on what the original user has selected.	
		if var3.get() ==1:
			plt.show()

		if var2.get() ==1:
			plt.savefig(inmat.get()+inmat1.get()+str((vol0[i]))[:-1]+str((vol1[i]))[:-1]+"_Temperature.pdf")

		plt.close()
















