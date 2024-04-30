import numpy as np
prieksmeti = ["Matene", "Latene", "Sports", "Programmēšna", "Mongoļu grozu pīšanas māksla"]
atzimes = [[1, 2, 3, 4, 5],[4, 5, 8, 9],[3, 4, 6, 7],[6,3,2,9,10],[10,10,10,10,10]]

def Videjais(lst): 
    return sum(lst) / len(lst) 

def izvelne():
    print("Esi sveicināts programā")

def mahinacija():
    # /dev/urandom shits
    print("----------\nAtzīmes:\n")
    for i in prieksmeti:
        #videja = Videjais(atzimes[i])
        print(f"{i}){prieksmeti[i]} (vid.): {atzimes[i]}")
    print(prieksmeti)

mahinacija()