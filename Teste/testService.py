from Repository.clientiRepository import ClientRepository
from Service.client_service import ClientService


def testAddClientService():
    client_repo = ClientRepository()
    clientService = ClientService(client_repo)
    clientService.adauga("11", "iulian", "123")

    clienti = clientService.get_all_clienti()
    assert len(clienti) == 1
    assert clienti[0].get_id_client() == "11"


def testModClientService():
    client_repo = ClientRepository()
    clientService = ClientService(client_repo)
    clientService.adauga("11", "iulian", "123")

    clienti = clientService.get_all_clienti()
    assert clienti[0].get_id_client() == "11"
    assert clienti[0].get_nume() == "iulian"


def testDelClientService():
    client_repo = ClientRepository()
    clientService = ClientService(client_repo)
    clientService.adauga("11", "iulian", "123")
    clientService.adauga("12", "andrei", "213")

    clientService.sterge("11")
    clienti = clientService.get_all_clienti()
    assert len(clienti) == 1
