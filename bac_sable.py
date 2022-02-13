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
def creation_configuration():
    """ Création de la configuration en créant chaque case de la grille.
    Utilisation de double liste et duu module random pour générer des 
    nombres aléatoires."""
    global configuration_courante
    configuration_courante.append(4*[])
    # création d'un nombre aléatoire grâce à la bibliothèque random
    
    nbr_alea = randint(0, 6)
    configuration_courante.append(["#"]*3)
    configuration_courante.append(["#", nbr_alea, nbr_alea, nbr_alea,  "#"])
    configuration_courante.append(["#", nbr_alea, nbr_alea, nbr_alea, "#"])
    configuration_courante.append(["#", nbr_alea, nbr_alea, nbr_alea, "#"])
    configuration_courante.append(["#"]*3)

    # modifie le texte du canvas 
    canvas.itemconfigure(texte, text= configuration_courante)
    

    configuration_courante.append(["#", nbr_alea, nbr_alea, nbr_alea,  "#"])
    configuration_courante.append(["#", nbr_alea, nbr_alea, nbr_alea,  "#"])
    configuration_courante.append(["#"]*3)



# Programme Principale
# création fenêtre
ecran = tk.Tk()

# création canvas placé sur la fenêtre
canvas = tk.Canvas(ecran, height=500, width= 800, bg="white")
# méthode grid row = 0 place a la premiere ligne
canvas.grid(row=0)

bouton = tk.Button(ecran, text="Aléatoire", command=creation_configuration)
# méthode grid row = 1 place a la deuxième ligne
bouton.grid(row=1)

# Creer une zone de texte sur le canvas
texte = canvas.create_text(300, 100, text="", fill="black")

ecran.mainloop()