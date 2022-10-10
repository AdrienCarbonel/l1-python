L = []
def syracuse(n):
    """Cette fonction renvoie la liste des valeurs de la suite de n jusqu'à 1

        n ----> int : Premier chiffre de la suite de Syracuse
    """
    L.append(n)
    while n > 1:
      if n % 2 == 0:
        n //= 2
        L.append(n)
      else:
        n = 3*n + 1
        L.append(n)
    return(L)


def tempsVol(n):
    return(len(syracuse(n)))


A = []
def tempsVolListe(n_max):
    for n in range(1,n_max+1):
        A.append(tempsVol(n))
    return(A)
print(tempsVolListe(8))

        

