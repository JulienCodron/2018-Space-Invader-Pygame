#!usr/bin/env python
#-*- coding:utf-8 -*-

#=====================================
#File: menu.py
#Date:  28/11/18 - 10/12/18
#Autor: CODRON JULIEN
#Projet Fin semestre 3, SPACE INVADERS
#=====================================

# Ce module permet d'afficher le menu de démarage au début du jeu.

#Import:
import pygame
import couleur

def execut_menu(surface): #notre surface est de 800/800
    '''
    Fonction lance le menu du jeu et demande au joueur s'il veut continuer
    Argument: surface - la fenêtre ouverte de pygame ou l'on dessine
    return: continuer - True ou False si le joueur veut continuer ou non
    '''
    pygame.mixer.music.load('assets/sounds/music_menu.mp3')
    pygame.mixer.music.play()
    terminer=False
    continuer=False
    dessine_menu(surface)
    pygame.display.update()
    while not terminer:
        for event in pygame.event.get():
            if event.type== pygame.QUIT :
                continuer=False
                terminer=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame. K_ESCAPE:
                    continuer=False
                    terminer=True
                if event.key==pygame.K_RETURN:
                    continuer=True
                    terminer=True
    return continuer


def dessine_menu(surface): #notre surface est de 800/800
    '''
    Fonction qui déssine le menu du jeu
    Argument: surface - la fenêtre ouverte sur pygame ou l'on dessine
    '''
    #dessine le l'image de fond à partir d'une image
    fond_menu = pygame.image.load("assets/images/menu.jpg")
    surface.blit(fond_menu,[0,0])

    #dessine l'icone en haut à gauche à partir d'une image
    monster =  pygame.image.load("assets/images/monster.png")
    surface.blit(monster,[50,200])

    #dessine le titre en grand
    titre_police = pygame.font.Font("assets/fonts/unifont.ttf",95)
    titre1=titre_police.render("Space Invaders",True, couleur.BLANC)
    surface.blit(titre1,[65,500])

    #dessine les instructions
    text_police = pygame.font.Font("assets/fonts/STARWARS.ttf",40)
    start=text_police.render("Press Enter to start",True, couleur.BLANC)
    surface.blit(start,[190,675])

    text_police2 = pygame.font.Font("assets/fonts/unifont.ttf",30)
    quiter=text_police2.render("to quit",True, couleur.BLANC)
    surface.blit(quiter,[80,20])

    esc =  pygame.image.load("assets/images/esc.png")
    surface.blit(esc,[5,5])



