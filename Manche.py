from customtkinter import *
import random

from PaquetCartes import PaquetCartes
from Board import Board
from Joueur import Joueur

class Manche():
    def __init__(self,joueurs,partie,interface):
        self.MEJ = 0
        self.partie = partie
        self.interface = interface
        
        
        self.liste_joueurs = [Joueur(joueurs[i],i,self.partie,self.interface) for i in range (len(joueurs))]
        self.liste_joueurs_ephemere = self.liste_joueurs #pareil que liste joueurs mais quand le dealer se couche on ne l'enleve pas pour pouvoir tjs donner la main a la personne a la gauche du dealer
        self.paquet = PaquetCartes() #type : PaquetCartes
        self.board = Board(self.partie,self.paquet) #type : Flop
        
        self.donnerLesMains() #donne deux cartes à chaque joueur, type : Carte
        
        '''
        Initialisation des rôles
        '''
        self.dealer = random.choice(self.liste_joueurs).numero #chosis un joueur au hasard pour être le dealer, type : int (numero du joueur)
        self.smallBlind = self.liste_joueurs[(self.dealer+1)%len(self.liste_joueurs)].numero # = joueur à gauche du dealer, type : int (numero du joueur)
        self.bigBlind = self.liste_joueurs[(self.smallBlind+1)%len(self.liste_joueurs)].numero #joueur qui précède le dealer (avec modulo pour que precedent de 0 → dernier elmt de la liste), type : int (numero du joueur)  
         
        self.liste_joueurs[self.dealer].label_badge.configure(text="D")
        self.liste_joueurs[self.dealer].frameBadge.grid(row=1,column=2,padx=5,pady=5)
        self.liste_joueurs[self.dealer].label_badge.grid(row=1,column=1,padx=5,pady=5)
        
        self.liste_joueurs[self.smallBlind].label_badge.configure(text="SB")
        self.liste_joueurs[self.smallBlind].frameBadge.grid(row=1,column=2,padx=5,pady=5)
        self.liste_joueurs[self.smallBlind].label_badge.grid(row=1,column=1,padx=5,pady=5)
        
        self.liste_joueurs[self.bigBlind].label_badge.configure(text="BB")
        self.liste_joueurs[self.bigBlind].frameBadge.grid(row=1,column=2,padx=5,pady=5)
        self.liste_joueurs[self.bigBlind].label_badge.grid(row=1,column=1,padx=5,pady=5)
        
        '''
        INITIALISATION DES MISES DE DEPART
        '''
        self.liste_joueurs[self.bigBlind].MEJ += 500
        self.liste_joueurs[self.bigBlind].solde -= 500
        self.liste_joueurs[self.bigBlind].labelSoldeVariable.configure(text="{} $".format(self.liste_joueurs[self.bigBlind].solde))
        self.liste_joueurs[self.bigBlind].labelMEJVariable.configure(text="{} $".format(self.liste_joueurs[self.bigBlind].MEJ))
        
        self.liste_joueurs[self.smallBlind].MEJ += 250
        self.liste_joueurs[self.smallBlind].solde -= 250
        self.liste_joueurs[self.smallBlind].labelSoldeVariable.configure(text="{} $".format(self.liste_joueurs[self.smallBlind].solde))
        self.liste_joueurs[self.smallBlind].labelMEJVariable.configure(text="{} $".format(self.liste_joueurs[self.smallBlind].MEJ))
        
        self.MEJ += (self.liste_joueurs[self.smallBlind].MEJ + self.liste_joueurs[self.bigBlind].MEJ)
        self.partie.labelMiseEnJeuVariable.configure(text="{} $".format(self.MEJ))
        
        self.interface.update()

  
    #--------
    # methodes
    #-------- 
    def donnerLesMains(self):
        #on crée la main de chaque joueur
        for joueur in self.liste_joueurs:
            joueur.donner_main(self.paquet)
            
    def setMainPreFlop(self):
        self.main = self.liste_joueurs[(self.bigBlind+1)%len(self.liste_joueurs)].numero #le joueur à gauche de la bigblinde commence, type : int (numero du joueur)
        self.liste_joueurs[self.main].setMain() #on modifie la main du joueur qui commence
        
        
    def donnerMainPostFlop(self):
        '''
        au postflop la main va tjs au premier joueur actif a gauche du dealer(dès qu'une carte supplementaire a été retourné)
        ''' 
        self.liste_joueurs[self.main].setMain() #on desactive la main du joueur actuel
        self.main = (self.dealer + 1)%len(self.partie.liste_joueurs)
        self.partie.manche.liste_joueurs[self.main].setMain() 
        
        
    def joueurSuivant(self):
        '''
        retire la main du joueur actuel pour le donner au joueur de gauche
        '''
        self.liste_joueurs[self.main].setMain()  
        self.main = self.liste_joueurs[(self.main+1)%len(self.liste_joueurs)].numero #on passe la main au joueur suivant avec modulo pour que le suivant du dernier joueur soit le premier, type : int
        self.liste_joueurs[self.main].setMain()
        
    def MAJDesRoles(self):
        self.dealer  = self.liste_joueurs_ephemere[self.dealer].numero -1
        self.smallBlind = self.liste_joueurs_ephemere[self.smallBlind].numero -1
        self.bigBlind = self.liste_joueurs_ephemere[self.bigBlind].numero -1