class ClientFilmRepository:
    def __init__(self):
        self.__inchirieri = {}

    def get_all(self):
        """
        Functia returneaza lista inchirierilor
        :return: o lista de tipul Inchiriere
        """
        return list(self.__inchirieri.values())

    def get_by_id(self, id_inchiriere):
        """
        Functia gaseste inchirierea cu un id dat
        :param id_inchiriere: string
        :return: un obiect de tipul Inchiriere, daca exista unul cu id-ul dat, altfel None
        """
        if id_inchiriere in self.__inchirieri:
            return self.__inchirieri[id_inchiriere]
        return None

    def adauga(self, inchiriere):
        """
        Functia adauga o inchiriere in dictionar
        :param inchiriere: obiect de tipul Inchiriere
        :return: nimic
        """
        if self.get_by_id(inchiriere.get_id_inchiriere()) is not None:
            raise KeyError("Exista deja o inchiriere cu id-ul dat")
        self.__inchirieri[inchiriere.get_id_inchiriere()] = inchiriere

    def modifica(self, inchiriere_noua):
        """
        Functia modifica o inchiriere din dictionar
        :param inchiriere_noua: obiect de tipul Inchiriere
        :return: nimic
        """
        if self.get_by_id(inchiriere_noua.get_id_inchiriere()) is None:
            raise KeyError("Nu exista nicio inchiriere cu id-ul dat")
        self.__inchirieri[inchiriere_noua.get_id_inchiriere()] = inchiriere_noua

    def sterge(self, id_inchiriere):
        """
        Functia sterge o inchiriere din dictionar
        :param id_inchiriere: string
        :return: nimic
        """
        if self.get_by_id(id_inchiriere) is None:
            raise KeyError("Nu exista nicio inchiriere cu id-ul dat")
        self.__inchirieri.pop(id_inchiriere)