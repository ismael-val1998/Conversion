def Conversion_Vitesse_kmH(vitesse):
    initial_vitesse = vitesse
    final_vitesse = initial_vitesse * 3.6
    float(final_vitesse)
    return final_vitesse

def Conversion_Vitesse_mS(vitesse):
    initial_vitesse = vitesse
    final_vitesse = initial_vitesse / 3.6
    float(final_vitesse)
    return final_vitesse


KmH = Conversion_Vitesse_kmH(15)
print("15 m/S vaut :" + str(KmH) + " km/h")

print("**************************************************")

mS = Conversion_Vitesse_mS(90)
print("90 km/h vaut : " + str(mS) + " m/s")