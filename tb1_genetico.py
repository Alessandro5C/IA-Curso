import numpy, random, pygame
import tb1_game as gtp
import tb1_funciones as f

class Genetico():
	def __init__(self, Tiempos, Muestra, nKeys, Probabilidad):
		self.Individuos={}
		self.T=Tiempos #Tamaño del ADN
		self.M=Muestra #Número de muestras de ADN
		self.nKeys=nKeys #Número de columnas
		self.N=len(f.get_states(self.nKeys)) #Número de genes posibles
		self.P=Probabilidad #Probabilidad de mutación genética
		self.gen=0
		self.last=0
		self.Objetivos= [] 

	def Parejas(self):
		Aleatorio = random.sample(range(int(self.M/2),self.M),int(self.M/2))
		Pareja = {}
		for i in range(int(self.M/2)):
			Pareja[i] = Aleatorio[i]
			Pareja[Aleatorio[i]] = i
		return Pareja	

	def Inicializacion(self):
		self.Objetivos = numpy.random.choice(\
			range(0,self.N),self.T,replace=True)
		for i in range(self.M):
			self.Individuos[i] = numpy.random.choice(\
				range(0,self.N),self.T,replace=True)		
		print('---Inicializacion----')
		self.Mostrar()
		
	def Seleccion(self):
		print('---Seleccion----')
		Pareja = self.Parejas()
		print('Parejas',Pareja)
		for k,v in Pareja.items():
			if self.Idoneidad(self.Individuos[k], self.Objetivos)\
				 >= self.Idoneidad(self.Individuos[v], self.Objetivos):
				self.Individuos[v] = self.Individuos[k]
		self.Mostrar()

	def Idoneidad(self, SerieDeEstados, SerieDeObj, GUI=False):
		#El valor de la idoneidad se calcula en base al resultado 
		#	obtenido en el juego, el cual aumenta puntos cada vez
		#	que se atine la Nota correcta
		auxGame = gtp.Logica(SerieDeEstados, SerieDeObj, self.nKeys)
		if GUI:
			if self.gen==0:
				return auxGame.play(True, self.gen)
			elif self.gen==self.last-1:
				return auxGame.play(True, self.gen)
			else:
				return auxGame.play(False, self.gen)
		pygame.display.set_caption(f'GEN: {self.gen} | SCORE: X')
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
			#Se excluye entre las posibles genes a aquel gen que ya se encontraba ahí
			ElegirGen = numpy.random.choice(possible_gen)
			print(ElegirGen)
			self.Individuos[ElegirI][ElegirPos] = ElegirGen
			print("****")
		self.Mostrar()

	#Muestra las cadenas de ADN y su Idoneidad
	def Mostrar(self, GUI=False):
		for i in range(self.M):
			if not GUI:
				print(self.Individuos[i],'f(x)=', \
					self.Idoneidad(self.Individuos[i], self.Objetivos))
			else:
				print(self.Individuos[i],'f(x)=', \
					self.Idoneidad(self.Individuos[i], self.Objetivos, True))
