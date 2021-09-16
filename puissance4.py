import pygame
from pygame import key
from pygame.version import ver

pygame.init()

#DEBUT INITIALISATION

# La taille de la fenetre quand on lance le programme
window = pygame.display.set_mode((1300, 1300))

#Couleurs RGB
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)

#Couleur noir
black = (0,0,0)

#Fonction qui affiche le rectangle bleu du puissance 4
def rectangePuissance4():  
    pygame.draw.rect(window, blue, pygame.Rect(25, 35, 1200, 1250))
    pygame.display.flip()

rectangePuissance4()

#Fonction qui affiche les rectangles noir du puissance 4
def rondPuissance4(x,y):
    pygame.draw.circle(window, black, (x, y), 50)
    pygame.display.flip()

#For qui affiche les ronds de façon horizontales
for horizontale in range(8):
    #For qui affiche les ronds de façon verticales
    for verticale in range(8):
        rondPuissance4((horizontale * 150) + 100, (verticale * 150) + 150)

def rondRouge():
    pygame.draw.circle(window, red, (550,50), 50)
    pygame.display.flip()

#FIN INITIALISATION

#Run programme
running = True

while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
	    rondRouge()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()