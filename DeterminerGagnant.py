from customtkinter import *

class DeterminerGagnant():
    
    def __init__(self, partie):
        self.partie = partie
        
        self.labelGagant= CTkLabel(self.partie.frameCartes, font=("Arial",15),text_color="orange", text="fin de manche")
        self.labelGagant.grid(row=1,column=1)
        