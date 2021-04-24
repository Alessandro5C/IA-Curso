import numpy
import random
import tb1_game as gtp
import pygame
import time
import tb1_funciones as f

class Genetico():
	def __init__(self, Tiempos, Muestra, nKeys, Probabilidad):
		self.Individuos={}
		self.Objetivos= [] 
		self.T=Tiempos
		self.M=Muestra
		self.nKeys=nKeys
		self.N=len(f.get_states(self.nKeys))
		self.P=Probabilidad
		self.gen=0
		self.last=0

	def Parejas(self):
		Aleatorio = random.sample(range(int(self.M/2),self.M),int(self.M/2))
		Pareja = {}
		for i in range(int(self.M/2)):
			Pareja[i] = Aleatorio[i]
			Pareja[Aleatorio[i]] = i
		return Pareja	

	def Inicializacion(self):
		# global Individuos
		# global Mejor
		# Individuos = {}
		# global Objetivos
		# Objetivos = []
		self.Objetivos = numpy.random.choice(range(0,self.N),self.T,replace=True)
		for i in range(self.M):
			self.Individuos[i] = numpy.random.choice(range(0,self.N),self.T,replace=True)
		
		print('---Inicializacion----')
		self.Mostrar()
		
	def Seleccion(self):
		print('---Seleccion----')
		Pareja = self.Parejas()
		print('Parejas',Pareja)
		for k,v in Pareja.items():
			if self.Idoneidad(self.Individuos[k], self.Objetivos) >= self.Idoneidad(self.Individuos[v], self.Objetivos):
				self.Individuos[v] = self.Individuos[k]
		self.Mostrar()

	def Idoneidad(self, SerieDeEstados, SerieDeObj, GUI=False):
		#print("TIPO DE DATO", type(SerieDeEstados))
		auxGame = gtp.Logica(SerieDeEstados, SerieDeObj, self.nKeys)
		if GUI:
			if self.gen==0:
				return auxGame.play(True, self.gen)
			elif self.gen==self.last-1:
				return auxGame.play(True, self.gen)
			else:
				return auxGame.play(False, self.gen)
			#msg pon GEN EN LA PARTE SUPERIOR
		# auxGame = display()
		pygame.display.set_caption(f'GENERATION: {self.gen} | SCORE: X')
		return auxGame.getJustResult()

	def Cruce(self):
		print('-----Cruce ------')
		Pareja = self.Parejas()
		print('Parejas',Pareja)
		item = 0
		for k,v in Pareja.items():
			if item % 2 == 0:
				Punto = random.randint(1,self.T-2)
				print('punto',Punto)
				Hijo1 = []
				Hijo2 = []
				Padre1 = self.Individuos[k]
				Padre2 = self.Individuos[v]
				Hijo1.extend(Padre1[0:Punto])
				Hijo1.extend(Padre2[Punto:])
				Hijo2.extend(Padre2[0:Punto])
				Hijo2.extend(Padre1[Punto:])
				self.Individuos[k] = Hijo1
				self.Individuos[v] = Hijo2
			item = item+1
		self.Mostrar(True)

	def Mutacion(self):
		print('-----Mutacion ----')
		for _i in range(int(self.N/2)):
			if random.randint(0, 99) >= self.P:
				continue
			ElegirI = random.randint(0,self.M-1)
			print(ElegirI)
			ElegirPos = random.randint(0,self.T-1)
			print(ElegirPos)

			gen_not_to_choose = self.Individuos[ElegirI][ElegirPos]
			possible_gen = list(range(0, gen_not_to_choose))
			possible_gen.extend(range(gen_not_to_choose+1, self.N))

			ElegirGen = numpy.random.choice(possible_gen)
			#El gen elegido no puede ser el mismo que ya estaba en Individuos[ElegirI][ElegirPos]
			print(ElegirGen)
			self.Individuos[ElegirI][ElegirPos] = ElegirGen
			print("****")
		self.Mostrar()

	def Mostrar(self, GUI=False):
		for i in range(self.M):
			if not GUI:
				print(self.Individuos[i],'f(x)=', self.Idoneidad(self.Individuos[i], self.Objetivos))
			else:
				print(self.Individuos[i],'f(x)=', self.Idoneidad(self.Individuos[i], self.Objetivos, True))

# Tiempos = 12
# Muestra = 2

# NKeys = 4
# NEstados = 15 #len(f.get_states(NKeys))
# Probabilidad = 15

# pygame.init()
# Inicializacion(Muestra, NEstados, Tiempos)
# #Añadido
# for e in range(1):
# 	print(f'GEN: {e+1}')
# 	if e > 0:
# 		Mutacion(Muestra, NEstados, Probabilidad, Tiempos)
# 	Seleccion(Muestra, Tiempos)
# 	Cruce(Muestra, Tiempos)

# print(Objetivos)
# pygame.quit()
# print("ADIOSSS")
	
