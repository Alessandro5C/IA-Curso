import tb1_genetico
import pygame

#Integrantes:
#+	U201919333 - Alessandro Carhuancho
#+	U201913424 - Andreluis Ingaroca
#+	U20191A355 - Sebastian Arana

if __name__=="__main__":
	algorithm = tb1_genetico.Genetico(Tiempos=20,\
		Muestra=6, nKeys=4, Probabilidad=20)
	algorithm.last=500
	pygame.init()

	pygame.mixer.init()
	pygame.mixer.music.load("resources/music.wav")
	pygame.mixer.music.play(-1)

	algorithm.Inicializacion()
	for gen in range(algorithm.last):
		print(f'GENERACIÓN: {gen}')
		pygame.mixer.music.rewind()
		algorithm.gen=gen
		if gen > 0:
			algorithm.Mutacion()
		algorithm.Seleccion()
		algorithm.Cruce()
		pygame.mixer.pause()
	print(algorithm.Objetivos)
	pygame.mixer.music.stop()
	pygame.quit()
	print("ADIOSSS")