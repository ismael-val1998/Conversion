
import conversion_vitesse

vitesse = int( input("Entrer une vitesse : ") )

question = print("Quel convertion souhaitez-vous faire ?? ")

reponse = print("\t 1 : Km/h vers m/s \n\t 2 : m/s vers  Km/h ")

choix = input("reponse : ")

mS = conversion_vitesse.Conversion_Vitesse_mS(vitesse)

kmH = conversion_vitesse.Conversion_Vitesse_kmH(vitesse)

if (int(choix) == 1 ):

    print(str(vitesse) + " km/h vaut : " + str(mS) + " m/s" )

elif (int(choix) == 2 ):

    print(str(vitesse) + " m/s vaut : " + str(kmH) + " Km/h" )

