import random

def choixOrdi(listeOption):

    return random.choice(listeOption)

def Vainqueur(choixOrdi,choixJoueur):

    decision="L'ordinateur a joue "+choixOrdi+", vous avez perdu"
    if(choixOrdi==choixJoueur):
        decision="Egalite"
    elif (choixJoueur, choixOrdi) in {('Pierre', 'Ciseaux'), ('Ciseaux','Feuille'), ('Feuille', 'Pierre') }:
        decision="Vous avez gagne"
    return decision

def main():

    while (True):

        listeOption =["Pierre","Feuille","Ciseaux"]

        print("Choisissez entre Pierre, Feuille, Ciseaux")
        answer=input()

        while answer not in listeOption:
            print("Choix invalide, option disponible: Pierre, Feuille, Ciseaux")
            answer=input()

        print(Vainqueur(choixOrdi(listeOption), answer)+"\nVoulez vous rejouer ? (o/n)")

        rejouer=input()
        if (rejouer=='n'):
            break

if __name__ == "__main__":
    main()
