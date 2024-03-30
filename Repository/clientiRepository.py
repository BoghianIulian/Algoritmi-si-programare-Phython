class ClientRepository:
    def __init__(self):
        self.__clienti = {}

    def get_all(self):
        """
        Functia returneaza lista clientilor
        :return: o lista de tipul Client
        """
        return list(self.__clienti.values())

    def get_by_id(self, id_client):
        """
        Functia gaseste clientul cu un id dat
        :param id_client: string
        :return: un obiect de tipul Client, daca exista unul cu id-ul dat, altfel None
        """
        if id_client in self.__clienti:
            return self.__clienti[id_client]
        return None

    def adauga(self, client):
        """
        Functia adauga un client in dictionar
        :param client: obiect de tipul Client
        :return: nimic
        """
        if self.get_by_id(client.get_id_client()) is not None:
            raise KeyError("Exista deja un client cu id-ul dat")
        self.__clienti[client.get_id_client()] = client

    def modifica(self, client_nou):
        """
        Functia modifica un client din dictionar
        :param client_nou: obiect de tipul Client
        :return: nimic
        """
        if self.get_by_id(client_nou.get_id_client()) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat")
        self.__clienti[client_nou.get_id_client()] = client_nou

    def sterge(self, id_client):
        """
        Functia sterge un client din dictionar
        :param id_client: string
        :return: nimic
        """
        if self.get_by_id(id_client) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat")
        self.__clienti.pop(id_client)