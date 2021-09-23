import random

def choixMot(listeMot):
    return random.choice(listeMot)

def main():

    english_words = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding", "abject", "ablaze",
                    "able", "abnormal", "aboard", "aboriginal", "abortive", "abounding", "abrasive", "abrupt", "absent",
                    "absorbed", "absorbing", "abstracted", "absurd", "abundant", "abusive", "accept", "acceptable",
                    "accessible", "accidental", "account", "accurate", "achiever", "acid", "acidic", "acoustic",
                    "acoustics", "acrid", "act", "action", "activity", "actor", "actually", "ad hoc", "adamant",
                    "adaptable", "add", "addicted", "addition", "adhesive", "adjoining", "adjustment", "admire", "admit"]
   
   #dictionnaire permettant de lister si une lettre a été trouvé ou pas
    listeLettre={}
    motADeviner=choixMot(english_words)
    chance= 10

    #On met toutes les valeurs du dictionnaire à False car aucune lettre n'a été trouvé encore
    for i in range (len(motADeviner)):
        listeLettre[i]=False
    
    while chance!=0:

        print("Entrez une lettre pour deviner le mot, Il vous reste %d chance(s)"%chance)
        chance-=1 
        answer=input()

        #dès qu'une lettre a été trouvé on l'enregistre dans le dictionnaire, sa valeur passe de False à la lettre trouvée
        for i in range(len(motADeviner)):
            if answer== motADeviner[i]:
                listeLettre[i]=answer
        
        #on affiche les lettres trouvées et les lettres non trouvées sont remplacés par "_"
        for lettre in listeLettre.values():
            print("_", end="") if lettre is False else print(lettre,end="")

        print("\n")

        if False not in listeLettre.values():
            break

    if chance==0:
        print("Vous n'avez pas pu trouver le mot avec le nombre de chance limite")
    else:
        print("Bravo vous avez trouve le mot "+ motADeviner)

if __name__ == "__main__":
    main()
