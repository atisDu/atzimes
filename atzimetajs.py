import json

prieksmeti = ["Matemātika", "Latviešu valoda", "Sports", "Programmēšana", "Mongoļu grozu pīšanas māksla"]
atzimes = [[1, 2, 3, 4, 5],[4, 5, 8, 9],[3, 4, 6, 7],[6,3,2,9,10],[10,10,10,10,10]]

kopums = {}
for prieksas in prieksmeti:
    for atskaites in atzimes: #pievieno visu sarakstu datus vārdnīcai
        kopums[prieksas] = atskaites
        atzimes.remove(atskaites)
        break

def videjais(lst): 
    return sum(lst) / len(lst)  #aprēķina vidējo vērtību katram atzīmju kopumam

def rakstit():
    global vards
    global prieksmeti  #norāda globālo mainīto izmantošanu
    global atzimes 
    with open(f'atzimes_{vards}.json', 'a', encoding='utf-8') as f: #atver json failu ar lietotāja ievadīto vārdu
        prieksmetu_skaits = int(input("Ievadiet priekšmetu skaitu: ")) 
        for i in range (0, prieksmetu_skaits): 
            prieksmets = input("Ievadi %r. priekšmeta nosaukumu: " % (i+1)) #ļauj ievadīt priekšmeta nosaukumu tik reizes, cik lietotājs ievadījis priekšmetu skaitu
            atzime = input("Ievadi %r. prieksmeta atzīmes, atdalot tās ar komatu (1, 2, 3): " % (i+1)).split(', ') #atdala atzīmes, katru kā int
            #Ievada kopuma vardnīcā
            kopums[prieksmets] = atzime
        #Ievada vārdnīcu json failā, pārveidojot to par JS objektu
        json.dump(kopums, f)
 
def parrakstit():
    global vards  #atver failu ar "w", izdzēšot visus bijušos datus
    with open(f'atzimes_{vards}.json', 'w', encoding='utf-8') as f:
        kopums = {}
        prieksmetu_skaits = int(input("Ievadiet priekšmetu skaitu: ")) 
        for i in range (0, prieksmetu_skaits): 
            prieksmets = input("Ievadi %r. priekšmeta nosaukumu: " % (i+1)) #ļauj ievadīt priekšmeta nosaukumu tik reizes, cik lietotājs ievadījis priekšmetu skaitu
            atzime = input("Ievadi %r. prieksmeta atzīmes, atdalot tās ar komatu (1, 2, 3): " % (i+1)).split(', ') #atdala atzīmes, katru kā int
            #Ievada kopuma vardnīcā
            kopums[prieksmets] = atzime
        json.dump(kopums, f)

def ielasit():
    global vards
    with open(f'atzimes_{vards}.json', 'r', encoding='utf-8') as f:
        kopums = json.load(f)
        
        
#3.1 (Atis) Pabeigts
def ka_iegut_videjo():
    print("----------\nAtzīmes:\n")
    for i in range(int(len(prieksmeti))):
        #videja = videjais(atzimes[i])
        print("%r)%r (vid. %r)" % (i,prieksmeti[i], videjais(atzimes[i])))
    print("----------")
    prieks_izvele = int(input("Kurā priekšmetā vēlies labot vidējo? (nr. pēc kārtas): "))
    min_pec_kartas = atzimes[i].index(min(atzimes[i])) 
    
    print("Tu vari izlabot vidējo atzīmi priekšmetā: %r,\nja tu izlabo %r. atzīmi uz:" % (prieksmeti[prieks_izvele], min_pec_kartas + 1))
    print("1|2|3|4|5|6|7|8|9|10")
    print("vid. (mainīsies uz):")
    for i in range (1, 10):
        atzimes[min_pec_kartas] = i
        print("%r" % videjais(atzimes[prieks_izvele]),sep="|")
    galvenais()
    
#3.2 (atis) Pabeigts
def ka_ietekme_videjo():
    print("Priekšmeti:\n")
    for i in range(len(prieksmeti)):
        #videja = videjais(atzimes[i])
        print("%r)%r" % (i,prieksmeti[i]))
    prieks_izvele = int(input("Ievadi priekšmeta nr. (pēc kartas), kura atzīmi vēlies analizēt: "))
    print("----------")
    print("Atzīmes %r: %r" % (prieksmeti[prieks_izvele], atzimes[prieks_izvele]))
    kuru_atzimi = int(input("ievadi atzīmes nr. (pēc kārtas), kuru vēlies analizēt: "))
    print("Ja %r. atzīmi labotu uz:\n1|2|3|4|5|6|7|8|9|10,\ntad vidējā atzīmi būtu:")
    for i in range (1, 10):
        atzimes[kuru_atzimi] = i
        print("%r" % videjais(atzimes[prieks_izvele]),sep="|")

def prognoze():
    try:
        print(f"Priekšmeti:\n1){prieksmeti[0]}\n2){prieksmeti[1]}\n3){prieksmeti[2]} \n3){prieksmeti[2]} \n4){prieksmeti[3]}")
        prieksmeta_numurs = int(input("Ievadi priekšmeta nr. (pēc kārtas), kura atzīmi vēlies analizēt:")) 
        if prieksmeta_numurs == 1: # ja lietotājs ievada 1 tad 
            print(f"Atzīmes {prieksmeti[0]} : {atzimes[0]}")
            print('Ja iegūst \n1|2|3|4|5|6|7|8|9|10\n tad vidējā atzīmi būtu: ')
            

            print('Kopējā vidējā atzīme:')
            
        elif prieksmeta_numurs == 2:
            print(f"Atzīmes {prieksmeti[1]}: {atzimes[1]}")  
        elif prieksmeta_numurs == 3:
            print(f"Atzīmes {prieksmeti[2]}: {atzimes[2]}")
        elif prieksmeta_numurs == 4:
            print(f"Atzīmes {prieksmeti[3]}: {atzimes[3]}")
    except ValueError:
        print('Nepareiza datu ievade') 


def galvenais():
        print("**********************************") #sveiciens
        print ("Sveicināti esat, filozofi un mācoņi, šai programmā lieliskajā. \nŠajā aparātā jūs varat ievadīt savus zināšanu skaitļu mērus un analizēt tos.")
        print("**********************************")
        global vards
        izvele = input("Vai vēlies ievadīt datus no jauna, vai ielasīt no faila? (jauns/ielasit):")
        if izvele == "jauns":
            vards = input("Ievadiet savu vārdu:")
            rakstit() # izsauc funkciju  
        elif izvele == "ielasit": 
            vards = input("Ievadiet savu vārdu:")
            ielasit()
        print("1 : Par cik jāuzlabo zemākā atzīme, lai iegūtu vēlamo vidējo vērtējumu? \n2 : Kā noteiktā atzīme ietekmē vidējo atzīmi priekšmetā un kopumā? \n3 : Ievadīt jaunus datus, papildinot iepriekšējos. \n4 : Pārrakstīt visus datus, izdzēšot vecos.\n“iziet” : Beigt programmas darbību (“iziet” var ievadīt visas programmas laikā)\n—--------")
        opcijas = int(input("Kuru darbību vēlaties veikt?:"))
        if opcijas == '1':
            ka_iegut_videjo()
        elif opcijas == '2':
            print("")
            #prognoze()
        elif opcijas == '3':
            print()
        elif opcijas == '4':
            print("----------\nAtzīmes:\n")
            for i in range(int(len(prieksmeti))):
                print("%r)%r (vid. %r)" % (i,prieksmeti[i], videjais(atzimes[i])))
            vai = input("Vai vēlaties pārrakstīt visus datus? (ja/ne):  ")
            if vai == "ja":
                print("Notiek datu dzēšana. . .")
                print("Dati dzēsti.")
                vards = input("Ievadiet savu vārdu:")
                parrakstit()
        elif opcijas == "iziet":
            exit() #beidz programmu
galvenais()