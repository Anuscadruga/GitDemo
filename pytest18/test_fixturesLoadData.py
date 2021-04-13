import pytest

from pytest18.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class DataloadExample(BaseClass): #am spus aici ca mosteneste BaseClass si de aici vom mostenii formatul de log

    def editProfile(self, dataLoad): #desi mentionam la inceputul clasei sa folosim dataLoad, declarat global, insa trebuie sa l declaram si in metoda, dupa self
        print(dataLoad[1]) #afiseaza al 2 lea index
        log = self.getLogger()
        log.info(dataLoad[0])