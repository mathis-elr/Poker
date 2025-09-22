from customtkinter import *

class Board():
    
    def __init__(self):
        self.board = []

    
    #--------
    # setters
    #--------   
    def tirerFlop(self,paquet):
        self.board = [paquet.tirerUneCarte(), paquet.tirerUneCarte(), paquet.tirerUneCarte()]
    
    def tirerCarte(self,paquet):
        self.board.append(paquet.tirerUneCarte())

    
    #--------
    # getters
    #--------   
    def getBoard(self):
        return self.board
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
