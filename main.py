# coding=UTF-8

from Tkinter import *
from tkMessageBox import *
import sys

# La fonction permet de valider ou non la phrase d'entrée.
def afficherCode():
    mot = entree.get()

# On analyse chaque mot de l'entrée. Si ce ne sont pas des caractères en majuscule, on alerte l'utilisateur.
    for char in mot:

        if ord(char) < 65 or ord(char) > 90:
            motBon = False
            showerror("Alerte", "Votre mot contient des caractères non adaptés.")
            return

    toplevel = Toplevel()
    canvas = Canvas(toplevel, width=400, height=200, bg='white')
    canvas.create_image(150,0,anchor=NW,image=img)
    canvas.create_text(125, 60, text="Code Bon \npour traduction", font="Courier 16", fill="blue")
    canvas.pack()

#Démarrage de la fenêtre
fenetre = Tk()
fenetre.title("Morse Code")
fenetre.geometry("600x600+200+200")

#Initialisation du frame contenant le texte d'entrée
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=BOTTOM, padx=10, pady=10)
Frame1.place(rely=1.0, relx=1.0, x=-10, y=-10, anchor=SE)

#Initialisation du frame contenant le bouton de confirmation
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=BOTTOM, padx=10, pady=10)
Frame2.place(rely=1.0, relx=0.0, x=10, y=-10, anchor=SW)

#Initialisation du canvas contenant la sortie (inclus dans le frame)
img = PhotoImage(file='./img/Check.gif')

#Petite triche pour redimensionner la flèche (à remplacer par PIL)
img = img.zoom(10)
img = img.subsample(32)

#Initialisation du champ d'entrée et du bouton de validation
value = StringVar()
value.set("VALEUR")
entree = Entry(Frame2, textvariable=value, width=30)
entree.pack()

bouton = Button(Frame1, text="Valider", command=afficherCode)
bouton.pack()

fenetre.mainloop()
