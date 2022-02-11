#####################
# groupe MI TD04
# MONNIER-BLONDEAU Alann
# VISBECQ Mathis
#nom3
# https://github.com/uvsq22102829/tas_de_sable.py.git
#####################


# Importation des librairies
import tkinter as tk
from random import randint
# Definition des Constantes

# Definition des Variables globales
# création de la liste
configuration_courante = []

# Definition des fonctions
def Creation_configuration():
    """ Création de la configuration en créant chaque case de la grille.
    Utilisation de double liste et duu module random pour générer des 
    nombres aléatoires."""
    global configuration_courante
    # création d'un nombre aléatoire grâce à la bibliothèque random
    nbr_alea = randint(0, 6)
    configuration_courante.append(["#"]*3)
    configuration_courante.append(["#", nbr_alea, nbr_alea, nbr_alea,  "#"])
    configuration_courante.append(["#", nbr_alea*3, "#"])
    configuration_courante.append(["#", nbr_alea*3, "#"])
    configuration_courante.append(["#"]*3)
    


# Programme Principale
# création fenêtre
ecran = tk.Tk()

# création canvas placé sur la fenêtre
canvas = tk.Canvas(ecran, height=500, width= 800, bg="white")
# méthode grid row = 0 place a la premiere ligne
canvas.grid(row=0)

bouton = tk.Button(ecran, text="Aléatoire")
# méthode grid row = 1 place a la deuxième ligne
bouton.grid(row=1)

ecran.mainloop()

