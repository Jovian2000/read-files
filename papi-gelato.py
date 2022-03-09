import yaml

with open("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/read-files/settings.yml", "r") as file:
    docs = yaml.safe_load(file)
    print(type(docs))
    for d,v in docs.items():
        print(d,v)

print("Welkom bij Papi Gelato")
hoorntjes = 0
bakjes = 0
bolletjes = 0
slagroom = 0
totaalPrijsSlagroom = 0
sprinkels = 0
totaalPrijsSprinkels = 0
caramelSausHorn = 0
totaalPrijsCaramelSausHorn = 0
caramelSausBak = 0
totaalPrijsCaramelSausBak = 0
smaakA = 0
smaakC = 0
# smaakM = 0
smaakV = 0

prijsBolletje = 0.95
prijsHoorntje = 1.25
prijsBakje = 0.80
prijsSlagroom = 0.55
prijsSprinkels = 0.30
prijsCaramelsausHorn = 0.60
prijsCaramelsausBak = 0.80

prijsPerLiter = 8.99
btw = 0.06


def particulierOfZakelijk():
    vraagParticulierOfZakelijk = input("Bent u 1) particulier of 2) zakelijk? ")
    if vraagParticulierOfZakelijk == "particulier" or vraagParticulierOfZakelijk == "Particulier" or vraagParticulierOfZakelijk == "1":
        vraagHoeveelheidBolletjes()
    elif vraagParticulierOfZakelijk == "zakelijk" or vraagParticulierOfZakelijk == "Zakelijk" or vraagParticulierOfZakelijk == "2":
        vraagHoeveelLiter()
    else:
        snapIkNiet()
        particulierOfZakelijk()
def vraagHoeveelheidBolletjes():
    aantalBolletjes = input("Hoeveel bolletjes wilt u? ")
    if int(aantalBolletjes) <= 3:
        vraagHornOfBak("", aantalBolletjes)
    elif int(aantalBolletjes) <=8: 
        print("Dan krijgt u van mij een bakje met " + str(aantalBolletjes) + " bolletjes.")
        vraagWelkeSmaak(aantalBolletjes,1,"B")
    elif int(aantalBolletjes) >=9:
        print("Sorry, zulke grote bakken hebben we niet") 
        vraagHoeveelheidBolletjes()
    else:
        snapIkNiet()
        vraagHoeveelheidBolletjes()
def vraagHornOfBak(hornOfBak,bolletjes):
    hornOfBak = input("Wilt u deze " + str(bolletjes) + " bolletjes in (A) een hoorntje of (B) een bakje? ")
    if hornOfBak == "A" or hornOfBak == "a":
        vraagWelkeSmaak(bolletjes,1,"A")
    elif hornOfBak == "B" or hornOfBak == "b":
        vraagWelkeSmaak(bolletjes,1,"B")
    else:
        snapIkNiet()
        vraagHornOfBak("", bolletjes)
def vraagWelkeSmaak(bolletjes,nummerBolletje,hornOfBak):
    while nummerBolletje <= int(bolletjes):
        global smaakA
        global smaakC
        # global smaakM
        global smaakV
        smaak = input("Welke smaak wilt u voor bolletje nummer " + str(nummerBolletje) + "? A) Aardbei, C) Chocolade, V) Vanille: ")
        if smaak == "A" or smaak == "a":
            smaakA = smaakA + 1
            nummerBolletje = nummerBolletje + 1
        elif smaak == "C" or smaak == "c":
            smaakC = smaakC + 1
            nummerBolletje = nummerBolletje + 1
        # elif smaak == "M" or smaak == "m":
        #     smaakM = smaakM + 1
        #     nummerBolletje = nummerBolletje + 1
        elif smaak == "V" or smaak == "v":
            smaakV = smaakV + 1
            nummerBolletje = nummerBolletje + 1
        else:
            snapIkNiet()
    if hornOfBak == "A":
        global hoorntjes
        hoorntjes = hoorntjes + 1
        vraagToppings(bolletjes,"A")

    else:
        global bakjes
        bakjes = bakjes + 1
        vraagToppings(bolletjes,"B")
def vraagToppings(bolletjes,hornOfBak):
    global slagroom
    global totaalPrijsSlagroom
    global sprinkels
    global totaalPrijsSprinkels
    global caramelSausHorn
    global totaalPrijsCaramelSausHorn
    global caramelSausBak
    global totaalPrijsCaramelSausBak
    keuzeToppings = input("Wat voor topping wilt u? A) geen, B) Slagroom, C) Sprinkels of D) Caramel Saus: ")
    if (keuzeToppings == "A" or keuzeToppings == "a") and hornOfBak == "A":
        vraagMeerBestellen(bolletjes,"hoorntje","")
    elif (keuzeToppings == "A" or keuzeToppings == "a") and hornOfBak == "B":
        vraagMeerBestellen(bolletjes,"bakje","")        
    elif (keuzeToppings == "B" or keuzeToppings == "b") and hornOfBak == "A":
        slagroom = slagroom + 1 
        totaalPrijsSlagroom = slagroom * 0.50
        vraagMeerBestellen(bolletjes,"hoorntje","")
    elif (keuzeToppings == "B" or keuzeToppings == "b") and hornOfBak == "B":
        slagroom = slagroom + 1
        totaalPrijsSlagroom = slagroom * 0.50
        vraagMeerBestellen(bolletjes,"bakje","")        
    elif (keuzeToppings == "C" or keuzeToppings == "c") and hornOfBak == "A":
        sprinkels = sprinkels + 1 
        totaalPrijsSprinkels = sprinkels * (int(bolletjes) * 0.30)
        vraagMeerBestellen(bolletjes,"hoorntje","")
    elif (keuzeToppings == "C" or keuzeToppings == "c") and hornOfBak == "B":
        sprinkels = sprinkels + 1 
        totaalPrijsSprinkels = sprinkels * (int(bolletjes) * 0.30)
        vraagMeerBestellen(bolletjes,"bakje","")        
    elif (keuzeToppings == "D" or keuzeToppings == "d") and hornOfBak == "A":
        caramelSausHorn = caramelSausHorn + 1 
        totaalPrijsCaramelSausHorn = caramelSausHorn * 0.60
        vraagMeerBestellen(bolletjes,"hoorntje","")
    elif (keuzeToppings == "D" or keuzeToppings == "d") and hornOfBak == "B":
        caramelSausBak = caramelSausBak + 1 
        totaalPrijsCaramelSausBak = caramelSausBak * 0.90
        vraagMeerBestellen(bolletjes,"bakje","")        
    else:
        snapIkNiet()
        vraagToppings(bolletjes,hornOfBak)
def vraagMeerBestellen(aantalBolletjes,hornOfBak,repeatOrNot):
    print("Hier is uw " + hornOfBak + " met " + str(aantalBolletjes), "bolletjes.")
    repeatOrNot = input("Wilt u nog meer bestellen? (Y/N): ")
    global bolletjes
    bolletjes = bolletjes + int(aantalBolletjes)
    if repeatOrNot == "Y" or repeatOrNot == "y":
        vraagHoeveelheidBolletjes()
    elif repeatOrNot == "N" or repeatOrNot == "n":
        bon()
        print("Bedankt en tot ziens!")        
    else:
        snapIkNiet()
        vraagMeerBestellen(bolletjes,hornOfBak,repeatOrNot)
def bon():
    global smaakA, smaakC, smaakV, bakjes, hoorntjes, slagroom, totaalPrijsSlagroom, sprinkels, totaalPrijsSprinkels, caramelSausHorn, totaalPrijsCaramelSausHorn, caramelSausBak, totaalPrijsCaramelSausBak, prijsBolletje, prijsHoorntje, prijsBakje, prijsSlagroom, prijsSprinkels, prijsCaramelsausHorn, prijsCaramelsausBak   
    print("-----------['Papi Gelato']-----------")
    print("")
    totaalPrijsAarbei = prijsBolletje * smaakA
    totaalPrijsChoco = prijsBolletje * smaakC
    # totaalPrijsMunt = prijsBolletje * smaakM
    totaalPrijsVanille = prijsBolletje * smaakV
    totaalPrijsHoorntjes = prijsHoorntje * hoorntjes
    totaalPrijsBakjes = prijsBakje * bakjes
    totaalPrijs = totaalPrijsAarbei + totaalPrijsChoco + totaalPrijsVanille + totaalPrijsHoorntjes + totaalPrijsBakjes + totaalPrijsSlagroom + totaalPrijsSprinkels + totaalPrijsCaramelSausHorn + totaalPrijsCaramelSausBak
    if int(smaakA) > 0:
        print("Bolletjes(Aardbei)       " + str(smaakA) + " x €" + str('{0:.2f}'.format(prijsBolletje)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsAarbei))) 
    if int(smaakC) > 0:
        print("Bolletjes(Chocolade)     " + str(smaakC) + " x €" + str('{0:.2f}'.format(prijsBolletje)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsChoco))) 
    # if int(smaakM) > 0:
    #     print("Bolletjes(Munt)          " + str(smaakM) + " x €" + str('{0:.2f}'.format(prijsBolletje)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsMunt))) 
    if int(smaakV) > 0:
        print("Bolletjes(Vanille)       " + str(smaakV) + " x €" + str('{0:.2f}'.format(prijsBolletje)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsVanille))) 
    if hoorntjes > 0:
        print("Hoorntjes                " + str(hoorntjes) + " x €" + str('{0:.2f}'.format(prijsHoorntje)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsHoorntjes))) 
    if bakjes > 0:
        print("Bakjes                   " + str(bakjes) +    " x €" + str('{0:.2f}'.format(prijsBakje)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsBakjes)))
    if slagroom > 0:
        print("Slagroom                 " + str(slagroom) +    " x €" + str('{0:.2f}'.format(prijsSlagroom)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsSlagroom)))
    if sprinkels > 0:
        print("Sprinkels                " + str(sprinkels) +    " x €" + str('{0:.2f}'.format(prijsSprinkels)) + " (per bolletje)" + "   = €" + str('{0:.2f}'.format(totaalPrijsSprinkels)))
    if caramelSausHorn > 0:
        print("Caramel saus (hoorntje)  " + str(caramelSausHorn) +    " x €" + str('{0:.2f}'.format(prijsCaramelsausHorn)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsCaramelSausHorn)))
    if caramelSausBak > 0:
        print("Caramel saus (bakje)     " + str(caramelSausBak) +    " x €" + str('{0:.2f}'.format(prijsCaramelsausBak)) + "                  = €" + str('{0:.2f}'.format(totaalPrijsCaramelSausBak)))                
    print    ("                                                    -------- +") 
    print    ("Totaal                                              = €" + str('{0:.2f}'.format(totaalPrijs))) 
def snapIkNiet():
    print("Sorry, dat is geen optie dat is geen optie die we aanbieden")
def vraagHoeveelLiter():
    liter = input("Hoeveel liter ijs wilt u? ")
    smaakZakelijk(liter,1)
def smaakZakelijk(liter,literNummer):
    while literNummer <= int(liter):
        global smaakA
        global smaakC
        # global smaakM
        global smaakV
        if literNummer == 1:
            smaakPerLiter = input("Welke smaak wilt u voor de " + str(literNummer) + "st liter? A) Aardbei, C) Chocolade, V) Vanille: ")
            if smaakPerLiter == "A" or smaakPerLiter == "a":
                smaakA = smaakA + 1
                literNummer = literNummer + 1
            elif smaakPerLiter == "C" or smaakPerLiter == "c":
                smaakC = smaakC + 1
                literNummer = literNummer + 1
            # elif smaakPerLiter == "M" or smaakPerLiter == "m":
            #     smaakM = smaakM + 1
            #     literNummer = literNummer + 1
            elif smaakPerLiter == "V" or smaakPerLiter == "v":
                smaakV = smaakV + 1
                literNummer = literNummer + 1
            else:
                snapIkNiet()
        else:
            smaakPerLiter = input("Welke smaak wilt u voor de " + str(literNummer) + "de liter? A) Aardbei, C) Chocolade, V) Vanille: ")
            if smaakPerLiter == "A" or smaakPerLiter == "a":
                smaakA = smaakA + 1
                literNummer = literNummer + 1
            elif smaakPerLiter == "C" or smaakPerLiter == "c":
                smaakC = smaakC + 1
                literNummer = literNummer + 1
            # elif smaakPerLiter == "M" or smaakPerLiter == "m":
            #     smaakM = smaakM + 1
            #     literNummer = literNummer + 1
            elif smaakPerLiter == "V" or smaakPerLiter == "v":
                smaakV = smaakV + 1
                literNummer = literNummer + 1
            else:
                snapIkNiet()
    bonZakelijk()
def bonZakelijk():
    global smaakA, smaakC, smaakV, btw, prijsPerLiter
    # global smaakM
    
    totaalPrijsLiterA = int(smaakA) * prijsPerLiter
    totaalPrijsLiterC = int(smaakC) * prijsPerLiter
    # totaalPrijsLiterM = int(smaakM) * prijsPerLiter
    totaalPrijsLiterV = int(smaakV) * prijsPerLiter
    totaalPrijs = totaalPrijsLiterA + totaalPrijsLiterC + totaalPrijsLiterV
    btwTotaalPrijs = totaalPrijs * btw
    print("-----------['Papi Gelato']-----------")
    print("")
    if smaakA > 0:
        print("Liter(Aardbei)       " + str(smaakA) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterA)))
    if smaakC > 0:     
        print("Liter(Chocolade)     " + str(smaakC) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterC)))
    # if smaakM > 0:
    #     print("Liter(Munt)          " + str(smaakM) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterM)))
    if smaakV > 0:
        print("Liter(Vanille)       " + str(smaakV) + " x €" + str('{0:.2f}'.format(prijsPerLiter)) + "   = €" + str('{0:.2f}'.format(totaalPrijsLiterV)))
    print("                                 ---------")
    print("Totaal                           = €" + str('{0:.2f}'.format(totaalPrijs)))
    print("Btw (6%)                         = €" + str('{0:.2f}'.format(btwTotaalPrijs))) 
particulierOfZakelijk()





# vraagHoeveelheidBolletjes()



 