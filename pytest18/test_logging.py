import logging
#ruland fisierul de mai jos se creaza un fisier de tip log
#ne va ajuta sa cream un obiect de tip log
def test_logging():

    logger = logging.getLogger(__name__) #__name__ va afisa numele testcaseului

    fileHandler = logging.FileHandler('logfile.log') #locatie
    #spunem in ce format vrem sa printam
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    #2021-04-03 16:23:26,035 : INFO : pytest18.test_logging : Information statemant
    fileHandler.setFormatter(formatter) #facem legatura cu obiectul nostru formatter

    logger.addHandler(fileHandler) #trebuie sa punem in ea filehandler object
    #filehandler este defapt fi;e location de la parent

    logger.setLevel(logging.INFO) # este important cu setam nivelul aici pt ca de acolo in jos o sa fie afisaty 
    logger.debug("A debug statemanet is executed")
    logger.info("Information statemant")
    logger.warning("Somthing is in warning mode")
    logger.error("a major error has happened")
    logger.critical("critical issue")