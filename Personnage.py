class Personnage:
    def __init__(self,pseudo : str, niveau : int =1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__point_de_vie = niveau
        self.__initiative = niveau

    def __str__(self):
        return f"Personnage {self.__pseudo} de niveau {self.__niveau} \\" \
            f"avec {self.__point_de_vie} points de vie et une initiative de {self.__initiative}"


    def attaque(self,opposant):
        pass

    def combat(self,opposant):
        pass

    def soin(self):
        self.__point_de_vie = self.__niveau

    def degats(self):
        return self.__niveau