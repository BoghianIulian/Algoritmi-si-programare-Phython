class FilmRepository:
    def __init__(self):
        self.__filme = {}

    def get_all(self):
        """
        Functia returneaza lista filmelor
        :return: o lista de tipul Film
        """
        return list(self.__filme.values())

    def get_by_id(self, id_film):
        """
        Functia gaseste filmul cu un id dat
        :param id_film: string
        :return: un obiect de tipul Film, daca exista unul cu id-ul dat, altfel None
        """
        if id_film in self.__filme:
            return self.__filme[id_film]
        return None

    def adauga(self, film):
        """
        Functia adauga un film in dictionar
        :param film: obiect de tipul Film
        :return: nimic
        """
        if self.get_by_id(film.get_id_film()) is not None:
            raise KeyError("Exista deja un film cu id-ul dat")
        self.__filme[film.get_id_film()] = film

    def modifica(self, film_nou):
        """
        Functia modifica un film
        :param film_nou: un obiect de tipul Film
        :return: nimic
        """
        if self.get_by_id(film_nou.get_id_film()) is None:
            raise KeyError("Nu exista niciun film cu id-ul dat")
        self.__filme[film_nou.get_id_film()] = film_nou

    def sterge(self, id_film):
        """
        Functia sterge un film din dictionar
        :param id_film: string
        :return: nimic
        """
        if self.get_by_id(id_film) is None:
            raise KeyError("Nu exista niciun film cu id-ul dat")
        self.__filme.pop(id_film)
