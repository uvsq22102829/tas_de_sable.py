#####################
# groupe MI TD04
# MONNIER-BLONDEAU Alann
# VISBECQ Mathis
#nom3
# lien clone
#####################


# Importation des librairies
import tkinter as tk
from random import randint
# Definition des Constantes

# Definition des Variables globales
#Donnée du nombre de grains de sable pour chaque case de la grille

# Definition des fonctions


# Programme Principale
# création fenêtre
ecran = tk.Tk()

# création canvas placé sur la fenêtre
canvas = tk.Canvas(ecran, height=400, width= 400, bg="white")
canvas.grid(row=0)

bouton = tk.Button(ecran, text="Aléa")
bouton.grid(row=1)

ecran.mainloop()


