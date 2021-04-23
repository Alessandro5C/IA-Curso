import tb1_genetico
import pygame

def load_sound(name):
    if not pygame.mixer or not pygame.mixer.get_init():
        pass
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print ('Cannot load sound: %s' % name)
        raise SystemExit(str(geterror()))
    return sound

if __name__=="__main__":
	algorithm = tb1_genetico.Genetico(Tiempos=12,\
		Muestra=4, nKeys=4, Probabilidad=15)
	pygame.init()

	#pygame.mixer.get_init()
	#mutrue=load_sound("punch.wav")
	#mufall= load_sound("boom.wav")
	#pygame.mixer.music.load("a.mp3")
	#pygame.mixer.music.play(-1)

	algorithm.Inicializacion()
	for gen in range(300):
		algorithm.gen=gen
		#msg en GEN:
		            # if lost==0:mutrue.play()
                    # else :mufall.play()
		if gen > 0:
			algorithm.Mutacion()
		algorithm.Seleccion()
		algorithm.Cruce()
		# pygame.display.set_caption(f'GENERATION: {gen}')
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
