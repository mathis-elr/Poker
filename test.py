'''
TESTS
'''
def comparerMains(mains):
    
    text=""
    
    # parcours des combinaisons (10 en tout), fin si gagnant trouvé
    for i in range(10):
        combinaisonIdesJoueurs = {joueur: mains[joueur][i][1] for joueur in mains}
        nb_None = sum(1 for valeur in combinaisonIdesJoueurs.values() if valeur is None)       
        
        # si personne a la combinaison, on boucle
        if nb_None != len(combinaisonIdesJoueurs):
            # on supprime ceux qui n'ont pas la combinaison
            if nb_None >= 1:
                for joueur in mains:
                    if mains[joueur][i][1] is None:
                        combinaisonIdesJoueurs.pop(joueur)
                            
            match len(combinaisonIdesJoueurs):
                
                case 1:
                    # on a le gagnant
                    joueur_gagnant, inutile = combinaisonIdesJoueurs.popitem()
                    combinaison = mains[joueur_gagnant][i]
                    match i:
                        case 2|6|8|9:  # Carré, Brelan, DoublePaire, Paire, CarteHaute
                            text = "{} gagne avec {} de {}".format(joueur_gagnant, combinaison[0], combinaison[1])
                        case 0|1|3|4|5:  # QuinteFlushRoyale, QuinteFlush, Full, Couleur, Quinte
                            text = "{} gagne avec {}".format(joueur_gagnant, combinaison[0])
                        case 7:
                            text = "{} gagne avec {} de {}".format(joueur_gagnant, combinaison[0], combinaison[1][0])
                                 
                    return text
                    
                case _:
                    if i == 7:  # cas de la double paire
                        for j in range(2):
                            max_valeur_paire_courante = max(v[j] for v in combinaisonIdesJoueurs.values())
                            joueurs_meilleurs_paires = [joueur for joueur,valeur in combinaisonIdesJoueurs.items() if max_valeur_paire_courante==valeur[j]]
                        
                            # cas où un joueur a une meilleure paire
                            if len(joueurs_meilleurs_paires) == 1:
                                joueur_gagnant = joueurs_meilleurs_paires[0]
                                text = "{} gagne avec {} de {}".format(joueur_gagnant, mains[joueur_gagnant][i][0], mains[joueur_gagnant][i][1][j])
                                return text
                            
                    else:  # tout sauf la double Paire (et Quinte Flush Royale)
                        valeur_max = max(combinaisonIdesJoueurs.values())
                        meilleurs_joueurs = [joueur for joueur,valeur in combinaisonIdesJoueurs.items() if valeur==valeur_max]       
                         
                        #pour gerer en cas de doublon (donc on boucle si len(meilleurs_joueurs>1 car egalité de combinaison)
                        if len(meilleurs_joueurs) == 1:
                            joueur_gagnant = meilleurs_joueurs[0]
                            text = "{} gagne avec {} de {}".format(joueur_gagnant, mains[joueur_gagnant][i][0], mains[joueur_gagnant][i][1])
                            return text
                        
                        if i == 9:
                            text = "égalité"
                            return text


#1. Cas où un seul joueur a une combinaison
mains1 = {
    "j1": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', None], ['Paire', None], ['Carte Haute', 12]],
    "j2": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', None], ['Paire', None], ['Carte Haute', None]]
}

#2. Cas où plusieurs joueurs ont la même combinaison — comparaison par valeur
mains2 = {
    "j1": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', None], ['Paire', 10], ['Carte Haute', 9]],
    "j2": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', None], ['Paire', 12], ['Carte Haute', 8]]
}

#3. Cas “Double Paire” (i=7) — avec un gagnant clair
mains3 = {
    "j1": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', [12,11]], ['Paire', None], ['Carte Haute', 12]],
    "j2": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', [13,10]], ['Paire', None], ['Carte Haute', 13]]
}


#4. Cas “Double Paire” — égalité
mains4 = {
    "j1": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', [12,11]], ['Paire', None], ['Carte Haute', 12]],
    "j2": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', [12,11]], ['Paire', None], ['Carte Haute', 11]]
}


#5. Cas général , test de toutes le combinaisons
mains5 = {
    "j1": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', 6], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', None], ['Paire', None], ['Carte Haute', 12]],
    "j2": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', 6], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', None], ['Paire', None], ['Carte Haute', 13]]
}


#6. Cas double paire pour un seul joueur
mains6 = {
    "j1": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', [12,11]], ['Paire', None], ['Carte Haute', 12]],
    "j2": [['Quinte Flush Royale', None], ['Quinte Flush', None], ['Carre', None], ['Full', None], ['Couleur', None], ['Quinte', None], ['Brelan', None], ['Double Paire', None], ['Paire', None], ['Carte Haute', 12]]
}


#print(comparerMains(mains1)) → ok

#print(comparerMains(mains2)) → pas ok, ligne 64 : text = "{} gagne avec {} de {}".format(joueur_gagnant, mains[joueur_gagnant][0], mains[joueur_gagnant][1]), correction : text = "{} gagne avec {} de {}".format(joueur_gagnant, mains[joueur_gagnant][i][0], mains[joueur_gagnant][i][1])
#print(comparerMains(mains2)) → pas ok car affiche j1 gagne avec Carte Haute de 9 alors que j2 gagne avec Paire de 12, correction ligne 53 à 62 : code long et faux avec boucle for avec recuperation du maximum a la base pour gerer les doublons mais remplacé par deux lignes qui font la même chose
#print(comparerMains(mains2)) → ok

#print(comparerMains(mains3)) → pas ok , meme chose que pour le test 2, on se complique la vie, on remlace ce code par un programme plus simple une boucle pour que ca parcours les deux paire si à la première y'avais egalite
#print(comparerMains(mains3)) → ok

#print(comparerMains(mains4)) → ok

#print(comparerMains(mains5)) → ok

#print(comparerMains(mains6)) → ok