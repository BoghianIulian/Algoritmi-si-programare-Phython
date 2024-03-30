class Film:
    def __init__(self, id_film, titlu, descriere, gen):
        self.__id_film = id_film
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id_film(self):
        return self.__id_film

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_gen(self):
        return self.__gen

    def set_id_film(self, id_film):
        self.__id_film = id_film

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_gen(self, gen):
        self.__gen = gen

    def __str__(self):
        return f"id: {self.__id_film}, titlu: {self.__titlu}, descriere: {self.__descriere}, gen: {self.__gen}"
