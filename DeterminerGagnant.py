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
                        joueur_gagnant, inutile = combinaisonIdesJoueurs.popitem()
                        combinaison = self.mains[joueur_gagnant][i]
                        match i:
                            case 2|6|7|8|9: #cas pour Carre, Brelan, DoublePaire, Paire, CarteHaute
                                self.text = "{} gagne avec {} de {}".format(joueur_gagnant.nom, combinaison[0], self.nomCarte(combinaison[1]))
                            case 0|1|3|4|5: #cas pour QuinteFlushRoyale ,QuinteFlush, Full, Couleur, Quinte
                                self.text = "{} gagne avec {}".format(joueur_gagnant.nom, combinaison[0])
                            case 7:
                                self.text = "{} gagne avec {} de {} et {}".format(joueur_gagnant.nom, combinaison[0], self.nomCarte(combinaison[1][0]), self.nomCarte(combinaison[1][1]))
                                
                        self.marquerGagnant(joueur_gagnant)
                        return #fin fonction
                        
                    case _:
                        
                        if i == 7: #cas de la double paire 
                            for j in range(2):
                                max_valeur_paire_courante = max(v[j] for v in combinaisonIdesJoueurs.values())
                                joueurs_meilleurs_paires = [joueur for joueur,valeur in combinaisonIdesJoueurs.items() if max_valeur_paire_courante==valeur[j]]
                        
                            
                            #cas ou un des deux joueurs a une meilleure paire
                            if len(joueurs_meilleurs_paires) == 1:
                                #on a un gagnant
                                joueur_gagnant = joueurs_meilleurs_paires[0]
                                self.text = "{} gagne avec {} de {} et {}".format(joueur_gagnant.nom, self.mains[joueur_gagnant][i][0], self.nomCarte(self.mains[joueur_gagnant][i][1][0]), self.nomCarte(self.mains[joueur_gagnant][i][1][1]))
                                self.marquerGagnant(joueur_gagnant)
                                break #fin fonction
                                
                        
                        else: #tout les cas sauf pour la double Paire (et la Quinte Flush Royale)
                            valeur_max = max(combinaisonIdesJoueurs.values())
                            meilleurs_joueurs = [joueur for joueur,valeur in combinaisonIdesJoueurs.items() if valeur==valeur_max]       
                         
                        #pour gerer en cas de doublon (donc on boucle si len(meilleurs_joueurs>1 car egalité de combinaison)
                            if len(meilleurs_joueurs) == 1:
                                #on a un gagnant
                                joueur_gagnant = meilleurs_joueurs[0]
                                self.text = "{} gagne avec {} de {}".format(joueur_gagnant.nom, self.mains[joueur_gagnant][i][0], self.nomCarte(self.mains[joueur_gagnant][i][1]))
                                self.marquerGagnant(joueur_gagnant)
                                break #fin fonction
                            
                            if i==9:
                                self.text = "egalité carte Haute"
                                self.partie.manche.finManche([])

    def marquerGagnant(self, gagnant):
        gagnant.label_badge.configure(text="👑")
        gagnant.frameBadge.configure(fg_color="gold") #sa change la couleur mais pendant que 5s grace a la ligne d'apres
        self.partie.interface.after(5000, lambda:gagnant.frameBadge.configure(fg_color="blue"))
        gagnant.frameBadge.grid(row=1,column=2,padx=5,pady=5)
        gagnant.label_badge.grid(row=1,column=1,padx=5,pady=5)
        
        self.partie.interface.update()
        
        self.partie.manche.finManche(gagnant)
        
        
    def nomCarte(self,valeur_carte):
        '''
        transforme une carte en valeur int
        '''
        match valeur_carte:
            case 11:
                return 'Valet'
            case 12:
                return 'Dame'
            case 13:
                return 'Roi'
            case 14:
                return 'As'
            case _:
                return str(valeur_carte)
        
        