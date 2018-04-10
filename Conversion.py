from EoSeqns import EoSeqns
import math
from tkinter import * 
import pandas as pd
import numpy as np
import sys 
import os
import matplotlib.pyplot as plt
from tkinter import filedialog



#Uo,n,Vo,Ko,kk,QE1,m1,QE2,m2,δ,t,ao,eo,m,g,co,с2,Z is the order of the data
#Uo,nn,Vo,Ko,kk,QE1,mE1,QE2,mE2,go,gb,ao,ae,m,me,fw,aa,z,va^3

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

#CUSTOM input
custom = []

##########
#This is used to select the element
#######
master = Tk()
Label(master,text= 'Select a Material',font='Helvetica 14 bold').grid(row=0)
Label(master,text='Please select a material from the drop down list on the right').grid(row=1,column=0)
inmat = StringVar(master)
inmat.set("--") # initial value

option = OptionMenu(master, inmat,"Ag","Al","Au","C","Cu","MgO","Mo","Nb","Pt","Ta","W","Custom Parameters").grid(row=1,column=1)


#making an ok button that can be used to close the window
def ok():
    master.quit() 
    master.destroy()
       

button1 = Button(master, text="OK", command=ok).grid(row=5)

master.mainloop()
##########################################################
#getting the pressure & temperature
########## 

master1 = Tk()
Label(master1, text="Enter Temperature Range",font='Helvetica 14 bold').grid(row=0)
Label(master1, text="Lowest Temperature/K").grid(row=1)
Label(master1, text="Highest Temperature/K").grid(row=2)
Label(master1, text="Step/K").grid(row=3)
Label(master1, text='Tick for output',font='Helvetica 11 bold').grid(row=4,column=0)

#vol = Entry(master1)
ltemp = Entry(master1)
htemp = Entry(master1)
step = Entry(master1)

#vol.grid(row=0, column=1)
ltemp.grid(row=1, column=1)
htemp.grid(row=2, column=1)
step.grid(row=3, column=1)

def ok1():

    master1.quit()
    #master1.destroy()
  
var1 = IntVar()
Checkbutton(master1, text="Graphs", variable=var1).grid(row=5,column=0)
var2 = IntVar()
Checkbutton(master1, text="Data Tables", variable=var2).grid(row=6,column=0)

Button(master1, text='OK', command=ok1).grid(row=5, column=1, sticky=W, pady=4)


master1.mainloop( )

#########################################
#Range of temperatures used
#########################################


TempK = range(int(ltemp.get()),int(htemp.get())+int(step.get()),int(step.get()))

presorvol = Tk()
Label(presorvol, text="Choose whether your input parameters are Pressure or volume").grid(row=4,column=0)



def ok6():
    presorvol.quit()
inputatt = StringVar(presorvol)
inputatt.set("--")
  
option = OptionMenu(presorvol, inputatt,"Pressure","Volume").grid(row=4,column=1)



Button(presorvol, text='OK', command=ok6).grid(row=7, column=0, sticky=W, pady=4)

presorvol.mainloop( )

print(var1.get())



if inputatt.get()=='Volume':
	root1 = Tk()
	root1.filename = filedialog.askopenfilename(title = "Select Volumes for "+str(inmat.get()))

	with open(root1.filename) as f:
	    vol = f.readlines()
	    vol = [float(vol[i]) for i in range(len(vol))]
	    vol = np.array(vol)
	listshape = (len(vol),len(TempK))


elif inputatt.get() =='Pressure':

	root1 = Tk()
	root1.filename = filedialog.askopenfilename(title = "Select Pressures for "+str(inmat.get()))

	with open(root1.filename) as f:
	    press = f.readlines()
	    press = [float(press[i]) for i in range(len(press))]
	    press = np.array(press)
	listshape = (len(press),len(TempK))
else:
	sys.exit()



##This little method allows a hardcoded way of selecting the material needed in the terminal.
test1=1
custtest= 0
while test1==1:

	


	#inmat = input("Please enter a material from the following: 'Ag,Al,Au,C,Cu,MgO,Mo,Nb,Pt,Ta,W': ")
	
	if inmat.get() == 'Ag':
		material =Ag
		test1=2
	elif inmat.get() == 'Al':
		material =Al
		test1=2
	elif inmat.get() =='Au':
		material =Au
		test1=2
	elif inmat.get() =='C':
		material =C
		test1=2
	elif inmat.get() =='Cu':
		material =Cu
		test1=2
	elif inmat.get() =='MgO':
		material = MgO
		test1=2
	elif inmat.get() =='Mo':
		material = Mo
		test1=2
	elif inmat.get() =='Nb':
		material = Nb
		test1=2
	elif inmat.get() =='Pt':
		material = Pt
		test1=2
	elif inmat.get() =='Ta':
		material = Ta
		test1=2
	elif inmat.get() =='W':
		material = Tung
		test1=2
	elif inmat.get() =='Custom Parameters':
		material= custom
		custtest = 1
		test1 = 2
		#used to initiate the if statement which allows the custom input to be put in 
		
	#else:
	#	print("\n You didn't enter a valid material, please try again \n")


	#0,1   2   3  4  5   6   7   8  9  10 11 12 13 14  15 16 17 18
	#Uo,nn,Vo,Ko,kk,QE1,mE1,QE2,mE2,go,gb,ao,ae,m,me,fw,aa,nnn,To
	#x
#Initializing lists

fcnxlst = np.ndarray(shape = listshape)
fcnvjbarlst = np.ndarray(shape = listshape)
fcnvcmollst = np.ndarray(shape = listshape)
fcnvacelllst = np.ndarray(shape = listshape)
fcnexlst = np.ndarray(shape = listshape)
fcnexplst=np.ndarray(shape = listshape)
freeelst=np.ndarray(shape = listshape)
entropylst = np.ndarray(shape = listshape)
inenergylst = np.ndarray(shape = listshape)
pthermallst = np.ndarray(shape = listshape)
Pxlst=np.ndarray(shape = listshape)
Preallst = np.ndarray(shape = listshape)
GibbsEnergylst = np.ndarray(shape = listshape)
Enthalpylst = np.ndarray(shape = listshape)
Cvlst = np.ndarray(shape = listshape)
KTthlst = np.ndarray(shape = listshape)
xxlst=np.ndarray(shape = listshape)
KTxlst = np.ndarray(shape = listshape)
Klst=np.ndarray(shape = listshape)
dPdTlst=np.ndarray(shape = listshape)
alphalst = np.ndarray(shape = listshape)
Cplst = np.ndarray(shape = listshape)
Kslst = np.ndarray(shape = listshape)
gamlst = np.ndarray(shape = listshape)
Ksglst = np.ndarray(shape = listshape)
KTGPalst = np.ndarray(shape = listshape)
alphaminus5lst = np.ndarray(shape = listshape)


##################################################################################################################

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

	def ok2():
    #print "value is", inmat.get()
		master2.quit()
		master2.destroy()
		



	Button(master2, text='OK', command=ok).grid(row=20, column=0, sticky=E, pady=4)

	master2.mainloop()
	
	material.append(float(Uo.get()))
	material.append(float(n.get()))
	material.append(float(Vo.get()))
	material.append(float(Ko.get()))
	material.append(float(kk.get()))
	material.append(float(QE1.get()))
	material.append(float(m1.get()))
	material.append(float(QE2.get()))
	material.append(float(m2.get()))
	material.append(float(delta.get()))
	material.append(float(t.get()))
	material.append(float(ao.get()))
	material.append(float(eo.get()))
	material.append(float(m.get()))
	material.append(float(g.get()))
	material.append(float(co.get()))
	material.append(float(c2.get()))
	material.append(float(Z.get()))
	material.append(float(To.get()))
	material.append(float(atom.get()))


	

if inputatt.get()=='Volume':
	attribute = vol
elif inputatt.get() =='Pressure':
	attribute = press
	
##################################################################################################################

for i in range(len(attribute)):
	for j in range(len(TempK)):
	
		if inputatt.get()=='Volume':

			#vcmol
			fcnvcmollst[i,j] = vol[i]*6.02214/10/material[19]
			#V Jbar**(-1)
			fcnvjbarlst[i,j] = fcnvcmollst[i,j]/ 10
			#fcnx
			fcnxlst[i,j] = fcnvjbarlst[i,j]/material[2]
			#fcnex
			fcnexlst[i,j] = EoSeqns().I(material[17],material[1],fcnxlst[i,j],material[2],material[3],material[4])

		elif inputatt.get() =='Pressure':

			fcnxlst[i,j] = EoSeqns().xAP2(material[1],material[17],material[18],material[2],material[3],material[4],1,1,0,1,1,0,material[5],material[6],material[7],material[8],material[9],material[10],0,material[11],material[13],material[14],material[12],TempK[j],press[i]*10000.)
			#V Jbar**(-1)
			fcnvjbarlst[i,j] = fcnxlst[i,j]* material[2]
			#vcmmol
			fcnvcmollst[i,j] = fcnxlst[i,j]* material[2] *10
			#fcnvacell
			fcnvacelllst[i,j] = fcnxlst[i,j]* material[2] *10 * material[19] /6.02214
			#fcnex
			fcnexlst[i,j] = EoSeqns().I(material[17],material[1],fcnxlst[i,j],material[2],material[3],material[4])
			


		#exp
		fcnexplst[i,j] = math.exp(EoSeqns().I_gamV(material[1],material[17],fcnxlst[i,j],material[2],material[3],material[4],material[9],material[10],0))
	
		#fcnfreee
		freeelst[i,j] = EoSeqns().F(material[1],material[17],material[2],material[3],material[4],material[18],fcnxlst[i,j],fcnexplst[i,j],1,1,0,1,1,0,material[5],material[6],material[7],material[8],TempK[j],material[9],0,material[10],material[11],material[13],material[14],material[12])+fcnexlst[i,j]+material[0]
		


	#entropy
		entropylst[i,j] = EoSeqns().S(material[1],material[17],material[2],material[3],material[4],material[18],fcnxlst[i,j],fcnexplst[i,j],1,1,0,1,1,0,material[5],material[6],material[7],material[8],TempK[j],material[9],0,material[10],material[11],material[13],material[14],material[12])
		
	#0,1   2   3  4  5   6   7   8  9  10 11 12 13 14  15 16 17 18,19
	#Uo,nn,Vo,Ko,kk,QE1,mE1,QE2,mE2,go,gb,ao,ae,m,me,fw,aa,nnn,To,unitcell

	#inEnergy

		inenergylst[i,j] = freeelst[i,j]+entropylst[i,j]*TempK[j]
		
	#pthermal

		pthermallst[i,j] = EoSeqns().Pth(material[1],material[17],material[2],material[3],material[4],material[18],fcnxlst[i,j],fcnexplst[i,j],fcnvjbarlst[i,j],1,1,0,1,1,0,material[5],material[6],material[7],material[8],TempK[j],material[9],0,material[10],material[11],material[13],material[14],material[12])
		


		#Px

		Pxlst[i,j] = EoSeqns().P(material[17],material[1],fcnxlst[i,j],material[2],material[3],material[4])
	
		#Preal

		Preallst[i,j] = Pxlst[i,j] +pthermallst[i,j]
		#GibbsEnergy

		GibbsEnergylst[i,j] = freeelst[i,j]+Preallst[i,j]*fcnvjbarlst[i,j]
 
	
		#Enthalpy

		Enthalpylst[i,j] = inenergylst[i,j]+Preallst[i,j]*fcnvjbarlst[i,j]


		#Cv

		Cvlst[i,j] = EoSeqns().CCv(material[1],material[17],material[2],material[3],material[4],material[18],fcnxlst[i,j],fcnexplst[i,j],1,1,0,1,1,0,material[5],material[6],material[7],material[8],TempK[j],material[9],0,material[10],material[11],material[13],material[14],material[12])
		
		#KTthermal

		KTthlst[i,j] = EoSeqns().KTth(material[1],material[17],material[2],material[3],material[4],material[18],fcnxlst[i,j],fcnexplst[i,j],fcnvjbarlst[i,j],1,1,0,1,1,0,material[5],material[6],material[7],material[8],TempK[j],material[9],0,material[10],material[11],material[13],material[14],material[12])



		#xx

		xxlst[i,j] = fcnxlst[i,j]**(1/3)

		#KTx

		KTxlst[i,j]=material[3]/xxlst[i,j]**6*math.exp(material[15]*(1-xxlst[i,j]))*((-5/xxlst[i,j]**2+4/xxlst[i,j])*(1+material[16]*xxlst[i,j]-material[16]*xxlst[i,j]**2)+(1/xxlst[i,j]-1)*(1+material[16]*xxlst[i,j]-material[16]*xxlst[i,j]**2)*(-material[15])+(1/xxlst[i,j]-1)*(material[16]-2*material[16]*xxlst[i,j]))*(-fcnxlst[i,j])*1000

		#KT

		Klst[i,j] = KTxlst[i,j] +KTthlst[i,j]

		#dPdT

		dPdTlst[i,j] = EoSeqns().dPdTth(material[1],material[17],material[2],material[3],material[4],material[18],fcnxlst[i,j],fcnexplst[i,j],fcnvjbarlst[i,j],1,1,0,1,1,0,material[5],material[6],material[7],material[8],TempK[j],material[9],0,material[10],material[11],material[13],material[14],material[12])

		#alpha

		alphalst[i,j] = dPdTlst[i,j]/(KTthlst[i,j]+KTxlst[i,j])

		#Cp

		Cplst[i,j]=Cvlst[i,j]+alphalst[i,j]**2*fcnvjbarlst[i,j]*TempK[j]*(KTthlst[i,j]+KTxlst[i,j])


		#Ks

		Kslst[i,j] = Klst[i,j]+TempK[j]*fcnvjbarlst[i,j]/Cvlst[i,j]*dPdTlst[i,j]**2

		

		#gam 

		gamlst[i,j] =alphalst[i,j]*fcnvjbarlst[i,j]*Klst[i,j]/Cvlst[i,j]

		#Ks (GPa)

		Ksglst[i,j]= Kslst[i,j]/10000


		#KT (GPa)

		KTGPalst[i,j] = Klst[i,j]/10000

		#alpha 10^(-5)

		alphaminus5lst[i,j] =alphalst[i,j]*100000



master3 = Tk()

S = Scrollbar(master3)
T = Text(master3, height=4, width=75)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Please select a dataset from the dropdown list on the right"""
T.insert(END, quote)

inval = StringVar(master3)
inval.set("--") # initial value

option = OptionMenu(master3, inval,"--","Compression (dimensionless)","Volume (Jbar^-1 )","Volume (cm^3mol^-1)","Volume (Å^3cell^-1)","Potential from Helmholtz Free Energy (Jmol^-1)","Helmholtz Free Energy (Jmol^-1)","Entropy (Jmol^-1K^-1)","Internal Energy (Jmol^-1)","Gibbs Energy (Jmol^-1)","Enthalpy (Jmol^-1)","Isochoric Heat Capacity (Jmol"+r'$^{-1}$'+'K'+r'$^{-1}$'+")","Potential part of real Pressure (bar)","Thermal part of real pressure (bar)","Real Pressure","Thermal Part of isothermal Bulk Modulus (bar)","Compression to the extent 1/3 (dimensionless)","Potential Part of the isothermal bulk Modulus (bar)","Isothermal Bulk Modulus","dP/dT slope (barK^-1)","Volume Coefficient of thermal expansivity","Isobaric heat capacity","Adiabatic bulk modulus","Thermodynamic Gruneisen parameter (dimensionless)","Einstein characteristic Temperature multiplier (dimensionless)")
option.pack()



def ok():
    #print "value is", inmat.get()
    master3.quit()
    master3.destroy()

#NEED TO WORK OUT HOW CHECKBOXES WORK

button = Button(master3, text="OK", command=ok)
button.pack()

master3.mainloop()

outval = []
if inval.get() == "Compression (dimensionless)":
	outval = fcnxlst
elif inval.get() == "Volume (Jbar^-1 )":
	outval = fcnvjbarlst
elif inval.get() == "Volume (cm^3mol^-1)":
	outval = fcnvcmollst
elif inval.get() == "Volume (Å^3cell^-1)":
	outval = fcnvacelllst
elif inval.get() == "Potential from Helmholtz Free Energy (Jmol^-1)":
	outval = fcnexlst
elif inval.get() == "Helmholtz Free Energy (Jmol^-1)":
	outval = freeelst
elif inval.get() == "Entropy (Jmol^-1K^-1)":
	outval = entropylst
elif inval.get() == "Internal Energy (Jmol^-1)":
	outval = inenergylst
elif inval.get() == "Gibbs Energy (Jmol^-1)":
	outval = GibbsEnergylst
elif inval.get() == "Enthalpy (Jmol^-1)":
	outval = Enthalpylst
elif inval.get() == "Isochoric Heat Capacity (Jmol"+r'$^{-1}$'+'K'+r'$^{-1}$'+")":
	outval = Cvlst
elif inval.get() == "Potential part of real Pressure (bar)":
	outval = Pxlst
elif inval.get() == "Thermal part of real pressure (bar)":
	outval = pthermallst
elif inval.get() == "Real Pressure":
	outval = Preallst
elif inval.get() == "Thermal Part of isothermal Bulk Modulus (bar)":
	outval = KTthlst
elif inval.get() == "Compression to the extent 1/3 (dimensionless)":
	outval = xxlst
elif inval.get() == "Potential Part of the isothermal bulk Modulus (bar)":
	outval = KTxlst
elif inval.get() == "Isothermal Bulk Modulus":
	outval = Klst
elif inval.get() == "dP/dT slope (barK^-1)":
	outval = dPdTlst
elif inval.get() == "Volume Coefficient of thermal expansivity":
	outval = alphalst
elif inval.get() == "Isobaric heat capacity":
	outval = Cplst
elif inval.get() == "Adiabatic bulk modulus":
	outval = Kslst
elif inval.get() == "Thermodynamic Gruneisen parameter (dimensionless)":
	outval = gamlst
elif inval.get() == "Einstein characteristic Temperature multiplier (dimensionless)":
	outval = fcnexplst


if inputatt.get()=='Volume':
#####showing the graph

	for i in range(len(outval)):
		if var1.get() ==1:
			plt.plot(list(TempK),outval[i],marker='o', linestyle='--',label = inval.get())
			plt.xlabel('Temperature/K')
			plt.ylabel(str(inval.get()))
			plt.title('Graph of '+inval.get()+' for '+inmat.get()+' at '+str(vol[i])+' Angstroms/cell')
			plt.show()



	###showing the dataset

		if var2.get() ==1:
			c= np.column_stack((list(TempK),outval[i]))


			df = pd.DataFrame(c,columns=('Temperature/Kelvin',inval.get()))


			root = Tk() 
			t1 = Text(root) 
			t1.pack() 

			class PrintToT1(object): 
			 def write(self, s): 
			     t1.insert(END, s) 
			sys.stdout = PrintToT1()
			with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
			    print('Data for '+inval.get()+' for '+inmat.get()+' at '+str(vol[i])+'Angstroms/cell')
			    print(df) 

			mainloop() 

elif inputatt.get()=='Pressure':

	#####showing the graph

	for i in range(len(outval)):
		if var1.get() ==1:
			plt.plot(list(TempK),outval[i],marker='o', linestyle='--',label = inval.get())
			plt.xlabel('Temperature/K')
			plt.ylabel(str(inval.get()))
			plt.title('Graph of '+inval.get()+' for '+inmat.get()+' at '+str(press[i])+' GPa')
			plt.show()



	###showing the dataset

		if var2.get() ==1:
			c= np.column_stack((list(TempK),outval[i]))


			df = pd.DataFrame(c,columns=('Temperature/Kelvin',inval.get()))


			root = Tk() 
			t1 = Text(root) 
			t1.pack() 

			class PrintToT1(object): 
			 def write(self, s): 
			     t1.insert(END, s) 
			sys.stdout = PrintToT1()
			with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
			    print('Data for '+inval.get()+' for '+inmat.get()+' at '+str(press[i])+'GPa')
			    print(df) 

			mainloop() 

sys.exit()

	






