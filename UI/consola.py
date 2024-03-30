class Consola:
    def __init__(self, inchiriere_service, client_service, film_service):
        self.__inchiriere_service = inchiriere_service
        self.__client_service = client_service
        self.__film_service = film_service

    def adauga_client(self):
        try:
            id_client = input("Introduceti id-ul clientului: ")
            nume = input("Introduceti numele clientului: ")
            cnp = input("Introduceti cnp-ul clientului: ")
            self.__client_service.adauga(id_client, nume, cnp)
        except KeyError as ke:
            print(ke)

    def adauga_film(self):
        try:
            id_film = input("Introduceti id-ul filmului: ")
            titlu = input("Introduceti titlul filmului: ")
            descriere = input("Introduceti descrierea filmului: ")
            gen = input("Introduceti genul filmului: ")
            self.__film_service.adauga(id_film, titlu, descriere, gen)
        except KeyError as ke:
            print(ke)

    def modifica_client(self):
        try:
            id_client = input("Introduceti id-ul clientului: ")
            nume = input("Introduceti numele clientului: ")
            cnp = input("Introduceti cnp-ul clientului: ")
            self.__client_service.modifica(id_client, nume, cnp)
        except KeyError as ke:
            print(ke)

    def modifica_film(self):
        try:
            id_film = input("Introduceti id-ul filmului: ")
            titlu = input("Introduceti titlul filmului: ")
            descriere = input("Introduceti descrierea filmului: ")
            gen = input("Introduceti genul filmului: ")
            self.__film_service.modifica(id_film, titlu, descriere, gen)
        except KeyError as ke:
            print(ke)

    def sterge_client(self):
        try:
            id_client = input("Introduceti id-ul clientului: ")
            self.__client_service.sterge(id_client)
        except KeyError as ke:
            print(ke)

    def sterge_film(self):
        try:
            id_film = input("Introduceti id-ul filmului: ")
            self.__film_service.sterge(id_film)
        except KeyError as ke:
            print(ke)

    def cauta_client(self):
        try:
            id_client = input("Introduceti id-ul clientului: ")
            return self.__client_service.find_by_id(id_client)
        except KeyError as ke:
            print(ke)

    def cauta_film(self):
        try:
            id_film = input("Introduceti id-ul filmului: ")
            return self.__film_service.find_by_id(id_film)
        except KeyError as ke:
            print(ke)

    def inchiriaza(self):
        try:
            id_inchiriere = input("Introduceti id-ul inchirierii: ")
            id_client = input("Introduceti id-ul clientului: ")
            id_film = input("Introduceti id-ul filmului: ")
            self.__inchiriere_service.inchiriaza(id_inchiriere, id_client, id_film)
        except KeyError as ke:
            print(ke)

    def returneaza(self):
        try:
            id_inchiriere = input("Introduceti id-ul inchirierii: ")
            id_client = input("Introduceti id-ul clientului: ")
            id_film = input("Introduceti id-ul filmului: ")
            self.__inchiriere_service.returneaza(id_inchiriere, id_client, id_film)
        except KeyError as ke:
            print(ke)

    def cele_mai_inchiriate(self):
        return self.__inchiriere_service.filme_inchiriate()

    def sort_clienti_dupa_nr_filme(self):
        return self.__inchiriere_service.clienti_inchiriat()

    def sort_clienti_dupa_nume(self):
        return self.__inchiriere_service.sortare_pt_nume()

    def primii_30per(self):
        return self.__inchiriere_service.primii()

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def afiseaza_meniu(self):
        print("1. Optiuni filme")
        print("2. Optiuni clienti")
        print("3. Optiuni inchirieri")

    def meniu_filme(self):
        print("1. Adauga film")
        print("2. Modifica film")
        print("3. Sterge film")
        print("4. Afiseaza toate filmele")
        print("5. Cauta film dupa id")
        print("6. Inchide program")

    def meniu_client(self):
        print("1. Adauga client")
        print("2. Modifica client")
        print("3. Sterge client")
        print("4. Afiseaza toti clientii")
        print("5. Cauta client dupa id")
        print("6. Inchide program")

    def meniu_inchirieri(self):
        print("1. Inchiriaza")
        print("2. Returneaza")
        print("3. Cele mai inchiriate filme")
        print("4. Clienti cu filme inchiriate ordonati dupa nume")
        print("5. Clienti cu filme inchiriate ordonati dupa nr de filme inchiriate")
        print("6. Primi 30% clienti cu filme inchiriate cu cele mai multe filme inchiriate")
        print("7. Afiseaza toate inchirierile")
        print("8. Inchide program")

    def Menu(self):
        while True:
            self.afiseaza_meniu()
            alegere = input("Introduceti alegerea: ")
            if alegere == "1":
                self.meniu_filme()
                optiune = input("Introduceti optiunea: ")
                if optiune == "1":
                    self.adauga_film()
                elif optiune == "2":
                    self.modifica_film()
                elif optiune == "3":
                    self.sterge_film()
                elif optiune == "4":
                    self.afiseaza(self.__film_service.get_all_filme())
                elif optiune == "5":
                    print(self.cauta_film())
                elif optiune == "6":
                    break
                else:
                    print("Optiune nu se gaseste in lista")
            elif alegere == "2":
                self.meniu_client()
                optiune = input("Introduceti optiunea: ")
                if optiune == "1":
                    self.adauga_client()
                elif optiune == "2":
                    self.modifica_client()
                elif optiune == "3":
                    self.sterge_client()
                elif optiune == "4":
                    self.afiseaza(self.__client_service.get_all_clienti())
                elif optiune == "5":
                    print(self.cauta_client())
                elif optiune == "6":
                    break
                else:
                    print("Optiune nu se gaseste in lista")
            elif alegere == "3":
                self.meniu_inchirieri()
                optiune = input("Introduceti optiunea: ")
                if optiune == "1":
                    self.inchiriaza()
                elif optiune == "2":
                    self.returneaza()
                elif optiune == "3":
                    print("Cele mai inchiriate filme sunt:", self.cele_mai_inchiriate())
                elif optiune == "4":
                    for i in self.sort_clienti_dupa_nume():
                        print(i)
                elif optiune == "5":
                    for i in self.sort_clienti_dupa_nr_filme():
                        print(i)
                elif optiune == "6":
                    self.primii_30per()
                elif optiune == "7":
                    self.afiseaza(self.__inchiriere_service.get_all_inchirieri())
                elif optiune == "8":
                    break
            else:
                print("Alegerea este invalida")
