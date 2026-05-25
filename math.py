import matplotlib.pyplot as plt
import numpy as np

global PI 
PI = 3.141592653589793

def sin(x:float, ordre:int=20):
    assert ordre >= 0, "l'ordre dans le développement limité est supérieur ou égal à 0."
    x = x % (2*PI)
    somme = 0
    fact = 1
    n=0
    fin = (ordre+1)//2
    if 0 <= x < PI/2:
        # si x mod(2PI) est plus proche de 0 dl en 0:
        for k in range(fin): 
            terme = ((-1)**k * x**(2*k+1))/fact
            somme += terme
            fact = fact * (n+2) * (n+3)
            n += 2
        return somme
    elif PI/2 <= x < PI:
        if fin == 0:return 1
        for k in range(fin):
            terme = ((-1)**k * (x-PI/2)**(2*k))/fact
            somme += terme
            fact = fact * (n+1) * (n+2)
            n += 2
        return somme
    elif PI <= x < 3*PI/2:
        # DL en pi
        for k in range(fin):
            terme = ((-1)**(k+1) * (x-PI)**(2*k+1))/fact
            somme += terme
            fact = fact * (n+2) * (n+3)
            n += 2
        return somme
    elif 3*PI/2 <= x < 2*PI:
        # dl en 3PI/2
        if fin == 0:return -1
        for k in range(fin):
            terme = ((-1)**(k+1) * (x-3*PI/2)**(2*k))/fact
            somme += terme
            fact = fact * (n+1) * (n+2)
            n += 2
        return somme
def courbe_sin(max_x:int=100, pas:float=0.1, ordre:int=20):
    # trace la courbe du sinus avec un dl d'ordre=ordre, de x=-max_x à x=max_x qui espace les valeurs d'un pas.
    x_vals = np.arange(-max_x, max_x+1, pas)
    y_vals = np.zeros(len(x_vals), dtype=float)
    x = - max_x
    j = 0
    while x < max_x and j < len(y_vals):
        y = sin(x, ordre)
        y_vals[j] = y
        x += pas
        j += 1
    plt.plot(x_vals, y_vals)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Courbe représentative du sinus")
    plt.grid(True)
    plt.show()


def cos(x:float, ordre:int=20):
    assert ordre >= 0, "l'ordre dans le développement limité est supérieur ou égal à 0."
    if ordre==0:return 1
    x = x % (2*PI)
    if x == 0: return 1
    somme = 0
    fact = 1
    n=0 
    fin = (ordre+1)//2
    if 0 < x < PI/2:
        for k in range(fin):
            terme = ((-1)**k * x**(2*k))/fact
            somme += terme
            fact = fact * (n+1) * (n+2)
            n += 2
        return somme
    elif PI/2 <= x < PI:
        for k in range(fin):
            terme = ((-1)**(k+1) * (x-PI/2)**(2*k+1))/fact
            somme += terme
            fact = fact * (n+2) * (n+3)
            n += 2
        return somme
    elif PI <= x < 3*PI/2:
        for k in range(fin):
            terme = ((-1)**(k+1) * (x-PI)**(2*k))/fact
            somme += terme
            fact = fact * (n+1) * (n+2)
            n += 2
        return somme
    elif 3*PI/2 <= x < 2*PI:
        for k in range(fin):
            terme = ((-1)**k * (x-3*PI/2)**(2*k+1))/fact
            somme += terme
            fact = fact * (n+2) * (n+3)
            n += 2
        return somme

def courbe_cos(max_x:int=100, pas:float=0.1, ordre:int=20):
    # trace la courbe du cos de x=-max_x à x=max_x
    x_vals = np.arange(-max_x, max_x+1, pas)
    y_vals = np.zeros(len(x_vals), dtype=float)
    x = - max_x
    j = 0
    while x < max_x and j < len(y_vals):
        y = cos(x, ordre)
        y_vals[j] = y
        x += pas
        j += 1
    plt.plot(x_vals, y_vals)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Courbe représentative du cosinus")
    plt.grid(True)
    plt.show()


def menu():
    # menu d'affichage contextuel
    print(r"___  ___      _   _")    
    print(r"|  \/  |     | | | |")  
    print(r"| .  . | __ _| |_| |__")  
    print(r"| |\/| |/ _` | __| '_ \ ")
    print(r"| |  | | (_| | |_| | | |")
    print(r"\_|  |_/\__,_|\__|_| |_|")                  

    print("\n<=============== Quelle fonction souhaitez-vous afficher ? ===============>\n")
    print("\t(1) - sinus\n\t(2) - cosinus\n")
def params():
    try:
        borne = int(input("Sur quel intervalle souhaitez-vous affichez la courbe ? (choisissez la borne sup).\n:>"))
        pas = float(input("Choisissez le pas entre deux unité (par défaut 1)\n:>"))
        ordre = int(input("Choisissez l'ordre de précision du développement de la fonction\n:>"))
        return (borne, pas, ordre)
    except TypeError as t:
        print(f"{e}")
        return None
def main():
    menu()
    choix = input(":>")
    if choix == "1" or choix.lower() == "sinus":
        borne, pas, ordre = params()
        courbe_sin(borne, pas, ordre)
    elif choix == "2" or choix.lower() == "cosinus":
        borne, pas, ordre = params()
        courbe_cos(borne, pas, ordre)
    else:
        print("Fonction non prise en charge")

if __name__ == "__main__":
    main()
