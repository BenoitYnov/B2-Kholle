#!/usr/bin/python3.6
#Auteur: Galmot Benoît

#Import
import csv
import argparse
import pandas as pd


#Variables
fichier = 'tableau.csv'
tableau = []


#Fonctions
#Lire le fichier csv
def lireFichier():
    with open(fichier, "r") as files:
        read_file = csv.reader(files)
        for row in read_file:
            for l in range(len(row)):
                if len(row) > 0:
                    tableau.append(row[l])


#Options avec argparse
parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument("-l", action="store_true", help="Affiche le contenu de la liste")
parser.add_argument("-a", nargs="*", help="Ajoute les items dans la liste")
parser.add_argument("-c", action="store_true", help="Supprime tous les éléments de la liste")
parser.add_argument("-s", "--max", action="store_true", help="Affiche la valeur maximum contenu dans la liste")
parser.add_argument("-s", "--min", action="store_true", help="Affiche la valeur minimum contenu dans la liste")
parser.add_argument("-s", "--moy", action="store_true", help="Affiche la moyenne de tous les éléments dans la liste")
parser.add_argument("-s", "--sum", action="store_true", help="Affiche la somme de tous les éléments dans la liste")
parser.add_argument("-t", action="store_true", help="Trie la liste dans l’ordre croissant")
parser.add_argument("-d", "--desc", action="store_true", help="Trie la liste dans l’ordre decroissant")
parser.add_argument("-h", "--help", action="store_true", help="Affiche le manuel d’utilisation de cette commande")
args = parser.parse_args()


#Affiche le contenu de la liste
if args.l:
    lireFichier()
    for nombre in tableau:
        print(nombre)


#Ajout de valeur dans le fichier 
elif args.a:
    with open(fichier, 'a') as fichierCSV:
        writer = csv.writer(fichierCSV)
        for nombre in args.a:
            fichierCSV.write(nombre + '\n')
            print('La valeur', nombre, 'a été ajouté')


#Supprime tous les éléments de la liste
elif args.c:
    with open(fichier, 'w+') as fichierCSV:
        fichierCSV.write('Valeurs\n')
        fichierCSV.close()
        print("Les valeurs ont été effacées")


#Affiche la valeur maximum contenu dans la liste
elif args.max:
    lireFichier()
    valeur = 0
    maximum = 0
    for valeurMax in tableau:
        try:
            valeur = int(valeurMax)
        except:
            print("")
        if valeur > maximum:
            maximum = valeur
    print('Le plus grand nombre est:', maximum)


#Affiche la valeur minimal contenu dans la liste
elif args.min:
    lireFichier()
    valeur = 999999
    minimum = 999999
    for valeurMin in tableau:
        try:
            valeur = int(valeurMin)
        except:
            print("")
        if valeur < minimum:
            minimum = valeur
    print('Le plus petit nombre est:', minimum)


#Moyenne et Somme du tableau à l'aide du module pandas
#Affiche la moyenne de tous les éléments dans la liste
elif args.moy:
    df = pd.read_csv(fichier)
    moyenne = df['Valeurs'].mean()
    print('La moyenne de tous les éléments est de:', moyenne)


#Affiche la somme de tous les éléments dans la liste
elif args.sum:
    df = pd.read_csv(fichier)
    total = df['Valeurs'].sum()
    print('La somme de tous les éléments est de:', total)


#Trier une liste, à l'aide du module pandas
#Trie la liste dans l’ordre croissant
elif args.t:
    df = pd.read_csv(fichier)
    p = df.sort_values(by='Valeurs', ascending=True)
    p.to_csv(fichier, index=False)
    print("Liste triée dans l'ordre croissant avec succès \n -l pour voir la nouvelle liste")


#Trie la liste dans l’ordre decroissant
elif args.desc:
    df = pd.read_csv(fichier)
    p = df.sort_values(by='Valeurs', ascending=False)
    p.to_csv(fichier, index=False)
    print("Liste triée dans l'ordre décroissant avec succès !\n -l pour voir la nouvelle liste")


#Affiche l'aide 
else:
    parser.print_help()
    