import pygame
import numpy as np
import time
pygame.init()
#Ancho y alto de pantalla
width, height = 680, 680
#Creacion de pantalla
screen = pygame.display.set_mode((height,width))
#Color de fondo=casi negro, casi oscuro
bg = 25, 25, 25
#Pinto el fondo del color elegido
screen.fill(bg)
nxC, nyC = 80, 80
dimCW = width / nxC
dimCH = height / nyC

#Control de ejecucion del juego (con el teclado)
pauseExect = False

#Estado de las celdas. Vivas = 1; Muertas = 0.
gameState = np.zeros((nxC, nyC))

#Automata palo
#gameState[5, 3] = 1
#gameState[5, 4] = 1
#gameState[5, 5] = 1

#Automata que se mueve
#gameState[21, 21] = 1
#gameState[22, 22] = 1
#gameState[22, 23] = 1
#gameState[21, 23] = 1
#gameState[20, 23] = 1

#Bucle de ejecucion
while True:
	newGameState = np.copy(gameState)
	
	screen.fill(bg)
	time.sleep(0.1)
	#Registro eventos de teclado
	ev = pygame.event.get()
	for event in ev:
		#Detecto si se presiona una tecla
		if event.type == pygame.KEYDOWN:
			pauseExect = not pauseExect
		#Detecto si se presiona el raton
		mouseClick = pygame.mouse.get_pressed()
		if sum(mouseClick) > 0:
			posX, posY = pygame.mouse.get_pos()
			celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			newGameState[celX, celY] = not mouseClick[2]

	for y in range (0, nxC):
		for x in range (0, nyC):
			
			if not pauseExect:

				#Calculo el num de vecinos cercanos.
				n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
						  gameState[(x)   % nxC, (y-1) % nyC] + \
				          gameState[(x+1) % nxC, (y-1) % nyC] + \
				          gameState[(x-1) % nxC, (y)   % nyC] + \
						  gameState[(x+1) % nxC, (y)   % nyC] + \
						  gameState[(x-1) % nxC, (y+1) % nyC] + \
					  	  gameState[(x)   % nxC, (y+1) % nyC] + \
						  gameState[(x+1) % nxC, (y+1) % nyC]
				# Regla #1: una celula muerta con exactamente 3 vecinas vivas, "revive"
				if gameState [x, y] == 0 and n_neigh == 3:
					newGameState [x, y] = 1

				#Regla #2: una celula viva con menos de 2 o mas de 3 vecinas vivas, "muere"
				elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh >3):
					newGameState [x, y] = 0

			#Creo el poligono de cada celda a dibujar.
			poly = [((x) * dimCW, y * dimCH), ((x+1) * dimCW, y * dimCH), ((x+1) * dimCW, (y+1) * dimCH), ((x) * dimCW, (y+1) * dimCH)]
			#Dibujo la celda para cada par de X e Y
			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
			else:
				pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
	#Actualizo el estado del juego
	gameState = np.copy(newGameState)
	#Actualizo la pantalla.
	pygame.display.flip()