from customtkinter import *
import random

from PaquetCartes import PaquetCartes
from Joueur import Joueur
from Board import Board

class Partie(CTk):
    def __init__(self,joueurs):
        super().__init__()
        self.title("♠️♣️ poker ♦️♥️")
        set_appearance_mode("dark")

        self.paquet = PaquetCartes(self) #type : PaquetCartes
        self.board = Board(self,self.paquet) #type : Flop
        self.liste_joueurs = [Joueur(joueurs[i],i,self) for i in range (len(joueurs))] #liste des joueurs de type Joueur(nom,numero,partie)
        self.MEJ = 0
        
        #crée un frame pour chaque joueur  
        self.creeFrames()     
        
        self.donnerLesMains() #donne deux cartes à chaque joueur, type : Carte
        
        self.dealer = random.choice(self.liste_joueurs).numero #chosis un joueur au hasard pour être le dealer, type : int (numero du joueur)
        self.smallBlind = self.liste_joueurs[(self.dealer+1)%len(self.liste_joueurs)].numero # = joueur à gauche du dealer, type : int (numero du joueur)
        self.bigBlind = self.liste_joueurs[(self.smallBlind+1)%len(self.liste_joueurs)].numero #joueur qui précède le dealer (avec modulo pour que precedent de 0 → dernier elmt de la liste), type : int (numero du joueur)  
        
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
        
        
        self.setMainPreFlop() # personne qui doit commencer (à gauche de la big blinde), type : int (numero du joueur)

        
        '''
        FRAME INFOS GENERALES
        '''
        frameInfoGenerales = CTkFrame(self) 
        frameInfoGenerales.grid(row=1,column=2)    
                
        '''
        BOUTONS QUITTER / NVL PARTIE
        '''
        frameBoutons= CTkFrame(frameInfoGenerales)
        frameBoutons.grid(row=1,column=1,padx=5,pady=10,sticky="n")

        btnNVLPartie = CTkButton(frameBoutons, text="Nouvelle partie",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white", command=self.nvlPartie)
        btnNVLPartie.grid(row=1,column=1,padx=10,pady=10)

        btnQuitter = CTkButton(frameBoutons, text="Quitter",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white",command=self.quitter)
        btnQuitter.grid(row=2,column=1,padx=10,pady=10)

        '''
        INFOS JOUEURS
        '''
        #frame pour les infos communes aux joueurs
        frameMiseEnJeu = CTkFrame(frameInfoGenerales, width=200, height=100,fg_color="green",border_color="white",border_width=3,corner_radius=20)
        frameMiseEnJeu.grid(row=2,column=1,padx=5,pady=10,sticky="s")

        frameLabelMEJ = CTkFrame(frameMiseEnJeu,fg_color="black",corner_radius=10)
        frameLabelMEJ.grid(row=1,column=1,padx=10,pady=10)

        labelMiseEnJeu = CTkLabel(frameLabelMEJ, text="Mise En Jeu", font=("Arial",15),text_color="white")
        labelMiseEnJeu.grid(row=2,column=1,padx=10,pady=10)

        self.labelMiseEnJeuVariable = CTkLabel(frameMiseEnJeu, text="{} $".format(self.MEJ), font=("Arial",20,"bold"),text_color="gold")
        self.labelMiseEnJeuVariable.grid(row=2,column=1,padx=10,pady=10)
        
        self.update()
                
        '''
        MESSAGE INFOS
        
        frameInfo = CTkFrame(frameInfoGenerales,fg_color="white",corner_radius=20)
        frameInfo.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

        labelInfo = CTkLabel(frameInfo, text="", font=("Times New Roman",40),text_color="black")
        labelInfo.grid(row=1,column=1,padx=20,pady=20) 
        ''' 
    
    
    #--------
    # setters
    #-------- 
    def donnerLesMains(self):
        #on crée la main de chaque joueur
        for joueur in self.liste_joueurs:
            joueur.donner_main(self.paquet)
            
    def setMainPreFlop(self):
        self.main = self.liste_joueurs[(self.bigBlind+1)%len(self.liste_joueurs)].numero #le joueur à gauche de la bigblinde commence, type : int (numero du joueur)
        self.liste_joueurs[self.main].setMain() #on modifie la main du joueur qui commence
        
    def creeFrames(self):
        for joueur in self.liste_joueurs:
            joueur.faireApparaitreFrame() 
    
    def setMainPostFlop(self):
        self.main = self.smallBlind #on donne tjs la main à la smallbinde après qu'une carte est été devoilé
        self.liste_joueurs[self.main].setMain()
        
    def changerMain(self):
        self.main = self.liste_joueurs[(self.main+1)%len(self.liste_joueurs)].numero #on passe la main au joueur suivant avec modulo pour que le suivant du dernier joueur soit le premier, type : int
        self.liste_joueurs[self.main].setMain()
    
    #--------
    # methodes
    #--------   
    def nvlPartie(self):
        pass
    
    def quitter(self):
        self.destroy()
        
        