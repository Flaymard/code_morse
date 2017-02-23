# coding=UTF-8

from Tkinter import *
from tkMessageBox import *
import sys
from cStringIO import StringIO

ABOUT = "Programme réalisé par Florian AYMARD\nhttps://github.io/flaymard"
# La fonction permet de valider ou non la phrase d'entrée.
def afficherCode():
    mot = entree.get()

# On analyse chaque mot de l'entrée. Si ce ne sont pas des caractères en majuscule, on alerte l'utilisateur.
    for char in mot:

        if ord(char) < 65 or ord(char) > 90:
            motBon = False
            showerror("Alerte", "Votre mot contient des caractères non adaptés.")
            return

    drawBits(mot)

def about():
    showinfo("À propos", ABOUT)

def convBin(a):
    sb = StringIO()
    for char in a[::-1]:
        unicodeVal = ord(char)
        for i in range(5):
            sb.write(str(unicodeVal%2))
            unicodeVal = (unicodeVal - unicodeVal%2)/2

    return (sb.getvalue())[::-1]

def initLines():
    for i in range(7):
        canvasCode.create_line(10, 8*i, 370, 8*i)

    canvasCode.pack()

def drawBits(motStr):
    canvasCode.delete()
    initLines()
    a = convBin(motStr)
    pasY = 8
    pasX = 15
    yDep = 8
    xDep = 15
    x = xDep
    y = yDep
    i = 1

    for bit in a:

        if bit == '1':
            canvasCode.create_rectangle(x, y, x + 8, y + 8, fill="blue")

        y += pasY
        if i%5 == 0:
            x += pasX
            y = yDep

        i = i + 1

    canvasCode.pack()


#Démarrage de la fenêtre
fenetre = Tk()
fenetre.title("Morse Code")
fenetre.geometry("400x200+0+0")

#Initialisation du frame contenant le texte d'entrée
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=BOTTOM, padx=10, pady=10)
Frame1.place(rely=1.0, relx=1.0, x=-10, y=-10, anchor=SE)

#Initialisation du frame contenant le bouton de confirmation
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=BOTTOM, padx=10, pady=10)
Frame2.place(rely=1.0, relx=0.0, x=10, y=-10, anchor=SW)

#Initialisation du frame labelisé contenant la valeur convertie
Frame3 = LabelFrame(fenetre, borderwidth=2, relief=GROOVE, text="Valeur convertie")
Frame3.pack(side=TOP, padx=10, pady=10)
canvasCode = Canvas(Frame3, width=570, height=50, bg='white')
canvasCode.pack()
initLines()
#Frame3.place(rely=1.0, relx=0.0, x=10, y=-10, anchor=NW)

#Initialisation du champ d'entrée et du bouton de validation
value = StringVar()
value.set("VALEUR")
entree = Entry(Frame2, textvariable=value, width=30)
entree.pack()

bouton = Button(Frame1, text="Valider", command=afficherCode)
bouton.pack()

#Initialisation de la barre de menu
menubar = Menu(fenetre)
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=about)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

fenetre.mainloop()
