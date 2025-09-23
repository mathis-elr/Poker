import inspect
from customtkinter import *


class Carte():
    def __init__(self,couleur,valeur,partie):
        self.partie = partie
        self.couleur = couleur
        self.valeur = valeur
        
    #getteurs
    def getCouleur(self):
        return self.couleur
    def getValeur(self):
        return self.valeur

    
    def DefinirCouleurCarte(self):
        '''
        renvoi la couleur (en anglais pour utiliser dans les variables de couleur) en fonction de la couleur de la carte
        '''
        if self.couleur=="trèfle" or self.couleur=="pique":
            return "black"
        else:
            #pour coeur et carreau
            return "red"
    
    def valeur_patern(self):
        if self.valeur=='As':
            return '{}'.format(self.valeur_signe())
        if self.valeur=='2':
            return '{}\n{}'.format(*[self.valeur_signe()]*2)
        if self.valeur=='3':
            return '{}\n{}\n{}'.format(*[self.valeur_signe()]*3)
        if self.valeur=='4':
            return '{}  {}\n\n{}  {}'.format(*[self.valeur_signe()]*4)
        if self.valeur=='5':
            return '{}  {}\n{}\n{}  {}'.format(*[self.valeur_signe()]*5)
        if self.valeur=='6':
            return '{}  {}\n{}  {}\n{}  {}'.format(*[self.valeur_signe()]*6)
        if self.valeur=='7':
            return '{}  {}\n{}\n{}  {}\n{}  {}'.format(*[self.valeur_signe()]*7)
        if self.valeur=='8':
            return '{}  {}\n{}  {}\n{}  {}\n{}  {}'.format(*[self.valeur_signe()]*8)
        if self.valeur=='9':
            return '{}  {}\n{} {} {}\n{}  {}\n{}  {}'.format(*[self.valeur_signe()]*9)
        if self.valeur=='10':
            return '{}  {}\n{} {} {}\n{} {} {}\n{}  {}'.format(*[self.valeur_signe()]*10)
        if self.valeur=='Valet':
            return '👲'
        if self.valeur=='Dame':
            return '👸'
        if self.valeur=='Roi':
            return '🤴'

    def valeur_signe(self):
        '''
        transforme le signe couleur (string) en un signe image
        '''
        if self.couleur=="trèfle":
            return '♣'
        elif self.couleur=="pique":
            return '♠'
        elif self.couleur=="carreau":
            return '♦'
        return '♥'
    
    def valeur_carte_physique(self):
        '''
        transforme une carte (Carte) en valeur int pour afficher sur la carte physique
        '''
        match self.valeur:
            case 'Valet':
                return 'V'
            case 'Dame':
                return 'D'
            case 'Roi':
                return 'R'
            case 'As':
                return 'As'
            case _:
                return int(self.valeur)
                
    def valeur_carte(self):
        '''
        transforme une carte en valeur int
        '''
        match self.valeur:
            case 'Valet':
                return 11
            case 'Dame':
                return 12
            case 'Roi':
                return 13
            case 'As':
                return 14
            case _:
                return int(self.valeur)
                
    
    def cartePhysiqueBoard(self,frameCarte):
        '''
        crée le contenu de la carte passé en paramètre (pour les cartes communes)
        '''
        frameCarte.configure(fg_color="white")
        
        #valeur de la carte et petits symboles correspondant a là couleur de la carte dans les 4 angles
        label_petit1 = CTkLabel(frameCarte, text="{}\n{}".format(self.valeur_carte_physique(),self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15))
        label_petit1.place(relx=0.1, rely=0.05, anchor="nw")

        label_petit2 = CTkLabel(frameCarte, text="{}\n{}".format(self.valeur_carte_physique(),self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15))
        label_petit2.place(relx=0.90, rely=0.05, anchor="ne")
        
        label_petit3 = CTkLabel(frameCarte, text="{}\n{}".format(self.valeur_carte_physique(),self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15))
        label_petit3.place(relx=0.1, rely=0.95, anchor="sw")

        label_petit4 = CTkLabel(frameCarte, text="{}\n{}".format(self.valeur_carte_physique(),self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15))
        label_petit4.place(relx=0.90, rely=0.95, anchor="se")

        #gros symboles au centre de la carte avec autant de symbole que la valeur de la carte
        if self.valeur==9 or self.valeur==10:
            taille_symbole=25
        elif self.valeur=='As' or self.valeur=='V' or self.valeur=='D' or self.valeur=='R':
            taille_symbole=45
        else:
            taille_symbole=35
            
        label_couleur = CTkLabel(frameCarte, text="{}".format(self.valeur_patern()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", taille_symbole))
        label_couleur.place(relx=0.5, rely=0.5, anchor="center")
        
        
    def afficherCartePhysiqueJoueur(self,frameCarte):
        '''
        afficher le contenu de la carte passé en paramètre (pour les cartes du joueur)
        '''
        frameCarte.configure(fg_color="white")
        
        #valeur de la carte et petits symboles correspondant a là couleur de la carte dans les 4 angles
        self.label_signe1 = CTkLabel(frameCarte, text="{}".format(self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15))
        self.label_signe2 = CTkLabel(frameCarte, text="{}".format(self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15))
        self.label_signe3 = CTkLabel(frameCarte, text="{}".format(self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15))
        self.label_signe4 = CTkLabel(frameCarte, text="{}".format(self.valeur_signe()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 15)) 
        
        self.label_valeur_centre = CTkLabel(frameCarte, text="{}".format(self.valeur_carte_physique()), text_color="{}".format(self.DefinirCouleurCarte()), font=("Arial", 20))
        
        self.label_signe1.place(relx=0.1, rely=0.03, anchor="nw")
        self.label_signe2.place(relx=0.90, rely=0.03, anchor="ne")
        self.label_signe3.place(relx=0.1, rely=0.95, anchor="sw")
        self.label_signe4.place(relx=0.90, rely=0.95, anchor="se")
        self.label_valeur_centre.place(relx=0.5, rely=0.5, anchor="center")
        
        
    def cacherCartePhysiqueJoueur(self,frameCarte):
        for children in frameCarte.winfo_children():
            children.destroy()
        frameCarte.configure(fg_color="#222222")