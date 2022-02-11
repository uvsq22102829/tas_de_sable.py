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
configuration_courante = []

# Definition des fonctions


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