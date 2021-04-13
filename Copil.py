from Lectia6 import Calculator

class Copil(Calculator):
    num2 = 300
#inheritanvce
#from 5 [care este file name] import Calculator [care este numele clasei]
#class Copil(Calcultor) - clasa copil extinde si preai toate metodele de la clasa parinte calcultor

    def __init__(self):
        Calculator.__init__(self, 2, 5)

    def getCompleteData(self):
        return self.num2 + self.num + self.suma()

obj = Copil()
print(obj.getCompleteData())