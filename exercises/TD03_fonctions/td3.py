def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return(temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3])

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    return(seconde // 86400, (seconde // 3600) % 24 , (seconde // 60) % 60 , seconde % 60)
print(secondeEnTemps(300000))
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def afficheTemps(temps):
    
   
    
    
afficheTemps((1,0,14,23)) 
