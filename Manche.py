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
        self.paquet = PaquetCartes() #type : PaquetCartes
        self.board = Board(self.partie,self.paquet) #type : Flop
        
        self.donnerLesMains() #donne deux cartes à chaque joueur, type : Carte
        
        self.dealer = random.choice(self.liste_joueurs).numero #chosis un joueur au hasard pour être le dealer, type : int (numero du joueur)
        self.smallBlind = self.liste_joueurs[(self.dealer+1)%len(self.liste_joueurs)].numero # = joueur à gauche du dealer, type : int (numero du joueur)
        self.bigBlind = self.liste_joueurs[(self.smallBlind+1)%len(self.liste_joueurs)].numero #joueur qui précède le dealer (avec modulo pour que precedent de 0 → dernier elmt de la liste), type : int (numero du joueur)  
        
        
        self.labelDealer = CTkLabel(self.liste_joueurs[self.dealer].frame, font=("Arial",15,"bold"), text_color="black", text="D")
        self.labelSmallBlind = CTkLabel(self.liste_joueurs[self.smallBlind].frame, font=("Arial",15,"bold"), text_color="black", text="SB")
        self.labelBigBlind = CTkLabel(self.liste_joueurs[self.bigBlind].frame, font=("Arial",15,"bold"), text_color="black", text="BB")
        self.labelDealer.grid(row=1,column=3,sticky="e", padx=20)
        self.labelSmallBlind.grid(row=1,column=3,sticky="e", padx=20)
        self.labelBigBlind.grid(row=1,column=3,sticky="e", padx=20)
        
        '''
        INITIALISATION DES MISES DE DEPART
        '''
        self.liste_joueurs[self.bigBlind].MEJ += 500
        self.liste_joueurs[self.bigBlind].solde -= 500
    
        self.liste_joueurs[self.smallBlind].MEJ += 250
        self.liste_joueurs[self.smallBlind].solde -= 250
        
        self.liste_joueurs[self.bigBlind].labelSoldeVariable.configure(text="{}".format(self.liste_joueurs[self.bigBlind].solde))
        self.liste_joueurs[self.bigBlind].labelMEJVariable.configure(text="{}".format(self.liste_joueurs[self.bigBlind].MEJ))
        self.liste_joueurs[self.smallBlind].labelSoldeVariable.configure(text="{}".format(self.liste_joueurs[self.smallBlind].solde))
        self.liste_joueurs[self.smallBlind].labelMEJVariable.configure(text="{}".format(self.liste_joueurs[self.smallBlind].MEJ))
        
        
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
        
        
    def setMainPostFlop(self):
        self.main = self.smallBlind #on donne tjs la main à la smallbinde après qu'une carte est été devoilé
        self.liste_joueurs[self.main].setMain()
        
        
    def changerMain(self):
        self.main = self.liste_joueurs[(self.main+1)%len(self.liste_joueurs)].numero #on passe la main au joueur suivant avec modulo pour que le suivant du dernier joueur soit le premier, type : int
        self.liste_joueurs[self.main].setMain()