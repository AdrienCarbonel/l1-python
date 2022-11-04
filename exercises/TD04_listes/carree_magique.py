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
    for k in range(len(carre)-1):
        for j in range(len(carre)-2):
            k -= 1
        somme_2 += carre[k][j-1-k]
        print(k,j)
    if somme_1 == somme_2:
        print(True)
    else:
        print("Les diagonales ne sont pas égales...")
    return("")      
    


        
  
            


print(testDiagonaleEgales(carree_magique))























