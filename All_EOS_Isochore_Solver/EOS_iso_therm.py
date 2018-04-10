#Author - Mark Corrigan
#Email - mark.corrigan1994@gmail.com
#MPhys Project 2017/18


#Importing all the needed packages for implementation of the various equations of state
from scipy.integrate import quad
import numpy as np

#This set of classes is used to code up various isothermal and thermal equations of state where they are used for plotting data

#At the bottom the algorithm for determining the temperature is also implemented

class isothermal:

	def AP2(self,v,params):
	# z, n, Vo, Ko,kk == params

		fw = -np.log(3 *params[3] / 10 / (1003.6 * (params[0] * params[1] / (params[2] * 10)) ** (5 / 3)))
		ff = (v/params[2]) ** (1 / 3)
		aa = 1.5 * (params[4] - 3) - fw
		P = 3 * params[3] * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)
		P=P/10000
		return P


	def BM3(self,v,params):
		#params == B0,V0,Bt
		P = (3/2)*params[0]*((params[1]/v)**(7/3)-(params[1]/v)**(5/3))*(1+((3/4)*(params[2]-4)*((params[1]/v)**(2/3)-1)))
		return P

	def Vinet(self,v,params):
	##params = B0,V0,Bt

		P = 3*params[0]*(v/params[1])**(-2/3)*(1-(v/params[1])**(1/3))*np.exp((3/2)*(params[2]-1)*(1-(v/params[1])**(1/3)))
		return P


####################################################################
###################################################################
###################################################################


class thermal:

	def simple(Temp,V,params):
		###params == akt
		p_therm = params[0]*(Temp-300)
		return( p_therm)



	def thermal_Pressure(self,Temp,V,params):
		####params == a0,V0,B0,dB,d2P
		P_th = (params[0]*params[2]*(Temp-300))+((params[3])*(Temp-300)*np.log(params[1]/V))+((params[4])*(Temp-300)**2)

		return (P_th)

	def Mie_gruinisen(self,T,V,params):
		##params == V_0,n,theta_0,q,gamma_0,unit

		
		R=8.31445/1E9

		gamma = params[4]*((V/params[0])**params[3])
	
		theta = params[2]*np.exp((params[4]-gamma)/params[3])

		E_th_1 = (9*params[1]*R*T)/(((theta/T)**3))
		E_th_2 = (9*params[1]*R*300)/((theta/300)**3)

	
		def integrand(z):
			return((z**3)/(np.exp(z)-1))

		I = quad(integrand, 0, (theta/T))
		I_300 = quad(integrand,0,theta/300)
	

		E_th_T = E_th_1*I[0]
		E_th_300 = E_th_2*I_300[0]
		Vm = V*6.02214*0.000001/(10*params[5])
		P_th = (gamma/Vm)*(E_th_T-E_th_300)

		return(P_th)


##############################################################################################################################################
##############################################################################################################################################

class temp:

	#this is the temperature algorithm which is detailed in the report  and in the main code for this program

	def temp_guess_fcn(self,vol1,vol2,isoparams1,isoparams2,thermparams1,thermparams2,iso1,iso2,therm1,therm2,error_type,volerr0,volerr1):
		
		#the initial guess for temperature is 100 K
		temp_guess = np.ones(len(vol1))
		temp_guess = [100 for i in range(len(vol1))]


		#The program gets the equations of state needed
		p_iso1 = getattr(isothermal(),iso1)
		p_iso2 = getattr(isothermal(),iso2)
		p_therm1 = getattr(thermal(),therm1)
		p_therm2 = getattr(thermal(),therm2)

		#Initialising arrays which are to be used later

		y1_error=[]
		y2_error=[]
	
		#The code iterates over all of the volumes given to it to calculate a temperature for all of them

		for i in range(len(vol1)):
			#the initial temperature step which is used is 150 k
			step = 150
			value= 100000
			
			counter =0
			#making sure that the code iterates a maximum of 10,000 times
			while counter<10000:
			
				#############################################################
				#Determining pressure for Material1
				############################################################

				P_Mat1 = p_iso1(vol1[i],isoparams1)
				
			
				Pth_Mat1 = p_therm1(temp_guess[i],vol1[i],thermparams1)
				
				P_tot_1 = P_Mat1+Pth_Mat1
				

				##################################################################
				#Determining pressure for Material2
				#############################################################
				P_Mat2 = p_iso2(vol2[i],isoparams2)

				

				Pth_Mat2 = p_therm2(temp_guess[i],vol2[i],thermparams2)
				P_tot_2 = P_Mat2+Pth_Mat2
				
				value_old = value
				#Value here is the absolute difference between the two pressures
				value = abs(P_tot_2-P_tot_1)



				counter = counter+1

				#If the difference between pressures is below a certain threshold then the algorithm stops iterating
				if value<0.0000001:
					break
				#If the current difference is less than the previous difference then the temperature is changed by the step 
				if value<value_old:
					temp_guess[i]=temp_guess[i]+step
				#If the current difference is greater than the previous difference then the sign of the temperature step is changed, and halved and then added to the temperature
				else:
					step = -step/2
					temp_guess[i]= temp_guess[i]+step


		#If there has been an error selected by the end user then this part of the code calculates it
		if error_type != "No errors needed":



			#initialising arrays for the errors
			y1_error=[]
			y2_error=[]

			#initialising an array for the temperature range - this will be an array of arrays
			temp_range =[]

			#the range over which each error bar is needed is the temperature guess +/- ((temperature guess/2)+/-10) in 20 K steps
			for i in range(len(vol1)):
				temp_range.append(range(int(temp_guess[i]-(temp_guess[i]/2)-10),int(temp_guess[i]+(temp_guess[i]/2)+10),20))	
	


			#the error in the pressure is stored in arrays which are initialised here
			P_tot_0_error = np.zeros(len(temp_range[i]))
			P_tot_1_error = np.zeros(len(temp_range[i]))
	




			##################################################################
			#Determining the uncertainty on Material 1
			##################################################################
			#This is the same as before only I calculate the pressure with the given volume, adding on the uncertainty, then take the pressure from this new pressure to find the uncertainty
			Px_0_error = p_iso1(volerr0[i],isoparams1)

			for j in range(len(temp_range[i])):
					#pthermal

				pthermal_0_error = p_therm1(temp_range[i][j],volerr0[i],thermparams1)

					#Ptot
				P_tot_0_error[j] = Px_0_error+pthermal_0_error

			y1_error.append(P_tot_0_error-P_tot_1)


			##################################################################################
			#Uncertainty on Material 2
			##################################################################################


			#Px
			Px_1_error = p_iso1(volerr1[i],isoparams2)

			for j in range(len(temp_range[i])):
					#pthermal

				pthermal_1_error = p_therm2(temp_range[i][j],volerr1[i],thermparams2)

					#Ptot
				P_tot_1_error[j] = Px_1_error+pthermal_1_error
			y2_error.append(P_tot_1_error-P_tot_2)

		return(temp_guess,y1_error,y2_error)


