import random

def Random(start,end):
    return random.randint(start,end)

def main():

    print("Veuillez entrer le numéro de départ")
    start=int(input())

    while start<0:    
        print("Le numéro ne peut pas être négatif")
        start=int(input())
        
    print("Veuillez entrer le numéro d'arrivée")
    end=int(input())

    while end<start:    
        print("Le numéro ne peut pas être inférieur au numéro d'arrivée")
        end=int(input())

    x=Random(start,end)

    while (True):
        print("Devinez le numéro")
        answer=int(input())

        if answer==x:
            print("Vous avez trouvé")
            break

        elif answer<x:
            print("Le nombre est plus grand")
        elif answer>x:
            print("Le nombre est plus petit") 

if __name__ == "__main__":
    main()
