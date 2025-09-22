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
        self.flop = Board(self,self.paquet) #type : Flop
        self.liste_joueurs = [Joueur(joueurs[i],i,self) for i in range (len(joueurs))] #liste des joueurs de type Joueur(nom,numero,partie)
        self.MEJ = 0
        
        posX = [1,1,3,3] # =lignes dans l'application (row dans le code)
        posY = [1,3,3,1] # =colonnes dans l'application (column dans le code)
        #crée un frame pour chaque joueur  
        self.creeFrames(posX,posY)     
        
        self.donnerLesMains() #donne deux cartes à chaque jour, type : Carte
        
        self.main = self.setMainDepart() #personne qui doit jouer, type : int (numero du joueur)
        self.bigBlind = self.liste_joueurs[(self.main-1)%len(self.liste_joueurs)].numero #joueur qui précède le joueur actuel avec module pour que precedent de 0 → dernier elmt de la liste, type : int (numero du joueur)
        self.smallBlind = self.main # = joueur qui commence, type : int (numero du joueur)
        
        '''
        INITIALISATION DES MISES DE DEPART
        '''
        self.liste_joueurs[self.bigBlind].MEJ = 500
        self.liste_joueurs[self.bigBlind].solde-=500
    
        self.liste_joueurs[self.smallBlind].MEJ = 250
        self.liste_joueurs[self.smallBlind].solde-=250
        
        self.liste_joueurs[self.bigBlind].labelSoldeVariable.configure(text="{}".format(self.liste_joueurs[self.bigBlind].solde))
        self.liste_joueurs[self.bigBlind].labelMEJVariable.configure(text="{}".format(self.liste_joueurs[self.bigBlind].MEJ))
        self.liste_joueurs[self.smallBlind].labelSoldeVariable.configure(text="{}".format(self.liste_joueurs[self.smallBlind].solde))
        self.liste_joueurs[self.smallBlind].labelMEJVariable.configure(text="{}".format(self.liste_joueurs[self.smallBlind].MEJ))
        self.update()
        
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

        self.labelMiseEnJeuVariable = CTkLabel(frameMiseEnJeu, text="700 $", font=("Arial",20,"bold"),text_color="gold")
        self.labelMiseEnJeuVariable.grid(row=2,column=1,padx=10,pady=10)
                
        '''
        MESSAGE INFOS
        
        frameInfo = CTkFrame(frameInfoGenerales,fg_color="white",corner_radius=20)
        frameInfo.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

        labelInfo = CTkLabel(frameInfo, text="", font=("Times New Roman",40),text_color="black")
        labelInfo.grid(row=1,column=1,padx=20,pady=20) 
        ''' 


        '''
        PLATEAU DE JEU
        '''
        #frame représentant le plateau de jeu (apparissions des cartes)
        frameCartes = CTkFrame(self, width=900, height=250,fg_color="green",border_color="red",border_width=5,corner_radius=60)
        frameCartes.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
        
        self.frameCarte1= CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte2 = CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte3= CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte4 = CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte5 = CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)  
        
            
    #--------
    # getters
    #--------    
    def getMEJ(self):
        return self.MEJ
    
    def getListeJoueurs(self):
        return self.liste_joueurs
    
    
    #--------
    # setters
    #-------- 
    def donnerLesMains(self):
        #on crée la main de chaque joueur
        for joueur in self.liste_joueurs:
            joueur.donner_main(self.paquet)
            
    def setMainDepart(self):
        numero_joueur = random.choice(self.liste_joueurs).numero #chosis un joueur au hasard pour commencer, type : int (numero du joueur)
        self.liste_joueurs[numero_joueur].setMain() #on modifie la main du joueur qui commence
        return numero_joueur
        
    def creeFrames(self,posX,posY):
        for i in range(len(self.liste_joueurs)):
            self.liste_joueurs[i].faireApparaitreFrame(posX[i],posY[i]) 
            
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
        
        