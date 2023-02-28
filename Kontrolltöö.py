from module1 import *
#Harjutus 4 Pood


ostud=[]
hinnad=[]
ostetud=[]

print("Kuskil veebipoes")
print()

spin1=kop(ostud,hinnad)
print(ostud)
print(hinnad)
print()

while True:
        print("Выбирете:")
        print("1 - Kustutage ostetud kaup loendist ja lisage loendisse ostetud[] ja koostage kviitung ")#+
        print("2 - Ostude ja nende hindade loendi kuvamine tähestikulises järjekorras")#+
        print("3 - Otsige üles kõige kallim kaup")#+
        print("4 - Leia odavaim kaup")#+
        print("5 - Leidke soovitud kauba hind")#+
        print("6 - Uuri, kas on sama hinnaga toodet, leia mitu sellist toodet ja kuva andmed ekraanile.")#+
        print("7 - Lõpetage programm")#+

        tegevust = int(input("Valige toiming: "))
        
        if tegevust==1:
           print("Eemaldage ostetud kaup loendist ja lisage see ostunimekirja")
           spin2=reost(ostud,hinnad)
           print()


        elif tegevust==2:
             print("Ostude ja nende hindade loendi kuvamine tähestikulises järjekorras")
             print()
             spin3=por(ostud,hinnad)
             print()


        elif tegevust==3:
             print("Otsige üles kõige kallim kaup")
             print()
             spin4=sortm(ostud,hinnad)
             print()

        elif tegevust==4:
             print("Leia odavaim kaup")
             print()
             spin5=sortmi(ostud,hinnad)
             print()

        elif tegevust==5:
             print("Leidke soovitud kauba hind")
             print()
             spin6=find(ostud,hinnad)
             print()

        elif tegevust==6:
             print("Uuri, kas on sama hinnaga toodet, leia mitu sellist toodet ja kuva andmed ekraanile.")
             print()
             spin7=omav(ostud,hinnad)
             print()
        else:
             tegevust==7
             print("Lõpetage programm") 
             break
