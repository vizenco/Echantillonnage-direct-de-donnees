import pandas
import sys, os

args = sys.argv

def process_file(id, type):
    path = os.getcwd()+'/'+args[0].replace(args[0].split('/')[-1], "resultats/"+type+"/"+args[id])
    dict = {}
    print("openning "+ path)
    try:
        file = open(path, 'r')
        idx=0
        lines=file.read().split('\n')
        print(len(lines))
        for line in lines:
            line = line.strip().replace(' ', '').split('-')
            if idx == 0:
                dict[idx]=(line[0], line[1])
                idx += 1
            elif(line[0]!="" and idx > 0):
                dict[idx]= (int(line[0]), int(line[1]))
                idx += 1
            
        file.close()
    except :
        print("erreur : ",sys.exc_info()[1])
    
    return dict

def generer_plots_area():
    datas = process_file(1, "area-sampling")

def generer_plots_freq():
    datas = process_file(1, "freq-sampling")

if __name__ == "__main__":
    
    if len(args) > 1:
       generer_plots_freq()
       generer_plots_area()


    else:
        print("usage:\
             python3 path_to_plots.py [list_of_files_names] \n    Les fichiers sont dans le repertoire python/ressources/resultats/area-sampling | freq-sampling  et doivent avoir été créés auparavant dans script.py et areasampling.py")