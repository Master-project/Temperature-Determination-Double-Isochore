#This set of equations is incredibly hard to understand
#Taken from Sokolova et al (2016)
#Conversion of Python to VBA
#Reproduces all results given in spreadsheets

#I am not responsible for any errors in the algorithms themselves but only their python implementation.

#Author - Mark Corrigan
#Email - mark.corrigan1994@gmail.com
#MPhys Project - 2017/18






import numpy as np
class EoSeqns:
	
	def __init__(self):
		self=self
		
	def f_gamV(self, x, n, z, Vo, Ko, kk, gamVo, gb, beta):

		self.x = x
		self.n = n
		self.z = z
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk
		self.gamVo = gamVo
		self.gb = gb
		self.beta = beta

		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))

		ff = x ** (1 / 3)

		aa = (1.5 * (kk - 3)) - fw

		KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)
		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)

		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)

		ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))

		ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))

		ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3

		kkx = (ex + ex1 - ex2) / (-KT / ff) / 3

		gt = gb - beta * x ** (1 / 3)

		gtx = -beta / 3 * x ** (-2 / 3)

		f_gamV = (gamVo + (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt)) / x

		return f_gamV
	

##############################################################################	

	def P(self, z, n, x, Vo, Ko,kk):
		self.z = z,
		self.n = n
		self.x = x
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk


		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))
		ff = x ** (1 / 3)
		aa = 1.5 * (kk - 3) - fw
		P = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)

		return P

########################################################################	



	def xAP2(self, n, z, Tr, Vo, Ko, kk, QBo, d, mb, QBo1, d1, mb1, QEo1, mE1, QEo2, mE2, gamVo, gb, beta, ao, m, mm, ae, TK, Pbar):

		self.n= n
		self.z = z
		self.Tr = Tr
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk
		self.QBo = QBo
		self.d = d
		self.mb = mb
		self.QBo1= QBo1
		self.d1 = d1
		self.mb1 = mb1
		self.QEo1 = QEo1
		self.mE1 = mE1
		self.QEo2 = QEo2
		self.mE2 = mE2
		self.gamVo = gamVo
		self.gb = gb
		self.beta = beta
		self.ao = ao
		self.m = m
		self.mm = mm
		self.ae = ae
		self.TK = TK
		self.Pbar = Pbar



		R = 8.31451
		e = 0.00000000001
		L = 0.4
		Rx = 1.3
		FL = 5000000
		i = 0
		
		while abs(Rx - L) >= e:
			x = (L + Rx) / 2
			i = i + 1

			fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))

			ff = x ** (1 / 3)

			aa = 1.5 * (kk - 3) - fw

			Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)

			KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)

			ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))

			ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))

			ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3

			kkx = (ex + ex1 - ex2) / (-KT / ff) / 3

			gt = gb - beta * x ** (1 / 3)
			#gt=t параметр t по Бураковскому
			gtx = -beta / 3 * x ** (-2 / 3)
			#gtx=dgt/dx=beta производная по х параметра t по Бураковскому
			gamV = (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt) + gamVo
			expp = np.exp(self.I_gamV(z, n, x, Vo, Ko, kk, gamVo, gb, beta) * (1))
			ff2 = (x + 0.00001) ** (1 / 3)
			KT2 = Ko * 1000 / ff2 ** 6 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) + (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * (-fw) + (1 / ff2 - 1) * (aa - 2 * aa * ff2)) * (-(x + 0.00001))
			ex = 3 / ff2 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
			ex1 = 1 / ff2 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff2)) * fw * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
			ex2 = Ko * 1000 * np.exp(fw * (1 - ff2)) * ((10 / ff2 ** 3 - 4 / ff2 ** 2) * (1 + aa * ff2 - aa * ff2 ** 2) + (-5 / ff2 ** 2 + 4 / ff2) * (aa - 2 * aa * ff2) + fw / ff2 ** 2 * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (aa - 2 * aa * ff2) * fw - (aa - 2 * aa * ff2) / ff2 ** 2 - 2 * aa * (1 / ff2 - 1)) / ff2 ** 3

			kkx2 = (ex + ex1 - ex2) / (-KT2 / ff2) / 3

			ff1 = (x - 0.00001) ** (1 / 3)
			KT1 = Ko * 1000 / ff1 ** 6 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) + (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * (-fw) + (1 / ff1 - 1) * (aa - 2 * aa * ff1)) * (-(x - 0.00001))
			ex = 3 / ff1 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
			ex1 = 1 / ff1 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff1)) * fw * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
			ex2 = Ko * 1000 * np.exp(fw * (1 - ff1)) * ((10 / ff1 ** 3 - 4 / ff1 ** 2) * (1 + aa * ff1 - aa * ff1 ** 2) + (-5 / ff1 ** 2 + 4 / ff1) * (aa - 2 * aa * ff1) + fw / ff1 ** 2 * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (aa - 2 * aa * ff1) * fw - (aa - 2 * aa * ff1) / ff1 ** 2 - 2 * aa * (1 / ff1 - 1)) / ff1 ** 3

			kkx1 = (ex + ex1 - ex2) / (-KT1 / ff1) / 3

			dkkdx = (kkx2 - kkx1) / (0.00002)

			qV = -1 / 2 * (-6 * KT * kkx ** 2 * Px * gt / x + 6 * KT * dkkdx * Px * gt + 6 * KT * kkx * KT * gt / x - 6 * KT * kkx * Px * gtx + 4 * gt ** 2 * KT * kkx * Px / x - 4 * gt ** 2 * KT ** 2 / x - 9 * KT ** 2 * dkkdx + 6 * gtx * KT ** 2) / (3 * KT - 2 * Px * gt) ** 2 * x / gamV

			a = ao / 1000000 * x ** m

			QB = QBo * expp
			QB1 = QBo1 * expp
			QE1 = QEo1 * expp
			QE2 = QEo2 * expp

			VV = x * Vo
			ggr = d * np.log(1 + QB / Tr / d)
			br = 1 / (np.exp(ggr) - 1)
			ex1r = np.exp(QB / Tr)
			PthBr = mb * R * ((Tr * QB * d * br / (Tr * d + QB)) * gamV / VV)

			gg = d * np.log(1 + QB / TK / d)
			b = 1 / (np.exp(gg) - 1)
			ex1 = np.exp(QB / TK)
			PthB = mb * R * ((TK * QB * d * b / (TK * d + QB)) * gamV / VV)

			gg1r = d1 * np.log(1 + QB1 / Tr / d1)
			b1r = 1 / (np.exp(gg1r) - 1)
			ex2r = np.exp(QB1 / Tr)
			PthBBr = mb1 * R * ((Tr * QB1 * d1 * b1r / (Tr * d1 + QB1)) * gamV / VV)

			gg1 = d1 * np.log(1 + QB1 / TK / d1)
			b1 = 1 / (np.exp(gg1) - 1)
			ex2 = np.exp(QB1 / TK)
			PthBB = mb1 * R * ((TK * QB1 * d1 * b1 / (TK * d1 + QB1)) * gamV / VV)


			e1 = np.exp(QE1 / TK)
			PthE1 = mE1 * R * ((QE1 / (e1 - 1)) * gamV / VV)

			e2 = np.exp(QE2 / TK)
			PthE2 = mE2 * R * ((QE2 / (e2 - 1)) * gamV / VV)

			e1r = np.exp(QE1 / Tr)
			PthE1r = mE1 * R * ((QE1 / (e1r - 1)) * gamV / VV)

			e2r = np.exp(QE2 / Tr)
			PthE2r = mE2 * R * ((QE2 / (e2r - 1)) * gamV / VV)

			Pa = 1.5 * n * R * ao / 1000000 * x ** (m) * (m) / x / Vo * (TK ** 2 - Tr ** 2)
			Pe = 1.5 * n * R * ae / 1000000 * x ** (mm) * (mm) / x / Vo * (TK ** 2 - Tr ** 2)

			Pth = PthB - PthBr + PthBB - PthBBr + PthE1 - PthE1r + PthE2 - PthE2r + Px + Pe + Pa - Pbar

			F = Pth

			if FL * F > 0:
				L = x 
			else:
				Rx = x

			if i > 100000:
				x = i

			if i > 100000:
				break

		return x

#####################################################################################################################################

	def I(self,z, nn, b, Vo, Ko, kk):

		self.z = z
		self.nn = nn
		self.b = b
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk

		e = 0.001
		a = 1
		if b < 1:
			a = b
			b = 1

		s2 = 1
		h = (b - a)
		S = (self.P(z, nn, a, Vo, Ko, kk) + self.P(z, nn, b, Vo, Ko, kk)) * Vo
		x = 1+e
		while x >= e:
			s3 = s2
			h = h / 2
			x = a + h
			s1 = 0
			while x < b:
				s1 = s1 + 2 * self.P(z, nn, x, Vo, Ko, kk) * Vo
				x = x + 2 * h
	
			S = S + s1
			s2 = (S + s1) * h / 3
			x = abs(s3 - s2) / 15


		if b > 1:
			I1 = -s2
		else:
			I1 = s2

		return I1

######################################################################################################################################################
	
	def I_gamV(self,z, n, b, Vo, Ko, kk, gamVo, gb, beta):

		self.z = z
		self.n = n
		self.b = b
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk
		self.gamVo = Vo
		self.gb = gb
		self.beta = beta

		e = 0.001
		a = 1
		if b < 1 :
			a = b
			b = 1


		s2 = 1
		h = (b - a)
		S = self.f_gamV(a, n, z, Vo, Ko, kk, gamVo, gb, beta) + self.f_gamV(b, n, z, Vo, Ko, kk, gamVo, gb, beta)
		x=1+e
		while x>e:
			s3 = s2
			h = h / 2
			s1 = 0
			x = a + h
			while x < b:
				s1 = s1 + 2 * self.f_gamV(x, n, z, Vo, Ko, kk, gamVo, gb, beta)
				x = x + 2 * h

			S = S + s1
			s2 = (S + s1) * h / 3
			x = abs(s3 - s2) / 15


		if b > 1:
			I_gamV = -s2
		else:
			I_gamV = s2

		return I_gamV

###############################################################################

	def F(self,n, z, Vo, Ko, kk, Tr, x, expp, QBo, d, mb, QB1o, d1, mb1, QE1o, mE1, QE2o, mE2, TK, gamVo, beta, gb, ao, m, mm, ae):

		self.n = n
		self.z = z
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk
		self.Tr = Tr
		self.x = x
		self.expp = expp
		self.QBo = QBo
		self.d = d
		self.mb = mb
		self.QB1o = QB1o
		self.d1 = d1
		self.mb1= mb1
		self.QE1o = QE1o
		self.mE1 = mE1
		self.QE2o = QE2o
		self.mE2 = mE2
		self.TK = TK
		self.gamVo = gamVo
		self.beta = beta
		self.gb = gb
		self.ao = ao
		self.m = m
		self.mm = mm
		self.ae = ae


		R = 8.31451

		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))
		ff = x ** (1 / 3)
		aa = 1.5 * (kk - 3) - fw
		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)
		KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)
		ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3
		kkx = (ex + ex1 - ex2) / (-KT / ff) / 3
		gt = gb - beta * x ** (1 / 3)
		gtx = -beta / 3 * x ** (-2 / 3)
		gamV = (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt) + gamVo
		ff2 = (x + 0.00001) ** (1 / 3)
		KT2 = Ko * 1000 / ff2 ** 6 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) + (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * (-fw) + (1 / ff2 - 1) * (aa - 2 * aa * ff2)) * (-(x + 0.00001))
		ex = 3 / ff2 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex1 = 1 / ff2 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff2)) * fw * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff2)) * ((10 / ff2 ** 3 - 4 / ff2 ** 2) * (1 + aa * ff2 - aa * ff2 ** 2) + (-5 / ff2 ** 2 + 4 / ff2) * (aa - 2 * aa * ff2) + fw / ff2 ** 2 * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (aa - 2 * aa * ff2) * fw - (aa - 2 * aa * ff2) / ff2 ** 2 - 2 * aa * (1 / ff2 - 1)) / ff2 ** 3
		kkx2 = (ex + ex1 - ex2) / (-KT2 / ff2) / 3

		ff1 = (x - 0.00001) ** (1 / 3)
		KT1 = Ko * 1000 / ff1 ** 6 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) + (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * (-fw) + (1 / ff1 - 1) * (aa - 2 * aa * ff1)) * (-(x - 0.00001))
		ex = 3 / ff1 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex1 = 1 / ff1 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff1)) * fw * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff1)) * ((10 / ff1 ** 3 - 4 / ff1 ** 2) * (1 + aa * ff1 - aa * ff1 ** 2) + (-5 / ff1 ** 2 + 4 / ff1) * (aa - 2 * aa * ff1) + fw / ff1 ** 2 * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (aa - 2 * aa * ff1) * fw - (aa - 2 * aa * ff1) / ff1 ** 2 - 2 * aa * (1 / ff1 - 1)) / ff1 ** 3
		kkx1 = (ex + ex1 - ex2) / (-KT1 / ff1) / 3

		dkkdx = (kkx2 - kkx1) / (0.00002)
		qV = -1 / 2 * (-6 * KT * kkx ** 2 * Px * gt / x + 6 * KT * dkkdx * Px * gt + 6 * KT * kkx * KT * gt / x - 6 * KT * kkx * Px * gtx + 4 * gt ** 2 * KT * kkx * Px / x - 4 * gt ** 2 * KT ** 2 / x - 9 * KT ** 2 * dkkdx + 6 * gtx * KT ** 2) / (3 * KT - 2 * Px * gt) ** 2 * x / gamV

		a = ao / 1000000 * x ** m

		QB = QBo * expp
		QB1 = QB1o * expp
		QE1 = QE1o * expp
		QE2 = QE2o * expp

		gg = d * np.log(1 + QB / TK / d)
		ex = np.exp(QB / TK)
		FB = mb * R * ((d - 1) * QB / 2 / d - TK * np.log(1 + 1 / (np.exp(gg) - 1)))

		gg1 = d1 * np.log(1 + QB1 / TK / d1)
		ex = np.exp(QB1 / TK)
		FB1 = mb1 * R * ((d1 - 1) * QB1 / 2 / d1 - TK * np.log(1 + 1 / (np.exp(gg1) - 1)))

		ex = np.exp(QE1 / TK)
		FE1 = mE1 * R * (QE1 / 2 + TK * np.log(1 - 1 / ex))
		ex = np.exp(QE2 / TK)
		FE2 = mE2 * R * (QE2 / 2 + TK * np.log(1 - 1 / np.exp(QE2 / TK)))

		ggr = d * np.log(1 + QB / Tr / d)
		ex = np.exp(QB / Tr)
		FBr = mb * R * ((d - 1) * QB / 2 / d - Tr * np.log(1 + 1 / (np.exp(ggr) - 1)))
		ggr1 = d1 * np.log(1 + QB1 / Tr / d1)
		ex = np.exp(QB1 / Tr)
		FBr1 = mb1 * R * ((d1 - 1) * QB1 / 2 / d1 - Tr * np.log(1 + 1 / (np.exp(ggr1) - 1)))

		ex = np.exp(QE1 / Tr)
		FE1r = mE1 * R * (QE1 / 2 + Tr * np.log(1 - 1 / ex))
		ex = np.exp(QE2 / Tr)
		FE2r = mE2 * R * (QE2 / 2 + Tr * np.log(1 - 1 / ex))

		Fa = -1.5 * n * R * ao / 1000000 * x ** (m) * (TK ** 2 - Tr ** 2)
		Fel = -1.5 * n * R * ae / 1000000 * x ** (mm) * (TK ** 2 - Tr ** 2)

		F = FB + FB1 + FE1 + FE2 - FBr - FBr1 - FE1r - FE2r + Fel + Fa

		return F

###############################################################################################################################

	def S(self,n, z, Vo, Ko, kk, Tr, x, expp, QBo, d, mb, QB1o, d1, mb1, QE1o, mE1, QE2o, mE2, TK, gamVo, beta, gb, ao, m, mm, ae):

		self.n = n
		self.z = z
		self.Vo = Vo
		self.kk = kk
		self.Tr = Tr
		self.x = x
		self.expp = expp
		self.QBo = QBo
		self.d = d
		self.mb = mb
		self.QB1o = QB1o
		self.d1 = d1
		self.mb1 = mb1
		self.QE1o = QE1o
		self.mE1 = mE1
		self.QE2o = QE2o
		self.mE2 = mE2
		self.TK = TK

		R = 8.31451

		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))
		ff = x ** (1 / 3)
		aa = 1.5 * (kk - 3) - fw
		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)
		KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)
		ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3
		kkx = (ex + ex1 - ex2) / (-KT / ff) / 3
		gt = gb - beta * x ** (1 / 3)
		gtx = -beta / 3 * x ** (-2 / 3)
		gamV = (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt) + gamVo
		ff2 = (x + 0.00001) ** (1 / 3)
		KT2 = Ko * 1000 / ff2 ** 6 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) + (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * (-fw) + (1 / ff2 - 1) * (aa - 2 * aa * ff2)) * (-(x + 0.00001))
		ex = 3 / ff2 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex1 = 1 / ff2 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff2)) * fw * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff2)) * ((10 / ff2 ** 3 - 4 / ff2 ** 2) * (1 + aa * ff2 - aa * ff2 ** 2) + (-5 / ff2 ** 2 + 4 / ff2) * (aa - 2 * aa * ff2) + fw / ff2 ** 2 * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (aa - 2 * aa * ff2) * fw - (aa - 2 * aa * ff2) / ff2 ** 2 - 2 * aa * (1 / ff2 - 1)) / ff2 ** 3
		kkx2 = (ex + ex1 - ex2) / (-KT2 / ff2) / 3
		ff1 = (x - 0.00001) ** (1 / 3)
		KT1 = Ko * 1000 / ff1 ** 6 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) + (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * (-fw) + (1 / ff1 - 1) * (aa - 2 * aa * ff1)) * (-(x - 0.00001))
		ex = 3 / ff1 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex1 = 1 / ff1 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff1)) * fw * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff1)) * ((10 / ff1 ** 3 - 4 / ff1 ** 2) * (1 + aa * ff1 - aa * ff1 ** 2) + (-5 / ff1 ** 2 + 4 / ff1) * (aa - 2 * aa * ff1) + fw / ff1 ** 2 * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (aa - 2 * aa * ff1) * fw - (aa - 2 * aa * ff1) / ff1 ** 2 - 2 * aa * (1 / ff1 - 1)) / ff1 ** 3
		kkx1 = (ex + ex1 - ex2) / (-KT1 / ff1) / 3
		dkkdx = (kkx2 - kkx1) / (0.00002)
		qV = -1 / 2 * (-6 * KT * kkx ** 2 * Px * gt / x + 6 * KT * dkkdx * Px * gt + 6 * KT * kkx * KT * gt / x - 6 * KT * kkx * Px * gtx + 4 * gt ** 2 * KT * kkx * Px / x - 4 * gt ** 2 * KT ** 2 / x - 9 * KT ** 2 * dkkdx + 6 * gtx * KT ** 2) / (3 * KT - 2 * Px * gt) ** 2 * x / gamV
		a = ao / 1000000 * x ** m
		QB = QBo * expp
		QB1 = QB1o * expp
		QE1 = QE1o * expp
		QE2 = QE2o * expp

		gg = d * np.log(1 + QB / TK / d)
		expS = 1 / (np.exp(gg) - 1)
		ex = np.exp(QB / TK)
		SB = mb * R * (np.log(1 + expS) + QB * d * expS / (TK * d + QB))

		gg1 = d1 * np.log(1 + QB1 / TK / d1)
		expS1 = 1 / (np.exp(gg1) - 1)
		ex = np.exp(QB1 / TK)
		SB1 = mb1 * R * (np.log(1 + expS1) + QB1 * d1 * expS1 / (TK * d1 + QB1))



		exp1 = np.exp(QE1 / TK)
		SE1 = mE1 * R * (-np.log(1 - 1 / exp1) + QE1 / TK / (exp1 - 1))

		exp2 = np.exp(QE2 / TK)
		SE2 = mE2 * R * (-np.log(1 - 1 / exp2) + QE2 / TK / (exp2 - 1))
		Sa = 3 * n * R * ao / 1000000 * x ** (m) * (TK)
		See = 3 * n * R * ae / 1000000 * x ** (mm) * (TK)

		S = SB + SB1 + SE1 + SE2 + See + Sa

		return S


########################################################################################################################################################################################################

	def CCv(self,n, z, Vo, Ko, kk, Tr, x, expp, QBo, d, mb, QB1o, d1, mb1, QE1o, mE1, QE2o, mE2, TK, gamVo, beta, gb, ao, m, mm, ae):

		self.n = n
		self.z = z
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk
		self.Tr = Tr
		self.x = x
		self.expp = expp
		self.QBo = QBo
		self.d = d
		self.mb = mb
		self.QB1o = QB1o
		self.d1 = d1
		self.mb1 = mb1
		self.QE1o = QE1o

		R = 8.31451

		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))
		ff = x ** (1 / 3)
		aa = 1.5 * (kk - 3) - fw
		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)
		KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)
		ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3
		kkx = (ex + ex1 - ex2) / (-KT / ff) / 3
		gt = gb - beta * x ** (1 / 3)
		gtx = -beta / 3 * x ** (-2 / 3)
		gamV = (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt) + gamVo
		ff2 = (x + 0.00001) ** (1 / 3)
		KT2 = Ko * 1000 / ff2 ** 6 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) + (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * (-fw) + (1 / ff2 - 1) * (aa - 2 * aa * ff2)) * (-(x + 0.00001))
		ex = 3 / ff2 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex1 = 1 / ff2 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff2)) * fw * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff2)) * ((10 / ff2 ** 3 - 4 / ff2 ** 2) * (1 + aa * ff2 - aa * ff2 ** 2) + (-5 / ff2 ** 2 + 4 / ff2) * (aa - 2 * aa * ff2) + fw / ff2 ** 2 * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (aa - 2 * aa * ff2) * fw - (aa - 2 * aa * ff2) / ff2 ** 2 - 2 * aa * (1 / ff2 - 1)) / ff2 ** 3
		kkx2 = (ex + ex1 - ex2) / (-KT2 / ff2) / 3
		ff1 = (x - 0.00001) ** (1 / 3)
		KT1 = Ko * 1000 / ff1 ** 6 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) + (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * (-fw) + (1 / ff1 - 1) * (aa - 2 * aa * ff1)) * (-(x - 0.00001))
		ex = 3 / ff1 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex1 = 1 / ff1 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff1)) * fw * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff1)) * ((10 / ff1 ** 3 - 4 / ff1 ** 2) * (1 + aa * ff1 - aa * ff1 ** 2) + (-5 / ff1 ** 2 + 4 / ff1) * (aa - 2 * aa * ff1) + fw / ff1 ** 2 * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (aa - 2 * aa * ff1) * fw - (aa - 2 * aa * ff1) / ff1 ** 2 - 2 * aa * (1 / ff1 - 1)) / ff1 ** 3
		kkx1 = (ex + ex1 - ex2) / (-KT1 / ff1) / 3

		dkkdx = (kkx2 - kkx1) / (0.00002)
		qV = -1 / 2 * (-6 * KT * kkx ** 2 * Px * gt / x + 6 * KT * dkkdx * Px * gt + 6 * KT * kkx * KT * gt / x - 6 * KT * kkx * Px * gtx + 4 * gt ** 2 * KT * kkx * Px / x - 4 * gt ** 2 * KT ** 2 / x - 9 * KT ** 2 * dkkdx + 6 * gtx * KT ** 2) / (3 * KT - 2 * Px * gt) ** 2 * x / gamV
		a = ao / 1000000 * x ** m

		QB = QBo * expp
		QB1 = QB1o * expp
		QE1 = QE1o * expp
		QE2 = QE2o * expp

		gg = d * np.log(1 + QB / TK / d)
		b = 1 / (np.exp(gg) - 1)
		expc = np.exp(QB / TK)
		CvB = mb * R * ((QB * d / (TK * d + QB)) ** 2 * b * (1 / d + 1 + b))

		gg1 = d1 * np.log(1 + QB1 / TK / d1)
		b1 = 1 / (np.exp(gg1) - 1)
		expc1 = np.exp(QB1 / TK)
		CvB1 = mb1 * R * ((QB1 * d1 / (TK * d1 + QB1)) ** 2 * b1 * (1 / d1 + 1 + b1))


		ex1 = np.exp(QE1 / TK)
		CvE1 = mE1 * R * (QE1 ** 2 / TK ** 2 * ex1 / (ex1 - 1) ** 2)

		ex2 = np.exp(QE2 / TK)
		CvE2 = mE2 * R * (QE2 ** 2 / TK ** 2 * ex2 / (ex2 - 1) ** 2)
		Cva = 3 * n * R * ao / 1000000 * x ** (m) * (TK)
		CvE = 3 * n * R * ae / 1000000 * x ** (mm) * (TK)

		CCv = CvB + CvB1 + CvE1 + CvE2 + CvE + Cva

		return CCv


##################################################################################################################################

	def Pth(self,n, z, Vo, Ko, kk, Tr, x, expp, V, QBo, d, mb, QB1o, d1, mb1, QE1o, mE1, QE2o, mE2, TK, gamVo, beta, gb, ao, m, mm, ae):

		self.n = n
		self.z = z
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk
		self.Tr = Tr
		self.x = x
		self.expp = expp
		self.V = V
		self.QBo = QBo
		self.d = d
		self.mb = mb
		self.QB1o = QB1o
		self.d1 = d1
		self.mb1 = mb1
		self.QE1o = QE1o
		self.mE1 = mE1
		self.QE2o = QE2o
		self.mE2 = mE2
		self.TK = TK
		self.gamVo = gamVo
		self.beta = beta
		self.gb = gb
		self.ao = ao
		self.m = m
		self.mm = mm
		self.ae = ae


		R = 8.31451

		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))
		ff = x ** (1 / 3)
		aa = 1.5 * (kk - 3) - fw
		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)
		KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)
		ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3
		kkx = (ex + ex1 - ex2) / (-KT / ff) / 3
		gt = gb - beta * x ** (1 / 3)
		gtx = -beta / 3 * x ** (-2 / 3)
		gamV = (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt) + gamVo
		ff2 = (x + 0.00001) ** (1 / 3)
		KT2 = Ko * 1000 / ff2 ** 6 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) + (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * (-fw) + (1 / ff2 - 1) * (aa - 2 * aa * ff2)) * (-(x + 0.00001))
		ex = 3 / ff2 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex1 = 1 / ff2 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff2)) * fw * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff2)) * ((10 / ff2 ** 3 - 4 / ff2 ** 2) * (1 + aa * ff2 - aa * ff2 ** 2) + (-5 / ff2 ** 2 + 4 / ff2) * (aa - 2 * aa * ff2) + fw / ff2 ** 2 * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (aa - 2 * aa * ff2) * fw - (aa - 2 * aa * ff2) / ff2 ** 2 - 2 * aa * (1 / ff2 - 1)) / ff2 ** 3
		kkx2 = (ex + ex1 - ex2) / (-KT2 / ff2) / 3
		ff1 = (x - 0.00001) ** (1 / 3)
		KT1 = Ko * 1000 / ff1 ** 6 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) + (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * (-fw) + (1 / ff1 - 1) * (aa - 2 * aa * ff1)) * (-(x - 0.00001))
		ex = 3 / ff1 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex1 = 1 / ff1 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff1)) * fw * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff1)) * ((10 / ff1 ** 3 - 4 / ff1 ** 2) * (1 + aa * ff1 - aa * ff1 ** 2) + (-5 / ff1 ** 2 + 4 / ff1) * (aa - 2 * aa * ff1) + fw / ff1 ** 2 * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (aa - 2 * aa * ff1) * fw - (aa - 2 * aa * ff1) / ff1 ** 2 - 2 * aa * (1 / ff1 - 1)) / ff1 ** 3
		kkx1 = (ex + ex1 - ex2) / (-KT1 / ff1) / 3
		dkkdx = (kkx2 - kkx1) / (0.00002)
		qV = -1 / 2 * (-6 * KT * kkx ** 2 * Px * gt / x + 6 * KT * dkkdx * Px * gt + 6 * KT * kkx * KT * gt / x - 6 * KT * kkx * Px * gtx + 4 * gt ** 2 * KT * kkx * Px / x - 4 * gt ** 2 * KT ** 2 / x - 9 * KT ** 2 * dkkdx + 6 * gtx * KT ** 2) / (3 * KT - 2 * Px * gt) ** 2 * x / gamV
		a = ao / 1000000 * x ** m

		QB = QBo * expp
		QB1 = QB1o * expp
		QE1 = QE1o * expp
		QE2 = QE2o * expp

		ggr = d * np.log(1 + QB / Tr / d)
		br = 1 / (np.exp(ggr) - 1)
		ex1r = np.exp(QB / Tr)
		PBr = mb * R * ((QB * (d - 1) / 2 / d + Tr * QB * d * br / (Tr * d + QB)) * gamV / V)

		gg = d * np.log(1 + QB / TK / d)
		b = 1 / (np.exp(gg) - 1)
		ex1 = np.exp(QB / TK)
		PB = mb * R * ((QB * (d - 1) / 2 / d + TK * QB * d * b / (TK * d + QB)) * gamV / V)

		gg1r = d1 * np.log(1 + QB1 / Tr / d1)
		b1r = 1 / (np.exp(gg1r) - 1)
		ex2r = np.exp(QB1 / Tr)
		PB1r = mb1 * R * ((QB1 * (d1 - 1) / 2 / d1 + Tr * QB1 * d1 * b1r / (Tr * d1 + QB1)) * gamV / V)

		gg1 = d1 * np.log(1 + QB1 / TK / d1)
		b1 = 1 / (np.exp(gg1) - 1)
		ex2 = np.exp(QB1 / TK)
		PB1 = mb1 * R * ((QB1 * (d1 - 1) / 2 / d1 + TK * QB1 * d1 * b1 / (TK * d1 + QB1)) * gamV / V)

		e1 = np.exp(QE1 / TK)
		PE1 = mE1 * R * ((QE1 / 2 + QE1 / (e1 - 1)) * gamV / V)

		e2 = np.exp(QE2 / TK)
		PE2 = mE2 * R * ((QE2 / 2 + QE2 / (e2 - 1)) * gamV / V)

		e1r = np.exp(QE1 / Tr)
		PE1r = mE1 * R * ((QE1 / 2 + QE1 / (e1r - 1)) * gamV / V)

		e2r = np.exp(QE2 / Tr)
		PE2r = mE2 * R * ((QE2 / 2 + QE2 / (e2r - 1)) * gamV / V)
		Pea = 3 / 2 * n * R * ao / 1000000 * x ** (m) * (m) / V * (TK ** 2 - Tr ** 2)
		Pee = 3 / 2 * n * R * ae / 1000000 * x ** (mm) * (mm) / V * (TK ** 2 - Tr ** 2)

		Pth = PB + PB1 + PE1 + PE2 - PBr - PB1r - PE1r - PE2r + Pee + Pea
		
		return Pth

########################################################################################################################################################################


	def KTth(self,n, z, Vo, Ko, kk, Tr, x, expp, V, QBo, d, mb, QB1o, d1, mb1, QE1o, mE1, QE2o, mE2, TK, gamVo, beta, gb, ao, m, mm, ae):

		self.n = n
		self.z = z
		self.Vo = Vo
		self.Ko = Ko
		self.kk = kk
		self.Tr = Tr
		self.x = x
		self.expp = expp
		self.V = V
		self.QBo = QBo
		self.d = d
		self.mb = mb
		self.QB1o = QB1o
		self.d1 = d1
		self.mb1 = mb1
		self.QE1o = QE1o
		self.mE1 = mE1
		self.QE2o = QE2o
		self.mE2 = mE2
		self.TK = TK
		self.gamVo = gamVo
		self.beta = beta
		self.gb = gb
		self.ao = ao
		self.m = m
		self.mm = mm
		self.ae = ae



		R = 8.31451

		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))
		ff = x ** (1 / 3)
		aa = 1.5 * (kk - 3) - fw
		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)
		KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)
		ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3
		kkx = (ex + ex1 - ex2) / (-KT / ff) / 3

		gt = gb - beta * x ** (1 / 3)
		gtx = -beta / 3 * x ** (-2 / 3)
		gamV = (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt) + gamVo
		ff2 = (x + 0.00001) ** (1 / 3)
		KT2 = Ko * 1000 / ff2 ** 6 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) + (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * (-fw) + (1 / ff2 - 1) * (aa - 2 * aa * ff2)) * (-(x + 0.00001))
		ex = 3 / ff2 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex1 = 1 / ff2 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff2)) * fw * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff2)) * ((10 / ff2 ** 3 - 4 / ff2 ** 2) * (1 + aa * ff2 - aa * ff2 ** 2) + (-5 / ff2 ** 2 + 4 / ff2) * (aa - 2 * aa * ff2) + fw / ff2 ** 2 * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (aa - 2 * aa * ff2) * fw - (aa - 2 * aa * ff2) / ff2 ** 2 - 2 * aa * (1 / ff2 - 1)) / ff2 ** 3
		kkx2 = (ex + ex1 - ex2) / (-KT2 / ff2) / 3
		
		ff1 = (x - 0.00001) ** (1 / 3)
		KT1 = Ko * 1000 / ff1 ** 6 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) + (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * (-fw) + (1 / ff1 - 1) * (aa - 2 * aa * ff1)) * (-(x - 0.00001))
		ex = 3 / ff1 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex1 = 1 / ff1 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff1)) * fw * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff1)) * ((10 / ff1 ** 3 - 4 / ff1 ** 2) * (1 + aa * ff1 - aa * ff1 ** 2) + (-5 / ff1 ** 2 + 4 / ff1) * (aa - 2 * aa * ff1) + fw / ff1 ** 2 * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (aa - 2 * aa * ff1) * fw - (aa - 2 * aa * ff1) / ff1 ** 2 - 2 * aa * (1 / ff1 - 1)) / ff1 ** 3
		kkx1 = (ex + ex1 - ex2) / (-KT1 / ff1) / 3
		
		dkkdx = (kkx2 - kkx1) / (0.00002)
		qV = -1 / 2 * (-6 * KT * kkx ** 2 * Px * gt / x + 6 * KT * dkkdx * Px * gt + 6 * KT * kkx * KT * gt / x - 6 * KT * kkx * Px * gtx + 4 * gt ** 2 * KT * kkx * Px / x - 4 * gt ** 2 * KT ** 2 / x - 9 * KT ** 2 * dkkdx + 6 * gtx * KT ** 2) / (3 * KT - 2 * Px * gt) ** 2 * x / gamV
		a = ao / 1000000 * x ** m

		QB = QBo * expp
		QB1 = QB1o * expp
		QE1 = QE1o * expp
		QE2 = QE2o * expp
		VV = Vo * x

		gg = d * np.log(1 + QB / Tr / d)
		ex = np.exp(QB / Tr)
		b = 1 / (np.exp(gg) - 1)
		KTB = mb * R * ((Tr * QB * d * b / (Tr * d + QB)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * Tr / VV * (QB * d / (Tr * d + QB)) ** 2 * b * (1 / d + 1 + b))
		dgV = 1 / 24 * a * mb * R * QB * (12 * gamV ** 2 * QB ** 3 * ex - 2 * m * gamV * QB * Tr ** 2 - 12 * m * gamV * QB ** 2 * Tr * ex - 2 * qV * gamV * QB * Tr ** 2 - 12 * m * gamV * QB ** 2 * Tr * ex + 16 * gamV * QB * Tr ** 2 * ex + 12 * gamV * QB ** 2 * Tr * ex + 4 * gamV ** 2 * QB * Tr ** 2 + 32 * gamV ** 2 * QB * Tr ** 2 * ex + 60 * gamV ** 2 * QB ** 2 * Tr * ex - 16 * qV * gamV * QB * Tr ** 2 * ex - 12 * qV * gamV * QB ** 2 * Tr * ex - 8 * m * QB * Tr ** 2 * ex - 2 * m * gamV * QB * Tr ** 2 + 8 * m ** 2 * QB * Tr ** 2 * ex - 16 * m * gamV * QB * Tr ** 2 * ex + m ** 2 * QB * Tr ** 2 - 16 * m * gamV * QB * Tr ** 2 * ex - m * QB * Tr ** 2 + 2 * gamV * QB * Tr ** 2 + 12 * gamV ** 2 * QB ** 3 * ex ** 3 - 36 * gamV * QB * Tr ** 2 * ex ** 2 - 12 * gamV * QB ** 2 * Tr * ex ** 3 + 16 * gamV * QB * Tr ** 2 * ex ** 3 - 60 * gamV ** 2 * QB ** 2 * Tr * ex ** 3 + 2 * gamV * QB * Tr ** 2 * ex ** 4) / VV / Tr ** 2 / (ex - 1) ** 4
		d2gV = 1 / 24 * a * mb * R * QB * (-16 * qV * gamV * QB * Tr ** 2 * ex ** 3 - 72 * gamV ** 2 * QB * Tr ** 2 * ex ** 2 + 32 * gamV ** 2 * QB * Tr ** 2 * ex ** 3 + 4 * gamV ** 2 * QB * Tr ** 2 * ex ** 4 + 12 * m * gamV * QB ** 2 * Tr * ex ** 3 + 12 * m * gamV * QB ** 2 * Tr * ex ** 3 + 12 * qV * gamV * QB ** 2 * Tr * ex ** 3 + 36 * qV * gamV * QB * Tr ** 2 * ex ** 2 + 18 * m * QB * Tr ** 2 * ex ** 2 - 8 * m * QB * Tr ** 2 * ex ** 3 - m * QB * Tr ** 2 * ex ** 4 - 2 * qV * gamV * QB * Tr ** 2 * ex ** 4 - 18 * m ** 2 * QB * Tr ** 2 * ex ** 2 + 8 * m ** 2 * QB * Tr ** 2 * ex ** 3 + m ** 2 * QB * Tr ** 2 * ex ** 4 - 2 * m * gamV * QB * Tr ** 2 * ex ** 4 + 36 * m * gamV * QB * Tr ** 2 * ex ** 2 - 16 * m * gamV * QB * Tr ** 2 * ex ** 3 - 2 * m * gamV * QB * Tr ** 2 * ex ** 4 + 48 * gamV ** 2 * QB ** 3 * ex ** 2 - 16 * m * gamV * QB * Tr ** 2 * ex ** 3 + 36 * m * gamV * QB * Tr ** 2 * ex ** 2) / VV / Tr ** 2 / (ex - 1) ** 4
		dPthBr = (KTB)

		gg = d * np.log(1 + QB / TK / d)
		ex = np.exp(QB / TK)
		b = 1 / (np.exp(gg) - 1)
		KTB = mb * R * ((TK * QB * d * b / (TK * d + QB)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * TK / VV * (QB * d / (TK * d + QB)) ** 2 * b * (1 / d + 1 + b))
		dgV = 1 / 24 * a * mb * R * QB * (12 * gamV ** 2 * QB ** 3 * ex - 2 * m * gamV * QB * TK ** 2 - 12 * m * gamV * QB ** 2 * TK * ex - 2 * qV * gamV * QB * TK ** 2 - 12 * m * gamV * QB ** 2 * TK * ex + 16 * gamV * QB * TK ** 2 * ex + 12 * gamV * QB ** 2 * TK * ex + 4 * gamV ** 2 * QB * TK ** 2 + 32 * gamV ** 2 * QB * TK ** 2 * ex + 60 * gamV ** 2 * QB ** 2 * TK * ex - 16 * qV * gamV * QB * TK ** 2 * ex - 12 * qV * gamV * QB ** 2 * TK * ex - 8 * m * QB * TK ** 2 * ex - 2 * m * gamV * QB * TK ** 2 + 8 * m ** 2 * QB * TK ** 2 * ex - 16 * m * gamV * QB * TK ** 2 * ex + m ** 2 * QB * TK ** 2 - 16 * m * gamV * QB * TK ** 2 * ex - m * QB * TK ** 2 + 2 * gamV * QB * TK ** 2 + 12 * gamV ** 2 * QB ** 3 * ex ** 3 - 36 * gamV * QB * TK ** 2 * ex ** 2 - 12 * gamV * QB ** 2 * TK * ex ** 3 + 16 * gamV * QB * TK ** 2 * ex ** 3 - 60 * gamV ** 2 * QB ** 2 * TK * ex ** 3 + 2 * gamV * QB * TK ** 2 * ex ** 4) / VV / TK ** 2 / (ex - 1) ** 4
		d2gV = 1 / 24 * a * mb * R * QB * (-16 * qV * gamV * QB * TK ** 2 * ex ** 3 - 72 * gamV ** 2 * QB * TK ** 2 * ex ** 2 + 32 * gamV ** 2 * QB * TK ** 2 * ex ** 3 + 4 * gamV ** 2 * QB * TK ** 2 * ex ** 4 + 12 * m * gamV * QB ** 2 * TK * ex ** 3 + 12 * m * gamV * QB ** 2 * TK * ex ** 3 + 12 * qV * gamV * QB ** 2 * TK * ex ** 3 + 36 * qV * gamV * QB * TK ** 2 * ex ** 2 + 18 * m * QB * TK ** 2 * ex ** 2 - 8 * m * QB * TK ** 2 * ex ** 3 - m * QB * TK ** 2 * ex ** 4 - 2 * qV * gamV * QB * TK ** 2 * ex ** 4 - 18 * m ** 2 * QB * TK ** 2 * ex ** 2 + 8 * m ** 2 * QB * TK ** 2 * ex ** 3 + m ** 2 * QB * TK ** 2 * ex ** 4 - 2 * m * gamV * QB * TK ** 2 * ex ** 4 + 36 * m * gamV * QB * TK ** 2 * ex ** 2 - 16 * m * gamV * QB * TK ** 2 * ex ** 3 - 2 * m * gamV * QB * TK ** 2 * ex ** 4 + 48 * gamV ** 2 * QB ** 3 * ex ** 2 - 16 * m * gamV * QB * TK ** 2 * ex ** 3 + 36 * m * gamV * QB * TK ** 2 * ex ** 2) / VV / TK ** 2 / (ex - 1) ** 4
		dPthB = (KTB)

		gg = d1 * np.log(1 + QB1 / Tr / d1)
		ex = np.exp(QB1 / Tr)
		b = 1 / (np.exp(gg) - 1)
		KTB = mb1 * R * ((Tr * QB1 * d1 * b / (Tr * d1 + QB1)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * Tr / VV * (QB1 * d1 / (Tr * d1 + QB1)) ** 2 * b * (1 / d1 + 1 + b))
		dgV = 1 / 24 * a * mb1 * R * QB1 * (12 * gamV ** 2 * QB1 ** 3 * ex - 2 * m * gamV * QB1 * Tr ** 2 - 12 * m * gamV * QB1 ** 2 * Tr * ex - 2 * qV * gamV * QB1 * Tr ** 2 - 12 * m * gamV * QB1 ** 2 * Tr * ex + 16 * gamV * QB1 * Tr ** 2 * ex + 12 * gamV * QB1 ** 2 * Tr * ex + 4 * gamV ** 2 * QB1 * Tr ** 2 + 32 * gamV ** 2 * QB1 * Tr ** 2 * ex + 60 * gamV ** 2 * QB1 ** 2 * Tr * ex - 16 * qV * gamV * QB1 * Tr ** 2 * ex - 12 * qV * gamV * QB1 ** 2 * Tr * ex - 8 * m * QB1 * Tr ** 2 * ex - 2 * m * gamV * QB1 * Tr ** 2 + 8 * m ** 2 * QB1 * Tr ** 2 * ex - 16 * m * gamV * QB1 * Tr ** 2 * ex + m ** 2 * QB1 * Tr ** 2 - 16 * m * gamV * QB1 * Tr ** 2 * ex - m * QB1 * Tr ** 2 + 2 * gamV * QB1 * Tr ** 2 + 12 * gamV ** 2 * QB1 ** 3 * ex ** 3 - 36 * gamV * QB1 * Tr ** 2 * ex ** 2 - 12 * gamV * QB1 ** 2 * Tr * ex ** 3 + 16 * gamV * QB1 * Tr ** 2 * ex ** 3 - 60 * gamV ** 2 * QB1 ** 2 * Tr * ex ** 3 + 2 * gamV * QB1 * Tr ** 2 * ex ** 4) / VV / Tr ** 2 / (ex - 1) ** 4
		d2gV = 1 / 24 * a * mb1 * R * QB1 * (-16 * qV * gamV * QB1 * Tr ** 2 * ex ** 3 - 72 * gamV ** 2 * QB1 * Tr ** 2 * ex ** 2 + 32 * gamV ** 2 * QB1 * Tr ** 2 * ex ** 3 + 4 * gamV ** 2 * QB1 * Tr ** 2 * ex ** 4 + 12 * m * gamV * QB1 ** 2 * Tr * ex ** 3 + 12 * m * gamV * QB1 ** 2 * Tr * ex ** 3 + 12 * qV * gamV * QB1 ** 2 * Tr * ex ** 3 + 36 * qV * gamV * QB1 * Tr ** 2 * ex ** 2 + 18 * m * QB1 * Tr ** 2 * ex ** 2 - 8 * m * QB1 * Tr ** 2 * ex ** 3 - m * QB1 * Tr ** 2 * ex ** 4 - 2 * qV * gamV * QB1 * Tr ** 2 * ex ** 4 - 18 * m ** 2 * QB1 * Tr ** 2 * ex ** 2 + 8 * m ** 2 * QB1 * Tr ** 2 * ex ** 3 + m ** 2 * QB1 * Tr ** 2 * ex ** 4 - 2 * m * gamV * QB1 * Tr ** 2 * ex ** 4 + 36 * m * gamV * QB1 * Tr ** 2 * ex ** 2 - 16 * m * gamV * QB1 * Tr ** 2 * ex ** 3 - 2 * m * gamV * QB1 * Tr ** 2 * ex ** 4 + 48 * gamV ** 2 * QB1 ** 3 * ex ** 2 - 16 * m * gamV * QB1 * Tr ** 2 * ex ** 3 + 36 * m * gamV * QB1 * Tr ** 2 * ex ** 2) / VV / Tr ** 2 / (ex - 1) ** 4
		dPthBBr = (KTB)

		gg = d1 * np.log(1 + QB1 / TK / d1)
		ex = np.exp(QB1 / TK)
		b = 1 / (np.exp(gg) - 1)
		KTB = mb1 * R * ((TK * QB1 * d1 * b / (TK * d1 + QB1)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * TK / VV * (QB1 * d1 / (TK * d1 + QB1)) ** 2 * b * (1 / d1 + 1 + b))
		dgV = 1 / 24 * a * mb1 * R * QB1 * (12 * gamV ** 2 * QB1 ** 3 * ex - 2 * m * gamV * QB1 * TK ** 2 - 12 * m * gamV * QB1 ** 2 * TK * ex - 2 * qV * gamV * QB1 * TK ** 2 - 12 * m * gamV * QB1 ** 2 * TK * ex + 16 * gamV * QB1 * TK ** 2 * ex + 12 * gamV * QB1 ** 2 * TK * ex + 4 * gamV ** 2 * QB1 * TK ** 2 + 32 * gamV ** 2 * QB1 * TK ** 2 * ex + 60 * gamV ** 2 * QB1 ** 2 * TK * ex - 16 * qV * gamV * QB1 * TK ** 2 * ex - 12 * qV * gamV * QB1 ** 2 * TK * ex - 8 * m * QB1 * TK ** 2 * ex - 2 * m * gamV * QB1 * TK ** 2 + 8 * m ** 2 * QB1 * TK ** 2 * ex - 16 * m * gamV * QB1 * TK ** 2 * ex + m ** 2 * QB1 * TK ** 2 - 16 * m * gamV * QB1 * TK ** 2 * ex - m * QB1 * TK ** 2 + 2 * gamV * QB1 * TK ** 2 + 12 * gamV ** 2 * QB1 ** 3 * ex ** 3 - 36 * gamV * QB1 * TK ** 2 * ex ** 2 - 12 * gamV * QB1 ** 2 * TK * ex ** 3 + 16 * gamV * QB1 * TK ** 2 * ex ** 3 - 60 * gamV ** 2 * QB1 ** 2 * TK * ex ** 3 + 2 * gamV * QB1 * TK ** 2 * ex ** 4) / VV / TK ** 2 / (ex - 1) ** 4
		d2gV = 1 / 24 * a * mb1 * R * QB1 * (-16 * qV * gamV * QB1 * TK ** 2 * ex ** 3 - 72 * gamV ** 2 * QB1 * TK ** 2 * ex ** 2 + 32 * gamV ** 2 * QB1 * TK ** 2 * ex ** 3 + 4 * gamV ** 2 * QB1 * TK ** 2 * ex ** 4 + 12 * m * gamV * QB1 ** 2 * TK * ex ** 3 + 12 * m * gamV * QB1 ** 2 * TK * ex ** 3 + 12 * qV * gamV * QB1 ** 2 * TK * ex ** 3 + 36 * qV * gamV * QB1 * TK ** 2 * ex ** 2 + 18 * m * QB1 * TK ** 2 * ex ** 2 - 8 * m * QB1 * TK ** 2 * ex ** 3 - m * QB1 * TK ** 2 * ex ** 4 - 2 * qV * gamV * QB1 * TK ** 2 * ex ** 4 - 18 * m ** 2 * QB1 * TK ** 2 * ex ** 2 + 8 * m ** 2 * QB1 * TK ** 2 * ex ** 3 + m ** 2 * QB1 * TK ** 2 * ex ** 4 - 2 * m * gamV * QB1 * TK ** 2 * ex ** 4 + 36 * m * gamV * QB1 * TK ** 2 * ex ** 2 - 16 * m * gamV * QB1 * TK ** 2 * ex ** 3 - 2 * m * gamV * QB1 * TK ** 2 * ex ** 4 + 48 * gamV ** 2 * QB1 ** 3 * ex ** 2 - 16 * m * gamV * QB1 * TK ** 2 * ex ** 3 + 36 * m * gamV * QB1 * TK ** 2 * ex ** 2) / VV / TK ** 2 / (ex - 1) ** 4
		dPthBB = (KTB)


		e1 = np.exp(QE1 / TK)
		KTB = mE1 * R * ((QE1 / (e1 - 1)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * TK / VV * (QE1 / TK) ** 2 * e1 / (e1 - 1) ** 2)
		dgV = 1 / 24 * a * mE1 * R * QE1 * (12 * gamV ** 2 * QE1 ** 3 * e1 - 2 * m * gamV * QE1 * TK ** 2 - 12 * m * gamV * QE1 ** 2 * TK * e1 - 2 * qV * gamV * QE1 * TK ** 2 - 12 * m * gamV * QE1 ** 2 * TK * e1 + 16 * gamV * QE1 * TK ** 2 * e1 + 12 * gamV * QE1 ** 2 * TK * e1 + 4 * gamV ** 2 * QE1 * TK ** 2 + 32 * gamV ** 2 * QE1 * TK ** 2 * e1 + 60 * gamV ** 2 * QE1 ** 2 * TK * e1 - 16 * qV * gamV * QE1 * TK ** 2 * e1 - 12 * qV * gamV * QE1 ** 2 * TK * e1 - 8 * m * QE1 * TK ** 2 * e1 - 2 * m * gamV * QE1 * TK ** 2 + 8 * m ** 2 * QE1 * TK ** 2 * e1 - 16 * m * gamV * QE1 * TK ** 2 * e1 + m ** 2 * QE1 * TK ** 2 - 16 * m * gamV * QE1 * TK ** 2 * e1 - m * QE1 * TK ** 2 + 2 * gamV * QE1 * TK ** 2 + 12 * gamV ** 2 * QE1 ** 3 * e1 ** 3 - 36 * gamV * QE1 * TK ** 2 * e1 ** 2 - 12 * gamV * QE1 ** 2 * TK * e1 ** 3 + 16 * gamV * QE1 * TK ** 2 * e1 ** 3 - 60 * gamV ** 2 * QE1 ** 2 * TK * e1 ** 3 + 2 * gamV * QE1 * TK ** 2 * e1 ** 4) / VV / TK ** 2 / (e1 - 1) ** 4
		d2gV = 1 / 24 * a * mE1 * R * QE1 * (-16 * qV * gamV * QE1 * TK ** 2 * e1 ** 3 - 72 * gamV ** 2 * QE1 * TK ** 2 * e1 ** 2 + 32 * gamV ** 2 * QE1 * TK ** 2 * e1 ** 3 + 4 * gamV ** 2 * QE1 * TK ** 2 * e1 ** 4 + 12 * m * gamV * QE1 ** 2 * TK * e1 ** 3 + 12 * m * gamV * QE1 ** 2 * TK * e1 ** 3 + 12 * qV * gamV * QE1 ** 2 * TK * e1 ** 3 + 36 * qV * gamV * QE1 * TK ** 2 * e1 ** 2 + 18 * m * QE1 * TK ** 2 * e1 ** 2 - 8 * m * QE1 * TK ** 2 * e1 ** 3 - m * QE1 * TK ** 2 * e1 ** 4 - 2 * qV * gamV * QE1 * TK ** 2 * e1 ** 4 - 18 * m ** 2 * QE1 * TK ** 2 * e1 ** 2 + 8 * m ** 2 * QE1 * TK ** 2 * e1 ** 3 + m ** 2 * QE1 * TK ** 2 * e1 ** 4 - 2 * m * gamV * QE1 * TK ** 2 * e1 ** 4 + 36 * m * gamV * QE1 * TK ** 2 * e1 ** 2 - 16 * m * gamV * QE1 * TK ** 2 * e1 ** 3 - 2 * m * gamV * QE1 * TK ** 2 * e1 ** 4 + 48 * gamV ** 2 * QE1 ** 3 * e1 ** 2 - 16 * m * gamV * QE1 * TK ** 2 * e1 ** 3 + 36 * m * gamV * QE1 * TK ** 2 * e1 ** 2) / VV / TK ** 2 / (e1 - 1) ** 4
		dPthE1 = (KTB)

		e2 = np.exp(QE2 / TK)
		KTB = mE2 * R * ((QE2 / (e2 - 1)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * TK / VV * (QE2 / TK) ** 2 * e2 / (e2 - 1) ** 2)
		dgV = 1 / 24 * a * mE2 * R * QE2 * (12 * gamV ** 2 * QE2 ** 3 * e2 - 2 * m * gamV * QE2 * TK ** 2 - 12 * m * gamV * QE2 ** 2 * TK * e2 - 2 * qV * gamV * QE2 * TK ** 2 - 12 * m * gamV * QE2 ** 2 * TK * e2 + 16 * gamV * QE2 * TK ** 2 * e2 + 12 * gamV * QE2 ** 2 * TK * e2 + 4 * gamV ** 2 * QE2 * TK ** 2 + 32 * gamV ** 2 * QE2 * TK ** 2 * e2 + 60 * gamV ** 2 * QE2 ** 2 * TK * e2 - 16 * qV * gamV * QE2 * TK ** 2 * e2 - 12 * qV * gamV * QE2 ** 2 * TK * e2 - 8 * m * QE2 * TK ** 2 * e2 - 2 * m * gamV * QE2 * TK ** 2 + 8 * m ** 2 * QE2 * TK ** 2 * e2 - 16 * m * gamV * QE2 * TK ** 2 * e2 + m ** 2 * QE2 * TK ** 2 - 16 * m * gamV * QE2 * TK ** 2 * e2 - m * QE2 * TK ** 2 + 2 * gamV * QE2 * TK ** 2 + 12 * gamV ** 2 * QE2 ** 3 * e2 ** 3 - 36 * gamV * QE2 * TK ** 2 * e2 ** 2 - 12 * gamV * QE2 ** 2 * TK * e2 ** 3 + 16 * gamV * QE2 * TK ** 2 * e2 ** 3 - 60 * gamV ** 2 * QE2 ** 2 * TK * e2 ** 3 + 2 * gamV * QE2 * TK ** 2 * e2 ** 4) / VV / TK ** 2 / (e2 - 1) ** 4
		d2gV = 1 / 24 * a * mE2 * R * QE2 * (-16 * qV * gamV * QE2 * TK ** 2 * e2 ** 3 - 72 * gamV ** 2 * QE2 * TK ** 2 * e2 ** 2 + 32 * gamV ** 2 * QE2 * TK ** 2 * e2 ** 3 + 4 * gamV ** 2 * QE2 * TK ** 2 * e2 ** 4 + 12 * m * gamV * QE2 ** 2 * TK * e2 ** 3 + 12 * m * gamV * QE2 ** 2 * TK * e2 ** 3 + 12 * qV * gamV * QE2 ** 2 * TK * e2 ** 3 + 36 * qV * gamV * QE2 * TK ** 2 * e2 ** 2 + 18 * m * QE2 * TK ** 2 * e2 ** 2 - 8 * m * QE2 * TK ** 2 * e2 ** 3 - m * QE2 * TK ** 2 * e2 ** 4 - 2 * qV * gamV * QE2 * TK ** 2 * e2 ** 4 - 18 * m ** 2 * QE2 * TK ** 2 * e2 ** 2 + 8 * m ** 2 * QE2 * TK ** 2 * e2 ** 3 + m ** 2 * QE2 * TK ** 2 * e2 ** 4 - 2 * m * gamV * QE2 * TK ** 2 * e2 ** 4 + 36 * m * gamV * QE2 * TK ** 2 * e2 ** 2 - 16 * m * gamV * QE2 * TK ** 2 * e2 ** 3 - 2 * m * gamV * QE2 * TK ** 2 * e2 ** 4 + 48 * gamV ** 2 * QE2 ** 3 * e2 ** 2 - 16 * m * gamV * QE2 * TK ** 2 * e2 ** 3 + 36 * m * gamV * QE2 * TK ** 2 * e2 ** 2) / VV / TK ** 2 / (e2 - 1) ** 4
		dPthE2 = (KTB)

		e1 = np.exp(QE1 / Tr)
		KTB = mE1 * R * ((QE1 / (e1 - 1)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * Tr / VV * (QE1 / Tr) ** 2 * e1 / (e1 - 1) ** 2)
		dgV = 1 / 24 * a * mE1 * R * QE1 * (12 * gamV ** 2 * QE1 ** 3 * e1 - 2 * m * gamV * QE1 * Tr ** 2 - 12 * m * gamV * QE1 ** 2 * Tr * e1 - 2 * qV * gamV * QE1 * Tr ** 2 - 12 * m * gamV * QE1 ** 2 * Tr * e1 + 16 * gamV * QE1 * Tr ** 2 * e1 + 12 * gamV * QE1 ** 2 * Tr * e1 + 4 * gamV ** 2 * QE1 * Tr ** 2 + 32 * gamV ** 2 * QE1 * Tr ** 2 * e1 + 60 * gamV ** 2 * QE1 ** 2 * Tr * e1 - 16 * qV * gamV * QE1 * Tr ** 2 * e1 - 12 * qV * gamV * QE1 ** 2 * Tr * e1 - 8 * m * QE1 * Tr ** 2 * e1 - 2 * m * gamV * QE1 * Tr ** 2 + 8 * m ** 2 * QE1 * Tr ** 2 * e1 - 16 * m * gamV * QE1 * Tr ** 2 * e1 + m ** 2 * QE1 * Tr ** 2 - 16 * m * gamV * QE1 * Tr ** 2 * e1 - m * QE1 * Tr ** 2 + 2 * gamV * QE1 * Tr ** 2 + 12 * gamV ** 2 * QE1 ** 3 * e1 ** 3 - 36 * gamV * QE1 * Tr ** 2 * e1 ** 2 - 12 * gamV * QE1 ** 2 * Tr * e1 ** 3 + 16 * gamV * QE1 * Tr ** 2 * e1 ** 3 - 60 * gamV ** 2 * QE1 ** 2 * Tr * e1 ** 3 + 2 * gamV * QE1 * Tr ** 2 * e1 ** 4) / VV / Tr ** 2 / (e1 - 1) ** 4
		d2gV = 1 / 24 * a * mE1 * R * QE1 * (-16 * qV * gamV * QE1 * Tr ** 2 * e1 ** 3 - 72 * gamV ** 2 * QE1 * Tr ** 2 * e1 ** 2 + 32 * gamV ** 2 * QE1 * Tr ** 2 * e1 ** 3 + 4 * gamV ** 2 * QE1 * Tr ** 2 * e1 ** 4 + 12 * m * gamV * QE1 ** 2 * Tr * e1 ** 3 + 12 * m * gamV * QE1 ** 2 * Tr * e1 ** 3 + 12 * qV * gamV * QE1 ** 2 * Tr * e1 ** 3 + 36 * qV * gamV * QE1 * Tr ** 2 * e1 ** 2 + 18 * m * QE1 * Tr ** 2 * e1 ** 2 - 8 * m * QE1 * Tr ** 2 * e1 ** 3 - m * QE1 * Tr ** 2 * e1 ** 4 - 2 * qV * gamV * QE1 * Tr ** 2 * e1 ** 4 - 18 * m ** 2 * QE1 * Tr ** 2 * e1 ** 2 + 8 * m ** 2 * QE1 * Tr ** 2 * e1 ** 3 + m ** 2 * QE1 * Tr ** 2 * e1 ** 4 - 2 * m * gamV * QE1 * Tr ** 2 * e1 ** 4 + 36 * m * gamV * QE1 * Tr ** 2 * e1 ** 2 - 16 * m * gamV * QE1 * Tr ** 2 * e1 ** 3 - 2 * m * gamV * QE1 * Tr ** 2 * e1 ** 4 + 48 * gamV ** 2 * QE1 ** 3 * e1 ** 2 - 16 * m * gamV * QE1 * Tr ** 2 * e1 ** 3 + 36 * m * gamV * QE1 * Tr ** 2 * e1 ** 2) / VV / Tr ** 2 / (e1 - 1) ** 4
		dPthE1r = (KTB)

		e2 = np.exp(QE2 / Tr)
		KTB = mE2 * R * ((QE2 / (e2 - 1)) * gamV / VV * (1 + gamV - qV) - gamV ** 2 * Tr / VV * (QE2 / Tr) ** 2 * e2 / (e2 - 1) ** 2)
		dgV = 1 / 24 * a * mE2 * R * QE2 * (12 * gamV ** 2 * QE2 ** 3 * e2 - 2 * m * gamV * QE2 * Tr ** 2 - 12 * m * gamV * QE2 ** 2 * Tr * e2 - 2 * qV * gamV * QE2 * Tr ** 2 - 12 * m * gamV * QE2 ** 2 * Tr * e2 + 16 * gamV * QE2 * Tr ** 2 * e2 + 12 * gamV * QE2 ** 2 * Tr * e2 + 4 * gamV ** 2 * QE2 * Tr ** 2 + 32 * gamV ** 2 * QE2 * Tr ** 2 * e2 + 60 * gamV ** 2 * QE2 ** 2 * Tr * e2 - 16 * qV * gamV * QE2 * Tr ** 2 * e2 - 12 * qV * gamV * QE2 ** 2 * Tr * e2 - 8 * m * QE2 * Tr ** 2 * e2 - 2 * m * gamV * QE2 * Tr ** 2 + 8 * m ** 2 * QE2 * Tr ** 2 * e2 - 16 * m * gamV * QE2 * Tr ** 2 * e2 + m ** 2 * QE2 * Tr ** 2 - 16 * m * gamV * QE2 * Tr ** 2 * e2 - m * QE2 * Tr ** 2 + 2 * gamV * QE2 * Tr ** 2 + 12 * gamV ** 2 * QE2 ** 3 * e2 ** 3 - 36 * gamV * QE2 * Tr ** 2 * e2 ** 2 - 12 * gamV * QE2 ** 2 * Tr * e2 ** 3 + 16 * gamV * QE2 * Tr ** 2 * e2 ** 3 - 60 * gamV ** 2 * QE2 ** 2 * Tr * e2 ** 3 + 2 * gamV * QE2 * Tr ** 2 * e2 ** 4) / VV / Tr ** 2 / (e2 - 1) ** 4
		d2gV = 1 / 24 * a * mE2 * R * QE2 * (-16 * qV * gamV * QE2 * Tr ** 2 * e2 ** 3 - 72 * gamV ** 2 * QE2 * Tr ** 2 * e2 ** 2 + 32 * gamV ** 2 * QE2 * Tr ** 2 * e2 ** 3 + 4 * gamV ** 2 * QE2 * Tr ** 2 * e2 ** 4 + 12 * m * gamV * QE2 ** 2 * Tr * e2 ** 3 + 12 * m * gamV * QE2 ** 2 * Tr * e2 ** 3 + 12 * qV * gamV * QE2 ** 2 * Tr * e2 ** 3 + 36 * qV * gamV * QE2 * Tr ** 2 * e2 ** 2 + 18 * m * QE2 * Tr ** 2 * e2 ** 2 - 8 * m * QE2 * Tr ** 2 * e2 ** 3 - m * QE2 * Tr ** 2 * e2 ** 4 - 2 * qV * gamV * QE2 * Tr ** 2 * e2 ** 4 - 18 * m ** 2 * QE2 * Tr ** 2 * e2 ** 2 + 8 * m ** 2 * QE2 * Tr ** 2 * e2 ** 3 + m ** 2 * QE2 * Tr ** 2 * e2 ** 4 - 2 * m * gamV * QE2 * Tr ** 2 * e2 ** 4 + 36 * m * gamV * QE2 * Tr ** 2 * e2 ** 2 - 16 * m * gamV * QE2 * Tr ** 2 * e2 ** 3 - 2 * m * gamV * QE2 * Tr ** 2 * e2 ** 4 + 48 * gamV ** 2 * QE2 ** 3 * e2 ** 2 - 16 * m * gamV * QE2 * Tr ** 2 * e2 ** 3 + 36 * m * gamV * QE2 * Tr ** 2 * e2 ** 2) / VV / Tr ** 2 / (e2 - 1) ** 4
		dPthE2r = (KTB)
		KTa = 3 / 2 * n * R * ao / 1000000 * x ** (m) * (m) / VV * (TK ** 2 - Tr ** 2) * (1 - m)
		KTe = 3 / 2 * n * R * ae / 1000000 * x ** (mm) * (mm) / VV * (TK ** 2 - Tr ** 2) * (1 - mm)

		dPdV = dPthB - dPthBr + dPthBB - dPthBBr + dPthE1 - dPthE1r + dPthE2 - dPthE2r + KTe + KTa

		KTth = dPdV
		return KTth
		

######################################################################################################################################################################################################


	def dPdTth(self,n, z, Vo, Ko, kk, Tr, x, expp, V, QBo, d, mb, QB1o, d1, mb1, QE1o, mE1, QE2o, mE2, TK, gamVo, beta, gb, ao, m, mm, ae):

		self.n = n
		self.z = z
		self.Vo = Vo
		self.Ko = Ko
		self. kk = kk
		self.Tr = Tr	
		self.x = x
		self.expp = expp
		self.V = V
		self.QBo = QBo
		self.d = d
		self.mb = mb
		self.QB1o = QB1o
		self.d1 = d1
		self.mb1 = mb1
		self.QE1o = QE1o
		self.mE1 = mE1
		self.QE2o = QE2o
		self.mE2 = mE2
		self.TK = TK
		self.gamVo = gamVo
		self.beta = beta
		self.gb = gb
		self.ao = ao
		self.m = m
		self.mm = mm
		self.ae = ae


		R = 8.31451

		fw = -np.log(3 * Ko / 10 / (1003.6 * (z * n / (Vo * 10)) ** (5 / 3)))
		ff = x ** (1 / 3)
		aa = 1.5 * (kk - 3) - fw
		Px = 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * (1 / ff ** 5 - 1 / ff ** 4) * (1 + aa * ff - aa * ff ** 2)
		KT = Ko * 1000 / ff ** 6 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) + (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * (-fw) + (1 / ff - 1) * (aa - 2 * aa * ff)) * (-x)
		ex = 3 / ff ** 4 * Ko * 1000 * np.exp(fw * (1 - ff)) * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex1 = 1 / ff ** 3 * Ko * 1000 * np.exp(fw * (1 - ff)) * fw * ((-5 / ff ** 2 + 4 / ff) * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (1 + aa * ff - aa * ff ** 2) * fw + (1 / ff - 1) * (aa - 2 * aa * ff))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff)) * ((10 / ff ** 3 - 4 / ff ** 2) * (1 + aa * ff - aa * ff ** 2) + (-5 / ff ** 2 + 4 / ff) * (aa - 2 * aa * ff) + fw / ff ** 2 * (1 + aa * ff - aa * ff ** 2) - (1 / ff - 1) * (aa - 2 * aa * ff) * fw - (aa - 2 * aa * ff) / ff ** 2 - 2 * aa * (1 / ff - 1)) / ff ** 3
		kkx = (ex + ex1 - ex2) / (-KT / ff) / 3

		gt = gb - beta * x ** (1 / 3)
		gtx = -beta / 3 * x ** (-2 / 3)
		gamV = (-3 * KT + 2 * Px * gt + 9 * KT * kkx - 6 * gt * KT) / 6 / (3 * KT - 2 * Px * gt) + gamVo
		ff2 = (x + 0.00001) ** (1 / 3)
		KT2 = Ko * 1000 / ff2 ** 6 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) + (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * (-fw) + (1 / ff2 - 1) * (aa - 2 * aa * ff2)) * (-(x + 0.00001))
		ex = 3 / ff2 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff2)) * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex1 = 1 / ff2 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff2)) * fw * ((-5 / ff2 ** 2 + 4 / ff2) * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (1 + aa * ff2 - aa * ff2 ** 2) * fw + (1 / ff2 - 1) * (aa - 2 * aa * ff2))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff2)) * ((10 / ff2 ** 3 - 4 / ff2 ** 2) * (1 + aa * ff2 - aa * ff2 ** 2) + (-5 / ff2 ** 2 + 4 / ff2) * (aa - 2 * aa * ff2) + fw / ff2 ** 2 * (1 + aa * ff2 - aa * ff2 ** 2) - (1 / ff2 - 1) * (aa - 2 * aa * ff2) * fw - (aa - 2 * aa * ff2) / ff2 ** 2 - 2 * aa * (1 / ff2 - 1)) / ff2 ** 3
		kkx2 = (ex + ex1 - ex2) / (-KT2 / ff2) / 3
	
		ff1 = (x - 0.00001) ** (1 / 3)
		KT1 = Ko * 1000 / ff1 ** 6 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) + (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * (-fw) + (1 / ff1 - 1) * (aa - 2 * aa * ff1)) * (-(x - 0.00001))
		ex = 3 / ff1 ** 4 * Ko * 1000 * np.exp(fw * (1 - ff1)) * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex1 = 1 / ff1 ** 3 * Ko * 1000 * np.exp(fw * (1 - ff1)) * fw * ((-5 / ff1 ** 2 + 4 / ff1) * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (1 + aa * ff1 - aa * ff1 ** 2) * fw + (1 / ff1 - 1) * (aa - 2 * aa * ff1))
		ex2 = Ko * 1000 * np.exp(fw * (1 - ff1)) * ((10 / ff1 ** 3 - 4 / ff1 ** 2) * (1 + aa * ff1 - aa * ff1 ** 2) + (-5 / ff1 ** 2 + 4 / ff1) * (aa - 2 * aa * ff1) + fw / ff1 ** 2 * (1 + aa * ff1 - aa * ff1 ** 2) - (1 / ff1 - 1) * (aa - 2 * aa * ff1) * fw - (aa - 2 * aa * ff1) / ff1 ** 2 - 2 * aa * (1 / ff1 - 1)) / ff1 ** 3
		kkx1 = (ex + ex1 - ex2) / (-KT1 / ff1) / 3
		
		dkkdx = (kkx2 - kkx1) / (0.00002)
		qV = -1 / 2 * (-6 * KT * kkx ** 2 * Px * gt / x + 6 * KT * dkkdx * Px * gt + 6 * KT * kkx * KT * gt / x - 6 * KT * kkx * Px * gtx + 4 * gt ** 2 * KT * kkx * Px / x - 4 * gt ** 2 * KT ** 2 / x - 9 * KT ** 2 * dkkdx + 6 * gtx * KT ** 2) / (3 * KT - 2 * Px * gt) ** 2 * x / gamV
		a = ao / 1000000 * x ** m

		QB = QBo * expp
		QB1 = QB1o * expp
		QE1 = QE1o * expp
		QE2 = QE2o * expp

		gg = d * np.log(1 + QB / TK / d)
		ex = np.exp(QB / TK)
		b = 1 / (np.exp(gg) - 1)
		dPB = mb * R * (gamV / V * (QB * d / (TK * d + QB)) ** 2 * b * (1 / d + 1 + b))

		gg = d1 * np.log(1 + QB1 / TK / d1)
		ex = np.exp(QB1 / TK)
		b = 1 / (np.exp(gg) - 1)
		dPB1 = mb1 * R * (gamV / V * (QB1 * d1 / (TK * d1 + QB1)) ** 2 * b * (1 / d1 + 1 + b))

		e1 = np.exp(QE1 / TK)
		dP1 = mE1 * R * (gamV / V * (QE1 / TK) ** 2 * e1 / (e1 - 1) ** 2)

		e2 = np.exp(QE2 / TK)
		dP2 = mE2 * R * (gamV / V * (QE2 / TK) ** 2 * e2 / (e2 - 1) ** 2)
		dPdTa = 3 * n * R * ao / 1000000 * x ** (m) * (TK) * m / V
		dPdTe = 3 * n * R * ae / 1000000 * x ** (mm) * (TK) * mm / V

		dPdTth = dPB + dPB1 + dP1 + dP2 + dPdTe + dPdTa

		return dPdTth


##########################################################################################################################################################

