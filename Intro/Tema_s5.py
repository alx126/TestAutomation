print('### Exerciții obligatorii ###\n')
print('### 1 ###\n')
# 1.Funcție care să calculeze și să returneze suma a două numere
def sumaNumerelor1(a, b):
    suma = a + b
    return suma


a = int(input("Introduceti un numar: "))
b = int(input("Introduceti un numar: "))
print(f'Suma numerelor este: {sumaNumerelor1(a, b)}.')


print('\n### 2 ###\n')
# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def numarParImpar(x):
    if x % 2 == 0:
        return True
    else:
        return False

x = int(input("Introduceti un numar: "))
print(f'{numarParImpar(x)}')


print('\n### 3 ###\n')
# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def numarCaractere(nume, prenume, nume_mijlociu):
    numar_caractere = len(nume) + len(prenume) + len(nume_mijlociu)
    print(f'Numarul total de caractere din numele complet este: {numar_caractere}.')


nume = input("Introduceti numele dvs: ")
prenume = input("Introduceti prenumele dvs: ")
nume_mijlociu = input("Introduceti numele dvs mijlociu: ")
numarCaractere(nume, prenume, nume_mijlociu)


print('\n### 4 ###\n')
# 4. Funcție care returnează aria dreptunghiului
def ariaDreptunghi(lungime, latime):
    aria = lungime * latime
    return aria

lungime = float(input("Lungimea dreptunghiului este: "))
latime = float(input("Latimea dreptunghiului este: "))
print(f'Aria dreptunghiului este: {ariaDreptunghi(lungime, latime)}.')


print('\n### 5 ###\n')
# 5. Funcție care returnează aria cercului
def ariaCerc(raza):
    Pi = 3.14
    aria = Pi * raza ** 2
    return aria

raza = float(input("Raza cercului este: "))
print(f'Aria cercului este: {ariaCerc(raza)}.')


print('\n### 6 ###\n')
# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.
def gasesteCaracter(c, text):
    if c in text:
        return True
    else:
        return False

text = input("Textul este:")
c = input("Introduceti caracterul cautat: ")

print(f'Exista caracterul in text? {gasesteCaracter(c, text)}.')


print('\n### 7 ###\n')
# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
def caractereInText(txt):
    carLower = 0
    carUpper = 0
    for i in range(len(txt)-1):
        if txt[i].islower():
            carLower += 1
        elif txt[i].isupper():
            carUpper += 1
    print(f'Caractere mici: {carLower}')
    print(f'Caractere mari: {carUpper}')
    # for car in txt:
    #     if car.islower():
    #         carLower += 1
    #     elif car.isupper():
    #         carUpper += 1
    # print(f'Caractere mici: {carLower}')
    # print(f'Caractere mari: {carUpper}')

txt = input("Introduceti textul: ")
caractereInText(txt)


print('\n### 8 ###\n')
# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
def numerePozitive(*args):
    numPoz = []
    for num in args:
        if num >= 0:
            numPoz.append(num)
    return numPoz


# print(numerePozitive(3,5, -1, -10, 100, 0, 2))
lista = input("Introduceti o lista de numere separate cu spatiu: ")
lista = lista.split()
for i in range(len(lista)):
    lista[i] = int(lista[i])

print(f'Lista cu numere pozitive este: {numerePozitive(*lista)}')


print('\n### 9 ###\n')
# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def comparNumere(x, y):
    if x > y:
        print(f'Primul număr ({x}) este mai mare decat al doilea nr ({y}).')
    elif y > x:
        print(f'Al doilea nr ({y}) este mai mare decat primul nr ({x}).')
    elif x == y:
        print("Numerele sunt egale.")

x = int(input("Primul nr este: "))
y = int(input("Al doilea nr este: "))

comparNumere(x, y)


print('\n### 10 ###\n')
# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

#numere = set()
def addNumberInSet(x, numere):
    if x in numere:
        print(f'Nu am adaugat numărul {x} în set. Acesta există deja')
        print(numere)
        return False
    else:
        numere.add(x)
        print(f'Am adaugat numărul nou {x} în set')
        print(numere)
        return True

numere = {1, 2, 3, 4, 5}
print(f'Avem urmatorul set de numere: {numere}')
x = int(input("Introduceti un nr in set: "))

print(addNumberInSet(x, numere))


print('### \nExerciții optionale ###\n')
print('### 1 ###\n')
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
def numarZile(luna):
    lista_luni = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie",
            "Noiembrie", "Decembrie"]
    if luna in lista_luni:
        if luna in ("Ianuarie", "Martie", "Mai", "Iulie", "August", "Octombrie", "Decembrie"):
            #print(f'Luna {luna} are 31 de zile.')
            return 31
        elif luna in ("Aprilie", "Iunie", "Septembrie", "Noiembrie"):
            #print(f'Luna {luna} are 30 de zile.')
            return 30
        elif luna == "Februarie":
            #print(f'Luna {luna} are 28/29 de zile.')
            return 28
    else:
        print("Numele introdus este incorect. Mai incercati o data.")

luna = input("Introduceti luna pt care doriti sa aflati nr de zile: ")
print(f'Luna {luna} are {numarZile(luna)} de zile.')


print('\n### 2 ###\n')
# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


print('\n### 3 ###\n')
# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
def dictNumere(*numere):
    dict_num = {}
    for i in range(10):
        dict_num[i] = numere.count(i)
    return dict_num


numere = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(f'{dictNumere(*numere)}')

for key, value in dictNumere(*numere).items():
    print(f'#{key} : {value}')


print('\n### 4 ###\n')
# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def maxNum(x, y, z):
    t = max(x, y, z)
    return t
x = int(input("Introduceti primul numar: "))
y = int(input("Introduceti al doilea numar: "))
z = int(input("Introduceti al treilea numar: "))
print(f'Numarul cel mai mare este: {maxNum(x, y, z)}.')


print('\n### 5 ###\n')
# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
def sumaNumere1(x):
    i = 0
    suma = 0
    while i <= x:
        suma += i
        i += 1
    return suma
x = int(input(f'Introduceti un numar: '))
print(sumaNumere1(x))

def sumaNumere(x):
    suma = 0
    for i in range(x+1):
        suma += i
    return suma
x = int(input(f'Introduceti un numar: '))
print(f'Suma nr de la 0 la {x} este: {sumaNumere(x)}.')
