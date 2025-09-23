from customtkinter import *

class Board():
    
    def __init__(self,partie,paquet):
        self.board = []
        self.partie = partie
        self.paquet = paquet
        
        
        '''
        BOARD
        '''
        #frame représentant le plateau de jeu (apparissions des cartes)
        self.frameCartes = CTkFrame(self.partie, width=900, height=250,fg_color="green",border_color="red",border_width=5,corner_radius=60)
        
        self.frameCarte1= CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte2 = CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte3= CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte4 = CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20)
        self.frameCarte5 = CTkFrame(self.frameCartes, fg_color="white",width=140,height=195,corner_radius=20) 

    
    #--------
    # setters
    #--------   
    def tirerFlop(self):
        self.board = [self.paquet.tirerUneCarte(), self.paquet.tirerUneCarte(), self.paquet.tirerUneCarte()]
    
    def tirerCarte(self):
        self.board.append(self.paquet.tirerUneCarte())

    
    #--------
    # getters
    #--------   
    def getBoard(self):
        return self.board
    
    
    #--------
    # methodes
    #-------- 
    def afficherFlop(self):
        #on affiche les cartes du self.board (le flop)
        self.board[0].cartePhysiqueBoard(self.frameCarte1)
        self.board[1].cartePhysiqueBoard(self.frameCarte2)
        self.board[2].cartePhysiqueBoard(self.frameCarte3)
        self.frameCarte1.grid(row=1,column=1,padx=50,pady=50)
        self.frameCarte2.grid(row=1,column=2,padx=50,pady=50)
        self.frameCarte3.grid(row=1,column=3,padx=50,pady=50)
        
        self.partie.update()
    
    def afficherCarte(self):
        #on affiche une carte supplémentaire (4e ou 5e)
        match len(self.board)-1:
            case 3:
                self.board[len(self.board)-1].cartePhysiqueBoard(self.frameCarte4)
                self.frameCarte4.grid(row=1,column=len(self.board),padx=50,pady=50)
            case 4:
                self.board[len(self.board)-1].cartePhysiqueBoard(self.frameCarte5)
                self.frameCarte5.grid(row=1,column=len(self.board),padx=50,pady=50)
    
        
        self.partie.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
