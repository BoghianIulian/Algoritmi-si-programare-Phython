from Domeniu.clientifilme import ClientFilm
from Repository.clientiRepository import ClientRepository
from Repository.filmeRepository import FilmRepository


class ClientFilmService:
    def __init__(self, inchiriere_repository, client_repository: ClientRepository, film_repository: FilmRepository):
        self.__inchiriere_repository = inchiriere_repository
        self.__client_repository = client_repository
        self.__film_repository = film_repository

    def get_all_inchirieri(self):
        """
         Functia returneaza lista inchirierilor
         :return: o lista de obiecte de tipul Inchirieri
         """
        return self.__inchiriere_repository.get_all()

    def inchiriaza(self, id_inchiriere, id_client, id_film):
        """
        Functia adauga o inchiriere
        :param id_inchiriere: string
        :param id_client: string
        :param id_film: string
        :return: nimic
        """
        if self.__client_repository.get_by_id(id_client) is None or self.__film_repository.get_by_id(id_film) is None:
            raise KeyError("Eroare: Nu exista clientul ori filmul cu id-ul respectiv")
        else:
            inchiriere = ClientFilm(id_inchiriere, id_client, id_film)
            self.__inchiriere_repository.adauga(inchiriere)

    def returneaza(self, id_inchiriere, id_client, id_film):
        if self.__client_repository.get_by_id(id_client) is None or self.__film_repository.get_by_id(id_film) is None:
            raise KeyError("Eroare: Ori clientul nu exista ori nu a inchiriat filmul cu id-ul respectiv")
        else:
            self.__inchiriere_repository.sterge(id_inchiriere)

    def filme_inchiriate(self):
        count = {}
        for element in self.__inchiriere_repository.get_all():
            if element.get_id_film() in count:
                count[element.get_id_film()] += 1
            else:
                count[element.get_id_film()] = 1
        maxim = 0
        lista = []
        for index in count.keys():
            if count[index] > maxim:
                maxim = count[index]
        for index in count.keys():
            if count[index] == maxim:
                lista.append(index)
        return lista

    def counter(self):
        count = {}
        for element in self.__inchiriere_repository.get_all():
            if element.get_id_client() in count:
                count[element.get_id_client()] += 1
            else:
                count[element.get_id_client()] = 1
        return count

    def clienti_inchiriat(self):
        count = self.counter()
        lista1 = []
        lista2 = []
        for index in count.keys():
            lista1.append(count[index])
        lista1.sort()
        index2 = 0
        while index2 < len(lista1) - 1:
            if lista1[index2] == lista1[index2 + 1]:
                lista1.pop(index2)
                index2 = index2 - 1
            index2 = index2 + 1
        for index in lista1:
            for k in count.keys():
                if index == count[k]:
                    lista2.append(self.__client_repository.get_by_id(k))
        return lista2

    def nume_client_inchiriere(self, id_client):
        lista = self.__client_repository.get_all()
        for client in lista:
            if client.get_id_client() == id_client:
                return client.get_nume()

    def sortare_pt_nume(self):
        lista = self.__client_repository.get_all()
        lista_noua = []
        for client in lista:
            lista_noua.append(client.get_nume())
        lista_noua.sort()
        count = self.counter()
        lista1 = []
        lista2 = []
        for index in count.keys():
            lista1.append(index)
        for nume in lista_noua:
            for indici in lista1:
                if nume == self.nume_client_inchiriere(indici):
                    lista2.append(self.__client_repository.get_by_id(indici))
        return lista2

    def primii(self):
        count = self.counter()
        lista1 = []
        lista2 = []
        rezultat1 = []
        rezultat2 = []
        for index in count:
            lista1.append(count[index])
        lista1.sort(reverse=True)
        per = int((30 * len(lista1)) / 100)
        for index in lista1:
            if per > 0:
                for k in count:
                    if index == count[k] and per > 0:
                        lista2.append(k)
                        per = per - 1
        for el in lista2:
            rezultat1.append(self.nume_client_inchiriere(el))
            rezultat2.append(count[el])
        for index in range(len(lista2)):
            print(rezultat1[index], rezultat2[index])
