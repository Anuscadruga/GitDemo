class Calculator:
    num = 200 #acest se poate chema cu calculator.num
#variabilele in metode se cheama cu self.prim

    def __init__(self, a, b):
        print("constructorul este chemat automat cand un obiect este creat")
        self.prim = a #prim si secund sunt variabilele pe care le dam unui oboect cannd il cream Calculator (4,5)
        self.secund = b

    def getData(self):
        print("acum se executa o metoda a clasei")

    def suma(self):
        return self.prim + self.secund + self.num

obiect1 = Calculator(2, 3)
obiect1.getData()
print(obiect1.num)
print(obiect1.suma())

obiect2 = Calculator(4, 5)
obiect2.getData()
print(obiect2.num)

#inheritanvce
#from 5 [care este file name] import Calculator [care este numele clasei]
#class Copil(Calcultor) - clasa copil extinde si preai toate metodele de la clasa parinte calcultor

str = "AnaMaria.Druga"
var = str.split(".")
str1 = " Ana "
#nu avem metoda trim si metoda strip
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())