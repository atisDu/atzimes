import numpy as np
import json

prieksmeti = ["Matemātika", "Latviešu valoda", "Sports", "Programmēšana", "Mongoļu grozu pīšanas māksla"]
atzimes = [[1, 2, 3, 4, 5],[4, 5, 8, 9],[3, 4, 6, 7],[6,3,2,9,10],[10,10,10,10,10]]

kopums = {}
for prieksas in prieksmeti:
    for atskaites in atzimes:
        kopums[prieksas] = atskaites
        atzimes.remove(atskaites)
        break



def Videjais(lst): 
    return sum(lst) / len(lst) 

def rakstit():
    global vards
    global prieksmeti 
    global atzimes 
    with open(f'atzimes_{vards}.json', 'a', encoding='utf-8') as f: #atver json failu ar lietotāja ievadīto vārdu
        for index in range(len(prieksmeti)):
            json.dump(str(prieksmeti[index]) + "/n" + str(atzimes[index]) + "\n", f) #json.dump lai rakstitu datus json faila
        # vajag izdomat, ka to rakstit un lasit ta, lai butu sasaistiti divi list: prieksmeti un atzimes

def parrakstit():
    global vards  #atver failu ar "w", izdzēšot visus bijušos datus
    with open(f'atzimes_{vards}.json', 'w', encoding='utf-8') as f:
        json.dump(f)

#3.1 (Atis) Pabeigts
def ka_iegut_videjo():
    
    print("----------\nAtzīmes:\n")
    for i in range(len(prieksmeti)):
        #videja = Videjais(atzimes[i])
        print("%r)%r (vid. %r)" % (i,prieksmeti[i], Videjais(atzimes[i])))
    print("----------")
    prieks_izvele = int(input("Kurā priekšmetā vēlies labot vidējo? (nr. pēc kārtas): "))
    min_cipars = min(atzimes[i])
    min_pec_kartas = atzimes[i].index(min(atzimes[i])) 
    
    print("Tu vari izlabot vidējo atzīmi priekšmetā: %r,\nja tu izlabo %r. atzīmi uz:" % (prieksmeti[prieks_izvele], min_pec_kartas + 1))
    print("1|2|3|4|5|6|7|8|9|10")
    print("vid. (mainīsies uz):")
    for i in range (1, 10):
        atzimes[min_pec_kartas] = i
        print("%r" % Videjais(atzimes[prieks_izvele]),sep="|")
    izvelne()
    
#3.2 (atis) Pabeigts
def ka_ietekme_videjo():
    print("Priekšmeti:\n")
    for i in range(len(prieksmeti)):
        #videja = Videjais(atzimes[i])
        print("%r)%r" % (i,prieksmeti[i]))
    prieks_izvele = int(input("Ievadi priekšmeta nr. (pēc kartas), kura atzīmi vēlies analizēt: "))
    print("----------")
    print("Atzīmes %r: %r" % (prieksmeti[prieks_izvele], atzimes[prieks_izvele]))
    kuru_atzimi = int(input("ievadi atzīmes nr. (pēc kārtas), kuru vēlies analizēt: "))
    print("Ja %r. atzīmi labotu uz:\n1|2|3|4|5|6|7|8|9|10,\ntad vidējā atzīmi būtu:")
    for i in range (1, 10):
        atzimes[kuru_atzimi] = i
        print("%r" % Videjais(atzimes[prieks_izvele]),sep="|")

ka_iegut_videjo()

''''
        

mahinacija()
'''
'''
def prognoze():
    try:
        print(f"Priekšmeti: {prieksmeti}")
        prieksmeta_numurs = int(input("Ievadi priekšmeta nr. (pēc kārtas), kura atzīmi vēlies analizēt:"))
        if prieksmeta_numurs == 1:
            print(f"Atzīmes atlasītajā priekšmetā: {atzimes[0]}")
            jauna_atzime 
        elif prieksmeta_numurs == 2:
            print(f"Atzīmes atlasītajā priekšmetā: {atzimes[1]}")
        elif prieksmeta_numurs == 3:
            print(f"Atzīmes atlasītajā priekšmetā: {atzimes[2]}")
        elif prieksmeta_numurs == 4:
            print(f"Atzīmes atlasītajā priekšmetā: {atzimes[3]}")
    except ValueError:
        print('Nepareiza datu ievade')
            
'''    


def galvenais():
    print("\n**********************************")
    print ("Sveicināti esat, filozofi un mācoņi, šai programmā lieliskajā. Šajā aparātā jūs varat ievadīt savus zināšanu skaitļu mērus un analizēt tos.")
    print("\n**********************************")
    izvele = ("Vai vēlies ievadīt datus no jauna, vai ielasīt no faila? (jauns/ielasit): (str tips)")
 
    izvelne = ("Izvēlne 1 : Par cik jāuzlabo zemākā atzīme, lai iegūtu vēlamo vidējo vērtējumu \n 2 : Kā noteiktā atzīme ietekmē vidējo atzīmi priekšmetā un kopumā. \n 3 : Ievadīt jaunus datus, papildinot iepriekšējos. \n4 : Pārrakstīt visus datus.\n“iziet” : Beigt programmas darbību (“iziet” var ievadīt jebkurā brīdī)")
    opcijas = int(input("Izvēlies kādu no dotajām opcijām:"))
    if opcijas == '1':
        ka_iegut_videjo()
    elif opcijas == '2':
        prognoze()
    elif opcijas == '3':
            

    
def izvelne():
    print("")
