import os, sys
import random
import matplotlib.pyplot as plt
import numpy as np


class transac:

    def __init__(self):
        self.contenu = []
        self.score = 0

    def __repr__(self):
        return str(self.contenu) + ", " + str(self.score)

    def __lessthen__(self, other):
        return len(self.contenu) < len(other.contenu)

    def __equal__(self, other):
        return self.contenu == other.contenu

    def contains_motif(self, motif):
        for c in motif:
            if c not in self.contenu:
                return False
        return True


def get_random_ligne(dataset, global_score):
    weights = []
    data_set1 = []
    var = 0.0
    for i in dataset:
        data_set1.append(i.contenu)
        var = i.score/global_score
        weights.append(var)

    return random.choices(data_set1, weights=weights, k=1)[0]


def get_motif(dataset, global_score):
    ligne_random = get_random_ligne(dataset, global_score)
    liste_de_motif = []
    while len(liste_de_motif) == 0:
        for obj in ligne_random:
            if random.randint(0, 1) == 1:
                liste_de_motif.append(obj)
    return liste_de_motif
    
def get_motif_area(dataset, global_score):
    ligne_random = get_random_ligne(dataset, global_score)
    liste_de_motif = []
    while len(liste_de_motif) == 0:
        for obj in ligne_random:
            if random.randint(0, 1) == 1:
                liste_de_motif.append(obj)
    return liste_de_motif

def find_file(fileName):
    path = os.getcwd()+'/'+sys.argv[0]
    path = path.replace(sys.argv[0].split('/')[-1],"/ressources/"+fileName)
   
    return path

def load_data_file(data):

    data_resulta = []
    global_score = 0
    tmp = 0

    with open(data, "r") as file:
        lignes = file.read().split("\n")
        tmp=0
        for ligne in lignes:
            data_resulta.append(transac())
            for a in ligne.split(" "):
                if a:
                    data_resulta[-1].contenu.append(int(a))
            
            data_resulta[-1].score = 2 ** (len(data_resulta[-1].contenu))
            tmp = 2 ** (len(data_resulta[-1].contenu))
            global_score += tmp

    return data_resulta, global_score


def frequence(motif, dataset):
    var = 0
    for sub_base in dataset:
        if type(sub_base) is type(transac()):
            if set(motif) <= set(sub_base.contenu):
                var += 1
        else:                                        #on teste une liste
            if set(motif) <= set(sub_base):
                var += 1
    return var


def generer_motif(dataset, score_global):
    patternList = []
    for i in range(100):
        var = get_motif(dataset, score_global)
        patternList.append(var)
    return patternList


def generer_frequency(data_set, motif_list):
    result = {}
    list_motif_unique = [set(y) for y in set(
        tuple(sorted(x)) for x in motif_list)]

    for item in data_set:
        for motif in list_motif_unique:
            if motif <= set(item.contenu):
                cle = tuple(sorted(motif))
                if cle not in result.keys():
                    result[cle] = 0
                result[cle] += 1
    return result
#analyse
#  
def generer_fichiers_resultat(dataset, score, file):
    areaList = generer_motif(dataset, score)
    itemFreq = 0
    itemFreqInAreaList = 0

    pathToResFile = sys.argv[0]
    pathToResFile = pathToResFile.replace(pathToResFile.split('/')[-1], 
        "resultats/freq-sampling/"+sys.argv[1].split('.')[0])

    fichier = open(pathToResFile+"_resultats.txt", "w")
    fichier.write("frequence(x) - FreqInSelectedMotifs(y) \n")
    for item in areaList:
        
        itemFreq = frequence(item, dataset)
        itemFreqInAreaList = frequence(item, areaList)
        fichier.write(str(itemFreq)+" - "+str(itemFreqInAreaList)+"\n")

    fichier.close()


if __name__ == "__main__":

    if len(sys.argv)>1:
        dataset, score = load_data_file(find_file(sys.argv[1]))
        # print(dataset, score)
        lel = get_random_ligne(dataset, score)
        print(lel)
        res1 = get_motif(dataset, score)
        print(res1)
        res2 = frequence(res1, dataset)
        print(res2)
        resres = generer_motif(dataset, score)
        # print(resres)
        resultat_frequence = generer_frequency(dataset,resres)
        print(resultat_frequence)

        generer_fichiers_resultat(dataset, score, sys.argv[1])

    else:
        print("usage: python3 chemin_vers_le_script  [nom_du_fichier_de_data] ")