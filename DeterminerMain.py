
class DeterminerMains():
    
    def __init__(self,partie,joueur):
        self.joueur = joueur
        self.partie = partie
        
        #cartes du joueurs, type : list [signe,valeur]
        self.cartes = [carte.getCarte() for carte in self.joueur.cartes] + [carte.getCarte() for carte in self.partie.manche.board.board]
        
        #deux dictionnaires qui comptent le nombre de signe de chacun des signes, type : {coeur:0,...,pique:0} et même chose pour les valeurs {Roi:0,...,As:0}
        self.nbCartesParCouleur = {couleur:0 for couleur in self.partie.manche.paquet.couleurs}
        self.nbCartesParValeur = {valeur:0 for valeur in self.partie.manche.paquet.valeurs}
        for carte in self.cartes:
            self.nbCartesParCouleur[carte[0]]+=1
            self.nbCartesParValeur[carte[1]]+=1
        
        #contient le prenom du joueur ainsi que toutes ces combinaisons de la forme [nom_combinaison,infor_sur_la_combinaison]
        self.jeu = [self.joueur.nom]
        
        print(self.cartes) 
   
        self.QuinteFlushRoyale() 
        self.QuinteFlush()
        self.Carre()
        self.Full()
        self.Couleur()
        self.Quinte()
        self.Couleur()
        self.Brelan()
        self.DoublePaire()
        self.Paire()
        self.carteHaute()
        
        print(self.jeu)
            

    '''
    COMBINAISONS
    '''
    def QuinteFlushRoyale(self):
        '''
        renvoi un boolen si la quinte flush royale existe (couleur + suite dans la couleur avec les cartes les plus hautes du jeu (10,V,D,R,As)
        '''
        couleur_royale=None
        #1 etape chercher si y a bien une couleur 
        if self.Couleur()!=[]:
            self.jeu.pop(-1)
            for k,v in self.nbCartesParCouleur.items():
                if v>4:
                    #couleur existante
                    couleur_royale=k

                    #2e etape on cherche a savoir si il ya bien une suite haute
                    cartes_requises_royale = [['10', couleur_royale], ['Valet', couleur_royale], ['Dame', couleur_royale], ['Roi', couleur_royale],['As', couleur_royale]]
                    #on regarde si les cartes requise se trouvent dans le jeu dun joueur
                    if all(carte in self.cartes for carte in cartes_requises_royale):
                        self.jeu.append(["QuinteFlushRoyale",couleur_royale])
                
    
    def QuinteFlush(self):
        '''
        renvoi un boolen si une quinte flush existe (couleur + suite dans la couleur)
        '''
        #1 etape chercher si y a bien une couleur 
        if self.Couleur()!=[]:
            self.jeu.pop(-1) #on viens d'appeller couleur donc ca ajoute couleur dans la lste mais pas au bon endroit
            #2 etape on cherche si il ya suite dans cette couleur
            if self.Quinte()==False:
                self.jeu.pop(-1)
                self.jeu.append(["QuinteFlush",None])
            

    def Carre(self):
        '''
        renvoi la valeur de la carte du carrée si un carré existe
        '''
        for k,v in self.nbCartesParValeur.items():
            if v==4:
                self.jeu.append(["Carre",k])


    def Full(self):
        '''
        renvoi la valeur de la carte qui fait brelan si brelan il y a (Full = Brelan + Paire)
        '''
        brelan_max = self.Brelan() #on stock la valeur du brelan si il y'en a une 
        if self.Paire()!=0:
            self.jeu.pop(-1) #on supprime la paire
            if brelan_max!=None:
                self.jeu.pop(-1) #on supprime le  brelan
                self.jeu.append(["Full",brelan_max])
        


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
                self.jeu.append(["Couleur", cartesCouleur])
        return cartesCouleur
            

    def Quinte(self):
        '''
        renvoi la carte la plus haute de la suite si suite il y a
        '''
        valeur_cartes = [self.valeurCarte(carte[1]) for carte in self.cartes]
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
                self.jeu.append(["Quinte", maxsuite[0]])
                return maxsuite[0]
        return False


    def Brelan(self):
        '''
        renvoi la valeur du brelan si il existe
        '''
        brelanMax=None
        for k,v in self.nbCartesParValeur.items():
            if v==3:
                brelanMax=k
        if brelanMax!=None:
            self.jeu.append(["Brelan", brelanMax])
            return brelanMax


    def DoublePaire(self):
        '''
        renvoi la paire la plus haute des deux si une double paires existe
        '''
        paires=[]
        for k,v in self.nbCartesParValeur.items():
            if v==2:
                if paires==2:
                    paires.pop(0) #on supprime la pire la plus petite si il existe déjà deux
                    paires.append(self.valeurCarte(k))
                else:
                    paires.append(self.valeurCarte(k))
        if len(paires)==2:
            self.jeu.append(["DoublePaire", paires])


    def Paire(self):
        '''
        renvoi la valeur de la paire maximum si elle existe
        '''
        paireMax = 0
        for k,v in self.nbCartesParValeur.items():
            if v==2:
                if self.valeurCarte(k)>paireMax:
                    paireMax=self.valeurCarte(k)
        if paireMax!=0:
            self.jeu.append(["Paire", paireMax])
        return paireMax
    
    
    def carteHaute(self):
        '''
        renvoi la meilleur carte de la main du joueur
        '''
        valeur_carte_max = 0
        for carte in self.cartes:
            if self.valeurCarte(carte[1])> valeur_carte_max:
                valeur_carte_max = self.valeurCarte(carte[1])
        self.jeu.append(["CarteHaute",valeur_carte_max])

    
    def valeurCarte(self,valeur_carte):
        '''
        transforme une carte en valeur int
        '''
        match valeur_carte:
            case 'Valet':
                return 11
            case 'Dame':
                return 12
            case 'Roi':
                return 13
            case 'As':
                return 14
            case _:
                return int(valeur_carte)
            
    
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