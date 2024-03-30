class Client:
    def __init__(self, id_client, nume, cnp):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp

    def get_id_client(self):
        return self.__id_client

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def set_id_client(self, id_client):
        self.__id_client = id_client

    def set_nume(self, nume):
        self.__nume = nume

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def __str__(self):
        return f"id: {self.__id_client}, nume: {self.__nume}, CNP: {self.__cnp}"