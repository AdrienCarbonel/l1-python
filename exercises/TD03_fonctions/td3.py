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
        print(temps[3],"Secondes","")
    elif temps[3] == 0:
        print("",end="")
    else:
        print(temps[3],"Seconde","")
    return("")


def demandeTemps():
    """Cette fonction permet de demander à l'utilisateur un temps et elle permet d'afficher si le temps entré par l'utilisateur ets le même que afficheTemps()

    Args:
        t ----> tuple : Temps entré par l'utilisateur
    """
    j = int(input("Entrez un nombre de jours :"))
    while j >= 366:
        j = int(input("Entrez un nouveau nombre de jours :"))
    h = int(input("Entrez un nombre d'heures :"))
    while h >= 24:
        h = int(input("Entrez un nouveau nombre d'heures :"))
    m = int(input("Entrez un nombre de minutes :"))
    while m >= 60:
        m = int(input("Entrez un nouveau nombre de minutes :"))
    s = int(input("Entrez un nombre de secondes :"))
    while s >= 60:
        s = int(input("Entrez un nouveau nombre de secondes :"))
    t = (j,h,m,s)
    
    return(t)    
    
    
afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    s = (temps1[0] + temps2[0] , temps1[1] + temps2[1] , temps1[2] + temps2[2] , temps1[3] + temps2[3])
    i = 0
    while temps1[3] + temps2[3] >= 60:
        s = (temps1[0] + temps2[0] , temps1[1] + temps2[1] , temps1[2] + temps2[2] + i , 0)
        i += 1
    while temps1[2] + temps2[2] >= 60:
        s = (temps1[0] + temps2[0] , temps1[1] + temps2[1] + i , 0 , temps1[3] + temps2[3])
        i += 1
    while temps1[1] + temps2[1] >= 24:
        s = (temps1[0] + temps2[0] + i , 0, temps1[2] + temps2[2] , temps1[3] + temps2[3])
        i += 1
    return(s)

    

print(sommeTemps((1,2,114,3),(23,9,6,7)))









    
    





