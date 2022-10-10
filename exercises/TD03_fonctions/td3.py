def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return(temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3])

temps = (3,23,1,34)
  

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    return(seconde // 86400, (seconde // 3600) % 24 , (seconde // 60) % 60 , seconde % 60)

temps = secondeEnTemps(100000)

def afficheTemps(temps):
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
        print(temps[2], "Minutes",end="")
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
print(afficheTemps((3,5,5,50)))
    
   
    
    


