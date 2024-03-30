from Domeniu.clienti import Client


class ClientService:
    def __init__(self, client_repository):
        self.__client_repository = client_repository

    def get_all_clienti(self):
        """
         Functia returneaza lista clientilor
         :return: o lista de obiecte de tipul Client
         """
        return self.__client_repository.get_all()

    def adauga(self, id_client, nume, cnp):
        """
        Functia adauga un client
        :param id_client: string
        :param nume: string
        :param cnp: string
        :return: nimic
        """
        client = Client(id_client, nume, cnp)
        self.__client_repository.adauga(client)

    def modifica(self, id_client, nume_nou, cnp_nou):
        """
        Functia modifica un client
        :param id_client: string
        :param nume_nou: string
        :param cnp_nou: string
        :return: nimic
        """
        client_modificat = Client(id_client, nume_nou, cnp_nou)
        self.__client_repository.modifica(client_modificat)

    def sterge(self, id_client):
        """
        Functia sterge un client
        :param id_client: string
        :return: nimic
        """
        self.__client_repository.sterge(id_client)

    def find_by_id(self, id_client):
        """
        Functia gaseste clientul cu un id dat
        :param id_client: string
        :return: o lista de obiecte de tipul Client, daca exista vreo unul cu id-ul dat, altfel None
        """
        return self.__client_repository.get_by_id(id_client)
