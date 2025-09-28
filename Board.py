from customtkinter import *

class Board():
    
    def __init__(self,partie,paquet):
        self.board = []
        self.partie = partie
        self.paquet = paquet
        


    #--------
    # methodes
    #-------- 
    def tirerFlop(self):
        self.board = [self.paquet.tirerUneCarte(), self.paquet.tirerUneCarte(), self.paquet.tirerUneCarte()]
    

    def afficherFlop(self):
        #on affiche les cartes du self.board (le flop)
        self.board[0].cartePhysiqueBoard(self.partie.frameCarte1)
        self.board[1].cartePhysiqueBoard(self.partie.frameCarte2)
        self.board[2].cartePhysiqueBoard(self.partie.frameCarte3)
        self.partie.frameCarte1.grid(row=1,column=1,padx=20,pady=20)
        self.partie.frameCarte2.grid(row=1,column=2,padx=20,pady=20)
        self.partie.frameCarte3.grid(row=1,column=3,padx=20,pady=20)
        
        self.partie.interface.update()
       
        
    def tirerCarte(self):
        self.board.append(self.paquet.tirerUneCarte())
    
    
    def afficherCarte(self):
        #on affiche une carte supplémentaire (4e ou 5e)
        match len(self.board)-1:
            case 3:
                self.board[3].cartePhysiqueBoard(self.partie.frameCarte4)
                self.partie.frameCarte4.grid(row=1,column=len(self.board),padx=20,pady=20)
            case 4:
                self.board[4].cartePhysiqueBoard(self.partie.frameCarte5)
                self.partie.frameCarte5.grid(row=1,column=len(self.board),padx=20,pady=20)
    
        
        self.partie.interface.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
