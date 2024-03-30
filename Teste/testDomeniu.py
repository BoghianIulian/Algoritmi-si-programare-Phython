from Domeniu.clienti import Client
from Domeniu.filme import Film
from Domeniu.clientifilme import ClientFilm


def testClient():
    client = Client("11", "iulian", "123")

    assert client.get_id_client() == "11"
    assert client.get_cnp() == "123"


def testClientSetteri():
    client = Client("11", "iulian", "123")

    client.set_id_client("12")
    assert client.get_id_client() == "12"

    client.set_cnp("231")
    assert client.get_cnp() == "231"


def testFilm():
    film = Film("1", "ted", "tare", "comedie")

    assert film.get_id_film() == "1"
    assert film.get_titlu() == "ted"


def testFilmSetteri():
    film = Film("1", "ted", "tare", "comedie")

    film.set_id_film("2")
    assert film.get_id_film() == "2"

    film.set_gen("fain")
    assert film.get_gen() == "fain"


def testClientFilm():
    clientfilm = ClientFilm("111", "11", "1")

    assert clientfilm.get_id_inchiriere() == "111"
    assert clientfilm.get_id_film() == "1"


def testClientFilmSetteri():
    clientfilm = ClientFilm("111", "11", "1")

    clientfilm.set_id_film("2")
    assert clientfilm.get_id_film() == "2"

    clientfilm.set_id_client("12")
    assert clientfilm.get_id_client() == "12"
