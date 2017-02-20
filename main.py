# coding=UTF-8

from Tkinter import *
from tkMessageBox import *
import sys

# La fonction permet de valider ou non la phrase d'entrée.
def afficherCode():
    mot = entree.get()

# On analyse chaque mot de l'entrée. Si ce ne sont pas des caractères en majuscule, on alerte l'utilisateur.
    for char in mot:
        code = {}
        print ord(char) - 65
        code[mot.index(char)] = ord(char) - 65
        print code
        if ord(char) < 65 or ord(char) > 90:
            motBon = False
            showerror("Alerte", "Votre mot contient des caractères non adaptés.")

    convertBin(code.values)

# Conversion en binaire et dessin direct
def convertBin(liste):
    for integer in liste:


#Démarrage de la fenêtre
fenetre = Tk()
fenetre.title("Morse Code")
fenetre.geometry("600x200+0+0")

#Initialisation du frame contenant le texte d'entrée
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=BOTTOM, padx=10, pady=10)
Frame1.place(rely=1.0, relx=1.0, x=-10, y=-10, anchor=SE)

#Initialisation du frame contenant le bouton de confirmation
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=BOTTOM, padx=10, pady=10)
Frame2.place(rely=1.0, relx=0.0, x=10, y=-10, anchor=SW)

#Initialisation du champ d'entrée et du bouton de validation
value = StringVar()
value.set("VALEUR")
entree = Entry(Frame2, textvariable=value, width=30)
entree.pack()

bouton = Button(Frame1, text="Valider", command=afficherCode)
bouton.pack()

fenetre.mainloop()
