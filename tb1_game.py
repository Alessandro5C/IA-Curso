import pygame,os,random
# from pygame.locals import *
import tb1_funciones as f
import time

# def load_sound(name):
#     if not pygame.mixer or not pygame.mixer.get_init():
#         pass
#     try:
#         sound = pygame.mixer.Sound(name)
#     except pygame.error:
#         print ('Cannot load sound: %s' % name)
#         #raise SystemExit(str(geterror()))
#    return sound

# wrong= load_sound("wrong.wav")

class Logica():
	def __init__(self, SerieDeMovimientos, SerieDeObjetivos, nKeys):
		self.__nCol=10
		self.nKeys=nKeys
		self.MovSeries=SerieDeMovimientos
		self.ObjSeries=SerieDeObjetivos
		self.nTiempos=len(SerieDeObjetivos)
		self.score=0
		self.states={}
		self.HeightObjSeries={}
		self.pantalla = display(400)
	
	def getJustResult(self):
		self.score=0
		for i in range(self.nTiempos):
			if self.MovSeries[i]==self.ObjSeries[i]:
				self.score+=1
		return self.score
		
	def associate(self):
		aux = f.get_states(self.nKeys)
		for i in range(len(f.get_states(self.nKeys))):
			self.states[i] = aux[i]
		# print(self.states, type(self.states))

		aux = []
		for i in range(len(self.ObjSeries)):
			self.HeightObjSeries[i]=-i

	def notesHeight(self):
		for i in range(len(self.ObjSeries)):
			self.HeightObjSeries[i]+=1

	def printOnCanvas(self, h, i):
		list_to_print = self.states[self.ObjSeries[i]]
		for e in list_to_print:
			# print(f"Coordenadas {h, e}") # Formato fila columna
			self.pantalla.printKey(h, e)
			#print_in_(h, e) #FUNCION PARA DIBUJAR EN GUI

	def printPressedOnCanvas(self, i, pressed):
		list_to_print = self.states[self.MovSeries[i]]
		for e in list_to_print:
			# print(f"Coordenadas {h, e}") # Formato fila columna
			self.pantalla.printPressed(pressed, e)
			#print_in_(h, e) #FUNCION PARA DIBUJAR EN GUI


	def printOnConsola(self):
		# print("------------------------")
		for i in range(len(self.ObjSeries)):
			h = self.HeightObjSeries[i]
			if not (h<0):
				if (h>=self.__nCol):
					#print(f"ya no se dibuja | altura->: {h}")
					continue
				# print(f"Toca dibujar el estado: {self.ObjSeries[i]}")
				self.printOnCanvas(h, i)
		# print("------------------------")

	def play(self, with_delay:bool, gen:int):
		self.associate()
		#musica_aqui
		score = 0
		for j in range(self.nTiempos+self.__nCol):
			self.pantalla.screen.fill((224,224,255))
			self.printOnConsola()
			# print("\n\nNuevo tiempo")
			if j>=self.__nCol:
				pressed = (self.MovSeries[j-self.__nCol] == self.ObjSeries[j-self.__nCol])
				if pressed:
					score += 1 
					pygame.display.set_caption(f'GENERATION: {gen} | SCORE: {score}')
					# pygame.mixer.unpause()
					# pygame.mixer.music.unpause()
				else:
					if with_delay:
						wrong = pygame.mixer.Sound("resources/wrong.wav")
						wrong.play()
					# pygame.mixer.pause()
					# score=score
					# pygame.mixer.music.pause()
						# pygame.mixer.init()
						# wrong.set_volume(0.5)
						# pygame.mixer.pause()
					#nose si hay q parar
					# pygame.mixer.wrong.set_volume(0.3)
				self.printPressedOnCanvas(j-self.__nCol, pressed)
				#if presed = False :::: aqui musica mal hecha
				# self.pantalla.click(j-10, pressed)
			pygame.display.update()
			if with_delay:
				time.sleep(0.15)
			self.notesHeight()
		return score


class key_properties():
	def __init__(self, witdh, height):
		self.__nCol=4
		self.__nFil=10

		self.__w= (witdh//self.__nCol)-1
		#no olvidar el height*2
		self.__h= (height//self.__nFil)

	def __to_x(self, col, witdh):
		return col*witdh//self.__nCol
	
	def __to_y(self, fil, height):
		#no olvidar el height*2
		return fil*height//self.__nFil

	def drawKey(self, screen, witdh, height, i, j):
		x, y = self.__to_x(j, witdh), self.__to_y(i, height)
		pygame.draw.rect(screen, (0,0,0), [x, y, self.__w, self.__h])

	def drawPressed(self, screen, witdh, height, j, rgb):
		x = self.__to_x(j,witdh)
		pygame.draw.rect(screen, rgb, [x, self.__to_y(9,height), self.__w, self.__h])
		# print("Pressed: ", x , self.__to_y(9,height))

	# def click(self,ps, idCol): #aqui tenemos que indicar la posición de la pantalla en la cual ha sido tocada (coord, X,y)
	# 	idCol=(pos_col)*self.value//self.__nCol
	# 	if ps[0] in range(idCol,idCol+self.w):
	# 		if ps[1] in range (self.y,self.y+self.h):
	# 			self.not_touched=False
	# 			return 0
	# 	return 1


class display():
	def __init__(self, value):
		self.width=value
		self.heigth=2*value
		self.piano_key= key_properties(self.width, self.heigth)
		self.screen=pygame.display.set_mode((self.width,self.heigth))
		self.not_touched = True

	def printKey(self, i, j):
		self.piano_key.drawKey(self.screen, self.width, self.heigth, i, j)

	def printPressed(self, pressed, j):
		if pressed:
			self.piano_key.drawPressed(self.screen, self.width, self.heigth, j, rgb=(76, 187, 23))
		else:
			self.piano_key.drawPressed(self.screen, self.width, self.heigth, j, rgb = (220,20,60))
		



	# def click(self,ps, idCol): #aqui tenemos que indicar la posición de la pantalla en la cual ha sido tocada (coord, X,y)
	# 	idCol=(pos_col)*self.value//self.__nCol
	# 	if ps[0] in range(idCol,idCol+self.w):
	# 		if ps[1] in range (self.y,self.y+self.h):
	# 			self.not_touched=False
	# 			return 0
	# 	return 1

	# def msg (self, text,color=(55,55,55),size=36,pos=(-1,-1)):
	# 	if pos[0] ==-1:pos=(self.screen.get_rect().centerx,pos[1])
	# 	if pos[1] ==-1:pos=(pos[0],self.screen.get_rect().centery)
	# 	font = pygame.font.Font(None, size)
	# 	text = font.render(text, 1, color)
	# 	textpos = text.get_rect()
	# 	textpos.centerx = pos[0]
	# 	textpos.centery= pos[1]
	# 	self.screen.blit(text, textpos)
	
	# def load_sound(self, name):
	# 	if not pygame.mixer or not pygame.mixer.get_init():
	# 		pass
	# 	try:
	# 		sound = pygame.mixer.Sound(name)
	# 	except pygame.error:
	# 		print ('Cannot load sound: %s' % name)
	# 		raise SystemExit(str(geterror()))
	# 	return sound

	# def game_loop(self, ObjSeries):
	# 	#pygame.init()
	# 	#pygame.mixer.get_init()
	# 	#mutrue=load_sound("punch.wav")
	# 	#mufall= load_sound("boom.wav")
	# 	#pygame.mixer.music.load("a.mp3")
	# 	#pygame.mixer.music.play(-1)
	# 	clock=pygame.time.Clock()
	# 	key_map=[0,1,0,4,1,0,1,0,2,0,2,0,3,3,1,2,3,1,0,2,3,1,0,1,2,3,0,1,2,3]
	# 	lost=0
	# 	time=0
	# 	delt=60*2
	# 	sb=[]
	# 	speey=4
	# 	score=0
	# 	while lost == 0:
	# 		for ls in key_map:

	# 			sb.append(button())
	# 			sb[-1].pos(i)
	# 			if lost!=0 : break
	# 			for j in range(wiy//(5*speey)):
	# 				time+=1/delt
	# 				clock.tick(delt)
	# 				self.screen.fill((224,224,255))
	# 				if lost!=0 : break
	# 				for k in range(len(sb)) :
	# 					try:
	# 						sb[k].y+=speey
	# 						sb[k].update(self.screen)
	# 						if sb[k].y >wiy-sb[k].l and sb[k].enclick == True : lost=1
	# 					except : pass
	# 				for event in pygame.event.get():
	# 					if event.type == QUIT or \
	# 					(event.type == KEYDOWN and event.key == K_ESCAPE):
	# 						pygame.quit()
	# 					elif event.type == MOUSEBUTTONDOWN:
	# 						print(pygame.mouse.get_pos())
	# 						lost=sb[score].click(pygame.mouse.get_pos())
	# 						# if lost==0:mutrue.play()
	# 						# else :mufall.play()
	# 						score+=1
	# 				msg(self.screen,"SCORE "+str(score),color=(0,128,255),pos=(-1,30))
	# 				pygame.display.update()
	# 		speey+=1
	# 	#pygame.mixer.music.stop()
	# 	#pygame.quit()
