print("Hello")
#https://www.journaldev.com/14036/python-data-types
#asa definesc comentarii

ana = 3 #tipul se ia automat
print(ana)
#in python avem data types insa nu trebuie mentionate automat

b, c, d = 5, 6.5, "Ana"
print(d)
print(f"{b} si mai avem nr {c}")
print("{} {}".format("value is ", b)) #value is  5 - folosim asta pt a concatena datatypes diferite
print(type(b)) #<class 'int'>

print(b+c) #asa se pot aduna
#listele permit orice tip de data si pot sa fie diferite
list = []
list.append("a")
list.append(1)
list.append("ana are mere")
print(list)
print(list[0])
print(list[-1])
print(list[0:2])
print(list[1:2])
print(list[:2])
print(list[0:])
list.insert(0, "am inserat ceva pe pozitia 0") #['am inserat ceva pe pozitia 0', 'a', 1, 'ana are mere']
list.append("sfarsit") #['am inserat ceva pe pozitia 0', 'a', 1, 'ana are mere', 'sfarsit']
print(list)
list[1]= "al doilea param" #am schimbat param de la index 1
del list[2] #am sters

#tuple sunt inumatabile spre deoseboire de liste, o data ce le creezi, nu le mai poti modifica
#in rest au aceleasi functii, mai putin ce implica modificarea ei
tuple = (1, 2, 3, 4, 5, 6)

#dictionarele sunt perechiile cheie valoare

dict = {"c":"hello", "abc":4, 5:6 }
print(dict[5]) #6
print(dict["c"]) #6
#print(dict["hello"]) # aici nu afiseaza pt ca el ia doar key primului element
dictionar1 = {}
dictionar1["ana"] = "maria"
dictionar1["vasrta"] = 29
print(dictionar1) #{'ana': 'maria', 'vasrta': 29}