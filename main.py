import tb1_genetico
import pygame
import time 
# def load_sound(name):
#     if not pygame.mixer or not pygame.mixer.get_init():
#         pass
#     try:
#         sound = pygame.mixer.Sound(name)
#     except pygame.error:
#         print ('Cannot load sound: %s' % name)
#     	#raise SystemExit(str(geterror()))
#     return sound

if __name__=="__main__":
	algorithm = tb1_genetico.Genetico(Tiempos=12,\
		Muestra=4, nKeys=4, Probabilidad=15)
	algorithm.last=300
	pygame.init()

	pygame.mixer.init()
	# music=load_sound("music.wav")
	pygame.mixer.music.load("resources/music.wav")
	pygame.mixer.music.play(-1)

	# music = pygame.mixer.Sound("music.wav")
	# music.set_volume(0)
	algorithm.Inicializacion()
	# music.play()
	for gen in range(algorithm.last):
		pygame.mixer.music.rewind()
		algorithm.gen=gen
		# pygame.mixer.unpause()
		if gen > 0:
			algorithm.Mutacion()
		algorithm.Seleccion()
		algorithm.Cruce()
		pygame.mixer.pause()
	print(algorithm.Objetivos)
	#pygame.mixer.music.stop()
	pygame.quit()
	print("ADIOSSS")

# Tiempos = 12
# Muestra = 4
# # NKeys = 4
# NEstados = 15 #len(f.get_states(NKeys))
# Probabilidad = 15

# pygame.init()
# genetico.Inicializacion(Muestra, NEstados, Tiempos)
# #Añadido
# for e in range(200):
# 	print(f'GEN: {e+1}')
# 	if e > 0:
# 		genetico.Mutacion(Muestra, NEstados, Probabilidad, Tiempos)
# 	genetico.Seleccion(Muestra, Tiempos)
# 	genetico.Cruce(Muestra, Tiempos)

# print(genetico.Objetivos)
# pygame.quit()
# print("ADIOSSS")
