from Domeniu.clienti import Client
from Repository.clientiRepository import ClientRepository


class ClientFileRepository(ClientRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__readFile()

    def adauga(self, client):
        super().adauga(client)
        self.__writeFile()

    def modifca(self, client):
        super().modifica(client)
        self.__writeFile()

    def sterge(self, id_client):
        super().sterge(id_client)
        self.__writeFile()

    def __readFile(self):
        with open(self.__file_name, 'r') as f:
            for line in f:
                line=line.strip('\n')
                array = line.split(",")
                if not array[0] == "\n":
                    client = Client(array[0], array[1], array[2])
                    super().adauga(client)

    def __writeFile(self):
        with open(self.__file_name, "w") as f:
            for client in self.get_all():
                f.write(f"{client.get_id_client()},{client.get_nume()},{client.get_cnp()},\n")
