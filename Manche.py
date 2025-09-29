from customtkinter import *
import random

from PaquetCartes import PaquetCartes
from Board import Board

class Manche():
    def __init__(self,lesJoueurs,partie):
        self.MEJ = 0
        self.partie = partie
        
        self.liste_joueurs = lesJoueurs.copy()
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
        self.dealer.label_badge.grid(row=1,column=1,padx=5,pady=5)
        
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
        
        
        '''
        LES CARTES COMMUNES
        '''
        self.frameCarte1= CTkFrame(self.partie.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte2 = CTkFrame(self.partie.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte3= CTkFrame(self.partie.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte4 = CTkFrame(self.partie.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte5 = CTkFrame(self.partie.frameCartes, fg_color="white",width=140,height=195,corner_radius=20) 
        
        self.partie.interface.update()

  
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
        
    def finManche(self, gagnant):

        gagnant.solde += self.MEJ
        for joueur in self.liste_joueurs:
            
            #on vire les personnes qui ont plus de sous
            if joueur.solde == 0:
                self.partie.liste_joueurs.remove(joueur)
                del joueur # appel du destructeur du joueur
                
            joueur.reset() #on reinitialise les infos des joueurs
            joueur.MAJMontants() #on met a jour les labels en consequence
            
        #si il reste qu'un joueur alors fin partie
        if self.partie.liste_joueurs==1:
            self.partie.finPartie()
        else:
            #on relance une nouvelle manche dans 5s
            self.partie.interface.after(5000,lambda:self.partie.nvlManche())
        