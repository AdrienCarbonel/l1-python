carree_magique =[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carree_pas_mag = [[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]
def afficheCarre(carre):
    for i in range(len(carre)):
        print("\n")
        for j in range(len(carre)):
            b = carre[i][j]
            print(b ,"", end ="")

    return("")

print(afficheCarre(carree_magique))


def testLigneEgales(carre):
    for i in range(len(carre)-1):
        if sum(carre[i]) == 34:
            print(True)
        else:
            print("Les lignes ne sont pas égales....")
    return("")



def testColonnesEgales(carre):
    for i in range(len(carre)):
        somme = 0
        for j in range(len(carre)):
            somme += carre[j][i]
        if  somme  == 34:
            print(True)
        else:
            print("Les colonnes ne sont pas égales...")
    
    return("")
    



def testDiagonaleEgales(carre):
    somme_1 = 0
    for i in range(len(carre)):
        somme_1 += carre[i][i]
    somme_2 = 0
    for j in range(len(carre)):
        somme_2 += carre[j][3-j]
    if somme_1 == somme_2:
        print("Les diagonales sont égales")
    else:
        print("Les diagonales ne sont pas égales...")
    
    return("")

    




def estMagique(carre):
    if testColonnesEgales(carre) == testLigneEgales(carre) == testDiagonaleEgales(carre):
        return(True)
    else:
        return(False)

def estNormal(carre):
    for i in range(len(carre)):
        for j in range(len(carre)):
            if carre[i] in carre:
                return(True)
            else:
                return("Le carré n'est pas normal...")


carre_normal=[[1,2,3],[4,5,6],[7,8,9]]
print(estNormal(carre_normal))





















