from customtkinter import *

class DefinirJoueurs(CTk):

    def __init__(self):
        super().__init__() #hérite de Ctk
        #crée la page
        self.title("Saisie des joueurs")
        set_appearance_mode("dark")    
        
        #text de demande d'entrée des noms des joueurs
        labelJoueurs = CTkLabel(self, text="Entrer les noms des joueurs", font=("Arial",20,"bold"),text_color="white")
        labelJoueurs.grid(row=1,column=1,padx=10,pady=10)

        self.frameJoueurs = CTkFrame(self,corner_radius=10,fg_color='white')
        self.frameJoueurs.grid(row=2,column=1,padx=10,pady=10)

        #2 entrées pour le nom du joueur 1 et 2
        entryNameJ1 = CTkEntry(self.frameJoueurs, placeholder_text="joueur 1", fg_color="#222222", placeholder_text_color='white')
        entryNameJ1.grid(row=1,column=1,padx=10,pady=10)
        entryNameJ2 = CTkEntry(self.frameJoueurs, placeholder_text="joueur 2", fg_color="#222222", placeholder_text_color='white')
        entryNameJ2.grid(row=2,column=1,padx=10,pady=10)
        
        self.joueurs = [entryNameJ1,entryNameJ2]
           
        #bouton pour ajouter des joueurs
        self.btnAjouterJoueur = CTkButton(self.frameJoueurs, text="➕",text_color='lightgrey',font=("Arial",10,"bold"), fg_color='darkgreen',hover_color='green',corner_radius=30,height=25,width=20,command=self.ajouterJoueur)
        self.btnSupprimerJoueur = CTkButton(self.frameJoueurs, text="➖",text_color='lightgrey',font=("Arial",10,"bold"), fg_color='darkred',hover_color='red', corner_radius=30,height=25,width=20,command=self.supprimerJoueur)
        self.btnAjouterJoueur.grid(row=2,column=2)

        #bouton pour commencer la partie
        btnJouer = CTkButton(self, text="Jouer",text_color='black',font=("Arial",15,"bold"), fg_color='white',hover_color='lightgrey',corner_radius=7,border_width=2,border_color="white", command=self.LancerPartie)
        btnJouer.grid(row=4,column=1,padx=20,pady=20)


        
    def ajouterJoueur(self):
        '''
        Ajoute un champs pour un joueur en plus dans la partie (max 4 joueurs)
        '''
        joueur = CTkEntry(self.frameJoueurs, placeholder_text="joueur {}".format(len(self.joueurs)+1), fg_color="#222222", placeholder_text_color='white')
        joueur.grid(row=len(self.joueurs)+1,column=1,padx=10,pady=10)
        self.joueurs.append(joueur)
        nb_joueurs = len(self.joueurs)
        
        if nb_joueurs<4:
            self.btnAjouterJoueur.grid(row=nb_joueurs,column=2)
        else:
            self.btnAjouterJoueur.grid_remove()
        if nb_joueurs>1:
            self.btnSupprimerJoueur.grid(row=nb_joueurs,column=3)
        else:
            self.btnSupprimerJoueur.grid_remove()
            
                     
    def supprimerJoueur(self):
        '''
        Retire un champs pour un joueur en moins dans la partie (min 2 joueurs)
        '''
        self.joueurs.pop(-1).destroy()
        nb_joueurs = len(self.joueurs)
        
        self.btnAjouterJoueur.grid(row=nb_joueurs,column=2)
        if nb_joueurs>2:
            self.btnSupprimerJoueur.grid(row=nb_joueurs,column=3)
        else:
            self.btnSupprimerJoueur.grid_remove()
            
            
    def LancerPartie(self):
        #verifier les noms saisies
        for joueur in self.joueurs:
            if joueur.get() == '' or ' ' in joueur.get():
                joueur.configure(border_color='red', placeholder_text_color='red')
            else:
                joueur.configure(border_color="#222222", placeholder_text_color='white')
          
        self.noms_joueurs = [joueur.get() for joueur in self.joueurs]  
            
        if '' not in self.noms_joueurs:     
            self.destroy()
            


            

