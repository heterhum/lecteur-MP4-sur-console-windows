from PIL import Image
import csv
import glob
from tqdm.auto import tqdm

def symbolen(nombre,symbole1,symbole2,symbole3,symbole4):
    if nombre<=255 and nombre>191:
        return symbole1
    elif nombre<=191 and nombre>127:
        return symbole3
    elif nombre<=127 and nombre>63:
        return symbole4
    else:
        return symbole2
    
def effcsv(sample_csv):
    f = open(sample_csv, "w+")
    f.close()
    return"Fichier CSV effacé"
    

def csvwrite(fichiercsv,extention,symbole1,symbole2,symbole3,symbole4,longueur,hauteur):
    path = r'bad-apple!!/imgfolder/*'+extention
    files = sorted(glob.glob(path))
    files = sorted(files, key=lambda x: int(x.split("\\")[-1].split(".")[0])) 

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
                    t.append(symbolen(impix[ligne,colonne],symbole1,symbole2,symbole3,symbole4))
                    
                y.append(" ".join(t))
                t.clear()
            y="\n".join(y)

            writer.writerow(y)
        print("Finie !")
        return files
