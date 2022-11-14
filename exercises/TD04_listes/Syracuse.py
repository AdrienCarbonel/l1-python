
def syracuse(n):
    L = []
    """Cette fonction renvoie la liste des valeurs de la suite de n jusqu'à 1

        n ----> int : Premier chiffre de la suite de Syracuse
    """
    while n > 1:
        if n % 2 == 0:
            n //= 2
            L.append(n)
        else:
            n = 3*n + 1
            L.append(n)
    return(L)


def testeConjecture(n_max):
    for n in range(1,n_max+1):
        a = syracuse(n)
    if a[-1] == 1:
        return(True)
    else:
        return("")
           
        
    
    
print(testeConjecture(8))


def tempsVols(n):
    compteur = 0
    s = syracuse(n)
    for i in range(len(s)):
        compteur += 1
        if s[i] == 1:
            return(compteur)
    else:
        if n == 1:
            return(compteur)

print("Le temps de vol de",3,"est",tempsVols(3))

def tempsVolsListe(n_max):
    P = []
    for i in range(1,n_max+1):
        P.append(tempsVols(i))
    return(P)

print(tempsVolsListe(10))



    









