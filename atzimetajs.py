import json
import ast

#Paraugvērtības
prieksmeti = ["Matemātika", "Latviešu valoda", "Sports", "Programmēšana", "Mongoļu grozu pīšanas māksla"]
atzimes = [[1, 2, 3, 4, 5],[4, 5, 8, 9],[3, 4, 6, 7],[6,3,2,9,10],[10,10,10,10,10]]

kopums = {}
for prieksas in prieksmeti:
    for atskaites in atzimes: #pievieno visu sarakstu datus vārdnīcai
        kopums[prieksas] = atskaites
        atzimes.remove(atskaites)
        break

def videjais(lst): 
    return sum(lst) / int(len(lst))  #aprēķina vidējo vērtību katram atzīmju kopumam

def rakstit(vards):
    global prieksmeti  #norāda globālo mainīto izmantošanu
    global atzimes 
    global kopums
    with open(f'{vards}_atzimes.json', 'a', encoding='utf-8') as f: #atver .json failu ar lietotāja ievadīto vārdu
        kopums = {}
        prieksmetu_skaits = int(input("Ievadiet priekšmetu skaitu: ")) 
         #Izdzēš paraugu
        prieksmeti = []
        atzimes = []
        for i in range (0, prieksmetu_skaits): 
            prieksmets = input("Ievadi %r. priekšmeta nosaukumu: " % (i+1)) #ļauj ievadīt priekšmeta nosaukumu tik reizes, cik lietotājs ievadījis priekšmetu skaitu
            atzime = input("Ievadi %r. prieksmeta atzīmes, atdalot tās ar komatu un atstarpi(1, 2, 3): " % (i+1)).split(', ') #atdala atzīmes, katru kā int
            #Ievada kopuma vardnīcā
            kopums[prieksmets] = atzime
            #Pievieno listiem jaunos datus
            prieksmeti.append(prieksmets)
            atzimes.append(atzime)

        #Ievada vārdnīcu json failā, pārveidojot to par JS objektu
        #print("Kopums ir %r" % (kopums))
        #print("Kopuma tziimes ir %r" % (kopums[prieksmets]))
        json.dump(kopums, f)
        print("-----------")
 
def parrakstit(vards):  #atver failu ar "w", izdzēšot visus bijušos datus
    global prieksmeti  #norāda globālo mainīto izmantošanu
    global atzimes
    global kopums 
    with open(f'{vards}_atzimes.json', 'w', encoding='utf-8') as f:
        kopums = {}
        #Izdzēšam iepriekšējo
        prieksmeti = []
        atzimes = []
        prieksmetu_skaits = int(input("Ievadiet priekšmetu skaitu: ")) 
        for i in range (0, prieksmetu_skaits): 
            prieksmets = input("Ievadi %r. priekšmeta nosaukumu: " % (i+1)) #ļauj ievadīt priekšmeta nosaukumu tik reizes, cik lietotājs ievadījis priekšmetu skaitu
            atzime = input("Ievadi %r. prieksmeta atzīmes, atdalot tās ar komatu un atstarpi(1, 2, 3): " % (i+1)).split(', ') #atdala atzīmes, katru kā int
            #Ievada kopuma vardnīcā
            kopums[prieksmets] = atzime
            #Pievieno listiem jaunos datus
            prieksmeti.append(prieksmets)
            atzimes.append(atzime)
        #Ierakst\ json failā
        json.dump(kopums, f)

def ielasit(vards):
    global kopums
    global prieksmeti  #norāda globālo mainīto izmantošanu
    global atzimes
    try:
        with open(f'{vards}_atzimes.json', 'r', encoding='utf-8') as f:
            
            kopums = {}

            #Iemaucu kopuma vārdnīcā
            kopums = json.load(f)

            #notīra 2d listus
            prieksmeti = []
            atzimes = []
            atzimes_nelab = []
            #Pretkukaiņošanas darbība (debug)
            print(kopums)        
            
            for key in kopums.keys():
                prieksmeti.append(key)
            for value in kopums.values():
                atzimes_nelab.append(value)

            

            for i in atzimes_nelab: 
                i = [int(x) for x in i]
                print("I, jeb apakškopa %r " % (i))
                atzimes.append(i)
            print("---------------")
            print("Atzīmes ielasītas!")
            print("---------------")
    except FileNotFoundError:
        print("Fails nav atrasts. Mēģini vēlreiz.")

        
#3.1 (Atis) Pabeigts
def ka_iegut_videjo():
    print("----------\nAtzīmes:\n")
    for i in range(int(len(prieksmeti))): #parāda katru priekšmetu un tā vidējo atzīmi
        #videja = videjais(atzimes[i])
        print("%r)%r (vid. %r)" % (i+1,prieksmeti[i], videjais(atzimes[i])))
    print("----------")
    prieks_izvele = int(input("Ievadi priekšmeta nr. (pēc kartas), kura atzīmi vēlies analizēt: ")) - 1
    #Minimālās vērtības indekss atzīmju sarakstā
    #min_pec_kartas = atzimes[i].index(min(atzimes[i])) 
    
    temp = min(atzimes)
    min_pec_kartas_kopa = [i for i, j in enumerate(atzimes) if j == temp]
    min_pec_kartas = min_pec_kartas_kopa[0]

    print("Tu vari izlabot vidējo atzīmi priekšmetā: %r,\nja tu izlabo %r. atzīmi uz:" % (prieksmeti[prieks_izvele], min_pec_kartas + 1)) #automātiski atrod zemāko atzīmi
    print("1|2|3|4|5|6|7|8|9|10")
    print("vid. (mainīsies uz):")
    for i in range (1, 10):
        atzimes[min_pec_kartas] = i #parāda visus iespējamos vērtējumus, ja to izlabo
        print("%r" % videjais(atzimes[prieks_izvele]),sep="|")
     # izsauc funkciju
    
#3.2 (atis) Pabeigts
def ka_ietekme_videjo():
    print("Priekšmeti:\n")
    for i in range(len(prieksmeti)): 
        #videja = videjais(atzimes[i]) 
        print("%r)%r" % (i,prieksmeti[i]))
    prieks_izvele = int(input("Ievadi priekšmeta nr. (pēc kartas), kura atzīmi vēlies analizēt: "))
    print("----------")
    print("Atzīmes %r: %r" % (prieksmeti[prieks_izvele], atzimes[prieks_izvele]))
    kuru_atzimi = int(input("Ievadi atzīmes nr. (pēc kārtas), kuru vēlies analizēt: ")) #nevis nosaka zemāko kā iepriekš, bet ļauj lietotājam izvēlēties, kuru atzīmi labot
    print("Ja %r. atzīmi labotu uz:\n1|2|3|4|5|6|7|8|9|10,\ntad vidējā atzīmi būtu:")
    for i in range (1, 10):
        atzimes[kuru_atzimi] = i 
        print("%r" % videjais(atzimes[prieks_izvele]),sep="|") #parāda visus iespējamos vērtējumus, ja to izlabo
'''
def prognoze():
    try:
        print(f"Priekšmeti:\n1){prieksmeti[0]}\n2){prieksmeti[1]}\n3){prieksmeti[2]} \n3){prieksmeti[2]} \n4){prieksmeti[3]}")
        prieksmeta_numurs = int(input("Ievadi priekšmeta nr. (pēc kārtas), kura atzīmi vēlies analizēt:")) 
        if prieksmeta_numurs == 1: # ja lietotājs ievada 1 tad analizē vidējā izmaiņas atkarībā no prognozētas nākotnes atzīmes
            print(f"Atzīmes {prieksmeti[0]} : {atzimes[0]}") 
            print('Ja iegūst \n1|2|3|4|5|6|7|8|9|10\n') 
            print("vid. (mainīsies uz):")
            for i in range (1, 10):
                atzimes[0] = i
                print(videjais(atzimes[prieksmeti[0]]),sep="|")

            print('Kopējā vidējā atzīme:')
            
        elif prieksmeta_numurs == 2:
            print(f"Atzīmes {prieksmeti[1]}: {atzimes[1]}")  
        elif prieksmeta_numurs == 3:
            print(f"Atzīmes {prieksmeti[2]}: {atzimes[2]}")
        elif prieksmeta_numurs == 4:
            print(f"Atzīmes {prieksmeti[3]}: {atzimes[3]}")
    except ValueError:
        print('Nepareiza datu ievade') 
'''

def galvenais():
        print("**********************************") #sveiciens
        print ("Sveicināti esat, filozofi un mācoņi, šai programmā lieliskajā. \nŠajā aparātā jūs varat ievadīt savus zināšanu skaitļu mērus un analizēt tos.")
        print("**********************************")
        
        izvele = input("Vai vēlies ievadīt datus no jauna, vai ielasīt no faila? (jauns/ielasit):")
        while izvele != "jauns" and izvele != "ielasit":
            print("Šāda vērtība neder! Ieraksti vai nu \"jauns\", \"ielasit\", vai \"iziet\".")
            izvele = input("Vai vēlies ievadīt datus no jauna, vai ielasīt no faila? (jauns/ielasit):")
        if izvele == "iziet" or izvele == "stop":
            print("Programma beidz darbību. Visu labu!")
            exit()
         #ļauj lietotājam veikt izvēli starp esošiem un jauniem datiem
        vards = input("Ievadiet savu vārdu: ")
        if izvele == "jauns":
            rakstit(vards) # izsauc funkciju  
        elif izvele == "ielasit": 
            ielasit(vards) # izsauc funkciju
        print("1 : Par cik jāuzlabo zemākā atzīme, lai iegūtu vēlamo vidējo vērtējumu? \n2 : Kā noteiktā atzīme ietekmē vidējo atzīmi priekšmetā un kopumā? \n3 : Ievadīt jaunus datus, papildinot iepriekšējos. \n4 : Pārrakstīt visus datus, izdzēšot vecos.\n“iziet” : Beigt programmas darbību (“iziet” var ievadīt visas programmas laikā)\n—--------")
        opcijas = input("Kuru darbību vēlaties veikt?:") #izvēlne, lieotājs var ievadīt skaitli no 1-4 vai "iziet"
        if opcijas == '1':
            ka_iegut_videjo() # izsauc funkciju
        elif opcijas == '2':
            print("")
            ka_ietekme_videjo()
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
                parrakstit(vards) # izsauc pārrakstīšanas funkciju
        elif opcijas == "iziet":
            print("Programma beidz darbību. Visu labu!") #ziņojot lietotājam, programma beidz darbu
            exit() #beidz programmu
galvenais()