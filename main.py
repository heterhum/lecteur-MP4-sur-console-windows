import csv
import time
from mp4toimg import video_to_frames
from csvcreate import csvwrite,effcsv
import os


video='C:/Users/xoxar/Desktop/perso/code/bad-apple!!/Rick_Roll.mp4'
path_to_folder='C:/Users/xoxar/Desktop/perso/code/bad-apple!!/imgfolder'
path_to_csv='C:/Users/xoxar/Desktop/perso/code/bad-apple!!/img.csv'
wanted_fps=15
extention=".jpeg"
symbole1=" "
symbole2="#"
longueur=150
hauteur=84
action=int(input())

def read(path_to_csv):
    with open(path_to_csv) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print("".join(row))
            time.sleep(0.06)
            #os.system("cls || clear")


if action==0:
    video_to_frames(video, path_to_folder,wanted_fps,extention)
    print("vidéo -> image, finie")
    n=input("Appuyez pour continuer ...")

    csvwrite(path_to_csv,extention,symbole1,symbole2,longueur,hauteur)
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