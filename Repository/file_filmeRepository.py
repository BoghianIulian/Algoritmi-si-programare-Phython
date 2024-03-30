from Domeniu.filme import Film
from Repository.filmeRepository import FilmRepository


class FilmFileRepository(FilmRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__readFile()

    def adauga(self, film):
        super().adauga(film)
        self.__writeFile()

    def modifica(self, film):
        super().modifica(film)
        self.__writeFile()

    def sterge(self, id_film):
        super().sterge(id_film)
        self.__writeFile()

    def __readFile(self):
        with open(self.__file_name, 'r') as f:
            for line in f:
                line=line.strip('\n')
                array = line.split(",")
                if not array[0] == "\n":
                    film = Film(array[0], array[1], array[2], array[3])
                    super().adauga(film)

    def __writeFile(self):
        with open(self.__file_name, 'w') as f:
            for film in self.get_all():
                f.write(f"{film.get_id_film()},{film.get_titlu()},{film.get_descriere()},{film.get_gen()}\n")
