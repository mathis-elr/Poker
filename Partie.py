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
        self.frameCartes.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
                
        
        '''
        Creation de la première manche
        '''
        self.liste_joueurs = [Joueur(nom_joueur,self) for nom_joueur in joueurs]
        self.manche = Manche(self.liste_joueurs,self)
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
          
            
    def nvlManche(self):
        #on enleve les cartes du flop 
        for frameCarte in self.frameCartes.winfo_children():
            frameCarte.destroy()
            
        for joueur in self.liste_joueurs:
            joueur.reset() #on reinitialise les infos des joueurs
            joueur.MAJMontants() #on met a jour les labels en consequence
            
        self.manche.__init__(self.liste_joueurs,self)
        self.manche.setMainPreFlop() #personne qui doit commencer (à gauche de la big blinde), type : Joueur
            
            
    def nvlPartie(self):
        '''
        on supprime la partie actuele et on en crée ue nouvelle avec les mêmes joueurs
        '''
        for widget in self.interface.winfo_children():
            widget.destroy()
            
        Partie(self.interface,self.noms_joueurs)
        
        
    def finPartie(self):
        '''
        lance une nouvelle partie 5s après l'appel de cette fonction
        '''
        self.interface.after(5000,lambda:self.nvlPartie())
    
    
    def quitter(self):
        '''
        ferme l'application → detruit la fenetre
        '''
        self.destroy()
        
        