from PIL import Image
import csv
import glob
from tqdm.auto import tqdm

def complement(x):
    if x>128:
        x = 255
    else:
        x = 0
    return x

def symbolen(nombre,symbole1,symbole2):
    if nombre==255:
        return symbole1
    else:
        return symbole2
    
def effcsv(sample_csv):
    f = open(sample_csv, "w+")
    f.close()
    return"Fichier CSV effacé"
    

def csvwrite(fichiercsv,extention,symbole1,symbole2,longueur,hauteur):
    path = r'C:/Users/xoxar/Desktop/perso/code/bad-apple!!/imgfolder/*'+extention
    files = sorted(glob.glob(path))
    files = sorted(files, key=lambda x: int(x.split("\\")[-1].split(".")[0])) #utilisé OS

    with open(fichiercsv, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        effcsv(fichiercsv)

        print("Début de l'écriture du CSV ...")

        for i in tqdm(files): 
            y=[]
            t=[]

            img = Image.open(i).convert('L')
            img = img.resize((longueur, hauteur))
            impix = img.load()
            for colonne in range(img.size[1]):
                for ligne in range(img.size[0]):
                    impix[ligne,colonne] = complement(impix[ligne,colonne])
                    t.append(symbolen(impix[ligne,colonne],symbole1,symbole2))
                    
                y.append(" ".join(t))
                t.clear()
            y="\n".join(y)

            writer.writerow(y)
        print("Finie !")
        return files