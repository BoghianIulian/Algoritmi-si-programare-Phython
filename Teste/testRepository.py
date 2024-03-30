from Domeniu.clienti import Client
from Repository.clientiRepository import ClientRepository


def testAddClient():
    client_repo = ClientRepository()
    client = Client("11", "iulian", "123")

    client_repo.adauga(client)

    clienti = client_repo.get_all()
    assert len(clienti) == 1
    assert clienti[0].get_id_client() == "11"


def testModClient():
    client_repo = ClientRepository()
    client = Client("11", "iulian", "123")
    clientnou2 = Client("11", "andrei", "1234")

    client_repo.adauga(client)
    client_repo.modifica(clientnou2)

    clienti = client_repo.get_all()
    assert clienti[0].get_nume() == "andrei"


def testDellClient():
    client_repo = ClientRepository()
    client = Client("11", "iulian", "123")
    clientnou1 = Client("12", "andrei", "123")
    clientnou2 = Client("22", "iulian", "1234")

    client_repo.adauga(client)
    client_repo.adauga(clientnou2)
    client_repo.adauga(clientnou1)

    client_repo.sterge("12")
    assert len(client_repo.get_all()) == 2
