class ClientFilm:
    def __init__(self, id_inchiriere, id_client, id_film):
        self.__id_inchiriere = id_inchiriere
        self.__id_client = id_client
        self.__id_film = id_film

    def get_id_inchiriere(self):
        return self.__id_inchiriere

    def get_id_client(self):
        return self.__id_client

    def get_id_film(self):
        return self.__id_film

    def set_id_inchiriere(self, id_inchiriere):
        self.__id_inchiriere = id_inchiriere

    def set_id_client(self, id_client):
        self.__id_client = id_client

    def set_id_film(self, id_film):
        self.__id_film = id_film

    def __str__(self):
        return f"id: {self.__id_inchiriere}, clientul: {self.__id_client}, filmul inchiriat: {self.__id_film}"
