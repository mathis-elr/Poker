from customtkinter import *
from DefinirJoueurs import DefinirJoueurs
from Partie import Partie

appdefinirJoueurs = DefinirJoueurs()
appdefinirJoueurs.mainloop()
    
if appdefinirJoueurs.noms_joueurs:
    applicationPartie = Partie(appdefinirJoueurs.noms_joueurs)
    applicationPartie.mainloop()
