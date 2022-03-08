#####################
# groupe MI TD04
# MONNIER-BLONDEAU Alann
# VISBECQ Mathis
# nom3 Lilian
# https://github.com/uvsq22102829/tas_de_sable.py.git
#####################


# Importation des librairies
from random import randint
import tkinter as tk


# Definition des Variables globales

# liste: contient valeur de grain de sable dans une liste a deux dimensions
liste = []

# liste_verification va permettre de vérifier si toute les valeurs présentent
# permettent d'atteindre la stabilisation
liste_verification = []

# liste de couleurs que prennent les carrés suivant leurs nombres de grain de sables
liste_couleur = ["blue", "black", "yellow", "green"]
# enregustrer les carres pour modifier leur couleur
pause = False
mode_configuration = "alea"
nbr_milieu = 30
jeu = 0
longueur = 5
# CONSTANTE




# Définitions des Fonctions
def play():
    """ Lance le changement de configuration si la partie n'est pas en pause"""
    global pause, liste, jeu, longueur
    if jeu != 1:
        creer_liste()
        affichage_configuration()
    jeu = 1
    modifier_configuration()


def get_taille():
    """ Récupère la taille rentrer par l'utilisateur"""
    global longueur
    longueur = int(entry.get())

def creer_liste():
    """ Méthode qui va créer une configuration initiale avec 0 grains de sables"""
    global liste, mode_configuration, longueur
    longueur += 2
    sous_liste = []
    for i in range(longueur):
        for j in range(longueur+1):
            if i == 0 or i == longueur - 1:
                sous_liste.append("#")
            elif j == 0 or j == longueur - 1:
                sous_liste.append("#")
            elif j == longueur:
                sous_liste.append([])
            else:
                sous_liste.append(0)
        liste.append(sous_liste)
        del sous_liste
        sous_liste = []


    if mode_configuration == "alea":
        configuration_aleatoire()

    elif mode_configuration == "grain_centre":
        configuration_centre()

    elif mode_configuration == "3_grains":
        configuration_par_3()

    elif mode_configuration == "identity":
        configuration_identity()

    elif mode_configuration == "sauvegarde":
        sauvegarde()




def random():
    """ Configuration démarre avec nombre de grain de sable aléatoire"""
    global mode_configuration
    mode_configuration = "alea"

def configuration_aleatoire():
    """ Va créer une configuration aléatoire après avoir cliqué sur le bouton."""
    global liste, longueur
    for i in range(longueur):
        for j in range(longueur):
            alea = randint(0, 9)
            if liste[i][j] != "#":
                liste[i][j] = alea


def pile_centree():
    """ Configuration demarre avec grains de sables au centre choisis par l'utilisateur et aucun autre autour"""
    global mode_configuration
    mode_configuration = "grain_centre"


def configuration_centre():
    """ Va créer une configuration centrée avec un gros grain de sable au milieu"""
    global liste, nbr_milieu, longueur
    for i in range(longueur):
        for j in range(longueur):
            if liste[i][j] != "#":
                if i == longueur//2 and j == longueur//2 :
                    liste[longueur//2][longueur//2] = nbr_milieu
                else:
                    liste[i][j] = 0


def stable():
    """Configuration demarre avec 3 grains de sable a chaque case"""
    global mode_configuration
    mode_configuration = "3_grains"


def configuration_par_3():
    """ Va créer une configuration centrée avec un grains de sable egale a 3"""
    global liste, nbr_milieu, longueur
    for i in range(longueur):
        for j in range(longueur):
            if liste[i][j] != "#":
                liste[i][j] = 3

def identity():
    """Configuration aditionne une configuration aléatoire avec Max_stable"""
    global mode_configuration
    mode_configuration = "identity"

def configuration_identity():
    """ Va créer une configuration centrée avec grains de sable égale à 3 + nbr aleatoire"""
    global liste, nbr_milieu, longueur
    for i in range(longueur):
        for j in range(longueur):
            if liste[i][j] != "#":
                alea = randint(0, 9)
                liste[i][j] = 3 + alea


def affichage_configuration():
    """ Affiche la configuration sous forme de carré de couleur"""
    global liste, longueur
    canvas.delete("all")
    x, x1, y, y1 = 0, (600 // (longueur-2)), 0, (600 // (longueur-2))
    for i in range(1, longueur-1):
        for j in range(1, longueur-1):

            carre = canvas.create_rectangle(x, y, x1, y1, fill="white")
            liste[i][longueur].insert(0, carre)

            x += (600 // (longueur-2))
            x1 += (600 // (longueur-2))

        x, x1 = 0, (600 // (longueur-2))
        y += 600 // (longueur-2)
        y1 += 600 // (longueur-2)




def modification_affichage_configuration():
    """ Va modifier la affichage de la configuration"""
    global liste_couleur, liste
    for i in range(1, longueur-1):
        for j in range(1, longueur-1):
            if liste[i][j] == 3 or liste[i][j] == 2 or  liste[i][j] == 1:
                 canvas.itemconfigure(liste[i][longueur][-j], fill=liste_couleur[liste[i][j]-1])
            elif liste[i][j] == 0:
                canvas.itemconfigure(liste[i][longueur][-j], fill="white")
            else:
                canvas.itemconfigure(liste[i][longueur][-j], fill=liste_couleur[-1])





def modifier_configuration():
    """ Va modifier la configurant pour chaque élément différent de # en
    appelant les fonctions additions() et soustraction()"""
    global liste, liste_verification, longueur

    for i in range(longueur):
        for j in range(longueur):
            if liste[i][j] != "#":
                if liste[i][j] >= 4:
                    additions(i, j)
                    soustractions(i, j)

    verification() # appelle la méthode verification() pour voir si la configuration est stabilisée
    modification_affichage_configuration()
    # va regarder si tout la liste_verification contient que des True ce
    # qui signifie que la configuration est stabilisée
    if liste_verification.count("True") != (len(liste) ** 2):
        liste_verification = []
        if pause == False:
            canvas.after(100, play)







def additions(i, j):
    """ Va ajouter un grain de sable au case autour en fonction de la position de l'élément choisis"""
    global liste
    # bord haut gauche
    if liste[i-1][j] == "#" and liste[i][j-1] == "#":
        liste[i+1][j] += 1
        liste[i][j+1] += 1

    # bord bas gauche
    elif liste[i + 1][j] == "#" and liste[i][j - 1] == "#":
        liste[i - 1][j] += 1
        liste[i][j + 1] += 1

    # bord bas droite
    elif liste[i+1][j] == "#" and liste[i][j+1] == "#":
        liste[i-1][j] += 1
        liste[i][j-1] += 1

    # bord haut droit
    elif liste[i - 1][j] == "#" and liste[i][j + 1] == "#":
        liste[i + 1][j] += 1
        liste[i][j - 1] += 1

    # ligne haut
    elif liste[i-1][j] == "#":
        liste[i+1][j] += 1
        liste[i][j-1] += 1
        liste[i][j+1] += 1

    # colone cote gauche
    elif liste[i][j-1] == "#":
        liste[i+1][j] += 1
        liste[i][j+1] += 1
        liste[i-1][j] += 1

    # colone cote droit
    elif liste[i][j+1] == "#":
        liste[i+1][j] += 1
        liste[i][j-1] += 1
        liste[i-1][j] += 1

    # ligne bas
    elif liste[i+1][j] == "#":
        liste[i-1][j] += 1
        liste[i][j-1] += 1
        liste[i][j+1] += 1

    # Case du milieu
    else:
        liste[i-1][j] += 1
        liste[i][j-1] += 1
        liste[i][j+1] += 1
        liste[i+1][j] += 1

def soustractions(i, j):
    """ Méthode qui va soustraire 4 grains de sables à l'éléments sélectionnés. """
    global liste
    liste[i][j] -= 4


def verification():
    """ Regarde si la configurtion est stabilisé ou non"""
    global liste, liste_verification, longueur
    while 1:
        for i in range(longueur):
            for j in range(longueur):
                if liste[i][j] == 0 or liste[i][j] == 1 or liste[i][j] == 2 or liste[i][j] == 3 or liste[i][j] == "#":
                    liste_verification.append("True")
                else:
                    liste_verification.append("False")
        break


def get_nbr_grain():
    """ Récupère la taille rentrer par l'utilisateur"""
    global nbr_milieu
    nbr_milieu = int(gros_grains.get())


def stop():
    """ Met pause a True pour stopper la configuration"""
    global pause
    if pause == False:
        btn_pause.configure(text="Reprendre")
        pause = True
        canvas.after_cancel(play)

    else:
        btn_pause.configure(text="Pause")
        pause = False
        canvas.after(100, play)

def btn_sauvegarde():
    """ Sauvegarde une configuration lorsqu'on est en pause"""
    global liste, pause, mode_configuration, longueur
    l2 = []
    if pause == 1:
        file = open("sauvegarde_configuration.txt", "w", encoding="Utf-8")
        for i in range(longueur):
            for j in range(longueur):
                if liste[i][j] != "#":
                    file.write(f"{liste[i][j]}")
        file.close()
    else:
        mode_configuration = "sauvegarde"

def sauvegarde():
    """ Va récupérer la dernière configuration qu'on avait enregistrer dans un fichier"""
    global liste, longueur
    sous_liste = []
    file = open("sauvegarde_configuration.txt", "r", encoding="Utf-8")
    for i in range(longueur):
        for j in range(longueur):
            if liste[i][j] != "#":
                ligne = int(file.readline(1))
                liste[i][j] = ligne
    file.close()


# Programme Principal

# Création de la fenêtre (taille, titre)
ecran = tk.Tk()
ecran.geometry("1200x700")
ecran.title("Projet tas de sable")
ecran.configure(bg="white")

# Création du canvas ou va apparaître les différentes configurations
canvas = tk.Canvas(ecran, height=600, width=600, bg="white", highlightthickness =0)
canvas.grid(row=0, column=0, rowspan=12)


# label avec un texte qui nous dit d'entrer taille configuration
tk.Label(ecran, text="Entrer la taille de la configuration shouaiter.").grid(row=0, column=1)

# création entry pour qu'on rentre la taille de la configuration qu'on shouaite
entry = tk.Entry(ecran)
entry.grid(row=1, column=1)

# Bouton qui va valider la taille qu'on a choisis pour la configuration
btn_valider = tk.Button(ecran, text="Valider", command=get_taille)
btn_valider.grid(row=1, column=2)

# btn qui va lancer les modifications des configurations
btn_play = tk.Button(ecran, text="Démarrer", command=play)
btn_play.grid(row=2, column=1)

# Btn qui va mettre en pause les changements de configurations lorsqu'on clique dessus
# et relancer quand clic de nouveau
btn_pause = tk.Button(ecran, text="PAUSE", command=stop)
btn_pause.grid(row=3, column=1)

# btn qui permet de sauvegarder une configuration lorsqu'on est en pause
btn_sauvegarder = tk.Button(ecran, text="SAUVEGARDER", command=btn_sauvegarde)
btn_sauvegarder.grid(row=4, column=1)


# label qui demande de choisir la configuration qu'on shouaite
tk.Label(ecran, text="Choississez la configuration que vous shouaitez. ").grid(row=5, column=1)

# Création du bouton alea pour creer une configuration aléatoire
tk.Button(ecran, text="RANDOM", command=random).grid(row=6, column=1)

# label qui demande d'entrée le nbr de grain de sable qu'on veut mettre au centre
tk.Label(ecran, text="Entrez le nombre total de grain de sable que vous voulez mettre au centre").grid(row=7, column=1)


# création entry et buton pour récupérer nombre grain de sable a mettre au centre si on choisi
# configuration Pile_centree
gros_grains = tk.Entry(ecran)
gros_grains.grid(row=8, column=1)
tk.Button(ecran, text="Valider", command=get_nbr_grain).grid(row=8, column=2)

# Création du bouton pile centrée pour creer une configuration avec un gain N choisis par l'utilisateur au milieu et rien autour
tk.Button(ecran, text="Pile_centree", command=pile_centree).grid(row=9, column=1)

# Configuration MaxStable donne 3 grain de sables à chaque case
tk.Button(ecran, text="Max_Stable", command=stable).grid(row=10, column=1)

# Configuration Identity : on appelle double max stable la configuration obtenue en additionant
# Max Stable à elle-même; alors Identity est obtenue en retranchant
# à double max stable la configuration stabilisée de double max stable,
# puis en stabilisant le résultat
tk.Button(ecran, text="IDENTITY", command=identity).grid(row=11, column=1)


# boucle gestion évènement
ecran.mainloop()



















































