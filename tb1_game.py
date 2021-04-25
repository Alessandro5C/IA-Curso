import pygame
import tb1_funciones as f
import time

class Logica():
	def __init__(self, SerieDeMovimientos, SerieDeObjetivos, nKeys):
		self.__nFil=10
		self.nKeys=nKeys
		self.MovSeries=SerieDeMovimientos
		self.ObjSeries=SerieDeObjetivos
		self.nTiempos=len(SerieDeObjetivos)
		self.states={}
		self.HeightObjSeries={}
		self.score=0 #Puntaje para mostrar
		self.pantalla = display(350) #Establece el tamaño de la pantalla
	
	#Solo calcula el puntaje
	def getJustResult(self):
		self.score=0
		for i in range(self.nTiempos):
			if self.MovSeries[i]==self.ObjSeries[i]:
				self.score+=1
		return self.score
	
	#Asociar un estado con una serie de notas
	#	eg. (Estado 3) Serie de teclas número 3 -> Posición de la tecla negra: Solo 3
	#	eg. (Estado 4) Serie de teclas número 4 -> Posición de la tecla negra: 0 y 1
	def associate(self):
		aux = f.get_states(self.nKeys)
		for i in range(len(aux)):
			self.states[i] = aux[i]

		aux = []
		for i in range(len(self.ObjSeries)):
			self.HeightObjSeries[i]=-i

	#Actualiza la altura de las teclas negras
	def notesHeight(self):
		for i in range(len(self.ObjSeries)):
			self.HeightObjSeries[i]+=1

	#Convierte un Estado a una serie de teclas negras e
	#	imprime tecla negra en el canvas/ventana
	def printOnCanvas(self, h, i):
		list_to_print = self.states[self.ObjSeries[i]]
		for e in list_to_print:
			self.pantalla.printKey(h, e)

	#Convierte un Estado a una serie de teclas e
	#	imprime la tecla presionada en el canvas/ventana
	def printPressedOnCanvas(self, i, pressed):
		list_to_print = self.states[self.MovSeries[i]]
		for e in list_to_print:
			self.pantalla.printPressed(pressed, e)

	#Indica la posición (altura y columna)
	#	en la cual se debe dibujar cada tecla negra
	def printOn(self):
		for i in range(len(self.ObjSeries)):
			h = self.HeightObjSeries[i]
			if not (h<0):
				if (h>=self.__nFil):
					continue
				self.printOnCanvas(h, i)

	#Bucle del juego a nivel lógico
	def play(self, with_delay:bool, gen:int):
		self.associate()
		score = 0
		#Mientras exista teclas negras
		for i in range(self.nTiempos+self.__nFil):
			self.pantalla.screen.fill((224,224,255))
			self.printOn()
			#Imprimir el color de la tecla presiona (Rojo-> Incorrecto & Verde-> Correcto)
			if i>=self.__nFil:
				pressed = (self.MovSeries[i-self.__nFil] == self.ObjSeries[i-self.__nFil])
				#Si se presiono correctamente aumenta puntaje, sino reproduce un sonido
				if pressed:
					score += 1 
					pygame.display.set_caption(f'GEN: {gen} | SCORE: {score}')
				else:
					if with_delay:
						wrong = pygame.mixer.Sound("resources/wrong.wav")
						wrong.play()
				self.printPressedOnCanvas(i-self.__nFil, pressed)
			pygame.display.update()
			if with_delay:
				time.sleep(0.15)
			self.notesHeight()
		return score

#Clase que representa a la tecla
#	sea negra o presionada 
class key_properties():
	def __init__(self, witdh, height):
		self.__nCol=4
		self.__nFil=10
		self.__w= (witdh//self.__nCol)-1
		self.__h= (height//self.__nFil)

	def __to_x(self, col, witdh):
		return col*witdh//self.__nCol
	
	def __to_y(self, fil, height):
		return (fil-1)*height//self.__nFil

	def drawKey(self, screen, witdh, height, i, j):
		x, y = self.__to_x(j, witdh), self.__to_y(i, height)
		pygame.draw.rect(screen, (0,0,0), [x, y, self.__w, self.__h])

	def drawPressed(self, screen, witdh, height, j, rgb):
		x = self.__to_x(j,witdh)
		pygame.draw.rect(screen, rgb, [x, self.__to_y(self.__nFil,height), self.__w, self.__h])

#Clase que representa la ventana y su canvas
class display():
	def __init__(self, value):
		self.width=value
		self.heigth=2*value
		self.piano_key= key_properties(self.width, self.heigth)
		self.screen=pygame.display.set_mode((self.width,self.heigth))

	def printKey(self, i, j):
		self.piano_key.drawKey(self.screen, self.width, self.heigth, i, j)

	def printPressed(self, pressed, j):
		if pressed:
			self.piano_key.drawPressed(self.screen, self.width, \
				self.heigth, j, rgb = (76, 187, 23))
		else:
			self.piano_key.drawPressed(self.screen, self.width, \
				self.heigth, j, rgb = (220, 20, 60))
