#este fisierul care se denumeste mereu asa, conftest
#este un fisier care contine fixture, ca sa nu le duplicam in teste
#conftest se foloseste pt a generaliza fisture si sa le facem valabile pt toate testele
#fixtures - prerequest
# de obicei se folosesc la ce ruleaza la inceput, de ex la invocarea browserului sau confiration properties
import pytest


@pytest.fixture(scope="class") #va rula fisrt, ce este in clasa si apoi last
def setup():
    print("I will be executing first")
    yield #cuvand cheie, tot ce este trecut dupa, o sa fie printat la sf
    print("I will be executing last")
#cum functioneaza fixtures
#ce metoda definim in fixture, va foi executata prima, inainte de toate, in cazul nostru setup
#prima oara printeaza din setup unde am definit fixture-ul, am pus adnotatia @pytest.fixture()
#a 2 a oara printeaza ce este definit in metoda def test_fixtures(setup):
#def test_fixtures(setup):
    #print("I will be executing test for fixtures")

@pytest.fixture()
def dataLoad():
    print("cream un user profil")
    return ["Ana", "Maria", "anuscadruga@gmail.com"]
@pytest.fixture(params=["chrome","Firefox"]) #prima data va lua Chrome si va rula testul si apoi va lua firefix si va rula cu el
def crossBrowser(request):
    return request.param