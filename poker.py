from customtkinter import *
import random
import time
import inspect

poker = CTk()
set_appearance_mode("dark")
poker.geometry("700+300")

def LancerLeJeu():
    '''
    CREATION DU JEU DE CARTE
    '''

    global table_cartes,table_couleur,table_numero,Carte1J1,Carte1J2,Carte2J1,Carte2J2

    table_couleur=["coeur","carreau","pique","trèfle"]
    table_numero=["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]
    table_cartes=[]

    #création du paquet de carte (52 cartes)
    for couleur in table_couleur:
        for numero in table_numero:
            table_cartes.append([numero,couleur])

    '''
    CREATION DES MAINS DES JOUEURS
    '''
    Carte1J1=[]
    Carte1J2=[]
    Carte2J1=[]
    Carte2J2=[]


    '''
    SAISIE DES JOUEURS
    '''
    DefinirJoueurs()







def DefinirJoueurs():
    '''
    fonction lancé lors de l'execution du programme 
    Demande à l'utilisateur de saisir les noms des joueurs puis lance la partie si le bouton 'jouer' est cliqué ( -> fonction NvlPartie())
    '''

    #accessibilité dans tout le code
    global entryNameJ1,entryNameJ2,labelJoueurs,btnJouer,soldeJ1,soldeJ2
    
    poker.title("Saisie Joueurs")

    #text de demande d'entrée des noms des joueurs
    labelJoueurs = CTkLabel(poker, text="Entrez les noms des joueurs", font=("Arial",20,"bold"),text_color="white")
    labelJoueurs.grid(row=1,column=1,padx=10,pady=10)

    #2 entrées pour le nom du joueur 1 et 2
    entryNameJ1 = CTkEntry(poker, placeholder_text="joueur 1")
    entryNameJ1.grid(row=2,column=1,padx=10,pady=10)
    entryNameJ2 = CTkEntry(poker, placeholder_text="joueur 2")
    entryNameJ2.grid(row=3,column=1,padx=10,pady=10)
    
    

    #bouton pour commencer la partie
    btnJouer = CTkButton(master=poker, text="Jouer",text_color='black',font=("Arial",15,"bold"), fg_color='white',hover_color='lightgrey',corner_radius=7,border_width=2,border_color="white", command=LancePartie)
    btnJouer.grid(row=4,column=1,padx=20,pady=20)

    





def LancePartie():
    
    #accessibilité dans tout le code
    global labelVoirCarte1J1,labelVoirCarte2J1,labelVoirCarte1J2,labelVoirCarte2J2,Carte1J1,Carte2J1,nomJ1,nomJ2,labelInfo,JCommence,main,ACheckJ1,ACheckJ2,JCommenceNom
    global NbCarteDevoile,carte1,carte2,carte3,carte4,carte5,soldeJ1,soldeJ2,AallInJ1,AallInJ2
    global Carte1J2,Carte2J2,entryMiseEnJeuJ1,entryMiseEnJeuJ2,labelMEJ1Variable,labelMEJ2Variable,labelMiseEnJeuVariable,labelSoldeJ1Variable,labelSoldeJ2Variable,MEJ,MEJ1,MEJ2
    global frameCarte1,frameCarte2,frameCarte3,frameCarte4,frameCarte5

    #verifie que les entry on une valeur
    if entryNameJ1.get()=="" or entryNameJ2.get()=="":
        None 
        #return 0
        
    poker.title("♥ ♦ poker ♣ ♠")

    #recupération des entry (noms des joueurs)
    nomJ1=entryNameJ1.get()
    nomJ2=entryNameJ2.get()

    '''
    SUPPRESION DE PAGE D'AJOUT DES JOUEURS
    '''
    btnJouer.grid_forget()
    entryNameJ1.grid_forget()
    entryNameJ2.grid_forget()
    labelJoueurs.grid_forget()
    
    
    '''
    MISE A JOUR DE LA POSITION DE LA FENETRE
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
    CREDITER LES SOLDES
    '''
    #solde Joueur 2
    soldeJ1 = 10000

    #solde joueur 2
    soldeJ2 = 10000
    
    
    '''
    INITIALISATION DES MISES
    '''
    #Mise en jeux Joueur 1
    MEJ1 = 0

    #Mise en jeux Joueur 2
    MEJ2 = 0

    #Mise en Jeux partie
    MEJ = 0


    '''
    INITIALISATION CHECK
    '''
    ACheckJ1=False
    ACheckJ2=False

    
    '''
    INITIALISATION CHECK
    '''
    AallInJ1=False
    AallInJ2=False


    '''
    jeux de cartes pour cette partie
    '''
    copieTableCartes = table_cartes.copy()


    '''
    TIRAGE DES CARTES
    '''
    #tirage des cartes au hasard J1
    Carte1J1 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte1J1)
    Carte2J1 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte2J1)

    #tirage des cartes au hasard J1
    Carte1J2 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte1J2)
    Carte2J2 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte2J2)

    #tirage du flop au hasard
    carte1 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte1)
    carte2 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte2)
    carte3 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte3)

    #tirage 4eme carte
    carte4 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte4)

    #tirage 5eme carte 
    carte5 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte5)

    #compteur de cartes dévoilés (3, 4, 5 ou 6(=dernier tour))
    NbCarteDevoile=0


    '''
    BOUTONS QUITTER / NVL PARTIE
    '''

    frameBoutons= CTkFrame(poker)
    frameBoutons.grid(row=2,column=2,padx=5,pady=10,sticky="n")

    btnNVLPartie = CTkButton(frameBoutons, text="Nouvelle partie",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white",command=LancePartie)
    btnNVLPartie.grid(row=1,column=1,padx=10,pady=10)

    btnQuitter = CTkButton(frameBoutons, text="Quitter",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white",command=quit)
    btnQuitter.grid(row=2,column=1,padx=10,pady=10)

    '''
    INFOS JOUEURS
    '''
    #frame pour les infos communes aux joueurs
    frameMiseEnJeu = CTkFrame(poker, width=200, height=100,fg_color="green",border_color="white",border_width=3,corner_radius=20)
    frameMiseEnJeu.grid(row=2,column=2,padx=5,pady=10,sticky="s")

    frameLabelMEJ = CTkFrame(frameMiseEnJeu,fg_color="black",corner_radius=10)
    frameLabelMEJ.grid(row=1,column=1,padx=10,pady=10)

    labelMiseEnJeu = CTkLabel(frameLabelMEJ, text="Mise En Jeu", font=("Arial",15),text_color="white")
    labelMiseEnJeu.grid(row=2,column=1,padx=10,pady=10)

    labelMiseEnJeuVariable = CTkLabel(frameMiseEnJeu, text="{} $".format(MEJ), font=("Arial",20,"bold"),text_color="gold")
    labelMiseEnJeuVariable.grid(row=2,column=1,padx=10,pady=10)

    '''
    PLATEAU DE JEU
    '''
    #frame représentant le plateau de jeu (apparissions des cartes)
    frameCartes = CTkFrame(poker, width=900, height=250,fg_color="green",border_color="red",border_width=5,corner_radius=60)
    frameCartes.grid(row=3,column=1,columnspan=3,padx=20,pady=20)
    
    frameCarte1= CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
    frameCarte2 = CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
    frameCarte3= CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
    frameCarte4 = CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
    frameCarte5 = CTkFrame(frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
    
    '''
    CREATION DES CARTES PHYSIQUES DE LA PARTIE
    '''
    carte_physique(frameCarte1,carte1)
    carte_physique(frameCarte2,carte2)
    carte_physique(frameCarte3,carte3)
    carte_physique(frameCarte4,carte4)
    carte_physique(frameCarte5,carte5)
     

    '''
    MESSAGE INFOS
    '''
    frameInfo = CTkFrame(poker,fg_color="white",corner_radius=20)
    frameInfo.grid(row=4,column=1,columnspan=3,padx=10,pady=10)

    labelInfo = CTkLabel(frameInfo, text="", font=("Times New Roman",40),text_color="black")
    labelInfo.grid(row=1,column=1,padx=20,pady=20)



    '''
    WIDGETS JOUEUR 1
    '''

    #affichage du nom du joueur 1
    labelJ1 = CTkLabel(poker, text="{}".format(nomJ1), font=("Arial",20,"bold"),text_color="yellow")
    labelJ1.grid(row=1,column=1,padx=10,pady=10)

    #frame pour les infos pour le joueur 1
    frameJ1 = CTkFrame(poker, width=350, height=200, fg_color="white",corner_radius=15)
    frameJ1.grid(row=2,column=1,padx=20,pady=10)

    '''
    VOIR CARTES J1
    '''
    #frame pour que le joueur 1 voit ses cartes
    frameVoirCartesJ1 = CTkFrame(frameJ1,height=50,fg_color="grey",border_color="black",border_width=2,corner_radius=10)
    frameVoirCartesJ1.grid(row=1,column=1,columnspan=2,padx=20,pady=20)

    btnVoirCartesJ1 = CTkButton(frameVoirCartesJ1, text="Voir Cartes",text_color='black', fg_color='white',hover_color='lightgrey',border_width=2,border_color="white",command=VoirCartesJ1)
    btnVoirCartesJ1.grid(row=1,column=1,padx=10,pady=10)

    labelVoirCarte1J1 = CTkLabel(frameVoirCartesJ1, text="{} de {}".format(Carte1J1[0],Carte1J1[1]), font=("Arial",15,"bold"),text_color="grey")
    labelVoirCarte1J1.grid(row=1,column=2,padx=10,pady=10)

    labelVoirCarte2J1 = CTkLabel(frameVoirCartesJ1, text="{} de {}".format(Carte2J1[0],Carte2J1[1]), font=("Arial",15,"bold"),text_color="grey")
    labelVoirCarte2J1.grid(row=1,column=3,padx=10,pady=10)
    
    '''
    SE COUCHER J1
    '''
    btnSeCoucherJ1 = CTkButton(frameJ1, text="se coucher",text_color='white', fg_color='darkblue',hover_color='blue',command=SeCoucheJ1)
    btnSeCoucherJ1.grid(row=1,column=3,padx=10,pady=10)
    
    '''
    SOLDE J1
    '''
    #frame pour visualiser le solde du joueur 1
    frameSoldeJ1 = CTkFrame(frameJ1,height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
    frameSoldeJ1.grid(row=2,column=1,padx=20,pady=1,sticky="w")

    #label simple pour exprimer le solde
    labelSoldeJ1 = CTkLabel(frameSoldeJ1, text="Solde :", font=("Arial",15),text_color="white")
    labelSoldeJ1.grid(row=1,column=1,padx=10,pady=10)

    #label contenant le solde (variable)
    labelSoldeJ1Variable = CTkLabel(frameSoldeJ1, text="{} $".format(soldeJ1), font=("Arial",15),text_color="white")
    labelSoldeJ1Variable.grid(row=1,column=2,padx=10,pady=10)

    '''
    MISE EN JEU J1
    '''
    #frame pour visualiser la somme mise en jeu par le joueur 1
    frameMEJ1 = CTkFrame(frameJ1,height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
    frameMEJ1.grid(row=2,column=2,padx=20,pady=1)

    #label simple pour exprimer la mise en jeu
    labelMEJ1 = CTkLabel(frameMEJ1, text="Mise en jeu :", font=("Arial",15),text_color="white")
    labelMEJ1.grid(row=1,column=1,padx=10,pady=10)

    #label contenant la mise en jeu (variable)
    labelMEJ1Variable = CTkLabel(frameMEJ1, text="{} $".format(MEJ1), font=("Arial",15),text_color="white")
    labelMEJ1Variable.grid(row=1,column=2,padx=10,pady=10)

    '''
    CHECK joueur 1
    '''
    btnCheckJ1 = CTkButton(frameJ1,width=50,height=50, text="check",text_color='black', fg_color='darkorange',hover_color='orange',command=CheckJ1,corner_radius=50)
    btnCheckJ1.grid(row=2,column=3,padx=10,pady=10)

    '''
    MISER J1
    '''
    #frame pour miser (joueur 1)
    frameMiserJ1 = CTkFrame(frameJ1, height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
    frameMiserJ1.grid(row=3,column=1,columnspan=3,padx=20,pady=20,sticky="w")

    #entrée pour la mise en jeu souhaité
    entryMiseEnJeuJ1 = CTkEntry(frameMiserJ1, placeholder_text="mise")
    entryMiseEnJeuJ1.grid(row=2,column=1,padx=10,pady=10)

    #bouton pour valider la mise en jeu
    btnMiserJ1 = CTkButton(frameMiserJ1, text="Miser",text_color='black', fg_color='white',hover_color='lightgrey',command=MiserJ1)
    btnMiserJ1.grid(row=2,column=2,padx=10,pady=10)

    #bouton pour allin
    btnAllInJ1 = CTkButton(frameMiserJ1, text="All In",text_color='black', fg_color='white',hover_color='red',command=AllInJ1)
    btnAllInJ1.grid(row=2,column=3,padx=10,pady=10)


    '''
    WIDGETS JOUEUR 2
    '''

    #affichage du nom du joueur 2
    labelJ2 = CTkLabel(poker, text="{}".format(nomJ2), font=("Arial",20,"bold"),text_color="yellow")
    labelJ2.grid(row=1,column=3,padx=10,pady=10)

    #frame pour les infos pour le joueur 2
    frameJ2 = CTkFrame(poker, width=350, height=200, fg_color="white",corner_radius=15)
    frameJ2.grid(row=2,column=3,padx=20,pady=10)

    '''
    VOIR CARTES J2
    '''
    #frame pour que le joueur 1 voit ses cartes
    frameVoirCartesJ2 = CTkFrame(frameJ2, width=100, height=50,fg_color="grey",border_color="black",border_width=2,corner_radius=10)
    frameVoirCartesJ2.grid(row=1,column=1,columnspan=2,padx=20,pady=20)

    btnVoirCartesJ2 = CTkButton(frameVoirCartesJ2, text="Voir Cartes",text_color="black", fg_color="white",hover_color="lightgrey",border_width=2,border_color="white",command=VoirCartesJ2)
    btnVoirCartesJ2.grid(row=1,column=1,padx=10,pady=10)

    labelVoirCarte1J2 = CTkLabel(frameVoirCartesJ2, text="{} de {}".format(Carte2J2[0],Carte2J2[1]), font=("Arial",15,"bold"),text_color="grey")
    labelVoirCarte1J2.grid(row=1,column=2,padx=10,pady=10)

    labelVoirCarte2J2 = CTkLabel(frameVoirCartesJ2, text="{} de {}".format(Carte1J2[0],Carte1J2[1]), font=("Arial",15,"bold"),text_color="grey")
    labelVoirCarte2J2.grid(row=1,column=3,padx=10,pady=10)
    
    '''
    SE COUCHER J2
    '''
    btnSeCoucherJ2 = CTkButton(frameJ2, text="se coucher",text_color='white', fg_color='darkblue',hover_color='blue',command=SeCoucheJ2)
    btnSeCoucherJ2.grid(row=1,column=3,padx=10,pady=10)

    '''
    SOLDE J2
    '''
    #frame pour visualiser le solde du joueur 1
    frameSoldeJ2 = CTkFrame(frameJ2,height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
    frameSoldeJ2.grid(row=2,column=1,padx=20,pady=1,sticky="w")

    #label simple pour exprimer le solde
    labelSoldeJ2 = CTkLabel(frameSoldeJ2, text="Solde :", font=("Arial",15),text_color="white")
    labelSoldeJ2.grid(row=1,column=1,padx=10,pady=10)

    #label contenant le solde (variable)
    labelSoldeJ2Variable = CTkLabel(frameSoldeJ2, text="{} $".format(soldeJ2), font=("Arial",15),text_color="white")
    labelSoldeJ2Variable.grid(row=1,column=2,padx=10,pady=10)

    '''
    MISE EN JEU J2
    '''
    #frame pour visualiser la somme mise en jeu par le joueur 2
    frameMEJ2 = CTkFrame(frameJ2,height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
    frameMEJ2.grid(row=2,column=2,padx=20,pady=1,sticky="w")

    #label simple pour exprimer la mise en jeu
    labelMEJ2 = CTkLabel(frameMEJ2, text="Mise en jeu :", font=("Arial",15),text_color="white")
    labelMEJ2.grid(row=1,column=1,padx=10,pady=10)

    #label contenant la mise en jeu (variable)
    labelMEJ2Variable = CTkLabel(frameMEJ2, text="{} $".format(MEJ2), font=("Arial",15),text_color="white")
    labelMEJ2Variable.grid(row=1,column=2,padx=10,pady=10)

    '''
    CHECK joueur 2
    '''
    btnCheckJ2 = CTkButton(frameJ2,width=50,height=50, text="check",text_color='black', fg_color='darkorange',hover_color='orange',command=CheckJ2,corner_radius=50)
    btnCheckJ2.grid(row=2,column=3,padx=10,pady=10)

    '''
    MISER J2
    '''
    #frame pour miser (joueur 1)
    frameMiserJ2 = CTkFrame(frameJ2, height=50,fg_color="black",border_color="black",border_width=5,corner_radius=10)
    frameMiserJ2.grid(row=3,column=1,columnspan=3,padx=20,pady=20,sticky="w")

    #entrée pour la mise en jeu souhaité
    entryMiseEnJeuJ2 = CTkEntry(frameMiserJ2, placeholder_text="mise")
    entryMiseEnJeuJ2.grid(row=2,column=1,padx=10,pady=10)

    #bouton pour valider la mise en jeu
    btnMiserJ2 = CTkButton(frameMiserJ2, text="Miser",text_color='black', fg_color='white',hover_color='lightgrey',command=MiserJ2)
    btnMiserJ2.grid(row=2,column=2,padx=10,pady=10)

    #bouton pour allin
    btnAllInJ2 = CTkButton(frameMiserJ2, text="All In",text_color='black', fg_color='white',hover_color='red',command=AllInJ2)
    btnAllInJ2.grid(row=2,column=3,padx=10,pady=10)


    '''
    PARTIE
    '''
    #determiner le joueur qui commence 
    if random.randint(1,2)==1:
        main=1
        JCommence = 1
        JCommenceNom=nomJ1
        labelInfo.configure(text="{} commence".format(nomJ1))
        MEJ1+=250
        MEJ2+=500
        MEJ+=(MEJ1+MEJ2)
        soldeJ1-=MEJ1
        soldeJ2-=MEJ2
    else:
        main=2
        JCommence = 2
        JCommenceNom=nomJ2
        labelInfo.configure(text="{} commence".format(nomJ2))
        MEJ1+=500
        MEJ2+=250
        MEJ+=(MEJ1+MEJ2)
        soldeJ1-=MEJ1
        soldeJ2-=MEJ2

    labelMEJ1Variable.configure(text="{} $".format(MEJ1))
    labelSoldeJ1Variable.configure(text="{} $".format(soldeJ1))
    labelMEJ2Variable.configure(text="{} $".format(MEJ2))
    labelSoldeJ2Variable.configure(text="{} $".format(soldeJ2))
    labelMiseEnJeuVariable.configure(text="{} $".format(MEJ))
    
    
    poker.update()
    
    
    
    


def Reinitialiser():
    '''
    lance une nouvelle manche
    '''
    global ACheckJ1,ACheckJ2,main,JCommence,JCommenceNom
    global carte1,carte2,carte3,carte4,carte5,Carte1J2,Carte1J1,Carte2J1,Carte2J2,NbCarteDevoile
    global labelVoirCarte1J1,labelVoirCarte1J2,labelVoirCarte2J1,labelVoirCarte2J2,labelInfo
    global labelMEJ1Variable,labelMEJ2Variable,labelMiseEnJeuVariable,labelSoldeJ1Variable,labelSoldeJ2Variable,entryMiseEnJeuJ1,entryMiseEnJeuJ2
    global MEJ,MEJ1,MEJ2,soldeJ1,soldeJ2
    global frameCarte1,frameCarte2,frameCarte3,frameCarte4,frameCarte5
    
    
    '''
    DESTRUCTION DES CARTES DU PLATEAU
    '''
    frameCarte1.grid_remove()
    frameCarte2.grid_remove()
    frameCarte3.grid_remove()
    frameCarte4.grid_remove()
    frameCarte5.grid_remove()
    
    '''
    REMISE A BLANC DES CARTES DU PLATEAU
    '''
    DetruireLabelFrame(frameCarte1,frameCarte2,frameCarte3,frameCarte4,frameCarte5)

    
    '''
    INITIALISATION CHECK
    '''
    ACheckJ1=False
    ACheckJ2=False

    '''
    CACHER LES CARTES DES JOUEURS   
    '''
    labelVoirCarte1J1.configure(text_color="grey")
    labelVoirCarte2J1.configure(text_color="grey")
    labelVoirCarte1J2.configure(text_color="grey")
    labelVoirCarte2J2.configure(text_color="grey")


    '''
    jeux de cartes pour cette partie
    '''
    copieTableCartes = table_cartes.copy()


    '''
    TIRAGE DES CARTES
    '''
    #tirage des cartes au hasard J1
    Carte1J1 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte1J1)
    Carte2J1 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte2J1)

    #tirage des cartes au hasard J1
    Carte1J2 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte1J2)
    Carte2J2 = random.choice(copieTableCartes)
    copieTableCartes.remove(Carte2J2)

    #tirage du flop au hasard
    carte1 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte1)
    carte2 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte2)
    carte3 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte3)

    #tirage 4eme carte
    carte4 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte4)

    #tirage 5eme carte 
    carte5 = random.choice(copieTableCartes)
    copieTableCartes.remove(carte5)

    #compteur de cartes dévoilés (3, 4, 5 ou 6(=dernier tour))
    NbCarteDevoile=0

    
    '''
    VOIR CARTES J1 (NOUVELLES CARTES)
    '''
    labelVoirCarte1J1.configure(text="{} de {}".format(Carte1J1[0],Carte1J1[1]))
    labelVoirCarte2J1.configure(text="{} de {}".format(Carte2J1[0],Carte2J1[1]))
    
    
    '''
    REMISE VALEUR PAR DEFAULT DE LA MISE JOUEUR 1
    '''
    entryMiseEnJeuJ1.configure(placeholder_text="mise")
    

    '''
    VOIR CARTES J2 (NOUVELLES CARTES)
    '''
    labelVoirCarte1J2.configure(text="{} de {}".format(Carte1J2[0],Carte1J2[1]))
    labelVoirCarte2J2.configure(text="{} de {}".format(Carte2J2[0],Carte2J2[1]))
    
    
    '''
    REMISE VALEUR PAR DEFAULT DE LA MISE JOUEUR 2
    '''
    entryMiseEnJeuJ2.configure(placeholder_text="mise")
    

    '''
    PARTIE
    '''
    #determiner le joueur qui commence en fonction de la partie précédente
    if JCommence==2:
        main=1
        JCommence = 1
        JCommenceNom=nomJ1
        labelInfo.configure(text="{} commence".format(nomJ1))
        MEJ1+=250
        MEJ2+=500
        MEJ+=(MEJ1+MEJ2)
        soldeJ1-=MEJ1
        soldeJ2-=MEJ2
    else:
        main=2
        JCommence = 2
        JCommenceNom=nomJ2
        labelInfo.configure(text="{} commence".format(nomJ2))
        MEJ1+=500
        MEJ2+=250
        MEJ+=(MEJ1+MEJ2)
        soldeJ1-=MEJ1
        soldeJ2-=MEJ2

    labelMEJ1Variable.configure(text="{} $".format(MEJ1))
    labelSoldeJ1Variable.configure(text="{} $".format(soldeJ1))
    labelMEJ2Variable.configure(text="{} $".format(MEJ2))
    labelSoldeJ2Variable.configure(text="{} $".format(soldeJ2))
    labelMiseEnJeuVariable.configure(text="{} $".format(MEJ))

    '''
    CREATION DES CARTES PHYSIQUES
    '''
    carte_physique(frameCarte1,carte1)
    carte_physique(frameCarte2,carte2)
    carte_physique(frameCarte3,carte3)
    carte_physique(frameCarte4,carte4)
    carte_physique(frameCarte5,carte5)
    
    
    poker.update()





def VoirCartesJ1():
    '''
    affiche les cartes du joueur 1 (chaque carte de la couleur correspondante à la couleur de la carte) pendant 5 secondes
    '''
    labelVoirCarte1J1.configure(text_color="{}".format(DefinirCouleurCarte(Carte1J1)))
    labelVoirCarte2J1.configure(text_color="{}".format(DefinirCouleurCarte(Carte2J1)))
    poker.update()

    time.sleep(3)

    labelVoirCarte1J1.configure(text_color="grey")
    labelVoirCarte2J1.configure(text_color="grey")

def VoirCartesJ2():
    '''
    affiche les cartes du joueur 2 (chaque carte de la couleur correspondante à la couleur de la carte) pendant 5 secondes
    '''
    labelVoirCarte1J2.configure(text_color="{}".format(DefinirCouleurCarte(Carte1J2)))
    labelVoirCarte2J2.configure(text_color="{}".format(DefinirCouleurCarte(Carte2J2)))
    poker.update()

    time.sleep(3)

    labelVoirCarte1J2.configure(text_color="grey")
    labelVoirCarte2J2.configure(text_color="grey")



def MiserJ1():
    '''
    action suite au clic du bouton "miser" par le joueur 1
    '''

    global main,MEJ,MEJ1,soldeJ1,NbCarteDevoile

    if NbCarteDevoile==6:
        return 0
    elif main!=1:
        labelInfo.configure(text="La main est à {}".format(nomJ2))
    else:

        mise = entryMiseEnJeuJ1.get()

        #si le joueur n'est pas le premier a jouer il faut qu'il s'alligne sur le prmeier joueur qui a jouer
        if int(mise)+MEJ1<MEJ2 and soldeJ1>0:
            labelInfo.configure(text="{} mise trop faible".format(nomJ1))
            poker.update()
            time.sleep(1)
            labelInfo.configure(text="La main est toujours à {}".format(nomJ1))

        #verification de solde pour fin de partie
        elif soldeJ1==0:
            return 0
            
        elif mise==soldeJ1:
            labelInfo.configure(text="{} fait tapis !".format(nomJ1))
            FinDeJeuParDepouillage()
            
        #mise en jeu plus grand que le solde disponible
        elif int(mise)>soldeJ1:
            labelInfo.configure(text="{} vous n'avez pas assez d'argent!".format(nomJ1))
            poker.update() 
            time.sleep(1)
            labelInfo.configure(text="La main est toujours à {}".format(nomJ1))   

        #mise à jour de la mise en jeu du joueur 1 et de la mise en jeu principale
        else:
            MEJ1=MEJ1+int(mise)
            MEJ=MEJ+int(mise)
            soldeJ1-=int(mise)
            labelMEJ1Variable.configure(text="{} $".format(MEJ1))
            labelMiseEnJeuVariable.configure(text="{} $".format(MEJ))
            labelSoldeJ1Variable.configure(text="{} $".format(soldeJ1))
            main = 2
            labelInfo.configure(text="A {} de jouer".format(nomJ2))

            if NbCarteDevoile==0 and MEJ1==MEJ2:
                frameCarte1.grid(row=1,column=1,padx=50,pady=50)
                frameCarte2.grid(row=1,column=2,padx=50,pady=50)
                frameCarte3.grid(row=1,column=3,padx=50,pady=50)
                main=JCommence
                labelInfo.configure(text="A {} de jouer".format(JCommenceNom))
                NbCarteDevoile=3
            elif NbCarteDevoile==3 and MEJ1==MEJ2:
                frameCarte4.grid(row=1,column=4,padx=50,pady=50)
                main=JCommence
                labelInfo.configure(text="A {} de jouer".format(JCommenceNom))
                NbCarteDevoile=4
            elif NbCarteDevoile==4 and MEJ1==MEJ2:
                frameCarte5.grid(row=1,column=5,padx=50,pady=50)
                labelInfo.configure(text="A {} de jouer".format(JCommenceNom))
                main=JCommence
                NbCarteDevoile=5
            elif NbCarteDevoile==5 and MEJ1==MEJ2:
                labelInfo.configure(text="Fin de partie")
                NbCarteDevoile=6
                FinPartie()
            else:
                main=2
                labelInfo.configure(text="A {} de jouer".format(nomJ2))
                

    poker.update()

def MiserJ2():
    '''
    action suite au clic du bouton "miser" par le joueur 2
    '''
    
    global main,MEJ,MEJ2,soldeJ2,NbCarteDevoile

    if NbCarteDevoile==6:
        return 0
    elif main!=2:
        labelInfo.configure(text="La main est à {}".format(nomJ1))
    else:

        mise = entryMiseEnJeuJ2.get()

        #si le joueur n'est pas le premier a jouer il faut qu'il s'alligne sur le prmeier joueur qui a jouer
        if int(mise)+MEJ2<MEJ1 and soldeJ2>0:
            labelInfo.configure(text="{} mise trop faible".format(nomJ2))
            poker.update()
            time.sleep(1)
            labelInfo.configure(text="La main est toujours à {}".format(nomJ2))

        #verification de solde pour fin de partie
        elif soldeJ2==0:
            return 0
            
        elif mise==soldeJ1:
            labelInfo.configure(text="{} fait tapis !".format(nomJ1))
            FinDeJeuParDepouillage()
            
        #mise en jeu plus grand que le solde disponible
        elif int(mise)>soldeJ2:
            labelInfo.configure(text="{} vous n'avez pas assez d'argent!".format(nomJ2))
            poker.update()
            time.sleep(1)
            labelInfo.configure(text="La main est toujours à {}".format(nomJ2))

        #mise à jour de la mise en jeu du joueur 2 et de la mise en jeu principale
        else:
            MEJ2+=int(mise)
            MEJ+=int(mise)
            soldeJ2-=int(mise)
            labelMEJ2Variable.configure(text="{} $".format(MEJ2))
            labelMiseEnJeuVariable.configure(text="{} $".format(MEJ))
            labelSoldeJ2Variable.configure(text="{} $".format(soldeJ2))
            main = 1
            labelInfo.configure(text="A {} de jouer".format(nomJ1))

            if NbCarteDevoile==0 and MEJ1==MEJ2:
                frameCarte1.grid(row=1,column=1,padx=50,pady=50)
                frameCarte2.grid(row=1,column=2,padx=50,pady=50)
                frameCarte3.grid(row=1,column=3,padx=50,pady=50)
                main=JCommence
                labelInfo.configure(text="A {} de jouer".format(JCommenceNom))
                NbCarteDevoile=3
            elif NbCarteDevoile==3 and MEJ1==MEJ2:
                frameCarte4.grid(row=1,column=4,padx=50,pady=50)
                main=JCommence
                labelInfo.configure(text="A {} de jouer".format(JCommenceNom))
                NbCarteDevoile=4
            elif NbCarteDevoile==4 and MEJ1==MEJ2:
                frameCarte5.grid(row=1,column=5,padx=50,pady=50)
                main=JCommence
                labelInfo.configure(text="A {} de jouer".format(JCommenceNom))
                NbCarteDevoile=5
            elif NbCarteDevoile==5 and MEJ1==MEJ2:
                labelInfo.configure(text="Fin de partie")
                NbCarteDevoile=6
                FinPartie()
            else:
                main=1
                labelInfo.configure(text="A {} de jouer".format(nomJ1))
                
                

    poker.update()






def AllInJ1():

    global main,MEJ,MEJ1,soldeJ1,AallInJ1

    if NbCarteDevoile==6:
        return 0
    elif main!=1:
        labelInfo.configure(text="La main est à {}".format(nomJ2))
    else:
        MEJ1+=soldeJ1
        MEJ+=soldeJ1 
        soldeJ1-=soldeJ1
        labelMEJ1Variable.configure(text="{} $".format(MEJ1))
        labelMiseEnJeuVariable.configure(text="{} $".format(MEJ))
        labelSoldeJ1Variable.configure(text="{} $".format(soldeJ1))
        if AallInJ2==True:
            labelInfo.configure(text="{} le suit !".format(nomJ1))
            FinDeJeuParDepouillage()
        else: 
            main = 2
            labelInfo.configure(text="{} fait tapis !".format(nomJ1))
            poker.update()
            time.sleep(1)
            labelInfo.configure(text="A {} de jouer".format(nomJ2))
            AallInJ1=True

    poker.update()

def AllInJ2():

    global main,MEJ,MEJ2,soldeJ2,AallInJ2

    if NbCarteDevoile==6:
        return 0
    elif main!=2:
        labelInfo.configure(text="La main est à {}".format(nomJ2))
    else:
        MEJ2+=soldeJ1
        MEJ+=soldeJ1 
        soldeJ2-=soldeJ2
        labelMEJ2Variable.configure(text="{} $".format(MEJ2))
        labelMiseEnJeuVariable.configure(text="{} $".format(MEJ))
        labelSoldeJ2Variable.configure(text="{} $".format(soldeJ2))
        if AallInJ1==True:
            labelInfo.configure(text="{} le suit !".format(nomJ2))
            FinDeJeuParDepouillage()
        else :
            main = 1
            labelInfo.configure(text="{} fait tapis !".format(nomJ2))
            poker.update()
            time.sleep(2)
            labelInfo.configure(text="A {} de jouer".format(nomJ1))
            AallInJ2=True

    poker.update()






def CheckJ1():

    global ACheckJ1,NbCarteDevoile,main

    if NbCarteDevoile>=3 and NbCarteDevoile<6 and main==1:
        if MEJ1!=MEJ2:
            labelInfo.configure(text="Check impossible, {} a miser".format(nomJ2))
            time.sleep(1)
            labelInfo.configure(text="la main est toujours à {}".format(nomJ2))
        elif ACheckJ2==True:
            if NbCarteDevoile==3 and MEJ1==MEJ2:
                frameCarte4.grid(row=1,column=4,padx=50,pady=50)
                labelInfo.configure(text="4e carte dévoilée, a {} de jouer".format(nomJ2))
                main=2
                NbCarteDevoile=4
            elif NbCarteDevoile==4 and MEJ1==MEJ2:
                frameCarte5.grid(row=1,column=5,padx=50,pady=50)
                labelInfo.configure(text="Dernière carte dévoilée, a {} de jouer".format(nomJ2))
                main=2
                NbCarteDevoile=5
            elif NbCarteDevoile==5 and MEJ1==MEJ2:
                labelInfo.configure(text="Fin de partie")
                NbCarteDevoile=6
                FinPartie()
        else:
            ACheckJ1=True
            main=2
            labelInfo.configure(text="{} Check".format(nomJ1))
            poker.update()
            time.sleep(1)
            labelInfo.configure(text="A {} de jouer".format(nomJ2))

def CheckJ2():

    global ACheckJ2,NbCarteDevoile,main

    if NbCarteDevoile>=3 and NbCarteDevoile<6 and main==2:
        if MEJ1!=MEJ2:
            labelInfo.configure(text="Check impossible, {} a miser".format(nomJ1))
            time.sleep(1)
            labelInfo.configure(text="la main est toujours à {}".format(nomJ2))
        elif ACheckJ1==True:
            if NbCarteDevoile==3 and MEJ1==MEJ2:
                frameCarte4.grid(row=1,column=4,padx=50,pady=50)
                labelInfo.configure(text="4e carte dévoilée, a {} de jouer".format(nomJ1))
                main=1
                NbCarteDevoile=4       
            elif NbCarteDevoile==4 and MEJ1==MEJ2:
                frameCarte5.grid(row=1,column=5,padx=50,pady=50)
                labelInfo.configure(text="Dernière carte dévoilée, a {} de jouer".format(nomJ1))
                main=1
                NbCarteDevoile=5
            elif NbCarteDevoile==5 and MEJ1==MEJ2:
                labelInfo.configure(text="Fin de partie")
                NbCarteDevoile=6
                FinPartie()

        else:
            ACheckJ2=True
            main=1
            labelInfo.configure(text="{} Check".format(nomJ2))
            poker.update()
            time.sleep(1)
            labelInfo.configure(text="A {} de jouer".format(nomJ1))
            
            
            
            
            
            
def SeCoucheJ1():
    
    global soldeJ2,MEJ,MEJ1,MEJ2,labelInfo
    
    if main==1:    
        #automatiquement J2 est gagnant
        labelInfo.configure(text="{} se couche".format(nomJ1))
        poker.update()
        time.sleep(1)
        labelInfo.configure(text="{} gagne".format(nomJ2))
        soldeJ2+=MEJ

        #remise à zéro des mises
        MEJ=0
        MEJ1=0
        MEJ2=0
        
        poker.update()
        time.sleep(5)
        
        '''
        LANCER UNE NOUVELLE PARTIE
        '''
        Reinitialiser()
    
def SeCoucheJ2():
    
    global soldeJ1,MEJ,MEJ1,MEJ2,labelInfo

    if main==2:
        #automatiquement J2 est gagnant
        labelInfo.configure(text="{} se couche".format(nomJ2))
        poker.update()
        time.sleep(1)
        labelInfo.configure(text="{} gagne".format(nomJ1))
        
        #créditement de J1
        soldeJ1+=MEJ

        #remise à zéro des mises
        MEJ=0
        MEJ1=0
        MEJ2=0
        
        poker.update()
        time.sleep(5)
        
        '''
        LANCER UNE NOUVELLE PARTIE
        '''
        Reinitialiser()
        
        
        
        
        
        
def FinDeJeuParDepouillage():
    
    global NbCarteDevoile,frameCarte1,frameCarte2,frameCarte3,frameCarte4,frameCarte5
    
    if NbCarteDevoile==0:
        frameCarte1.grid(row=1,column=1,padx=50,pady=50)
        frameCarte2.grid(row=1,column=2,padx=50,pady=50)
        frameCarte3.grid(row=1,column=3,padx=50,pady=50)
        NbCarteDevoile=3
    if NbCarteDevoile==3:
        frameCarte4.grid(row=1,column=4,padx=50,pady=50)
        NbCarteDevoile=4
    if NbCarteDevoile==4:
        frameCarte5.grid(row=1,column=5,padx=50,pady=50)
        NbCarteDevoile=6

    FinPartie()

    






def FinPartie():
    
    global soldeJ1,soldeJ2,MEJ,MEJ1,MEJ2,labelInfo,labelVoirCarte2J1,labelVoirCarte1J1,labelVoirCarte1J2,labelVoirCarte2J2


    '''
    AFFICHER LES CARTES DES JOUEURS
    '''
    labelVoirCarte1J1.configure(text_color="{}".format(DefinirCouleurCarte(Carte1J2)))
    labelVoirCarte2J1.configure(text_color="{}".format(DefinirCouleurCarte(Carte2J2)))
    
    labelVoirCarte1J2.configure(text_color="{}".format(DefinirCouleurCarte(Carte1J2)))
    labelVoirCarte2J2.configure(text_color="{}".format(DefinirCouleurCarte(Carte2J2)))


    '''
    MAIN DES JOUEURS
    '''
    cartes_jeuJ1=[carte1]+[carte2]+[carte3]+[carte4]+[carte5]+[Carte1J1]+[Carte2J1]
    cartes_jeuJ2=[carte1]+[carte2]+[carte3]+[carte4]+[carte5]+[Carte1J2]+[Carte2J2]


    '''
    CALCUL NOMBRE DE CARTE PAR NUMERO ET PAR COULEUR POUR CHAQUE JOUEUR
    '''
    #calcul du nombre de cartes par couleur J1
    NbcouleurJ1={i:0 for i in table_couleur}
    for carte in cartes_jeuJ1:
        NbcouleurJ1[carte[1]]+=1

    #calcul du nombre de cartes par couleur J2
    NbcouleurJ2={i:0 for i in table_couleur}
    for carte in cartes_jeuJ2:
        NbcouleurJ2[carte[1]]+=1


    #calcul du nombre de cartes par numero J1
    NbnumeroJ1={i:0 for i in table_numero}
    for carte in cartes_jeuJ1:
        NbnumeroJ1[carte[0]]+=1

    #calcul du nombre de cartes par numero J2
    NbnumeroJ2={i:0 for i in table_numero}
    for carte in cartes_jeuJ2:
        NbnumeroJ2[carte[0]]+=1


    '''
    VERIFICATION DES COMBINAISONS
    '''
    #contiendra la combinaison gagante
    texte=None
    
    #quint flush royale pour J1
    if QuinteFlushRoyale(cartes_jeuJ1,NbcouleurJ1):
        texte="WOW {} gagne avec Quint Flush Royale !".format(nomJ1)
    #quint flush royale pour J2
    elif QuinteFlushRoyale(cartes_jeuJ2,NbcouleurJ2):
        texte="WOW {} gagne avec Quint Flush Royale !".format(nomJ2)

    #quint flush pour J1
    elif QuinteFlush(NbcouleurJ1,cartes_jeuJ1):
        texte="Incroyable {} gagne avec Quint Flush !".format(nomJ1)
    #quint flush pour J2
    elif QuinteFlush(NbcouleurJ2,cartes_jeuJ2):
        texte="Incroyable {} gagne avec Quint Flush !".format(nomJ2)

    #Carre pour les deux joueurs
    elif Carre(NbnumeroJ1)!=None and Carre(NbnumeroJ2)!=None:
        if valeur_carte(Carre(NbnumeroJ1))>valeur_carte(Carre(NbnumeroJ2)):
            texte="{} gagne avec un carre de {}".format(nomJ1,Carre(NbnumeroJ1))
        else:
            texte="{} gagne avec un carre de {}".format(nomJ2,Carre(NbnumeroJ2))
    #Carre pour J1
    elif Carre(NbnumeroJ1)!=None:
        texte="{} gagne avec un carre de {}".format(nomJ1,Carre(NbnumeroJ1))
    #Carre pour J2
    elif Carre(NbnumeroJ2)!=None:
        texte="{} gagne avec un carre de {}".format(nomJ2,Carre(NbnumeroJ2))

    #Full pour les deux joueurs
    elif Full(NbnumeroJ1)!=None and Full(NbnumeroJ2)!=None:
        if valeur_carte(Full(NbnumeroJ1))>valeur_carte(Full(NbnumeroJ2)):
            texte="{} gagne avec un full".format(nomJ1)
        else:
            texte="{} gagne avec un full".format(nomJ2)
    #Full pour J1
    elif Full(NbnumeroJ1)!=None:
        texte="{} gagne avec un full".format(nomJ1)
    #Full pour J2
    elif Full(NbnumeroJ2)!=None:
        texte="{} gagne avec un full".format(nomJ2)

    #Couleur pour les deux joueurs
    elif Couleur(NbcouleurJ1,cartes_jeuJ1)!=None and Couleur(NbcouleurJ2,cartes_jeuJ2)!=None:
        if Couleur(NbcouleurJ1,cartes_jeuJ1)[0]>Couleur(NbcouleurJ2,cartes_jeuJ2)[0]:
            texte=ComparaisonCartesCouleur(Couleur(NbcouleurJ1,cartes_jeuJ1),Couleur(NbcouleurJ2,cartes_jeuJ2))
    #Couleur pour J1
    elif Couleur(NbcouleurJ1,cartes_jeuJ1)!=None:
        texte="{} gagne avec une couleur".format(nomJ1)
    #Couleur pour J2
    elif Couleur(NbcouleurJ2,cartes_jeuJ2)!=None:
        texte="{} gagne avec une couleur".format(nomJ2)

    #Quinte pour les deux joueurs
    elif Quinte(cartes_jeuJ1)!=None and Quinte(cartes_jeuJ2)!=None:
        if Quinte(cartes_jeuJ1)>Quinte(cartes_jeuJ2):
            texte="{} gagne avec une suite".format(nomJ1)
        elif Quinte(cartes_jeuJ1)==Quinte(cartes_jeuJ2):
            texte="Suite égale pour les deux joueurs, partage de la mise"
        else:
            texte="{} gagne avec une suite".format(nomJ2)
    #Quinte pour J1
    elif Quinte(cartes_jeuJ1)!=None:
        texte="{} gagne avec une suite".format(nomJ1)
    #Quintepour J2
    elif Quinte(cartes_jeuJ2)!=None:
        texte="{} gagne avec une suite".format(nomJ2)

    #Brelan pour les deux joueurs
    elif Brelan(NbnumeroJ1)!=None and Brelan(NbnumeroJ2)!=None:
        if valeur_carte(Brelan(NbnumeroJ1))>valeur_carte(Brelan(NbnumeroJ2)):
            texte="{} gagne avec un brelan de {}".format(nomJ1,valeur_carte(Brelan(NbnumeroJ1)))
        else:
            texte="{} gagne avec un brelan de {}".format(nomJ2,valeur_carte(Brelan(NbnumeroJ2)))
    #Brelan pour J1
    elif Brelan(NbnumeroJ1)!=None:
        texte="{} gagne avec un brelan de {}".format(nomJ1,valeur_carte(Brelan(NbnumeroJ1)))
    #Brelan pour J2
    elif Brelan(NbnumeroJ2)!=None:
        texte="{} gagne avec un brelan de {}".format(nomJ2,valeur_carte(Brelan(NbnumeroJ2)))

    #Double paires de la même valeur pour les deux joueurs → gagnant = carte haute
    elif DoublePaire(NbnumeroJ1)==DoublePaire(NbnumeroJ2) and DoublePaire(NbnumeroJ1)!=None and DoublePaire(NbnumeroJ2)!=None:
        texte=ComparaisonCartesHautes(cartes_jeuJ1,cartes_jeuJ2)
    #Double paires pour les deux joueurs
    elif DoublePaire(NbnumeroJ1)!=None and DoublePaire(NbnumeroJ2)!=None:
        if valeur_carte(DoublePaire(NbnumeroJ1))>valeur_carte(DoublePaire(NbnumeroJ2)):
            texte="{} gagne avec la paire la plus forte".format(nomJ1)
        else:
            texte="{} gagne avec la paire la plus forte".format(nomJ2)
    #Double paires pour J1
    elif DoublePaire(NbnumeroJ1)!=None:
        texte="{} gagne avec double paire".format(nomJ1)
    #Double paires pour J2
    elif DoublePaire(NbnumeroJ2)!=None:
        texte="{} gagne avec double paire".format(nomJ2)

    #paire de la même valeur pour les deux joueurs → gagnant = carte haute dans le kick (comparaison des 3 meilleures cartes pour chaque joueur) → sinon égalite
    elif Paire(NbnumeroJ1)==Paire(NbnumeroJ2) and Paire(NbnumeroJ2)!=0 and Paire(NbnumeroJ2)!=0:
        texte=ComparaisonCartesHautes(cartes_jeuJ1,cartes_jeuJ2)
    #paire pour les deux joueurs
    elif Paire(NbnumeroJ1)!=0 and Paire(NbnumeroJ2)!=0:
        if valeur_carte(Paire(NbnumeroJ1))>valeur_carte(Paire(NbnumeroJ2)):
            texte="{} gagne avec la paire la plus forte".format(nomJ1)
        else:
            texte="{} gagne avec la paire la plus forte".format(nomJ2)
    #paire pour J1
    elif Paire(NbnumeroJ1)!=0:
        texte="{} gagne avec une paire de {}".format(nomJ1,valeur_carte(Paire(NbnumeroJ1)))
    #paire pour J2
    elif Paire(NbnumeroJ2)!=0:
        texte="{} gagne avec une paire de {}".format(nomJ2,valeur_carte(Paire(NbnumeroJ2)))

    #determiner la carte haute pour les deux joueurs
    else:
        texte=ComparaisonCartesHautes(cartes_jeuJ1,cartes_jeuJ2)



    '''
    DEETERMINER LE GAGANT
    '''
    #affichage du gagnant
    labelInfo.configure(text="{}".format(texte))
    poker.update()

    #crediter le joueur gagnant
    print(nomJ1,nomJ2)
    if nomJ1 in texte and nomJ2 not in texte:
        soldeJ1+=MEJ
    elif nomJ2 in texte and nomJ1 not in texte:
        soldeJ2+=MEJ
    else:
        soldeJ1+=MEJ1
        soldeJ2+=MEJ2
        
    #remise à zéro des mises
    MEJ=0
    MEJ1=0
    MEJ2=0

    #verifier que les deux joueurs ont encore du solde pour recommencer une manche, sinon fin de partie
    if soldeJ1<=0:
        labelInfo.configure(text="{} est fauché ... {} gagne la partie !".format(nomJ1,nomJ2))
        return 0
    elif soldeJ2<=0:
        labelInfo.configure(text="{} est fauché ... {} gagne la partie !".format(nomJ2,nomJ1))
        return 0
    else:
        '''
        LANCER UNE NOUVELLE PARTIE
        '''
        time.sleep(7) 
        Reinitialiser()
    







def QuinteFlushRoyale(cartes,Nbcouleur):
    '''
    renvoi un boolen si la quinte flush royale existe (couleur + suite dans la couleur avec les cartes les plus hautes du jeu (10,V,D,R,As)
    '''
    couleur_royale=None
    #1 etape chercher si y a bien une couleur 
    if Couleur(Nbcouleur,cartes)!=None:
        for k,v in Nbcouleur.items():
            if v>4:
                #couleur existante
                couleur_royale=k

                #2e etape on cherche a savoir si il ya bien une suite haute
                cartes_requises_royale = [['10', couleur_royale], ['Valet', couleur_royale], ['Dame', couleur_royale], ['Roi', couleur_royale],['As', couleur_royale]]
                #on regarde si les cartes requise se trouvent dans le jeu dun joueur
                if all(carte in cartes for carte in cartes_requises_royale):
                    return True
    return False
                
    
def QuinteFlush(Nbcouleur,cartes):
    '''
    renvoi un boolen si une quinte flush existe (couleur + suite dans la couleur)
    '''
    #1 etape chercher si y a bien une couleur 
    cartesCouleur = Couleur(Nbcouleur,cartes)
    if cartesCouleur!=None:
        #2 etape on cherche si il ya suite dans cette couleur
        if Quinte(cartes):
            return True
    return False
        


def Carre(Nbnumero):
    '''
    renvoi la valeur la valeur de la carte du carrée si un carré existe
    '''
    for k,v in Nbnumero.items():
        if v==4:
            return k


def Full(Nbnumero):
    '''
    renvoi la valeur de la carte qui fait brelan si brelan il y a
    '''
    #full correspond à avoir une paire ainsi qu'un brelan, on verifie que les deux existent
    if Paire(Nbnumero)!=0 and Brelan(Nbnumero)!=None:
        return Brelan(Nbnumero)


def Couleur(Nbcouleur,cartes):
    '''
    determine si il y a au moins 5 cartes du même signe, si c'est le cas renvoi la liste des valeurs des cartes qui forment la couleur
    '''
    cartesCouleur=[]
    for key,value in Nbcouleur.items():
        if value>4:
            for a,b in cartes:
                if b==key:
                    cartesCouleur.append(valeur_carte(a))
            cartesCouleur.sort(reverse=True)
            return cartesCouleur
        
def ComparaisonCartesCouleur(cartes1,cartes2):
    '''
    dans le cas ou deux joueurs on couleur, determine la carte la plus forte dans la couleur de chaque joueur
    '''
    for i in range(len(cartes1)):
        if cartes1[i] > cartes2[i]:
            return "{} gagne avec une couleur plus forte".format(nomJ1)
        elif cartes1[i] < cartes2[i]:
            return "{} gagne avec une couleur plus forte".format(nomJ2)


def Quinte(cartes):
    '''
    renvoi la carte la plus haute de la suite si suite il y a
    '''
    valeur_cartes = [valeur_carte(carte[0]) for carte in cartes]
    valeur_cartes.sort(reverse=True)
    
    #rajoute un 1 dans la liste des cartes si il y a un As car il peut à la fois valoir 1 et 14 (seulement dans une suite)
    if 14 in valeur_cartes:
        valeur_cartes.insert(len(valeur_cartes)+1,1)
        

    maxsuite=[]
    for i in valeur_cartes:
        #suite maximale trouvé
        if maxsuite==[]:
            maxsuite.append(i)
        #notre liste de cartes est ordonné (decroissant) donc on compare la carte actuelle à la précédente
        elif maxsuite[-1] - 1 == i or maxsuite[-1] == i:
            #en cas de doublon ne le prend pas en compte, ex ['6','7','8','8',9','10'] ici il ya suite et si on prend en compte les doublon avce notre algo, il renverra None (pas de suite)
            if i not in maxsuite:
                maxsuite.append(i)
        else:
            maxsuite=[i]
        
        #suite maximale trouvé, renvoi de la plus grande valeur de la suite et fin fonction
        if len(maxsuite)==5:
            return maxsuite[0]


def Brelan(Nbnumero):
    '''
    renvoi la valeur du brelan si il existe
    '''
    brelanMax=None
    for k,v in Nbnumero.items():
        if v==3:
            brelanMax=k
    return brelanMax


def DoublePaire(Nbnumero):
    '''
    renvoi la paire la plus haute des deux si une double paires existe
    '''
    paires=[]
    for k,v in Nbnumero.items():
        if v==2:
            if paires==2:
                paires.pop(0)
                paires.append(k)
            else:
                paires.append(k)
    return paires[1] if len(paires)==2 else None


def Paire(Nbnumero):
    '''
    renvoi la valeur de la paire maximum si elle existe
    '''
    paireMax = 0
    for k,v in Nbnumero.items():
        if v==2:
            if valeur_carte(k)>paireMax:
                paireMax=valeur_carte(k)
    return paireMax

def ComparaisonCartesHautes(cartes1,cartes2):
    '''
    aucun joueur n'a de combinaison, on prend la meilleure main finale composé des 5 meilleurs cartes de chaque joueurs et on les compares, 
    si les 5 sont égales alors égalité
    '''
    #liste avec seulement les valeurs des cartes de chaque joueur
    cartesVal1 = [valeur_carte(carte[0]) for carte in cartes1]
    cartesVal2 = [valeur_carte(carte[0]) for carte in cartes2]
    
    #ranger les cartes dans l'odre décroissant
    cartesVal1.sort(reverse=True)
    cartesVal2.sort(reverse=True)
    
    for i in range(len(cartesVal1)-2):
        if cartesVal1[i] > cartesVal2[i]:
            return "{} gagne avec la carte la plus forte".format(nomJ1)
        elif cartesVal1[i] < cartesVal2[i]:
            return "{} gagne avec la carte la plus forte".format(nomJ2)
    return "Egalité, vous avez les mêmes cartes"
    
    
    
    
    
    
def valeur_signe(couleur):
    '''
    transforme le signe couleur (string) en un signe image
    '''
    if couleur=="trèfle":
        return '♣'
    elif couleur=="pique":
        return '♠'
    elif couleur=="carreau":
        return '♦'
    return '♥'

def valeur_carte(num_carte):
    '''
    transforme num_carte(string) en un entier et le retourne
    '''
    if num_carte=='Valet' and inspect.stack()[1].function=="carte_physique":
        return 'V'
    elif num_carte=='Dame' and inspect.stack()[1].function=="carte_physique":
        return 'D'
    elif num_carte=='Roi' and inspect.stack()[1].function=="carte_physique":
        return 'R'
    elif num_carte=='Valet':
        return 11
    elif num_carte=='Dame':
        return 12
    elif num_carte=='Roi':
        return 13
    elif num_carte=='As' and inspect.stack()[1].function=="carte_physique":
        return 'As'
    elif num_carte=='As': #faire une condition si quinte ou affichage carte alors as peut etre 1 et 14
        return 14
    
    return int(num_carte)

def valeur_patern(carte,signeCarte):
    '''
    renvoi le paterne a afficher sur la carte en fonction de la couleur de la carte
    '''
    if carte[0]=='As':
        return '{}'.format(signeCarte)
    if carte[0]=='2':
        return '{}\n{}'.format(*[signeCarte]*2)
    if carte[0]=='3':
        return '{}\n{}\n{}'.format(*[signeCarte]*3)
    if carte[0]=='4':
        return '{}  {}\n\n{}  {}'.format(*[signeCarte]*4)
    if carte[0]=='5':
        return '{}  {}\n{}\n{}  {}'.format(*[signeCarte]*5)
    if carte[0]=='6':
        return '{}  {}\n{}  {}\n{}  {}'.format(*[signeCarte]*6)
    if carte[0]=='7':
        return '{}  {}\n{}\n{}  {}\n{}  {}'.format(*[signeCarte]*7)
    if carte[0]=='8':
        return '{}  {}\n{}  {}\n{}  {}\n{}  {}'.format(*[signeCarte]*8)
    if carte[0]=='9':
        return '{}  {}\n{} {} {}\n{}  {}\n{}  {}'.format(*[signeCarte]*9)
    if carte[0]=='10':
        return '{}  {}\n{} {} {}\n{} {} {}\n{}  {}'.format(*[signeCarte]*10)
    if carte[0]=='Valet':
        return '👲'
    if carte[0]=='Dame':
        return '👸'
    if carte[0]=='Roi':
        return '🤴'
        
    
def carte_physique(frameCarte,carte):
    '''
    crée le contenu de la carte passé en paramètre
    '''
    #récupération du signe de la carte pour savoir quel symbole appliquer sur la carte
    signeCarte = valeur_signe(carte[1])
    #récupération de la valeur de la carte pour l'inscrire sur la carte
    numerocarte = valeur_carte(carte[0])
    #nombre de symbole a appliquer en fonction de la valeur de la carte
    paternCarte = valeur_patern(carte,signeCarte)
    
    #valeur de la carte et petits symboles correspondant a là couleur de la carte dans les 4 angles
    label_petit1 = CTkLabel(frameCarte, text="{}\n{}".format(numerocarte,signeCarte), text_color="{}".format(DefinirCouleurCarte(carte)), font=("Arial", 15))
    label_petit1.place(relx=0.05, rely=0.05, anchor="nw")

    label_petit2 = CTkLabel(frameCarte, text="{}\n{}".format(numerocarte,signeCarte), text_color="{}".format(DefinirCouleurCarte(carte)), font=("Arial", 15))
    label_petit2.place(relx=0.95, rely=0.05, anchor="ne")
    
    label_petit3 = CTkLabel(frameCarte, text="{}\n{}".format(signeCarte,numerocarte), text_color="{}".format(DefinirCouleurCarte(carte)), font=("Arial", 15))
    label_petit3.place(relx=0.05, rely=0.95, anchor="sw")

    label_petit4 = CTkLabel(frameCarte, text="{}\n{}".format(signeCarte,numerocarte), text_color="{}".format(DefinirCouleurCarte(carte)), font=("Arial", 15))
    label_petit4.place(relx=0.95, rely=0.95, anchor="se")

    #gros symboles au centre de la carte avec autant de symbole que la valeur de la carte
    if numerocarte==9 or numerocarte==10:
        taille_symbole=30
    elif numerocarte=='As' or numerocarte=='V' or numerocarte=='D' or numerocarte=='R':
        taille_symbole=45
    else:
        taille_symbole=35
        
    label_couleur = CTkLabel(frameCarte, text="{}".format(paternCarte), text_color="{}".format(DefinirCouleurCarte(carte)), font=("Arial", taille_symbole))
    label_couleur.place(relx=0.5, rely=0.5, anchor="center")
    

def DefinirCouleurCarte(carte):
    '''
    renvoi la couleur (en anglais pour utiliser dans les variables de couleur) en fonction de la couleur de la carte
    '''
    if carte[1]=="trèfle" or carte[1]=="pique":
        return "black"
    else:
        #pour coeur et carreau
        return "red"
    
    
def DetruireLabelFrame(frame1,frame2,frame3,frame4,frame5):
    '''
    en fin de partie permet d'effacer le contenu de toutes les cartes (enlever tout les widgets)
    '''
    frames=[frame1,frame2,frame3,frame4,frame5]
    for frame in frames:
        for label in frame.winfo_children():
            label.destroy()



#Lancer une partie
LancerLeJeu()

poker.mainloop()