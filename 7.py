#read and write files
#file = open('text.txt') #daca este localizat intr un alt director, trebuie sa ii punem intregul path
#file.read() #ne ajuta sa citim ce este in fisier, dar nu afiseaza ce citeste
#print(file.read()) #afiseaza tot ce este in fiseir
#print(file.read(2)) #afiseaza doar primele 2 caractere
#print(file.readline()) #citeste prima linie
#print(file.readline()) #citest linia 2


#line = file.readline()
#while line != "": #asa verificam daca avem am ajuns la finalul fisierului si printam si fiecare linie
    #print(line)
    #line = file.readline() #aici se citeste linia 2 si tot asa
#readlines() # va citi doc insa il va stoca intr o lista [a, b, c, 4, 5] si apoi o putem citi linie cu linie prin iteratie

#for line in file.readlines():#daca folosim readlines, pt a parcurge lista, o iteram
    #print(line)

#file.close()  # un fisier deschis, trebuie si inchis

#scrierea datelor in fisiere
#exercitiu
#citeste fisierul si stocheaza toate liniile in lista
#reverse the list
#write the line back to the file
with open('text.txt', 'r') as reader:#'r' - este read mode- citeste  #chestia asta inlocuieste deschidere si inchidere file = open('text.txt') si file.close()
    content = reader.readlines() #['ana are mere0\n', 'subita1\n', 'lavinia2\n', 'g3\n', 't4\n', 't5\n', 't6']
    #print(content)
    #content.reverse()
    #print(content)
    reversed(content) #['t6', 't5\n', 't4\n', 'g3\n', 'lavinia2\n', 'subita1\n', 'ana are mere0\n'], el nu modifica lista
    with open("text.txt", 'w') as writer: #w de la write
        for line in reversed(content):
            writer.write(line)
