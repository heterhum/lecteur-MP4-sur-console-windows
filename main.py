import csv
import time
from mp4toimg import video_to_frames
from csvcreate import csvwrite,effcsv
import os


video='.../Rick_Roll.mp4' #path to your mp4
path_to_folder='.../imgfolder'
path_to_csv='.../img.csv'
wanted_fps=15
extention=".jpeg" 
symbole1="?"
symbole2="@"
symbole3="%"
symbole4="$"
longueur=150*2
hauteur=84*2
action=int(input("choose your action :"))

def read(path_to_csv):
    with open(path_to_csv) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print("".join(row))
            time.sleep(1/wanted_fps)
            #os.system("cls || clear")


if action==0:
    video_to_frames(video, path_to_folder,wanted_fps,extention)
    print("vidéo -> image, finie")
    n=input("Appuyez pour continuer ...")

    csvwrite(path_to_csv,extention,symbole1,symbole2,symbole3,symbole4,longueur,hauteur)
    print("image -> csv, finie")
    n=input("Appuyez pour continuer ...")

    read(path_to_csv)
    print("Vidéo finie !")
    n=input("Appuyé pour finir le script ...")

elif action==1 and os.path.getsize(path_to_csv) != 0:
    read(path_to_csv)
    print("Vidéo finie !")
    n=input("Appuyé pour finir le script ...")

elif action==2:
    video_to_frames(video, path_to_folder,wanted_fps,extention)
    print("vidéo -> image, finie")
    n=input("Appuyez pour continuer ...")

    csvwrite(path_to_csv,extention,symbole1,symbole2,longueur,hauteur)
    print("image -> csv, finie")
    n=input("Appuyez pour finir le script ...")
        
elif action==3:
    effcsv(path_to_csv)
    print("fichier CSV effacé")

    for filename in os.listdir(path_to_folder):
        os.remove(path_to_folder + "/" + filename)
    print("Dossier vidéo effacé")
    n=input("Appuyez pour finir le script ...")

else:
    print("votre nombre de correspond a aucune action")
    print("help:")
    print("0=tout faire, écriture des images dans le dossier, écriture du csv, lecture du csv")
    print("1=seulement lecture du csv")
    print("2=écriture des images dans le dossier, écriture du csv")
    print("3=effacé completement tout ce qui ce trouve dans le dossier et le fichier csv")
    n=input("Appuyez pour finir le script ...")
