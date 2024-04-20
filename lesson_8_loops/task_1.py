# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
list1 = []; 
for i in range(1,11): list1.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for i in list1: 
    if(i % 2 == 0): print(str(i) + " ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
print()
i = 1
while(i <= 5): 
    print(str(i) + " ", end="")
    i+=1
print()
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
print()
dictionary = {"name": "John", "age": 30, "city": "New York"}
for i in dictionary.items(): print(str(i) + " ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
print()
list2 = [[10,20,30], [40,50,60], [70,80,90]]
for i in list2: 
    for j in i: 
        print(str(j) + " ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
print()
for i in range(1,6):
    print(str(i) + " ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
print()
print(list(enumerate(list1)))
print()
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
print(tuple(zip(list1, list2)))
print()
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
list1 = []; 
for i in range(1,11): list1.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
while list1[0] < 50:
    for i in range(len(list1)):
        list1[i]*=2
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
list1 = []; k = 1
while(k < 11):
    list1.append(k*k)
    k+=1
print(list1)
print()
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(11):
    print(str(7*i) + " ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
print()
list1 = []
for i in range(1, 6):
    for j in range(1, 6):
        list1.append((i,j))
for sublist in list1:
    print(str(sublist) + " ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
print()
for i in list1:
    if i[0] < i[1]:
        print(str(i) + " ", end="")
print()
# CODUL TĂU VINE MAI SUS:

# Folosind o buclă while, caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
print()
list1 = [4,9,30,6,2]; i = 0; k = 0
while(i<len(list1)):
    if list1[i] > 10:
        k = list1[i]
        print(k)
        break
    i+=1
if k == 0: print("Nu există valori mai mari decât 10")
print()
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
size = int(input("Introdeti dimensiunea pătratului:"))
for i in range(size):
    print()
    for j in range(size):
        print("*", end="")
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(7):
     print()
     for j in range(i):
         print(j+1, end="")
print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
print()
k = "54321"
for i in range(len(k),0,-1):
    print(k[:i])
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
k = "abcdefg"
print()
for j in range(len(k),0,-1):
    print(k[-j:])
print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(8):
    for j in range(8):
        if i%2 == 0:
            print("+-", end="")
        else: print("-+", end="")
    print()
print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
list1 = []
for i in range(3,244):
    if(243%i == 0):
        list1.append(i)
for i in range(1,len(list1)+1):
    print(" ".join(str(x) for x in list1[:i]))
for i in range(len(list1)-1,0,-1):
    print(" ".join(str(x) for x in list1[-i:]))
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
