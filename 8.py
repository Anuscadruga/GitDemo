item = 4

#if item == 0:
    #raise Exception("cosul este gol")

#assert(item == 0) #va retunra AssertionError
#asemanator cu try catch din JAVA
try:
    with open("text.txt", 'r') as reader:
        reader.read()
except:
    print("am ajuns aici pt ca s a aruncat o exceptie")

try:
    with open("file.txt", 'r') as reader:
        reader.read()
except Exception as e: #e - este ce afiseaza budefault python
    print(e)
finally:
    print("asta se executa indiferent daca avem sau nu exceptie")
#uneori aceste blocuri de try except sunt utile atunci cand avem pop up uri si atunci cand apara un pop up 