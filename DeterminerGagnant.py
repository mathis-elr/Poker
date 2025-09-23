from customtkinter import *

class DeterminerGagnant():
    
    def __init__(self, partie):
        self.partie = partie
        
        self.labelGagant= CTkLabel(self.partie.board.frameCartes, font=("Arial",15),text_color="orange")
        self.labelGagant.grid(row=1,column=1)
        
        self.partie.update()