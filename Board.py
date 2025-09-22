from customtkinter import *

class Board():
    
    def __init__(self,partie,paquet):
        self.board = []
        self.partie = partie
        self.paquet = paquet

    
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
        self.board[0].cartePhysiqueBoard(self.partie.frameCarte1)
        self.board[1].cartePhysiqueBoard(self.partie.frameCarte2)
        self.board[2].cartePhysiqueBoard(self.partie.frameCarte3)
        self.partie.frameCarte1.grid(row=1,column=1,padx=50,pady=50)
        self.partie.frameCarte2.grid(row=1,column=2,padx=50,pady=50)
        self.partie.frameCarte3.grid(row=1,column=3,padx=50,pady=50)
        
        self.partie.update()
    
    def afficherCarte(self,frame):
        #on affiche une carte supplémentaire (4e ou 5e)
        self.board[len(self.board)-1].cartePhysiqueBoard(frame)
        frame.grid(row=1,column=len(self.board),padx=50,pady=50)
        
        self.partie.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
