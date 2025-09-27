cartes_2 = [['10'], ['Valet'], ['Dame'], ['Roi'],['As']]
cartes_1 = [['10'], ['Valet'], ['Dame'], ['Roi']]
if all(carte in cartes_1 for carte in cartes_2):
    print(True)
else:
    print(False)