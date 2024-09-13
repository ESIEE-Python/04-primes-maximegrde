"""Importe le module de maths pour la racine carrée"""
from math import sqrt
#### Fonction secondaire


def isprime(p):
    """Détermine si p est premier ou non en renvoyant vrai ou faux"""
    if p in (0,1):
        return False
    premier = True
    for d in range (2,int(sqrt(p))+1):
        if p%d ==0:
            premier = False
            break
    return premier


#### Fonction principale

def main():
    """appelle itérativement la fonction isprime pour p variant de 0 à 100"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n) is True:
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
