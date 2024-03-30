from Repository.clientFilmRepository import ClientFilmRepository
from Domeniu.clientifilme import ClientFilm


class ClientFilmFileRepository(ClientFilmRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__readFile()

    def adauga(self, inchiriere):
        super().adauga(inchiriere)
        self.__writeFile()

    def sterge(self, id_inchiriere):
        super().sterge(id_inchiriere)
        self.__writeFile()

    def __readFile(self):
        with open(self.__file_name, 'r') as f:
            for line in f:
                line = line.strip('\n')
                array = line.split(",")
                if not array[0] == "\n":
                    inchiriere = ClientFilm(array[0], array[1], array[2])
                    super().adauga(inchiriere)

    def __writeFile(self):
        with open(self.__file_name, "w") as f:
            for inchiriere in self.get_all():
                f.write(f"{inchiriere.get_id_inchiriere()},{inchiriere.get_id_client()},{inchiriere.get_id_film()}\n")
