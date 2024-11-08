"""
efze
"""
def isprime(p):
    """ 
    Doc
    """
    if p <=1:
        return False
    for i in range(2,int(p**0.5)+1): ##Il suffit de tester jusqu'à la racine carré du p
        if p % i ==0 :
            return False
    return True
#### Fonction principale

def main():
    """
        Doc
        """
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
