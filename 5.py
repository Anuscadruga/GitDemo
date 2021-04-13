salut = "buna"

if salut == "buna":
    print(f"Ana iti spune {salut}")
else:
    print(f"Ana iti spune doar {salut}")

#for loop

list = [1,2, 3, 4, 5, 6, 8]

for numar in list:
    print(numar*2)
print(list)

#sum of first natural numbers

suma = 0
for numar in range(0, 10):
    suma += numar
print(suma)

for numar in range(0,10,2):
    print(f"numarul par este {numar}")
i = 10
while i > 0:
    print(i)
    i = i - 1

