#observatie: orice fisier pytest incepe cu "test_" sau se termine cu _test
#in pytest, mereu metodele incep cu test_
#fircare bucata de cod trebuie inclusa in metode
#numele metodelor trebuie sa aiba un sens


#desi pare ca o metoda pe python, aceasta nu va afosa nimic desi pare scris in python.
#acesta nu poate fi rula ca un test normal
#va trebui sa selectam sa fie rulat ca un pytest
#se selecteaza din configuration> pytest in bin si apoi selectam ce test sa ruleze pytest in bin
#in pytest daca avem mai multe metode cu acelasi nume, o sa se suprascrie si va arata ca va rula 1, in python am fi avut eroare
import pytest

#pt a marca anumite metode pe care dorin sa le rulam, fiolosim @pytest.mark.smoke
#@pytest.mark.smoke - pytest trebuie important, mark - cuv cheie si smoke este denumirea, putem pune si altceva
@pytest.mark.smoke
#@pytest.mark.skip #daca scriem asa, vom da skip la acest test si ne si arata in consola ca am dat skip
#@pytest.mark.xfail #acest test va rula insa nu va da passed sau nu, doar va rula si nu va arata eroare, nu va raporta nimic
def test_firstProgram():
    #print("Hello")
    message = "hello"
    assert message == "Hi, test failed"

#test_1.py::test_firstProgram PASSED [100%]Hello #va afisa asta in pytest
#in pytest fiecare metoda este tradusa ca un test
#test_1.py::test_firstProgram FAILED                                      [100%]
#test_1.py:8 (test_firstProgram)
#hello != Hi, test failed

#Expected :Hi, test failed
#Actual   :hello

def test_secondProgram():
    a = 4
    b = 5
    assert a+2 ==6, "addition do not match"

#pt a rula din cmd avem urmatoarele comenzi:
#ma duc pe fisierul meu de pytest si dau copy path
#deschid cmd si pun comanda cd C:\Users\Ana-Maria\PycharmProjects1\PythonTesting\pytest18
#si asta de cu cd si path ma duce la C:\Users\Ana-Maria\PycharmProjects1\PythonTesting\pytest18
#de aici pot rula comenzile pt testele mele cu py.test
#py.test - ruleaza intregul pytest pe care il avem
#py.test test_1.py -v -s se ruleaza toate si ne arata care a trecut si care nu
#py.test -k Program -v -s - va rula doar testele(metodele) care contin program
# -k permite rulam dupa un cuvant din metoda
# -s - afiseaza log urile in output
#  -v afiseaza mai multe infiormatii in metadata
#py.test <filename>   se pot rula anumite fisiere de tip py test
# -m smoke - vine de marked adica rulat toate marcate cu @pytest.mark.smoke

def test_fixtures(setup):
    print("I will be executing test for fixtures")

def test_crossBrowser(crossBrowser): #pt ca o metoda sa ruleze un fixture, trebuie sa ii atribuim un paramentru
    print(crossBrowser)
#data driver si parametrazation can be done with retunr statements in tuple format
#cand definim fixture ca scope doar pt o clasa, va rula o data la inceput inainte ca clasa sa fie initializata si apoi la sf


#HTML REPORT FOR test cases

#py.test --html=report.html -s  - se ruleaza cpmanda asta in cmd , -s este pt log uri