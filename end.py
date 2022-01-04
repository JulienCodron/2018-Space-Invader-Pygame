#!usr/bin/env python
#-*- coding:utf-8 -*-

#=====================================
#File: end.py
#Date:  28/11/18 - 10/12/18
#Autor: CODRON JULIEN
#Projet Fin semestre 3, SPACE INVADERS
#=====================================

#Ce mofule permet d'afficher l'écran de fin de partie.

#Import:
import pygame
import couleur


def execut_end(surface,WorL,score):
    '''
    qui exécute l’une des deux autre selon la victoire du joueur ‘W’ ou la
    défaite du joueur ‘L’ et qui géré la gestion d’évènement de pygame pour
    savoir si le joueur veux rejouez ou quitté.
    Arguement: -surface , Surface de pygame ou l'on dessine
               -WorL , qui est un str 'l' pour loose et 'w' pour win
               -score , int représentant le score du joueur
    return bool, la decision du joueur de continuer ou quiter
    '''
    pygame.mixer.music.load('assets/sounds/music_go.mp3')
    pygame.mixer.music.play()
    terminer = False
    continuer= False
    if WorL == 'l':
        dessine_go(surface,score)
    else:
        dessine_win(surface,score)
    pygame.display.update()
    while not terminer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                continuer=False
                terminer=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer=False
                    terminer=True
                if event.key == pygame.K_c:
                    continuer=True
                    terminer=True
    return continuer

def dessine_go(surface,score):
    '''
    Fonction qui dessine l'écran de fin lors ce que le joueur à perdu
    Arguement: -surface , Surface de pygame ou l'on dessine
               -WorL , qui est un str 'l' pour loose et 'w' pour win
               -score , int représentant le score du joueur
    return: None
    '''
    fond_jeu = pygame.image.load("assets/images/fond_jeu.jpg")
    surface.blit(fond_jeu,[0,0])

    

    polic_go = pygame.font.Font("assets/fonts/STARWARS.ttf",80)
    gameover=polic_go.render("GAME OVER",True, couleur.BLANC)
    surface.blit(gameover,[140,200])

    
    police_reste = pygame.font.Font("assets/fonts/STARWARS.ttf",40)    
    continu=police_reste.render("Press C To Try Again",True, couleur.BLANC)
    surface.blit(continu,[170,450])
    ou=police_reste.render("Or",True, couleur.BLANC)
    surface.blit(ou,[370,500])
    stop=police_reste.render("Press Esc To Quit",True, couleur.BLANC)
    surface.blit(stop,[200,550])
    score=police_reste.render("score : "+ str(score),True, couleur.BLANC)
    surface.blit(score,[250,300])

                              
def dessine_win(surface,score):
    '''
    Fonction qui dessine l'écran de fin lors ce que le joueur à gagner
    Arguement: -surface , Surface de pygame ou l'on dessine
               -WorL , qui est un str 'l' pour loose et 'w' pour win
               -score , int représentant le score du joueur
    return: None
    '''
    fond_jeu = pygame.image.load("assets/images/fond_jeu.jpg")
    surface.blit(fond_jeu,[0,0])

    polic_go = pygame.font.Font("assets/fonts/STARWARS.ttf",80)
    gameover=polic_go.render("YOU WIN !!",True, couleur.BLANC)
    surface.blit(gameover,[140,200])
    
    police_reste = pygame.font.Font("assets/fonts/STARWARS.ttf",40)    
    continu=police_reste.render("Press C To Try Again",True, couleur.BLANC)
    surface.blit(continu,[170,450])
    ou=police_reste.render("Or",True, couleur.BLANC)
    surface.blit(ou,[370,500])
    stop=police_reste.render("Press Esc To Quit",True, couleur.BLANC)
    surface.blit(stop,[200,550])
    score=police_reste.render("score : "+ str(score),True, couleur.BLANC)
    surface.blit(score,[250,300])
                              

