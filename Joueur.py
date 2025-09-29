from customtkinter import *
import time
from DeterminerGagnant import DeterminerGagnant

class Joueur():
    
    def __init__(self,nom,partie):
        self.nom = nom
        self.solde = 10000
        self.MEJ = 0
        self.CheckStatut = False
        self.AllInStatut = False
        self.cartes = []
        self.main = False
        self.partie = partie
        
        #frame contenant toutes les infos du joueur
        self.frame = CTkFrame(self.partie.interface, fg_color="white",corner_radius=15)
        
        '''
        NOM JOUEUR
        '''
        self.label_nomJoueur = CTkLabel(self.frame, text="{}".format(self.nom), font=("Arial",15,"bold"), text_color="black")
        
        '''
        BADGE
        '''
        self.frameBadge = CTkFrame(self.frame, width=30, height=30, corner_radius=15, fg_color="blue")
        self.label_badge = CTkLabel(self.frameBadge, font=("Arial",15,"bold"), text_color="white")
        
        '''
        CARTES PHYSIQUE CLIQUABLES
        '''
        #frame pour que le joueur voit ses cartes
        self.frameVoirCarte1 = CTkFrame(self.frame,fg_color="#222222",border_color="red",border_width=2,corner_radius=10,width=70,height=99)
        self.frameVoirCarte2 = CTkFrame(self.frame,fg_color="#222222",border_color="red",border_width=2,corner_radius=10,width=70,height=99)
        
        # cliquer sur les cartes pour voir le contenu
        self.frameVoirCarte1.bind("<Button-1>",self.voirCarte1)
        self.frameVoirCarte2.bind("<Button-1>",self.voirCarte2)
        

        '''
        SOLDE/MEJ
        '''
        self.frameSoldeMEJ = CTkFrame(self.frame, fg_color="white")
        
        #frame concernant le solde
        self.frameSolde = CTkFrame(self.frameSoldeMEJ,fg_color="gold",corner_radius=10)
        self.labelSolde = CTkLabel(self.frameSolde, text="Solde ", font=("Arial",12,"bold"),text_color="black")
        self.labelSoldeVariable = CTkLabel(self.frameSolde, text="{} $".format(self.solde), font=("Arial",13),text_color="black")

        #frame concernant la somme mise en jeu par le joueur dans cette manche
        self.frameMEJ = CTkFrame(self.frameSoldeMEJ,fg_color="gold",corner_radius=10)
        self.labelMEJ = CTkLabel(self.frameMEJ, text="Mise en jeu ", font=("Arial",12,"bold"),text_color="black")
        self.labelMEJVariable = CTkLabel(self.frameMEJ, text="{} $".format(self.MEJ), font=("Arial",13),text_color="black")

        '''
        MISER/BOUTONS
        '''
        self.frameMiserBoutons = CTkFrame(self.frame, fg_color="green", border_color="red",border_width=2,corner_radius=10)
        
        self.entryMiseEnJeu = CTkEntry(self.frameMiserBoutons, text_color="#221C1C",fg_color='#D3D3D3', border_color="#221C1C",state="disabled")
        self.btnMiser = CTkButton(self.frameMiserBoutons, command=lambda: self.mise(self.entryMiseEnJeu.get()), text="miser", text_color='white', font=("Arial",16,"bold"), fg_color='red', hover_color='darkred', corner_radius=10, state="disabled")
        
        self.btnSuivre = CTkButton(self.frameMiserBoutons, command= self.suivre, text="suivre",text_color='white', font=("Arial",16,"bold"), fg_color='red',hover_color='darkred', corner_radius=10, state="disabled")
        self.btnAllIn = CTkButton(self.frameMiserBoutons, command= self.allIn, text="all In",text_color='white', font=("Arial",16,"bold"), fg_color='red',hover_color='darkred', corner_radius=10, state="disabled")
        self.btnCheckJ = CTkButton(self.frameMiserBoutons, command=self.check, text="check",text_color='black', font=("Arial",16,"bold"), fg_color="#FDB470",hover_color='darkorange',corner_radius=20, state="disabled")
        self.btnSeCoucher = CTkButton(self.frameMiserBoutons, command=self.seCoucher, text="se coucher",text_color='black', font=("Arial",16,"bold"), fg_color="#FDB470",hover_color='darkorange',corner_radius=20, state="disabled")

        
    #--------
    #methodes
    #--------  
    def donner_main(self,paquet):
        self.cartes = [paquet.tirerUneCarte(), paquet.tirerUneCarte()]
      
        
    def setMain(self):
        
        #si il a la main
        if self.main:
            self.main = False
            self.frame.configure(fg_color="white")
            self.frameSoldeMEJ.configure(fg_color="white")
            self.btnAllIn.configure(state="disabled")
            self.btnCheckJ.configure(state="disabled")
            self.btnMiser.configure(state="disabled")
            self.btnSeCoucher.configure(state="disabled")
            self.btnSuivre.configure(state="disabled")
            self.entryMiseEnJeu.configure(state="disabled")
            
        
        #sinon on lui donne la main
        else:
            self.main = True
            
            #on regarde si le joueur a fait a fait allIn
            if self.AllInStatut or len(self.partie.manche.liste_joueurs)==1:
                
                #on regarde si tout le monde a fait allIn
                if all(joueur.AllInStatut==True for joueur in self.partie.manche.liste_joueurs) or len(self.partie.manche.liste_joueurs)==1:
                    
                    #on devoile toutes les cartes restantes
                    match len(self.partie.manche.board.board):
                        case 0:
                            self.partie.manche.board.tirerFlop()
                            self.partie.manche.board.afficherFlop()
                            
                            self.partie.manche.board.tirerCarte()
                            self.partie.manche.board.afficherCarte()
                            
                            self.partie.manche.board.tirerCarte()
                            self.partie.manche.board.afficherCarte()
                        case 3 :
                            self.partie.manche.board.tirerCarte()
                            self.partie.manche.board.afficherCarte()
                            
                            self.partie.manche.board.tirerCarte()
                            self.partie.manche.board.afficherCarte()
                        case 4:
                            self.partie.manche.board.tirerCarte()
                            self.partie.manche.board.afficherCarte()
                    
                    self.partie.interface.update()        
                    self.setMain()
                    DeterminerGagnant(self.partie)
                    return 
                
                #on passe au joueur suivant
                self.joueurSuivant()
                return
            
            self.frame.configure(fg_color="#87D3FF")
            self.frameSoldeMEJ.configure(fg_color="#87D3FF")
            self.btnAllIn.configure(state="normal")
            self.btnMiser.configure(state="normal")
            self.btnSeCoucher.configure(state="normal")
            self.entryMiseEnJeu.configure(state="normal")
            
            #si ma mise est égale à la mise de tout les autres joueurs, le check est possible
            if all(self.MEJ == joueur.MEJ for joueur in self.partie.manche.liste_joueurs): 
                self.btnCheckJ.configure(state="normal")
            #sinon le bouton reste desactivé
            
            #si la mise de tout les joueur n'est pas égale
            if any(self.MEJ != joueur.MEJ for joueur in self.partie.manche.liste_joueurs):
                self.btnSuivre.configure(state="normal")
            
        self.partie.interface.update()
      
     
    def faireApparaitreFrame(self):
        
        #position dans la grille
        posX = [1, 1, 3, 3]  # lignes
        posY = [1, 3, 3, 1]  # colonnes
        
        self.frame.grid(row=posX[self.partie.liste_joueurs.index(self)],column=posY[self.partie.liste_joueurs.index(self)],padx=20,pady=20)
        
        #ligne 1
        self.label_nomJoueur.grid(row=1,column=1,padx=5,pady=5)
        
        self.frameSoldeMEJ.grid(row=1,column=3,padx=10,pady=10)
        self.frameSolde.grid(row=3,column=1,padx=5,pady=1,sticky="w")
        self.labelSolde.grid(row=1,column=1,padx=10,pady=10)
        self.labelSoldeVariable.grid(row=1,column=2,padx=10,pady=10)
        self.frameMEJ.grid(row=3,column=2,padx=5,pady=1)
        self.labelMEJ.grid(row=1,column=1,padx=10,pady=10)
        self.labelMEJVariable.grid(row=1,column=2,padx=10,pady=10)
        
        #ligne 2
        self.frameVoirCarte1.grid(row=2,column=1,padx=10,pady=10)
        self.frameVoirCarte2.grid(row=2,column=2,padx=10,pady=10)
        
        self.frameMiserBoutons.grid(row=2,column=3,padx=10,pady=10)
        self.entryMiseEnJeu.grid(row=1,column=1,padx=10,pady=10)
        self.btnMiser.grid(row=1,column=2,padx=10,pady=10)
        
        self.btnCheckJ.grid(row=2,column=1,padx=10,pady=10)
        self.btnSuivre.grid(row=2,column=2,padx=10,pady=10)
        self.btnSeCoucher.grid(row=3,column=1,padx=10,pady=10)
        self.btnAllIn.grid(row=3,column=2,padx=10,pady=10)


        
        
    def voirCarte1(self,event):
        self.cartes[0].afficherCartePhysiqueJoueur(self.frameVoirCarte1)
        self.partie.interface.update()
        self.partie.interface.after(3000,lambda:self.cartes[0].cacherCartePhysiqueJoueur(self.frameVoirCarte1)) #lambda : pour pas que sa s'exectute tout dessuite et que ça "freeze" le mainloop (ex : pouvoir regarder deux cartes en même temps)
    
    
    def voirCarte2(self,event):
        self.cartes[1].afficherCartePhysiqueJoueur(self.frameVoirCarte2)
        self.partie.interface.update()
        self.partie.interface.after(3000,lambda:self.cartes[1].cacherCartePhysiqueJoueur(self.frameVoirCarte2))
        
    
    def mise(self,montant):
        montant = int(montant)
        
        #cas ou le montant entrée est incorrecte
        if not (0 < montant < self.solde) and not self.AllInStatut:
            self.entryMiseEnJeu.configure(border_color="red", text_color="red")
            return #on sort de la fonction
        
        #cas ou le joueur n'aligne pas sa MEJ avec celle du joueur precedent
        if (montant+self.MEJ) < self.partie.manche.liste_joueurs[(self.partie.manche.liste_joueurs.index(self) - 1)%len(self.partie.manche.liste_joueurs)].MEJ:
            self.entryMiseEnJeu.configure(border_color="red", text_color="red")
            return #on sort de la fonction
        
        #maj solde en fonction du montant  
        self.solde-=montant
        self.MEJ+=montant
        self.partie.manche.MEJ+=montant
        self.MAJMontants()
                
        #cas pre flop
        if len(self.partie.manche.board.board)==0:
                    
            #cas ou tout le monde c'est aligné sur une surenchère de la mise de depart de la grosse blinde
            if all(joueur.MEJ==self.MEJ for joueur in self.partie.manche.liste_joueurs) and self.MEJ!=500:
                #on devoile le flop
                self.partie.manche.board.tirerFlop()
                self.partie.manche.board.afficherFlop()
                
                self.partie.manche.donnerMainPostFlop()  
                    
            #cas ou tous le monde ne c'est pas encore aligné
            else:                               
                self.partie.manche.joueurSuivant()
                           
        #cas post flop
        else:
        
            #cas ou tous les joueurs ont mis la même mise
            if all(joueur.MEJ==self.MEJ for joueur in self.partie.manche.liste_joueurs):
                match len(self.partie.manche.board.board):
                    case 3 | 4:
                        self.partie.manche.board.tirerCarte()
                        self.partie.manche.board.afficherCarte()
                    case _:
                        self.setMain()
                        DeterminerGagnant(self.partie)
                        return 
                        
                self.partie.manche.donnerMainPostFlop()        
                                
            #cas ou tous le monde n'a pas encore mis la meme mise
            else:
                self.partie.manche.joueurSuivant()            
        
        
    def check(self):
        
        self.CheckStatut = True
        
        #si tout les joueurs ont check ou si c'est la big blinde qui a check au pre Flop
        if all(joueur.CheckStatut==True for joueur in self.partie.manche.liste_joueurs) or len(self.partie.manche.board.board)==0 and self.partie.manche.bigBlind == self:
            #devoiler carte(s) sur le board en fonction du nombres de cartes déjà devoilées
            match len(self.partie.manche.board.board):
                case 0:
                    #on devoile le flop
                    self.partie.manche.board.tirerFlop()
                    self.partie.manche.board.afficherFlop()
                case 3 | 4:
                    self.partie.manche.board.tirerCarte()
                    self.partie.manche.board.afficherCarte()
                case _:
                    self.setMain()
                    DeterminerGagnant(self.partie)
                    return
            
            
            #on reinitialise le bouton check de tous les joueurs
            for joueur in self.partie.manche.liste_joueurs:
                joueur.CheckStatut = False
                joueur.btnCheckJ.configure(fg_color="#FDB470")  
                   
            self.partie.manche.donnerMainPostFlop()   

        #sinon (donc si une personne n'a pas check)
        else:
            self.btnCheckJ.configure(fg_color="darkorange")
            self.partie.manche.joueurSuivant()
                        
        self.partie.interface.update()
  
        
    def MAJMontants(self):
        '''
        Mettre à jour des labels variables (solde, MEJ joueur, MEJ principale)
        '''
        self.entryMiseEnJeu.delete(0, "end")
        self.labelSoldeVariable.configure(text="{} $".format(self.solde))
        self.labelMEJVariable.configure(text="{} $".format(self.MEJ))
        self.partie.labelMiseEnJeuVariable.configure(text="{} $".format(self.partie.manche.MEJ))
        self.entryMiseEnJeu.configure(border_color="grey", text_color="white")
        
        self.partie.interface.update()
                    
    def suivre(self):
        '''
        miser la même chose que le joueur precedent ou allIn si j'ai pas assez pour m'aligner
        '''
        MEJ_joueur_precedent = self.partie.manche.liste_joueurs[(self.partie.manche.liste_joueurs.index(self) - 1)%len(self.partie.manche.liste_joueurs)].MEJ
        #si mon solde + ma mise en jeu est supérieur ou egal à la mise en jeu du joueur precedent
        if self.solde + self.MEJ > MEJ_joueur_precedent:
            montant = MEJ_joueur_precedent - self.MEJ 
            self.mise(montant)

        #sinon (inferieur ou égal)
        else:
            self.allIn()
    
    
    def allIn(self):
        self.AllInStatut = True
        self.mise(self.solde)
       
     
    def seCoucher(self):
        '''
        on me retire de la liste des joueurs de la manche ainsi que que de la liste ephemere si je suis pas le dealer
        '''
        #cas ou il ne reste que 2 joueurs (et que dcp comme cette fonction est appellé le joueur courant se couche donc plus qu'un seul joueur)
        if len(self.partie.manche.liste_joueurs) == 2:
            #fin de manche il ne reste qu'un joueur qui gagne
            self.partie.manche.liste_joueurs.remove(self)
            self.setMain()
            self.frame.configure(fg_color="red")
            self.partie.manche.main = self.partie.manche.liste_joueurs[0]
            self.partie.manche.main.setMain()

        #sinon on le supprime de la manche et on passe au joueur suivant
        else:
            self.partie.manche.joueurSuivant()
            
            if self == self.partie.manche.dealer:
                #on garde le dealer dans une liste (liste_joueurs_ephemere)pour pouvoir continuer a donner la main a gauche du dealer même si il c'est couché
                self.partie.manche.liste_joueurs_ephemere.remove(self)
            
            self.partie.manche.liste_joueurs.remove(self)
            
        self.frame.configure(fg_color="red")
        
        
    def reset(self):
        self.MEJ = 0
        self.CheckStatut = False
        self.AllInStatut = False
        self.cartes = []
        self.main = False
        
        #suppression du contenu des cartes 
        for children in self.frameVoirCarte1.winfo_children():
            children.destroy()
        for children in self.frameVoirCarte2.winfo_children():
            children.destroy()
            
        self.frameVoirCarte1.configure(self.frame,fg_color="#222222",border_color="red",border_width=2)
        self.frameVoirCarte2.configure(self.frame,fg_color="#222222",border_color="red",border_width=2)
    
    def __del__(self):
        if self.frame.winfo_exists():
            self.frame.destroy()
        
        
    
    
