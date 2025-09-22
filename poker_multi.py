from customtkinter import *
import random
import time
from Joueur import Joueur
from PaquetCartes import PaquetCartes
from Partie import Partie

poker = CTk()
set_appearance_mode("dark")
poker.geometry("700+300")


def Jouer(entryJoueurs):
    
    
    #créer le paquet de carte
    paquet = PaquetCartes()
    
    
    '''
    Instancier les joueurs saisie en type "Joueur"
    '''
    joueurs=[]
    for joueur in entryJoueurs:
        nom=joueur.get()
        solde=entrySoldeDep.get()
        type_joueur= Joueur("{}".format(nom),solde,frameInfo)
        joueurs.append(type_joueur)
        type_joueur.donner_main(paquet)
        
        
    for widget in poker.winfo_children():
        widget.destroy()
        
    poker.title("♥ ♦ poker ♣ ♠")
    
    '''
    POSITION DE LA FENETRE
    '''
    #recuperer la taille de l'ecran
    largeur_ecran = poker.winfo_screenwidth()
    hauteur_ecran = poker.winfo_screenheight()

    # Calculer la position en pourcentage
    pourcentage_x = 0.035
    pourcentage_y = 0.06

    # Appliquer la fenetre au centre de l'ecran
    poker.geometry("{}+{}".format(int(largeur_ecran * pourcentage_x),int(hauteur_ecran * pourcentage_y)))
  
   
    '''
    BOUTONS QUITTER / NVL PARTIE
    '''

    frameBoutons= CTkFrame(poker)
    frameBoutons.grid(row=1,column=2,padx=5,pady=10,sticky="n")

    btnNVLPartie = CTkButton(frameBoutons, text="Nouvelle partie",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white")
    btnNVLPartie.grid(row=1,column=1,padx=10,pady=10)

    btnQuitter = CTkButton(frameBoutons, text="Quitter",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white",command=quit)
    btnQuitter.grid(row=2,column=1,padx=10,pady=10)

    '''
    INFOS JOUEURS
    '''
    #frame pour les infos communes aux joueurs
    frameMiseEnJeu = CTkFrame(poker, width=200, height=100,fg_color="green",border_color="white",border_width=3,corner_radius=20)
    frameMiseEnJeu.grid(row=1,column=2,padx=5,pady=10,sticky="s")

    frameLabelMEJ = CTkFrame(frameMiseEnJeu,fg_color="black",corner_radius=10)
    frameLabelMEJ.grid(row=1,column=1,padx=10,pady=10)

    labelMiseEnJeu = CTkLabel(frameLabelMEJ, text="Mise En Jeu", font=("Arial",15),text_color="white")
    labelMiseEnJeu.grid(row=2,column=1,padx=10,pady=10)

    labelMiseEnJeuVariable = CTkLabel(frameMiseEnJeu, text="{} $".format(partie.getMEJ()), font=("Arial",20,"bold"),text_color="gold")
    labelMiseEnJeuVariable.grid(row=2,column=1,padx=10,pady=10)


    '''
    PLATEAU DE JEU
    '''
    #frame représentant le plateau de jeu (apparissions des cartes)
    frameCartes = CTkFrame(poker, width=900, height=250,fg_color="green",border_color="red",border_width=5,corner_radius=60)
    frameCartes.grid(row=2,column=1,columnspan=3,padx=20,pady=20) 
    
    #création des 5 cartes physique
    framesCartes=[]
    cartes=[]
    for i in range(5):
        frameCarte = CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        framesCartes.append(frameCarte)
        cartes.append(paquet.tirerUneCarte())
    
    for carte in cartes:
        carte.carte_physique(framesCartes[cartes.index(carte)])
        
    
    
    '''
    MESSAGE INFOS
    '''
    frameInfo = CTkFrame(frameCartes,fg_color="white",corner_radius=20)
    frameInfo.grid(row=1,column=1,columnspan=3,padx=10,pady=10)

    labelInfo = CTkLabel(frameInfo, text="", font=("Times New Roman",40),text_color="black")
    labelInfo.grid(row=1,column=1,padx=20,pady=20)
    
    '''
    CREATION FRAME INFO POUR CHAQUE JOUEUR
    '''
    for joueur in joueurs:
        #frame principal
        frame = CTkFrame(poker, width=350, height=200, fg_color="white",corner_radius=15)

        '''
        VOIR CARTES
        '''
        #frame pour que le joueur voit ses cartes
        frameVoirCartes = CTkFrame(frame,height=50,fg_color="grey",border_color="black",border_width=2,corner_radius=10)
        btnVoirCartes = CTkButton(frameVoirCartes, text="Voir Cartes",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white")
        labelVoirCarte = CTkLabel(frameVoirCartes, text="{} de {}".format(joueur.carte1.getValeur(),joueur.carte1.getCouleur()), font=("Arial",15,"bold"),text_color="white")
        labelVoirCarte2 = CTkLabel(frameVoirCartes, text="{} de {}".format(joueur.carte2.getValeur(),joueur.carte2.getCouleur()), font=("Arial",15,"bold"),text_color="white")
        
        '''
        SE COUCHER
        '''
        btnSeCoucher = CTkButton(frame, text="se coucher",text_color='white', fg_color='darkblue',hover_color='blue')
        
        '''
        SOLDE
        '''
        #frame pour visualiser le solde
        frameSolde = CTkFrame(frame,height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
        #label simple pour exprimer le solde
        labelSolde = CTkLabel(frameSolde, text="Solde :", font=("Arial",15),text_color="white")
        #label contenant le solde (variable)
        labelSoldeVariable = CTkLabel(frameSolde, text="{} $".format(joueur.getSolde()), font=("Arial",15),text_color="white")

        '''
        MISE EN JEU
        '''
        #frame pour visualiser la somme mise en jeu par le joueur
        frameMEJ = CTkFrame(frame,height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
        #label simple pour exprimer la mise en jeu
        labelMEJ = CTkLabel(frameMEJ, text="Mise en jeu :", font=("Arial",15),text_color="white")
        #label contenant la mise en jeu (variable)
        labelMEJVariable = CTkLabel(frameMEJ, text="{} $".format(joueur.getMEJ()), font=("Arial",15),text_color="white")

        '''
        CHECK
        '''
        btnCheckJ = CTkButton(frame,width=50,height=50, text="check",text_color='black', fg_color='darkorange',hover_color='orange',corner_radius=50)

        '''
        MISER
        '''
        #frame pour miser 
        frameMiser = CTkFrame(frame, height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
        #entrée pour la mise en jeu souhaité
        entryMiseEnJeu = CTkEntry(frameMiser, placeholder_text="mise")
        #bouton pour valider la mise en jeu
        btnMiser = CTkButton(frameMiser, text="Miser",text_color='black', fg_color='white',hover_color='lightgrey')
        #bouton pour allin
        btnAllIn = CTkButton(frameMiser, text="All In",text_color='black', fg_color='white',hover_color='red')
        
        
        '''
        POSITIONNER LES FRAMES DU JOUEUR
        '''
        ligne=[1,1,3,3]
        colonne=[1,3,3,1]
        frame.grid(row=ligne[joueurs.index(joueur)],column=colonne[joueurs.index(joueur)],padx=20,pady=20)
        frameVoirCartes.grid(row=1,column=1,columnspan=2,padx=20,pady=20)
        btnVoirCartes.grid(row=1,column=1,padx=10,pady=10)
        labelVoirCarte.grid(row=1,column=2,padx=10,pady=10)
        labelVoirCarte2.grid(row=1,column=3,padx=10,pady=10)
        btnSeCoucher.grid(row=1,column=3,padx=10,pady=10)
        frameSolde.grid(row=2,column=1,padx=20,pady=1,sticky="w")
        labelSolde.grid(row=1,column=1,padx=10,pady=10)
        labelSoldeVariable.grid(row=1,column=2,padx=10,pady=10)
        frameMEJ.grid(row=2,column=2,padx=20,pady=1)
        labelMEJ.grid(row=1,column=1,padx=10,pady=10)
        labelMEJVariable.grid(row=1,column=2,padx=10,pady=10)
        btnCheckJ.grid(row=2,column=3,padx=10,pady=10)
        frameMiser.grid(row=3,column=1,columnspan=3,padx=20,pady=20,sticky="w")
        entryMiseEnJeu.grid(row=2,column=1,padx=10,pady=10)
        btnMiser.grid(row=2,column=2,padx=10,pady=10)
        btnAllIn.grid(row=2,column=3,padx=10,pady=10) 


        #créer une partie
        partie = Partie(joueurs)
    
    

        



def DefinirJoueurs():
    '''
    fonction lancé lors de l'execution du programme 
    Demande à l'utilisateur de saisir les noms des joueurs puis lance la partie si le bouton 'jouer' est cliqué ( -> fonction NvlPartie())
    '''

    #accessibilité dans tout le code
    global labelJoueurs,btnJouer,soldeJ1,soldeJ2,frameJoueurs,btnAddJoueur,btnDellJoueur,entrySoldeDep
    
    poker.title("Saisie Joueurs")

    #text de demande d'entrée des noms des joueurs
    labelJoueurs = CTkLabel(poker, text="Entrez les noms des joueurs", font=("Arial",20,"bold"),text_color="white")
    labelJoueurs.grid(row=1,column=1,padx=10,pady=10)

    frameJoueurs = CTkFrame(poker,border_color="white")
    frameJoueurs.grid(row=2,column=1,padx=10,pady=10)
    
    entryJoueurs=[]
    
    #bouton pour ajouter des joueurs
    btnAddJoueur = CTkButton(frameJoueurs, text="+",text_color='black',font=("Arial",15,"bold"), fg_color='white',hover_color='green',corner_radius=50,height=20,width=10,command=lambda :AddJoueur(entryJoueurs))
    btnDellJoueur = CTkButton(frameJoueurs, text="-",text_color='black',font=("Arial",15,"bold"), fg_color='white',hover_color='red',corner_radius=50,height=20,width=30,command=lambda :DellJoueur(entryJoueurs))
    
    AddJoueur(entryJoueurs)
    AddJoueur(entryJoueurs)
    
    #entry du solde de départ des joueurs
    entrySoldeDep = CTkEntry(poker, placeholder_text="solde de départ")
    entrySoldeDep.grid(row=4,column=1,padx=10,pady=10)

    #bouton pour commencer la partie
    btnJouer = CTkButton(poker, text="Jouer",text_color='black',font=("Arial",15,"bold"), fg_color='white',hover_color='lightgrey',corner_radius=7,border_width=2,border_color="white",command=lambda:Jouer(entryJoueurs))
    btnJouer.grid(row=5,column=1,padx=20,pady=20)
    



def AddJoueur(entryJoueurs):
    '''
    Ajoute un champs pour un joueur en plus dans la partie (max 4 joueurs)
    '''
    entry = CTkEntry(frameJoueurs, placeholder_text="joueur {}".format(len(entryJoueurs)+1))
    entry.grid(row=len(entryJoueurs),column=1,padx=10,pady=10)
    entryJoueurs.append(entry)
    if len(entryJoueurs)<4:
        btnAddJoueur.grid(row=len(entryJoueurs)-1,column=2,padx=5,pady=5)
    else:
        btnAddJoueur.grid_remove()
    if len(entryJoueurs)>1:
        btnDellJoueur.grid(row=len(entryJoueurs)-1,column=3,padx=5,pady=5)
    else:
        btnDellJoueur.grid_remove()

        
def DellJoueur(entryJoueurs):
    '''
    Retire un champs pour un joueur en moins dans la partie (min 2 joueurs)
    '''
    entryJoueurs.pop(-1).destroy()
    btnAddJoueur.grid(row=len(entryJoueurs)-1,column=2,padx=5,pady=5)
    if len(entryJoueurs)>2:
        btnDellJoueur.grid(row=len(entryJoueurs)-1,column=3,padx=5,pady=5)
    else:
        btnDellJoueur.grid_remove()
    
    

DefinirJoueurs()
poker.mainloop()
         


 
        
        
 
        
 

