def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return(temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3])


  

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    return(seconde // 86400, (seconde // 3600) % 24 , (seconde // 60) % 60 , seconde % 60)

temps = secondeEnTemps(100000)

def afficheTemps(temps):
    """Cette fonction permet d'afficher le temps en Jours , Heures , Minutes et Secondes
       temps ----> Tuple : Le temps à afficher
    """
    if temps[0] > 1:
        print(temps[0], "Jours","",end="")
    elif temps[0] == 0:
        print("",end="")
        
    else:
        print(temps[0], "Jour")
    if temps[1] > 1:
        print(temps[1],"Heures","",end="")
    elif temps[1] == 0:
        print("",end="")
    else:
        print(temps[1],"Heure","",end="")
    if temps[2] > 1:
        print(temps[2], "Minutes","",end="")
    elif temps[2] == 0:
        print("",end="")
    else:
        print(temps[2], "Minute","",end="")
    if temps[3] > 1:
        print(temps[3],"Secondes","",end="")
    elif temps[3] == 0:
        print("",end="")
    else:
        print(temps[3],"Seconde","",end="")
    return("")

j = int(input("Entrez un nombre de jours :"))
h = int(input("Entrez un nombre d'heures :"))
m = int(input("Entrez un nombre de minutes :"))
s = int(input("Entrez un nombre de secondes :"))
def demandeTemps(j,h,m,s):
    """Cette fonction permet de demander à l'utilisateur un temps et elle permet d'afficher si le temps entré par l'utilisateur ets le même que afficheTemps()

    Args:
        t ----> string : Temps entré par l'utilisateur
    """
    t = (j,h,m,s)
    while t != temps:
        if j > 365:
            print("Error")
        if h > 23:
            print("Error")
        if m > 59:
            print("Error")
        if s > 59:
            print("Error")
    if t == afficheTemps(temps):
        print("Félicitations !")
    return(t == temps)


    
    
   
    
    




