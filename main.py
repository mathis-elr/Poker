from customtkinter import *
from DefinirJoueurs import DefinirJoueurs
from Partie import Partie

appdefinirJoueurs = DefinirJoueurs()
appdefinirJoueurs.mainloop()
    
if appdefinirJoueurs.noms_joueurs:
    poker = CTk()
    Partie(poker,appdefinirJoueurs.noms_joueurs)
    poker.mainloop()
  