from Repository.file_filmeRepository import FilmFileRepository
from Service.client_service import ClientService
from Service.film_service import FilmService
from Service.clientfilm_service import ClientFilmService
from Teste.All_Tests import All_Tests
from UI.consola import Consola
from Repository.file_clientiRepository import ClientFileRepository
from Repository.file_clientfilmRepository import ClientFilmFileRepository


def meniu():
    client_repository = ClientFileRepository("Data/clienti")
    film_repository = FilmFileRepository("Data/filme")
    inchiriere_repository = ClientFilmFileRepository("Data/inscrieri")
    client_service = ClientService(client_repository)
    film_service = FilmService(film_repository)
    inchiriere_service = ClientFilmService(inchiriere_repository, client_repository, film_repository)
    consola = Consola(inchiriere_service, client_service, film_service)
    consola.Menu()

All_Tests()
meniu()
