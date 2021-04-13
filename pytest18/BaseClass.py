import inspect
import logging

#codul l am scris in metoda
#vom defini acesta metoda in celelalte testcase uri
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)  # __name__ va afisa numele testcaseului

        fileHandler = logging.FileHandler('logfile.log')  # locatie
        # spunem in ce format vrem sa printam
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        # 2021-04-03 16:23:26,035 : INFO : pytest18.test_logging : Information statemant
        fileHandler.setFormatter(formatter)  # facem legatura cu obiectul nostru formatter

        logger.addHandler(fileHandler)  # trebuie sa punem in ea filehandler object
        # filehandler este defapt fi;e location de la parent

        logger.setLevel(logging.INFO)
        return logger