import random

def Random(start,end):
    return random.randint(start,end)

def main():
    x=Random(0,9)

    while (True):
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
