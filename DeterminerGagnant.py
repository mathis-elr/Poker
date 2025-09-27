from customtkinter import *
from DeterminerMain import DeterminerMains
class DeterminerGagnant():
    
    def __init__(self, partie):
        self.partie = partie
        
        self.mains = []
        self.text = ""
        
        for joueur in self.partie.manche.liste_joueurs:
            main_joueur = DeterminerMains(self.partie,joueur)
            self.mains.append(main_joueur.jeu)
            
        print(self.mains)
        
        #self.comparerMains()
        
        self.labelGagant= CTkLabel(self.partie.frameCartes, text="{}".format(self.text),font=("Arial",40),text_color="orange", fg_color="white")
        self.labelGagant.grid(row=1,column=1,columnspan=5)
    
    '''
    METHODES
    '''
    def comparerMains(self):
        pass
