from Carte import Carte
import random

class PaquetCartes():
    
    def __init__(self,partie):
        self.partie = partie
        self.cartes=[]
        self.couleurs=["coeur","carreau","pique","trèfle"]
        self.valeurs=["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]
        self.remplirPaquet()
        
    def remplirPaquet(self):
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.cartes.append(Carte(couleur,valeur,self.partie))
            
    def __repr__(self):
        return f"{self.cartes}"
                
    def tirerUneCarte(self):
        carte = random.choice(self.cartes)
        self.cartes.remove(carte)
        return carte