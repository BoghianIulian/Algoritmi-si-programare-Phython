from unittest import TestCase

from Domeniu.clienti import Client

class TestClient(TestCase):
    def setUp(self):
        self.client = Client("22" , "boghi" , "1234")

    def test_id(self):
        self.assertTrue(self.client.get_id_client() == "22" , "ID-ul clientrului trebuie sa fie 22")
        self.client.set_id_client("21")
        self.assertTrue(self.client.get_id_client() == "21" , "ID-ul clientului trebuie sa fie 21")

    def test_nume(self):
        self.assertTrue(self.client.get_nume() == "boghi" , "numele clientului trebuie sa fie boghi")
        self.client.set_nume("boghian")
        self.assertTrue(self.client.get_nume() == "boghian")

    def test_cnp(self):
        self.assertTrue(self.client.get_cnp() == "1234" , "CNP-ul clientrului trebuie sa fie 1234")
        self.client.set_cnp("12345")
        self.assertTrue(self.client.get_cnp() == "12345")
