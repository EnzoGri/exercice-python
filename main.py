from tkinter import * 
from tkinter import messagebox, Toplevel


def exercice1():
    fenetreExercice = Toplevel()
    fenetreExercice.title("Exercice 1")
    fenetreExercice.geometry("300x200")
    l_Variable1: int 
    l_Variable1 = 3
    l_Variable2: int
    l_Variable2 = l_Variable1 + 5
    labelVarible1 = Label(fenetreExercice, text=f"Variable1 = {l_Variable1}", font=("Arial", 12))
    labelVarible1.pack(pady=20)
    labelVarible2 = Label(fenetreExercice, text=f"Variable2 = {l_Variable2}", font=("Arial", 12))
    labelVarible2.pack(pady=20)

def exercice2():
    fenetreExercice = Toplevel()
    fenetreExercice.title("Exercice 2")
    fenetreExercice.geometry("300x200")
    l_Variable1: int
    l_Variable1 = 9
    l_Variable2: int
    l_Variable2 = l_Variable1 * l_Variable1
    l_Variable1 = 0
    labelVarible1 = Label(fenetreExercice, text=f"Variable1 = {l_Variable1}", font=("Arial", 12))
    labelVarible1.pack(pady=20)
    labelVarible2 = Label(fenetreExercice, text=f"Variable2 = {l_Variable2}", font=("Arial", 12))
    labelVarible2.pack(pady=20)

def exercice3():
    def calculerCarre():
        try:
            valeur = int(inputValue.get())
            resultat = valeur ** 2
            var_resultat.set(f"Le carré de {valeur} est {resultat}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide !")

    fenetreExercice = Toplevel()
    fenetreExercice.title("Exercice 3")
    fenetreExercice.geometry("300x200")
    
    labelExercice = Label(fenetreExercice, text="Saisissez un nombre", font=("Arial", 12))
    labelExercice.pack(pady=20)
    inputValue = Entry(fenetreExercice, font=("Arial", 12))
    inputValue.pack(pady=5)

    bouton_calculer = Button(fenetreExercice, text="Calculer", command=calculerCarre, font=("Arial", 12))
    bouton_calculer.pack(pady=10)

    var_resultat = StringVar()
    var_resultat.set("Le résultat apparaîtra ici")

    label_resultat = Label(fenetreExercice, textvariable=var_resultat, font=("Arial", 12))
    label_resultat.pack(pady=10)

def exercice4():
    def intervertion():
            try:
                inputA = str(l_userInputA.get())
                inputB = str(l_userInputB.get())
                temp:str = inputA
                inputA = inputB
                inputB = temp
                varResultat.set(f"1ere valeur = {inputA} / 2eme valeur = {inputB}")
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer quelque chose !")
        
    fenetreExercice = Toplevel()
    fenetreExercice.title("Exercice 4")
    fenetreExercice.geometry("300x200")

    labelExercice = Label(fenetreExercice, text="Saisissez deux valeurs", font=("Arial",12))
    labelExercice.pack(pady=20)

    l_userInputA = Entry(fenetreExercice, font=("Arial",12))
    l_userInputA.pack(pady=5)
    l_userInputB = Entry(fenetreExercice, font=("Arial",12))
    l_userInputB.pack(pady=5)
    
    boutonIntervertir = Button(fenetreExercice,text="Intervertir", command=intervertion)
    boutonIntervertir.pack(pady=5)

    varResultat = StringVar()
    varResultat.set("Le résultat apparaitre ici")

    labelResultat = Label(fenetreExercice, textvariable=varResultat)
    labelResultat.pack(pady=5)

def exercice5():
    print("Exercice 5. Calcul de la TVA")
    l_montantHT:int = int(input("Montant Hors Taxe > "))
    l_tauxTaxe:int = int(input("Pourcentage de la taxe > "))

    l_montantTVA:int = l_montantHT * (l_tauxTaxe / 100)
    l_montantTTC:int = l_montantHT + l_montantTVA
    print(f"Montant Hors Taxe : {l_montantHT}\nMontant de la Taxe : {l_montantTVA}\nMontant TTC : {l_montantTTC}")

def exercice6():
    print("Exercice 6. Valeur positive ou négative")
    l_userInput:int = int(input("Saisissez un nombre réel > "))
    if l_userInput > 0:
        print(f"{l_userInput} est positif !")
    elif l_userInput < 0:
        print(f"{l_userInput} est négatif !")
    else:
        print(f"VOtre nombre est {l_userInput}, il est donc nul")

def exercice7():
    print("Exercice 7. Suite de valeur dans l'ordre croissant ou non")
    l_userInput1:int = int(input("Saisissez un premier nombre réel > "))
    l_userInput2:int = int(input("Saisissez un deuxième nombre réel > "))
    l_userInput3:int = int(input("Saisissez un troisième nombre réel > "))
    if l_userInput1 <= l_userInput2 and l_userInput2 <= l_userInput3:
        print(f"Vos nombres sont dans le bonne ordre: {l_userInput1} < {l_userInput2} < {l_userInput3}")
    else:
        print("Vos nombres sont dans le désordre")

def exercice8():
    print("Exercice 8. Calcul de l'heure + 1minute")
    l_heure:int = int(input("Saisissez l'heure > "))
    l_minute:int = int(input("Saisissez les minutes > "))

    l_minute += 1
    if l_minute >= 60:
        l_minute = 0
        l_heure += 1
        if l_heure >= 24:
            l_heure = 0
    print(f"Dans une minute, il sera {l_heure} heure(s) {l_minute}.")

def exercice9():
    print("Exercice 9. Boucle tant que la valeur n'est pas comprise entre 1 et 3")
    l_userInput:int = int(input("Saisissez un chiffre entre 1 et 3 > "))

    while l_userInput < 1 or l_userInput > 3:
        l_userInput = int(input(f"{l_userInput} n'est pas compris entre 1 et 3, Saisissez à nouveau > "))
    print(f"{l_userInput} est bien compris entre 1 et 3")

def exercice10():
    print("Zxercice 10. Plus grand ou plus petit")
    l_userInput:int = int(input("Saisissez un chiffre entre 10 et 20 > "))

    while l_userInput < 10 or l_userInput > 20:
        if l_userInput < 10:
            l_userInput = int(input("Plus grand !, Saisissez à nouveau > "))
        else:
            l_userInput = int(input("Plus bas !, Saisissez à nouveau > "))

    print(f"{l_userInput} est bien compris entre 10 et 20")

def exercice11():
    print("Exercice 11. Affiche les 10 chiffres suivants")
    l_userInput:int = int(input("Saisissez un nombre > "))
    for i in range(1,11):
        print(l_userInput + i)

def exercice12():
    print("Exercice 12. Table de multiplication")
    l_userInput:int = int(input("Saisissez un chiffre pour afficher sa table de multiplication > "))
    l_nombreMultiplicateur:int = int(input("saisissez le nombre de multiplication > ")) + 1
    for i in range(1,l_nombreMultiplicateur):
        print(f"{l_userInput} x {i} = {l_userInput * i}")

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*30)
    print("MENU DES EXERCICES".center(30))
    print("="*30)
    print("1. Déclaration de variables et affectation de valeurs")
    print("2. Carré d'une valeur")
    print("3. Carré d'une valeur saisie par l'utilisateur")
    print("4. Echange de valeur entre 2 variables")
    print("5. Calcul de la TVA")
    print("6. Valeur positive ou négative")
    print("7. Suite de valeur dans l'ordre croissant ou non")
    print("8. Calcul de l'heure + 1minute")
    print("9. Boucle tant que la valeur n'est pas comprise entre 1 et 3")
    print("10. Plus grand ou plus petit")
    print("11. Affiche les 10 chiffres suivants")
    print("12. Table de multiplication")
    print("13. Quitter")
    print("="*30)
exercices = {
    1: exercice1,
    2: exercice2,
    3: exercice3,
    4: exercice4,
    5: exercice5,
    6: exercice6,
    7: exercice7,
    8: exercice8,
    9: exercice9,
    10: exercice10,
    11: exercice11,
    12: exercice12
}
def creerBouton(parent:str, numberButton:int):
    for i in range (1, numberButton + 1):
        bouton = Button(parent, text=f"Exercice {i}", command=exercices[i])
        bouton.pack(padx=5)

def main():
    fenetre = Tk()
    fenetre.title("Série d'exercice Python")
    label = Label(fenetre, text="Menu d'exercices Python !", font=("Arial", 14))
    label.pack(pady=20, padx=10)
    fenetreBouton = Frame(fenetre)
    fenetreBouton.pack()
    creerBouton(fenetreBouton, 12)

    # button1 = Button(fenetreBouton, text="Exercice 1", command=exercice1)
    # button1.grid(padx=5, column=0, row=1)

    # button2 = Button(fenetreBouton, text="Exercice 2", command=exercice2)
    # button2.grid(padx=5, pady=5, column=1, row=1)

    # button3 = Button(fenetreBouton, text="Exercice 3",command=exercice3)
    # button3.grid(padx=5, pady=5, column=2, row=1)

    # button4 = Button(fenetreBouton, text="Exercice 4", command=exercice4)
    # button4.grid(padx=5, pady=5, column=0, row=2)

    # button5 = Button(fenetreBouton, text="Exercice 5")
    # button5.grid(padx=5, pady=5, column=1, row=2)

    # button6 = Button(fenetreBouton, text="Exercice 6")
    # button6.grid(padx=5, pady=5, column=2, row=2)

    # button7 = Button(fenetreBouton, text="Exercice 7")
    # button7.grid(padx=5, pady=5, column=0, row=3)

    # button8 = Button(fenetreBouton, text="Exercice 8")
    # button8.grid(padx=5, pady=5, column=1, row=3)

    # button9 = Button(fenetreBouton, text="Exercice 9")
    # button9.grid(padx=5, pady=5, column=2, row=3)

    # button10 = Button(fenetreBouton, text="Exercice 10")
    # button10.grid(padx=5, pady=5, column=0, row=4)

    # button11 = Button(fenetreBouton, text="Exercice 11")
    # button11.grid(padx=5, pady=5, column=1, row=4)

    # button12 = Button(fenetreBouton, text="Exercice 12")
    # button12.grid(padx=5, pady=5, column=2, row=4)

    fenetre.mainloop()
        
    
if __name__ == "__main__":
    main()

