from customtkinter import *
from DeterminerMain import DeterminerMains
class DeterminerGagnant():
    
    def __init__(self, partie):
        self.partie = partie
        
        self.mains = {} #dictionnaire de type joueur : liste de liste des combinaisons pour chaque joueur
        self.text = ""
          
        for joueur in self.partie.manche.liste_joueurs:
            #affiche leur cartes
            joueur.cartes[0].afficherCartePhysiqueJoueur(joueur.frameVoirCarte1)
            joueur.cartes[1].afficherCartePhysiqueJoueur(joueur.frameVoirCarte2)
            
            #analyse les cartes des joueurs
            main_joueur = DeterminerMains(self.partie,joueur)
            self.mains[main_joueur.jeu[0]] = main_joueur.jeu[1:]
        
        #determine le gagant en comparant les maisn des joueurs pas couché
        self.comparerMains()
        
        #affiche le gagant
        self.labelGagant= CTkLabel(self.partie.frameCartes, text="{}".format(self.text),font=("Arial",40),text_color="orange")
        self.labelGagant.grid(row=2,column=1,columnspan=5,pady=10)
        self.partie.interface.update()
    
    '''
    METHODES
    '''
    def comparerMains(self):
        
        #parcour des combinaisons (10 en tout), fin si gagnant trouvé
        for i in range(10):
            combinaisonIdesJoueurs = {joueur:self.mains[joueur][i][1] for joueur in self.mains}
            nb_None = sum(1 for valeur in combinaisonIdesJoueurs.values() if valeur==None)       
            
            #si personne a la combinaison, on boucle
            if nb_None != len(combinaisonIdesJoueurs):
                
                #on supprimes ceux qui ont pas la combinaison
                if nb_None >=1 : #si y a au moins un None on peut les sortir
                    for joueur in self.mains:
                        if self.mains[joueur][i][1]==None:
                            combinaisonIdesJoueurs.pop(joueur)
                            
                match len(combinaisonIdesJoueurs):
                    
                    case 1:
                        
                        #on a le gagnant
                        joueur, nom_combinaison = combinaisonIdesJoueurs.popitem()
                        combinaison = self.mains[joueur][i]
                        match i:
                            case 2|6|7|8|9: #cas pour Carre, Brelan, DoublrPaire, Paire, CarteHaute
                                self.text = "{} gagne avec {} de {}".format(joueur.nom, combinaison[0], combinaison[1])
                            case 0|1|3|4|5: #cas pour QuinteFlushRoyale ,QuinteFlush, Full, Couleur, Quinte
                                self.text = "{} gagne avec {}".format(joueur.nom, combinaison[0])
                        return #fin fonction
                        
                    case _:
                        
                        if i == 7: #cas de la double paire 
                            meilleure_paire = []
                            valeur_meilleure_paire = 0
                            for i in range(2):
                                pairesI = {joueur:self.mains[joueur][i][1] for joueur in combinaisonIdesJoueurs} 
                                for joueur, valeur_paire in pairesI.items():
                                    print(joueur,valeur_paire)
                                    if valeur_paire >=valeur_meilleure_paire:
                                        valeur_meilleure_paire = valeur_paire
                                        meilleure_paire.append(joueur)
                            
                            #cas ou un des deux joueurs a une meilleure paire
                            if len(meilleure_paire) == 1:
                                #on a un gagnant
                                joueur_gagnant = joueurs_meilleure_valeur[0]
                                self.text = "{} gagne avec {} de {}".format(joueur_gagnant.nom,self.mains[joueur_gagnant][0], valeur_paire)
                                break #fin fonction
                                
                        
                        else: #tout les cas sauf pour la double Paire (et la Quinte Flush Royale)
                            joueurs_meilleure_valeur = []
                            valeur_meilleure_carte = 0
                            for joueur in combinaisonIdesJoueurs:
                                print("combinaisonIdesJoueurs[joueur]: ",combinaisonIdesJoueurs[joueur])
                                if combinaisonIdesJoueurs[joueur] >= valeur_meilleure_carte: #PROBLEME ICI LIST >= INT
                                    valeur_meilleure_carte = combinaisonIdesJoueurs[joueur]
                                    joueurs_meilleure_valeur.append(joueur)
                                    
                            if joueurs_meilleure_valeur == 1:
                                #on a un gagnant
                                joueur_gagnant = joueurs_meilleure_valeur[0]
                                self.text = "{} gagne avec {} de {}".format(joueur_gagnant.nom,self.mains[joueur_gagnant][0], self.mains[joueur_gagnant][1])
                                break #fin fonction
                            
                            if i==10:
                                self.text = "egalité"
        