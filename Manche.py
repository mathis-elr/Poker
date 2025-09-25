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
        
        self.liste_joueurs = [Joueur(joueur,self.partie,self.interface) for joueur in joueurs]
        self.liste_joueurs_ephemere = self.liste_joueurs.copy() #pareil que liste joueurs mais quand le dealer se couche on ne l'enleve pas pour pouvoir tjs donner la main a la personne a la gauche du dealer
        self.paquet = PaquetCartes() #type : PaquetCartes
        self.board = Board(self.partie,self.paquet) #type : Flop
        
        self.donnerLesMains() #donne deux cartes à chaque joueur, type : Carte
        
        '''
        Initialisation des rôles
        '''
        self.dealer = random.choice(self.liste_joueurs)#chosis un joueur au hasard pour être le dealer, type : Joueur
        self.smallBlind = self.liste_joueurs[(self.liste_joueurs.index(self.dealer) + 1)%len(self.liste_joueurs)]# = joueur à gauche du dealer, type : Joueur
        self.bigBlind = self.liste_joueurs[(self.liste_joueurs.index(self.smallBlind) + 1)%len(self.liste_joueurs)] #joueur qui précède le dealer (avec modulo pour que precedent de 0 → dernier elmt de la liste), type : Joueur
         
        self.dealer.label_badge.configure(text="D")
        self.dealer.frameBadge.grid(row=1,column=2,padx=5,pady=5)
        self.dealer.label_badge.grid(row=1,column=1,padx=5,pady=15)
        
        self.smallBlind.label_badge.configure(text="SB")
        self.smallBlind.frameBadge.grid(row=1,column=2,padx=5,pady=5)
        self.smallBlind.label_badge.grid(row=1,column=1,padx=5,pady=5)
        
        self.bigBlind.label_badge.configure(text="BB")
        self.bigBlind.frameBadge.grid(row=1,column=2,padx=5,pady=5)
        self.bigBlind.label_badge.grid(row=1,column=1,padx=5,pady=5)
        
        '''
        INITIALISATION DES MISES DE DEPART
        '''
        self.bigBlind.MEJ += 500
        self.bigBlind.solde -= 500
        self.bigBlind.labelSoldeVariable.configure(text="{} $".format(self.bigBlind.solde))
        self.bigBlind.labelMEJVariable.configure(text="{} $".format(self.bigBlind.MEJ))
        
        self.smallBlind.MEJ += 250
        self.smallBlind.solde -= 250
        self.smallBlind.labelSoldeVariable.configure(text="{} $".format(self.smallBlind.solde))
        self.smallBlind.labelMEJVariable.configure(text="{} $".format(self.smallBlind.MEJ))
        
        self.MEJ += (self.smallBlind.MEJ + self.bigBlind.MEJ)
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
        self.main = self.liste_joueurs[(self.liste_joueurs.index(self.bigBlind) + 1)%len(self.liste_joueurs)] #le joueur à gauche de la bigblinde commence, type : Joueur
        self.main.setMain() #on modifie la main du joueur qui commence
        
        
    def donnerMainPostFlop(self):
        '''
        au postflop la main va tjs au premier joueur actif a gauche du dealer(dès qu'une carte supplementaire a été retourné)
        ''' 
        self.main.setMain() #on desactive la main du joueur actuel
        self.main = self.liste_joueurs[(self.liste_joueurs_ephemere.index(self.dealer) + 1)%len(self.liste_joueurs_ephemere)]
        self.main.setMain() 
        
        
    def joueurSuivant(self):
        '''
        retire la main du joueur actuel pour le donner au joueur de gauche
        '''
        self.main.setMain()  
        self.main = self.liste_joueurs[(self.liste_joueurs.index(self.main)+1)%len(self.liste_joueurs)] #on passe la main au joueur suivant avec modulo pour que le suivant du dernier joueur soit le premier, type : Joueur
        self.main.setMain()