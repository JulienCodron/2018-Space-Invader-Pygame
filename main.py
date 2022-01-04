#!usr/bin/env python
#-*- coding:utf-8 -*-

#=====================================
#File: __main__.py
#Date:  28/11/18 - 10/12/18
#Autor: CODRON JULIEN
#Projet Fin semestre 3, SPACE INVADERS
#=====================================

#Ce module est le principal, c'est celui qu'il faut lancé pour démarer l'application.

#Import:
import menu
import pygame
import couleur
import scenario
import end
from pygame.locals import *


def main():
    pygame.init()
    pygame.mixer.fadeout(300)
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.set_volume(0.1)
    clock= pygame.time.Clock()
    surface= pygame.display.set_mode((800,800))
    pygame.key.set_repeat(5,6)
    pygame.display.set_caption("Space Invaders")
    surface.fill(couleur.NOIR)
    continuer = menu.execut_menu(surface)
    terminer = False
    if not continuer:
        pygame.quit()
        terminer=True
    niveau = 1
    lvl = scenario.init(surface,niveau)
    pygame.key.set_repeat(30,1)
    lvl = scenario.execute(surface,lvl)
    if lvl[0] == 0:
        pygame.quit()
        terminer=True
    if lvl[0] == 1:
        if end.execut_end(surface,"l",lvl[1]):
            main()
            termiener = True
        else:
            pygame.quit()
            terminer = True
    if lvl[0] == 2:
        if end.execut_end(surface,'w',lvl[1]):
            main()
            termiener = True
        else:
            pygame.quit()
            terminer = True
            
            
if __name__=='__main__':
    main()
    
