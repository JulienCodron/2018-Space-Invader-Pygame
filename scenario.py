#!usr/bin/env python
#-*- coding:utf-8 -*-

#=====================================
#File: scenario.py
#Date:  28/11/18 - 10/12/18
#Autor: CODRON JULIEN
#Projet Fin semestre 3, SPACE INVADERS
#=====================================

# Ce module permet de rafraichir le jeu, et gére toute la partie algorithmique de celui-ci.

#Import:
import pygame
import couleur
import end
from random import *

def init(surface,niveau):
    '''
    Cette fonction permet d'initialisé le niveau choisi,
    Argument : niveau = int, il correspond au niveau que l'on veut initialiser
    Return :  lvl = dict{d'objet}, return un dictionnaire d'objet vaisseau, bloc initialiser à leurs position initiale dans ce niveau
    '''
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/sounds/music.mp3')
    pygame.mixer.music.play()
    lvl = {}
    if niveau == 1:
        lvl['joueur'] = Vsojoueur(surface,370,700)
        lvl['enemies'] = []
        lvl['wall'] = []
        lvl['tir'] =[]
        tipe = 0
        for i in range (5):
            for j in range(11):
                if tipe == 0 or tipe == 1:
                    lvl['enemies'].append(Vso(surface,35+j*60,100+i*60,'0'))
                if tipe == 2 or tipe == 3:
                    lvl['enemies'].append(Vso(surface,35+j*60,100+i*60,'1'))
                if tipe == 4:
                    lvl['enemies'].append(Vso(surface,35+j*60,100+i*60,'2'))
            tipe += 1
        
        for i in range (4):
            lvl['wall'].append(Wall(surface,100+i*170+0*30,640,3))
            lvl['wall'].append(Wall(surface,100+i*170+1*30,640,2))
            lvl['wall'].append(Wall(surface,100+i*170+2*30,640,3))
            lvl['wall'].append(Wall(surface,100+i*170+0*30,620,2))
            lvl['wall'].append(Wall(surface,100+i*170+2*30,620,2))
            lvl['wall'].append(Wall(surface,100+i*170+1*30,620,1))
            lvl['wall'].append(Wall(surface,100+i*170+0*30,600,1))
            lvl['wall'].append(Wall(surface,100+i*170+2*30,600,1))


                        
    if niveau == 2:
        lvl = {}
    return lvl

        
def execute(surface,niveau):
    '''
    Fonction qui utilise le dictionnaire initialisé dans la fonction init(), et qui
    déssiné le niveau, et qui permet également la gestion des évenement avec pygame,
    le déroulement du niveau.
    Argument: - surface : la fenêtre de pygame
              - niveau : dictionnaire- comprends les attributs du niveau
    return: liste de 1 avec le score en second elements
    '''
    InvaderHit = pygame.mixer.Sound("assets/sounds/InvaderHit.wav")
    InvaderBullet = pygame.mixer.Sound("assets/sounds/InvaderBullet.wav")
    ShipBullet = pygame.mixer.Sound("assets/sounds/ShipBullet.wav")
    ShipHit = pygame.mixer.Sound("assets/sounds/ShipHit.wav")
    InvaderHit.set_volume(0.1)
    ShipBullet.set_volume(0.2)
    InvaderBullet.set_volume(0.2)
    ShipHit.set_volume(0.3)
    
    terminer = False
    i=0
    score = 0
    bullet = 6
    vie = 3
    while not terminer:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT :
                return [0,score]
                terminer=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return [0,score] 
                    terminer=True
                if keys[pygame.K_LEFT]:
                    niveau["joueur"].gauche()
                    
                if keys[pygame.K_RIGHT]:
                    niveau["joueur"].droite()

                if event.key == pygame.K_SPACE:
                    if bullet >0:
                        bullet-=1
                        ShipBullet.play()
                        score-=10
                        niveau['tir'].append(niveau["joueur"].tir())
                
        surface.fill((couleur.NOIR))
        fond_jeu = pygame.image.load("assets/images/fond_jeu.jpg")
        surface.blit(fond_jeu,[0,0])
        hud(surface,vie,bullet,score)
        niveau['joueur'].update()
        for ennemi in niveau['enemies']:
            if ennemi != 0:
                ennemi.update()
        for wall in niveau['wall']:
            wall.update()
        for tir in niveau['tir']:
            tir.update()


        nben = 0
        for y in range(len(niveau['enemies'])):
            if niveau['enemies'][y] != 0:
                nben += 1
                if niveau['enemies'][y].posy == 680:
                    return [1,score]
                    terminer = True
                if niveau['enemies'][y] != 0:
                    if not (y >= 44 and y <=55):
                        if niveau['enemies'][y+11]==0:
                            rand = randint (0,100)
                            if rand == 50:
                                InvaderBullet.play()
                                niveau['tir'].append(niveau['enemies'][y].tir())
                    else:
                        rand = randint (0,100)
                        if rand == 50:
                            niveau['tir'].append(niveau['enemies'][y].tir())
                        
                for walls in niveau['wall']:
                    if niveau['enemies'][y] != 0:
                        if niveau['enemies'][y].superpose(walls.posx,walls.posy):
                            score-=50
                            InvaderHit.play()
                            niveau['wall'].remove(walls)
        
                if niveau['enemies'][y] != 0:
                    niveau['enemies'][y].replace(i)
        if nben == 0:
            return [2,score]
            terminer = True
           

        randolist =[]
        for s in range(len(niveau["tir"])):
            a = True
            if niveau["tir"][s] != 0:
                if niveau["tir"][s].posy >= 850 or niveau["tir"][s].posy <= 0:
                    if niveau["tir"][s].who != "ennemi":
                        bullet+=1
                    randolist.append(niveau["tir"][s])
                for wally in niveau['wall']:
                    if niveau["tir"][s].superpose_wall(wally.posx,wally.posy):
                        score-=10
                        InvaderHit.play()
                        wally.etat-=1
                        randolist.append(niveau["tir"][s])
                        a = False
                if not a and niveau["tir"][s].who != 'ennemi':
                    bullet+=1
                for cpt in range(len(niveau['enemies'])):
                    if niveau['enemies'][cpt] != 0:
                        if niveau["tir"][s].superpose_enemies(niveau['enemies'][cpt].posx,niveau['enemies'][cpt].posy):
                            if niveau["tir"][s].who != 'ennemi':
                                bullet+=1
                            score+=100
                            randolist.append(niveau["tir"][s])
                            InvaderHit.play()
                            niveau['enemies'][cpt] = 0
                if niveau["tir"][s].superpose_joueur(niveau['joueur'].posx,niveau['joueur'].posy):
                    ShipHit.play()
                    score-=200
                    vie-=1
                    niveau['joueur'] = Vsojoueur(surface,370,700)
                    niveau["tir"]=[]
                    a = False
                    bullet = 6
                    break
                
            if a:
                niveau["tir"][s].replace()
                
        for suptir in randolist:
            if suptir in niveau["tir"]:
                niveau["tir"].remove(suptir)
            
        for mur in niveau['wall']:
            if mur.etat<=0:
                niveau['wall'].remove(mur)

                
        if i == 16:
            i=0
        i+=1
        
        if vie < 0:
            return [1,score]
        
        pygame.display.update()
        
    return niveau


def hud(surface,vie,bullets,score):
    '''
    Fonction appelé dans la fonction execute, elle permet de déssiner l'hud du jeux
    Arguments: - vie : int
               - bullets: int
    Return : None
    '''
    rectangle=pygame.draw.rect(surface,couleur.NOIR,pygame.Rect(0,760,800,800),0)
    
    img = pygame.image.load("assets/images/joueur.png")
    surface.blit(img,[10,765])
    
    vie_police = pygame.font.Font("assets/fonts/unifont.ttf",40)
    vie=vie_police.render("x"+str(vie),True, couleur.BLANC)
    surface.blit(vie,[85,760])

    img2 = pygame.image.load("assets/images/tir.png")
    surface.blit(img2,[772,771])

    bullets=vie_police.render("Bullet:"+str(bullets),True, couleur.BLANC)
    surface.blit(bullets,[600,760])

    score=vie_police.render("Score:"+str(score),True, couleur.BLANC)
    surface.blit(score,[300,760])
   

    	





        
class Vso:
    def __init__(self,surface,posx,posy,who):
        '''
        Initialise la class Vso , qui est un objet représentent un vaisseau, il
        peut être allié ou énemni, et il a une position
        Argument: self -Vso
                  surface -Fenetre pygame
                  posx,posy -int
                  who -str
        Return : None
        ''' 
        self.surface = surface
        self.posx = posx
        self.posy = posy
        self.who = who
        self.direct = 'd'
        self.face = 0
        if who == '0' :
            self.img = pygame.image.load("assets/images/InvaderA1.png")
        if who == '1':
            self.img = pygame.image.load("assets/images/InvaderB1.png")
        if who == '2':
            self.img = pygame.image.load("assets/images/InvaderC1.png")

    def replace(self,i):
        '''
        fonction qui permet le déplacement des ennemis
        Arguments: self -Vso
                   i  -int
        Return: None
        '''
        if self.face == 1:
            self.face = 0
        else:
            self.face = 1
        self.position()
        if self.direct == 'd':
            self.posx+=5
        if self.direct == 'g':
            self.posx-=5
        if i == 15:
            if self.direct == 'd':
                self.direct = 'g'
            else:
                self.direct = 'd'
            self.posy+=10

    def update(self):
        '''
        dessine le vaisseau par rapport à sa position
        Argument: self, -Vso
        Return: None
        '''
        self.surface.blit(self.img,[self.posx,self.posy])


    def position(self):
        '''
        Change l'image du personnage à chaque déplacement pour créer une petite animation
        argument: self -Vso
        Return: None
        '''
        if self.face == 0 and self.who == '0':
            self.img = pygame.image.load("assets/images/InvaderA1.png")
        if self.face == 1 and self.who == '0':
            self.img = pygame.image.load("assets/images/InvaderA2.png")
        if self.face == 0 and self.who == '1':
            self.img = pygame.image.load("assets/images/InvaderB1.png")
        if self.face == 1 and self.who == '1':
            self.img = pygame.image.load("assets/images/InvaderB2.png")
        if self.face == 0 and self.who == '2':
            self.img = pygame.image.load("assets/images/InvaderC1.png")
        if self.face == 1 and self.who == '2':
            self.img = pygame.image.load("assets/images/InvaderC2.png")

    def superpose(self,x,y):
        '''
        Retourne un booléen qui indique si un vaisseau est superposé à un autre élément en qui est en p
        osition x-y
        Argument: self -Vso
                  x,y  -int
        Return: Bool
        '''
        if self.posx >= x and self.posx <= x+30 and self.posy+32 >= y and self.posy+32 <= y+20:
            return True
        if self.posx+48 >= x and self.posx+48 <= x+30 and self.posy+32 >= y and self.posy+32 <= y+20:
            return True

    def tir(self):
        '''
        Créer un tir d'un ennemi par rapport à sa position et le retourne
        Argument: self, -Vso
        Return : Tir ,Objet
        '''
        tir = Tir(self.surface,self.posx+20,self.posy+35,'ennemi')
        return tir
        

class Vsojoueur:
    def __init__(self,surface,posx,posy):
        '''
        Initialise la class Vso , qui est un objet représentent un vaisseau, il
        peut être allié ou énemni, et il a une position
        Argument: self -Vso
                  surface -Fenetre pygame
                  posx,posy -int
                  who -str
        Return : None
        ''' 
        self.surface = surface
        self.posx = posx
        self.posy = posy
        self.direct = 'd'
        self.face = 0
        self.img = pygame.image.load("assets/images/joueur.png")

    def update(self):
        '''
        dessine le vaisseau par rapport à sa position
        Argument: self, -Vso
        Return: None
        '''
        self.surface.blit(self.img,[self.posx,self.posy])


    def droite(self):
        '''
        met à jour la position du vaisseau
        Argument: self, -Vso
        Return: None
        '''
        if self.posx <= 700:
            self.posx += 15
        
    def gauche(self):
        '''
        met à jour la position du vaisseau
        Argument: self, -Vso
        Return: None
        '''
        if self.posx >= 40:
            self.posx -= 15

    def tir(self):
        '''
        Créer un tir du joueur par rapport à sa position et le retourne
        Argument: self, -Vso
        Return : Tir ,Objet
        '''
        tir = Tir(self.surface,self.posx+25,self.posy-35,'joueur')
        return tir
        


class Wall:
    def __init__(self,surface,posx,posy,etat=0):
        '''
        Initialise la class Wall , qui est un objet représentent un mur,
        il a un nombre de point de vie, une position et peu être détruit par des tirs énnemi.
        Argument: self -Wall
                  surface -Fenetre pygame
                  posx,posy -int
                  etat -str
        Return : None
        '''
        self.surface = surface
        self.posx = posx
        self.posy = posy
        self.etat = etat
        if self.etat == 3:
            self.img = pygame.image.load("assets/images/Wall0.png")
        if self.etat == 2:
            self.img = pygame.image.load("assets/images/Wall1.png")
        if self.etat == 1:
            self.img = pygame.image.load("assets/images/Wall2.png")

    def update(self):
        '''
        met à jour l'étatdu mure et le change son image
        Argument: self, -Vso
        Return: None
        '''
        if self.etat == 3:
            self.img = pygame.image.load("assets/images/Wall0.png")
        if self.etat == 2:
            self.img = pygame.image.load("assets/images/Wall1.png")
        if self.etat == 1:
            self.img = pygame.image.load("assets/images/Wall2.png")
            
        self.surface.blit(self.img,[self.posx,self.posy])




class Tir:
    def __init__(self,surface,posx,posy,who):
        '''
        Initialise la class tir , qui est un objet représentent un tir,
        Il possède une postion de départ et traverse toute la fenêtre et s'arréte
        à la fin de celle-ci ou à la rencontre d'un obstacle.
        '''
        self.posx = posx
        self.posy = posy
        self.surface = surface
        self.who = who
        if who == 'ennemi':
            self.img = pygame.image.load("assets/images/bullet.png")
        else:
            self.img = pygame.image.load("assets/images/tir.png")

            
    def replace(self):
        '''
        Méthode qui permet de replacé un tir à chaque appelle
        Argument: self, Tir
        Return: None
        '''
        if not((self.posy >=860) or (self.posy<=-100)):
            if self.who == "ennemi":
                self.posy+=10
            else:
               self.posy-=10


            
    def update(self):
        '''
        methode qui redescine le tir
        Argument: self, Tir
        Return: None
        '''
        self.surface.blit(self.img,[self.posx,self.posy])


    def superpose_wall(self,x,y):
        '''
        Méthode qui retourne un boolean, True si un tir est à la même position qu'un objet Wall 
        Argument: self, Tir
                  x,y ,int,int
        Return Bool
        '''
        if self.posx >= x and self.posx <= x+30 and self.posy+17>= y and self.posy+17 <= y+20:
            return True
        if self.posx+8 >= x and self.posx+8 <= x+30 and self.posy+17 >= y and self.posy+17 <= y+20:
            return True

    def superpose_joueur(self,x,y):
        '''
        Méthode qui retourne un boolean, True si un tir est à la même position qu'un objet Joueur 
        Argument: self, Tir
                  x,y ,int,int
        Return Bool
        '''
        if self.posx >= x and self.posx <= x+60 and self.posy+17>= y and self.posy+17 <= y+32:
            return True
        if self.posx+8 >= x and self.posx+8 <= x+60 and self.posy+17 >= y and self.posy+17 <= y+32:
            return True

    def superpose_enemies(self,x,y):
        '''
        Méthode qui retourne un boolean, True si un tir est à la même position qu'un objet Enemies 
        Argument: self, Tir
                  x,y ,int,int
        Return Bool
        '''
        if self.posx >= x and self.posx <= x+48 and self.posy+17>= y and self.posy+17 <= y+32:
            return True
        if self.posx+8 >= x and self.posx+8 <= x+48 and self.posy+17 >= y and self.posy+17 <= y+32:
            return True

            
        

        
