from customtkinter import *
import random


from Joueur import Joueur
from Manche import Manche


class Partie():
    def __init__(self,interface,joueurs):
        
        self.interface = interface
        self.interface.title("♠️♣️ poker ♦️♥️")
        set_appearance_mode("dark")

        self.noms_joueurs = joueurs
        
        '''
        FRAME INFOS GENERALES
        '''
        frameInfoGenerales = CTkFrame(self.interface) 
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
        frameMiseEnJeu = CTkFrame(frameInfoGenerales, width=200, height=100,fg_color="green",border_color="red",border_width=3,corner_radius=20)
        frameMiseEnJeu.grid(row=2,column=1,padx=10,pady=10,sticky="s")

        labelMiseEnJeu = CTkLabel(frameMiseEnJeu, text="Mise En Jeu", font=("Arial",20,"bold"),text_color="gold")
        labelMiseEnJeu.grid(row=1,column=1,padx=10,pady=10)

        self.labelMiseEnJeuVariable = CTkLabel(frameMiseEnJeu, text="0 $", font=("Arial",20),text_color="gold")
        self.labelMiseEnJeuVariable.grid(row=2,column=1,padx=10,pady=10)
        
        
        '''
        BOARD
        '''
        #frame représentant le plateau de jeu (apparissions des cartes)
        self.frameCartes = CTkFrame(self.interface, width=900, height=250,fg_color="green",border_color="red",border_width=5,corner_radius=60)
        
        self.frameCarte1= CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte2 = CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte3= CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte4 = CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte5 = CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20) 
        
        self.frameCartes.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
                
        
        '''
        Creation de la première manche
        '''
        self.liste_joueurs = [Joueur(joueur,self,self.interface) for joueur in joueurs]
        self.manche = Manche(self.liste_joueurs,self,interface)
        self.manche.setMainPreFlop() #personne qui doit commencer (à gauche de la big blinde), type : Joueur
        
        self.creeFrames() #crée les joueurs dans l'interface
        
    
    #--------
    # methodes
    #--------   
    def creeFrames(self):
        '''
        afficher les frames de chaque joueurs
        '''
        for joueur in self.liste_joueurs:
            joueur.faireApparaitreFrame() 
            
    def nvlPartie(self):
        '''
        on supprime la patie actuele t on en crée ue nouvelle
        '''
        for widget in self.interface.winfo_children():
            widget.destroy()
            
        Partie(self.interface,self.noms_joueurs)
    
    def quitter(self):
        '''
        ferme l'application → detruit la fenetre
        '''
        self.destroy()
        
        