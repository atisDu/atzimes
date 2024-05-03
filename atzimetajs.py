import numpy as np
import json

prieksmeti = ["Matemātika", "Latviešu valoda", "Sports", "Programmēšana", "Mongoļu grozu pīšanas māksla"]
atzimes = [[1, 2, 3, 4, 5],[4, 5, 8, 9],[3, 4, 6, 7],[6,3,2,9,10],[10,10,10,10,10]]


def Videjais(lst): 
    return sum(lst) / len(lst) 

def izvelne():
    print("")

def rakstit():
    global vards 
    with open(f'atzimes_{vards}.json', 'w', encoding='utf-8') as f:
        json.dump(prieksmeti, f, ensure_ascii=False, indent=4) #json.dump lai rakstitu datus json faila
        # vajag izdomat, ka to rakstit un lasit ta, lai butu sasaistiti divi list: prieksmeti un atzimes

def ka_iegut_videjo():
    # /dev/urandom shits
    print("----------\nAtzīmes:\n")
    for i in range(len(prieksmeti)):
        #videja = Videjais(atzimes[i])
        print("%r)%r (vid. %r)" % (i,prieksmeti[i], Videjais(atzimes[i])))
    print("----------")
    prieks_izvele = input("Kurā priekšmetā vēlies labot vidējo? (nr. pēc kārtas): ")
    print("Tu vari izlabot vidējo atzīmi priekšmetā: %r, ja tu izlabo " % (prieksmeti[prieks_izvele]))
ka_iegut_videjo()

''''
        

mahinacija()
'''

def prognoze():
    try:
        print(f"Priekšmeti: {prieksmeti}")
        prieksmeta_numurs = int(input("Ievadi priekšmeta nr. (pēc kārtas), kura atzīmi vēlies analizēt:"))
        ''' if prieksmeta_numurs == :
                print(f"Atzīmes atlasītajā priekšmetā: {}")
            elif 
        
        '''
    raise ValueError:
            
    


def galvenais():
    print("\n**********************************")
    print ("Sveicināti esat, filozofi un mācoņi, šai programmā lieliskajā. Šajā aparātā jūs varat ievadīt savus zināšanu skaitļu mērus un analizēt tos.")
    print("\n**********************************")
    

