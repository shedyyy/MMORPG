import sys
from Personnage import Personnage
def main():
    p : Personnage = Personnage("Merlin")
    print(f"{p} fait {p.degats()} dégats")

    p2 : Personnage = Personnage("Coman", 45)
    print(f"{p2} fait {p2.degats} dégats")

    

if __name__ == "__main__":
    sys.exit(main())