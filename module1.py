
def kop(ostud:list, hinnad:list):

    n=int(input("Kui palju tooteid soovite osta? "))
    for i in range(n):
        print()
        log=input("Sisesta toote nimi: ")
        print()
        j=float(input("Sisesta toote hind: "))
        ostud.append(log)
        hinnad.append(j)
     
    return ostud,hinnad


def reost(ostud:list, hinnad:list):

    ostetud=[]
    spin1= input("Millist eset nimekirjast soovite osta?: ")
    

    if spin1 in ostud:
        ind = ostud.index(spin1)
        ostetud.append(ostud.pop(ind))
        hinnad.pop(ind)
        print(f"toode {spin1} ostetud!")
    else:
         print(f"Seda toodet ei leitud ostunimekirjast")
                
    if ostetud:
        print("\n tsekk")
        t=0
        for i in range(len(ostetud)):
            print(f"{ostetud[i]}")
            t+=hinnad[i]
        print(f"\n Kokku: {t}")







def por(ostud:list, hinnad:list):

    spin2 = sorted(ostud)
            
    for item in spin2:
        index = ostud.index(item)
        price = hinnad[index]

        print(f"{item}: {price}")



def sortm(ostud:list, hinnad:list):
   

    maxh = max(hinnad)
    ind = hinnad.index(maxh)
    ostu = ostud[ind]

    print(f"Kõige kallim ese: {ostu}, hind: {maxh}")


def sortmi(ostud:list, hinnad:list):
 

    minh = min(hinnad)
    ind = hinnad.index(minh)
    ostu = ostud[ind]

    print(f"Odavaim toode: {ostu}, hind: {minh}")



def find(ostud:list, hinnad:list):

   spin3 = input("Millist toodet soovite leida? ")
            
   if spin3 in ostud:
      ind = ostud.index(spin3)
      hinna = hinnad[ind]

      print(f"{spin3}: {hinna}")
   else:
      print(f"{spin3} ostunimekirjast ei leitud")

def omav(ostud:list, hinnad:list):  
 
    spin4=[x for x in hinnad if hinnad.count(x)>1 ]
    spin4=list(set(spin4))
    for hin in spin4:
        n=hinnad.count(hin)
        f=-1
        print(f"{hin}")
        for j in range(n):
            f=hinnad.index(hin,f+1)
            log=ostud[f]
            print(log)
