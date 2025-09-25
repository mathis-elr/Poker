from customtkinter import *

from DeterminerMain import DeterminerMain

class DeterminerGagnant():
    
    def __init__(self, partie):
        self.partie = partie
        
        self.mains = {}
        self.gagant = {"joueur" : None,"main" : None}
        
        for joueur in self.partie.manche.liste_joueurs:
            main = DeterminerMain(joueur)
            self.mains[joueur] = main
        
        self.comparerMains()
        
        self.labelGagant= CTkLabel(self.partie.frameCartes, font=("Arial",15),text_color="orange", text="{} gagne avec {}".format(self.comparerMains["joueur"], self.comparerMains["main"]))
        self.labelGagant.grid(row=1,column=1,columnspan=5)
    
    
    def comparerMains(self):
        pass