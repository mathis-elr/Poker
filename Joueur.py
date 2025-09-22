from customtkinter import *
import time

class Joueur():
    
    def __init__(self,nom,numero,partie):
        self.nom = nom
        self.numero = numero
        self.solde = 10000
        self.MEJ = 0
        self.CheckStatut = False
        self.AllInStatut = False
        self.cartes = []
        self.main = False
        self.partie = partie
        
        self.frame = CTkFrame(partie, fg_color="white",corner_radius=15)
        
        '''
        NOM JOUEUR
        '''
        self.label_nomJoueur = CTkLabel(self.frame, text="{}".format(self.getNom()), font=("Arial",15,"bold"), text_color="black")
        
        '''
        CARTES PHYSIQUE CLIQUABLES
        '''
        #frame pour que le joueur voit ses cartes
        self.frameVoirCarte1 = CTkFrame(self.frame,fg_color="#222222",border_color="red",border_width=2,corner_radius=10,width=70,height=99)
        self.frameVoirCarte2 = CTkFrame(self.frame,fg_color="#222222",border_color="red",border_width=2,corner_radius=10,width=70,height=99)
        self.frameVoirCarte1.bind("<Button-1>",self.voirCarte1)
        self.frameVoirCarte2.bind("<Button-1>",self.voirCarte2)
        

        '''
        SOLDE/MEJ/BOUTONS
        '''
        self.frameAutre = CTkFrame(self.frame, fg_color="white")
        self.frameSoldeMEJ = CTkFrame(self.frameAutre, fg_color="white")
        #frame pour visualiser le solde
        self.frameSolde = CTkFrame(self.frameSoldeMEJ,fg_color="yellow",corner_radius=10)
        #label simple pour exprimer le solde
        self.labelSolde = CTkLabel(self.frameSolde, text="Solde :", font=("Arial",12,"bold"),text_color="black")
        #label contenant le solde (variable)
        self.labelSoldeVariable = CTkLabel(self.frameSolde, text="{} $".format(self.getSolde()), font=("Arial",12,"bold"),text_color="black")

        #frame pour visualiser la somme mise en jeu par le joueur
        self.frameMEJ = CTkFrame(self.frameSoldeMEJ,fg_color="yellow",corner_radius=10)
        #label simple pour exprimer la mise en jeu
        self.labelMEJ = CTkLabel(self.frameMEJ, text="Mise en jeu :", font=("Arial",12,"bold"),text_color="black")
        #label contenant la mise en jeu (variable)
        self.labelMEJVariable = CTkLabel(self.frameMEJ, text="{} $".format(self.getMEJ()), font=("Arial",12,"bold"),text_color="black")

        self.frameBoutons = CTkFrame(self.frameAutre, fg_color="white")
        self.btnCheckJ = CTkButton(self.frameBoutons, text="check",text_color='black', fg_color="#FDB470",hover_color='darkorange',corner_radius=50,width=100, command=self.check,state="disable")
        self.btnSeCoucher = CTkButton(self.frameBoutons, text="se coucher",text_color='white', fg_color="#6B7AFF",hover_color='darkblue',corner_radius=50, width=100,command=self.seCoucher,state="disable")

        '''
        MISER
        '''
        #frame pour miser 
        self.frameMiser = CTkFrame(self.frame,fg_color="black",border_color="black",border_width=5,corner_radius=10)
        #entrée pour la mise en jeu souhaité
        self.entryMiseEnJeu = CTkEntry(self.frameMiser, state="disabled")
        #bouton pour valider la mise en jeu
        self.btnMiser = CTkButton(self.frameMiser, text="Miser",text_color='black', fg_color='white',hover_color='lightgrey',command=self.mise,state="disable")
        #bouton pour allin
        self.btnAllIn = CTkButton(self.frameMiser, text="All In",text_color='black', fg_color='white',hover_color='red',command= self.allIn,state="disable")
        
        
    #--------
    #setters
    #--------
    def donner_main(self,paquet):
        self.cartes = [paquet.tirerUneCarte(), paquet.tirerUneCarte()]
        
    def setMEJ(self,montant):
        self.MEJ+=montant
        
    def setSolde(self,montant):
        self.solde+=montant    
    
    def setCheckStatut(self):
        self.CheckStatut = not self.CheckStatut
        
    def setAllInStatut(self):
        self.AllInStatut = not self.AllInStatut
        
    def setMain(self):
        if self.main:
            self.main = False
            self.frame.configure(fg_color="white")
            self.btnAllIn.configure(state="disable")
            self.btnCheckJ.configure(state="disable")
            self.btnMiser.configure(state="disable")
            self.btnSeCoucher.configure(state="disable")
            self.entryMiseEnJeu.configure(state="disabled")
        else:
            self.main = True
            self.frame.configure(fg_color="#5CB5FF")
            self.btnAllIn.configure(state="normal")
            self.btnMiser.configure(state="normal")
            self.btnSeCoucher.configure(state="normal")
            self.entryMiseEnJeu.configure(state="normal", placeholder_text="mise")
            
            #si le jour precedent a check ou que je suis la small blinde et qu'avec le joueur precedent on à la même MEJ
            if self.partie.liste_joueurs[(self.numero - 1)%len(self.partie.liste_joueurs)].check \
            or self.partie.smallBlinde == self.numero and self.partie.liste_joueurs[(self.numero - 1)%len(self.partie.liste_joueurs)].MEJ == self.MEJ:
                self.btnCheckJ.configure(state="normal")
            #sinon le bouton reste desactivé
            
        self.partie.update()
      
    #--------
    #getteurs
    #--------
    def getCarte1(self):
        return self.cartes[0]
        
    def getCarte2(self):
        return self.cartes[1]
    
    def getMesCartes(self):
        return self.cartes
    
    def getCartes(self, board):
        return [self.carte1,self.carte2] + board.getBoard()
    
    def getNom(self):
        return self.nom
    
    def getSolde(self):
        return self.solde
    
    def getMEJ(self):
        return self.MEJ
    
    def getCheckStatut(self):
        return self.CheckStatut
    
    def getAllInStatut(self):
        return self.AllInStatut
    
    def getMain(self):
        return self.main
    
    #--------
    #methodes
    #--------   
    def faireApparaitreFrame(self,l,c):
        self.frame.grid(row=l,column=c,padx=20,pady=20)
        
        #ligne 1
        self.label_nomJoueur.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
        
        #ligne 2
        self.frameVoirCarte1.grid(row=2,column=1,padx=10,pady=10)
        self.frameVoirCarte2.grid(row=2,column=2,padx=10,pady=10)

        self.frameAutre.grid(row=2,column=3,padx=10,pady=10)
        
        self.frameSoldeMEJ.grid(row=1,column=1,padx=10,pady=10)
        self.frameSolde.grid(row=3,column=1,padx=5,pady=1,sticky="w")
        self.labelSolde.grid(row=1,column=1,padx=10,pady=10)
        self.labelSoldeVariable.grid(row=1,column=2,padx=10,pady=10)
        self.frameMEJ.grid(row=3,column=2,padx=5,pady=1)
        self.labelMEJ.grid(row=1,column=1,padx=10,pady=10)
        self.labelMEJVariable.grid(row=1,column=2,padx=10,pady=10)
        
        self.frameBoutons.grid(row=2,column=1)
        self.btnCheckJ.grid(row=1,column=1,padx=10,pady=10)
        self.btnSeCoucher.grid(row=1,column=2,padx=10,pady=10)
        
        #ligne 3
        self.frameMiser.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
        self.entryMiseEnJeu.grid(row=2,column=1,padx=10,pady=10)
        self.btnMiser.grid(row=2,column=2,padx=10,pady=10)
        self.btnAllIn.grid(row=2,column=3,padx=10,pady=10)
        
        
    def voirCarte1(self,event):
        self.getCarte1().afficherCartePhysiqueJoueur(self.frameVoirCarte1)
        self.partie.update()
        self.partie.after(3000,lambda:self.getCarte1().cacherCartePhysiqueJoueur(self.frameVoirCarte1)) #lambda : pour pas que sa s'exectute tout dessuite et que ça "freeze" le mainloop (ex : pouvoir regarder deux cartes en même temps)
    
    
    def voirCarte2(self,event):
        self.getCarte2().afficherCartePhysiqueJoueur(self.frameVoirCarte2)
        self.partie.update()
        self.partie.after(3000,lambda:self.getCarte2().cacherCartePhysiqueJoueur(self.frameVoirCarte2))
        
        
    def allIn(self):
        pass 
    
    
    def mise(self):
        montant = int(self.entryMiseEnJeu.get()) #on recupère le montant
        if montant < self.solde and montant > 0: 
            if (montant+self.MEJ) >= self.partie.liste_joueurs[(self.numero - 1)%len(self.partie.liste_joueurs)].MEJ: # le joueur doit s'aligner avec la mise du joueur précedent (on utilise modulo pour le joueur precedent, ainsi precedent de 0 → dernier elmt de la liste)
                self.solde-=montant
                self.MEJ+=montant
                self.partie.MEJ+=montant
                
                self.entryMiseEnJeu.delete(0, "end")
                self.labelSoldeVariable.configure(text="{}".format(self.solde))
                self.labelMEJVariable.configure(text="{}".format(self.MEJ))
                self.partie.labelMiseEnJeuVariable.configure(text="{}".format(self.partie.MEJ))
                self.entryMiseEnJeu.configure(border_color="grey", text_color="white")
                self.setMain() #on desactive sa main
            
                self.partie.changerMain() #on passe au joueur suivant
            #sinon erreur le montant doit être compris entre 1 et la MEJ du joueur precedent (inclus) 
            else:
                self.entryMiseEnJeu.configure(border_color="red", text_color="red")
            
        #sinon erreur montant ne peut être supérieur au solde    
        else:
            self.entryMiseEnJeu.configure(border_color="red", text_color="red")
            
        self.partie.update()
        
    
    def check(self):
        #si c'est la big blind qui check et que aucune carte n'a été dévoilée
        if self.partie.bigBlind == self.numero and len(self.partie.flop.board)==0: 
            #on devoile le flop
            self.partie.flop.tirerFlop()
            self.partie.flop.afficherFlop()
            
            self.setMain()
            self.partie.main = self.partie.smallBlind
            self.partie.liste_joueurs[self.partie.main].setMain()
            
        else:
            self.CheckStatut = True
            #on verifie si tout le monde a check
            if False in [joueur.getCheckStatut() for joueur in self.partie.liste_joueurs]:
                #tout le monde n'a pas check on passe au joueur suivant
                self.btnCheckJ.configure(fg_color="darkorange")
                self.setMain() 
                self.partie.changerMain()
                self.partie.update()
            else:
                #devoiler carte(s) sur le board
                match len(self.partie.flop.board):
                    case 3:
                        self.partie.flop.tirerCarte()
                        self.partie.flop.afficherCarte(self.partie.frameCarte4)
                    case 4:
                        self.partie.flop.tirerCarte()
                        self.partie.flop.afficherCarte(self.partie.frameCarte5)
                    case _:
                        exit
                
                #donner la main à la smallBlinde
                self.setMain()
                self.partie.main = self.partie.smallBlind
                self.partie.liste_joueurs[self.partie.main].setMain()
                
                #on reinitialise le bouton check de tous les joueurs
                for joueur in self.partie.liste_joueurs:
                    joueur.btnCheckJ.configure(fg_color="#FDB470")
                    
        self.partie.update()
                    
                
    def seCoucher(self):
        pass