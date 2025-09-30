def exercice1():
    print("Exercice 1. Déclaration de variables et affectation de valeurs")
    l_Variable1: int 
    l_Variable1 = 3
    l_Variable2: int
    l_Variable2 = l_Variable1 + 5

    print(l_Variable1)
    print(l_Variable2)

def exercice2():
    print("Zxercice 2. Carré d'une valeur")
    l_Variable1: int
    l_Variable1 = 9
    l_Variable2: int
    l_Variable2 = l_Variable1 * l_Variable1
    l_Variable1 = 0
    print(l_Variable1)
    print(l_Variable2)

def exercice3():
    print("Exercice 3. Carré d'une valeur saisie par l'utilisateur")
    l_userNumber:int = int(input("Veuillez saisir un nombre > "))
    l_userNumber = l_userNumber * l_userNumber
    print(f"Votre nombre au carré est {l_userNumber}")

def exercice4():
    print("Exercice 4. Echange de valeur entre 2 variables")
    l_userInputA:str = input("Saisissez une première valeur > ")
    l_userInputB:str = input("Saisissez une deuxième valeur > ")
    
    l_temp:str = l_userInputA
    l_userInputA = l_userInputB
    l_userInputB = l_temp
    print(f"1ère valeur = {l_userInputA} / 2ème valeur = {l_userInputB}")

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

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez un exercice (1-13) : ")

        if choix == "1":
            exercice1()
        elif choix == "2":
            exercice2()
        elif choix == "3":
            exercice3()
        elif choix == "4":
            exercice4()
        elif choix == "5":
            exercice5()
        elif choix == "6":
            exercice6()
        elif choix == "7":
            exercice7()
        elif choix == "8":
            exercice8()
        elif choix == "9":
            exercice9()
        elif choix == "10":
            exercice10()
        elif choix == "11":
            exercice11()
        elif choix == "12":
            exercice12()
        elif choix == "13":
            print("\nAu revoir !")
            break  # Sort de la boucle while
        else:
            print("\nChoix invalide. Veuillez entrer un nombre entre 1 et 12.\n")
    
if __name__ == "__main__":
    main()
