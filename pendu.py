# Import de la fonction random pour le choix du mot
import random
import os

listeMots = ["chat", "chien", "pigeon", "dauphin", "souris", "girafe", "paon", "lion", "tigre", "hamster", "lapin", "papillon", "loup", "renard", "requin"]
mots = [mot.upper() for mot in listeMots]
mot_choisi = random.choice(mots)

# gestion du mot cache
mot_cache = ""
for nbrLettre in mot_choisi :
    mot_cache += "-"
nbrTiret = mot_cache.count("-")

# Creation dessin potence
potence = [
    """
    Jouez : 
                 -------
                |
                |
                |
                |
                |
                |
               ===
    """,
    """
    Jouez : 
                 -------
                |       |
                |
                |
                |
                |
                |
               ===
    """,
    """
    Jouez : 
                 -------
                |       |
                |       0
                |
                |
                |
                |
               ===
    """,
    """
    Jouez : 
                 -------
                |       |
                |       0
                |      / 
                |
                |
                |
               ===
    """,
    """
    Jouez : 
                 -------
                |       |
                |       0
                |      /|
                |
                |
                |
               ===
    """,
    """
    Jouez : 
                 -------
                |       |
                |       0
                |      /|\\
                |
                |
                |
               ===
    """,
    """
    Jouez : 
                 -------
                |       | 
                |       0
                |      /|\\   
                |       |
                |
                |
               ===
    """,
    """
    Jouez : 
                 -------
                |       |
                |       0
                |      /|\\
                |       |
                |      /
                |
               ===
    """,
    """
    Perdu... 
                 -------
                |       |
                |       0
                |      /|\\
                |       |
                |      / \\
                |
               ===
    """,
    """
    Victoire !!!
                 -------
                |       
                |       
                |      \\0/
                |       |
                |       |
                |    _ / \\
               ===
    """
]

# Gestion des tours
tour = 0
num= 1
nbrDeFaux = 0
defaite = "Tu as perdu... La mort est à tous les coins de rue"
victoire = "\nBRAVO, t'es un CHAMPION !!\n"
finDuJeu = False
pasDedans = "La lettre n'est pas dans le mot."

intro = "Bienvenue au jeu du pendu ! :)"
egal = "======================================"
ligne = "--------------------------------------"
espace = "\n"
print(espace)
print(intro)
print(espace)

while tour <= 8 :
    print(espace)
    print(egal)
    print(f'Tour : {num}')
    print(ligne)
    
    if finDuJeu == False :
        print(potence[tour])
        print(f'Le mot est "{mot_cache}".\nIl reste {nbrTiret} lettres inconnues.\n')
        inpLettre = input("Entrez une lettre : ").upper()

        while len(inpLettre) != 1:
            print("Vous devez entrer une seule lettre !")
            inpLettre = input("Entrez une lettre : ").upper()

    else :
        print(potence[8])
        print(defaite)  
        print("Tu feras mieux la prochaine fois")
        pasDedans = ""
        print(ligne)
        reset = input("Voulez-vous relancer ? y/n : ").upper()
        if reset == "Y":
            mot_choisi = random.choice(mots)
            mot_cache = ""
            for nbrLettre in mot_choisi:
                mot_cache += "-"
            nbrTiret = mot_cache.count("-")
            tour = 0
            num = 1
            nbrDeFaux = 0
            finDuJeu = False
            continue
        elif reset == "N" :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Nous souhaitons vous revoir prochainement :)")
            break
        
    while True:
        if inpLettre.isalpha():
            found_indices = [i for i, lettre in enumerate(mot_choisi) if inpLettre == lettre]
            if found_indices:
                for index in found_indices:
                    mot_cache = mot_cache[:index] + inpLettre + mot_cache[index + 1:].upper()
                    nbrTiret = mot_cache.count("-")
                    if nbrTiret == 0 :
                        print(espace)
                        print(egal)
                        print(victoire)
                        print(ligne)
                        tour = 9
                        print(potence[9])
                        print(f"Tu n'as fait que {nbrDeFaux} erreurs. Tu as du talent !")
                        print(ligne)
                        reset = input("Voulez-vous relancer ? y/n : ").upper()
                        if reset == "Y":
                            mot_choisi = random.choice(mots)
                            mot_cache = ""
                            for nbrLettre in mot_choisi:
                                mot_cache += "-"
                            nbrTiret = mot_cache.count("-")
                            tour = 0
                            num = 1
                            nbrDeFaux = 0
                            finDuJeu = False
                            continue
                        elif reset == "N" :
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Nous souhaitons vous revoir prochainement :)")
                            break
                                    
            else:
                print(pasDedans)
                nbrDeFaux += 1
                tour += 1
                num += 1
                if tour == 8 :
                    finDuJeu = True
            break
        else:
            print("L'entrée doit contenir seulement des lettres.")
            break
