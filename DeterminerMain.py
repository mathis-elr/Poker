
class DeterminerMains():
    
    def __init__(self,partie,joueur):
        self.joueur = joueur
        self.partie = partie
        self.cartes = [carte.getCarte() for carte in self.joueur.cartes] + [carte.getCarte() for carte in self.partie.manche.board.board] #cartes du joueurs, type : list [signe,valeur]
        self.nbCartesParCouleur = {couleur:0 for couleur in self.partie.manche.paquet.couleurs}
        self.nbCartesParValeur = {valeur:0 for valeur in self.partie.manche.paquet.valeurs}
        for carte in self.cartes:
            self.nbCartesParCouleur[carte[0]]+=1
            self.nbCartesParValeur[carte[1]]+=1
            
        self.jeux = {}
        
        print(self.cartes) #ok
        print(self.nbCartesParCouleur) #ok
        print(self.nbCartesParValeur) #ok
            


    def QuinteFlushRoyale(self):
        '''
        renvoi un boolen si la quinte flush royale existe (couleur + suite dans la couleur avec les cartes les plus hautes du jeu (10,V,D,R,As)
        '''
        couleur_royale=None
        #1 etape chercher si y a bien une couleur 
        if self.Couleur()!=None:
            for k,v in self.nbCartesParCouleur.items():
                if v>4:
                    #couleur existante
                    couleur_royale=k

                    #2e etape on cherche a savoir si il ya bien une suite haute
                    cartes_requises_royale = [['10', couleur_royale], ['Valet', couleur_royale], ['Dame', couleur_royale], ['Roi', couleur_royale],['As', couleur_royale]]
                    #on regarde si les cartes requise se trouvent dans le jeu dun joueur
                    if all(carte in self.cartes for carte in cartes_requises_royale):
                        return True
        return False
                
    
    def QuinteFlush(self):
        '''
        renvoi un boolen si une quinte flush existe (couleur + suite dans la couleur)
        '''
        #1 etape chercher si y a bien une couleur 
        cartesCouleur = self.Couleur()
        if cartesCouleur!=None:
            #2 etape on cherche si il ya suite dans cette couleur
            if self.Quinte():
                return True
        return False
            


    def Carre(self):
        '''
        renvoi la valeur de la carte du carrée si un carré existe
        '''
        for k,v in self.nbCartesParValeur.items():
            if v==4:
                return k


    def Full(self):
        '''
        renvoi la valeur de la carte qui fait brelan si brelan il y a
        '''
        #full correspond à avoir une paire ainsi qu'un brelan, on verifie que les deux existent
        if self.Paire()!=0 and self.Brelan()!=None:
            return self.Brelan()


    def Couleur(self):
        '''
        determine si il y a au moins 5 cartes du même signe, si c'est le cas renvoi la liste des valeurs des cartes qui forment la couleur
        '''
        cartesCouleur=[]
        for key,value in self.nbCartesParCouleur.items():
            if value>4:
                for a,b in self.cartes:
                    if b==key:
                        cartesCouleur.append(self.valeurCarte(a))
                cartesCouleur.sort(reverse=True)
                return cartesCouleur
            

    def Quinte(self):
        '''
        renvoi la carte la plus haute de la suite si suite il y a
        '''
        valeur_cartes = [self.valeurCarte(carte[0]) for carte in self.cartes]
        valeur_cartes.sort(reverse=True)
        
        #rajoute un 1 dans la liste des cartes si il y a un As car il peut à la fois valoir 1 et 14 (seulement dans une suite)
        if 14 in valeur_cartes:
            valeur_cartes.insert(len(valeur_cartes)+1,1)
            

        maxsuite=[]
        for i in valeur_cartes:
            #suite maximale trouvé
            if maxsuite==[]:
                maxsuite.append(i)
            #notre liste de cartes est ordonné (decroissant) donc on compare la carte actuelle à la précédente
            elif maxsuite[-1] - 1 == i or maxsuite[-1] == i:
                #en cas de doublon ne le prend pas en compte, ex ['6','7','8','8',9','10'] ici il ya suite et si on prend en compte les doublon avce notre algo, il renverra None (pas de suite)
                if i not in maxsuite:
                    maxsuite.append(i)
            else:
                maxsuite=[i]
            
            #suite maximale trouvé, renvoi de la plus grande valeur de la suite et fin fonction
            if len(maxsuite)==5:
                return maxsuite[0]


    def Brelan(self):
        '''
        renvoi la valeur du brelan si il existe
        '''
        brelanMax=None
        for k,v in self.nbCartesParValeur.items():
            if v==3:
                brelanMax=k
        return brelanMax


    def DoublePaire(self):
        '''
        renvoi la paire la plus haute des deux si une double paires existe
        '''
        paires=[]
        for k,v in self.nbCartesParValeur.items():
            if v==2:
                if paires==2:
                    paires.pop(0)
                    paires.append(k)
                else:
                    paires.append(k)
        return paires[1] if len(paires)==2 else None


    def Paire(self):
        '''
        renvoi la valeur de la paire maximum si elle existe
        '''
        paireMax = 0
        for k,v in self.nbCartesParValeur.items():
            if v==2:
                if self.valeurCarte(k)>paireMax:
                    paireMax=self.valeurCarte(k)
        return paireMax
    
    
    def valeurCarte(self,carte):
        '''
        transforme une carte en valeur int
        '''
        match carte:
            case 'Valet':
                return 11
            case 'Dame':
                return 12
            case 'Roi':
                return 13
            case 'As':
                return 14
            case _:
                return int(carte)