from Domeniu.filme import Film


class FilmService:
    def __init__(self, film_repository):
        self.__film_repository = film_repository

    def get_all_filme(self):
        """
        Functia returneaza lista filmelor
        :return: o lista de obiecte de tipul Film
        """
        return self.__film_repository.get_all()

    def adauga(self, id_film, titlu, descriere, gen):
        """
        Functia adauga un film
        :param id_film: string
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return: nimic
        """
        film = Film(id_film, titlu, descriere, gen)
        self.__film_repository.adauga(film)

    def modifica(self, id_film, titlu_nou, descriere_nou, gen_nou):
        """
        Functia modifica un film
        :param id_film: string
        :param titlu_nou: string
        :param descriere_nou: string
        :param gen_nou: string
        :return: nimic
        """
        film_modificat = Film(id_film, titlu_nou, descriere_nou, gen_nou)
        self.__film_repository.modifica(film_modificat)

    def sterge(self, id_film):
        """
        Functia sterge un film
        :param id_film: string
        :return: nimic
        """
        self.__film_repository.sterge(id_film)

    def find_by_id(self, id_film):
        """
        Functia gaseste filmul cu un id dat
        :param id_film: string
        :return: o lista de obiecte de tipul Film, daca exista vreo unul cu id-ul dat, altfel None
        """
        return self.__film_repository.get_by_id(id_film)
