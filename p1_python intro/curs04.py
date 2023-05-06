"""
Structuri repetitive = modalitati prin care putem executa un cod in mod repetat
pana cand o anumita conditie nu mai este indeplinita
sau pana cand nu ne mai incadram intr-un anumit interval

Exista patru tipuri de structuri repetitive:
 - while
 - do while (nu e in scopul cursului)
 - for
 - for each

Modalitati de control al structurilor repetitive:
 - break
 - continue
"""

"""
1. While (trad. engleza: cât timp)
Este o structura repetitiva in care se executa o serie de instructiuni cat timp expresia de evaluat este adevarata
De regula, variabila de control a while-ului se declara in afara acestuia.

Sintaxa generala:

                            while expresie_de_evaluat:
                                instructiune
"""

# Exercitiu 1: Vreau sa afisez pe ecran toate numerele de la 1 la 10
c = 1
while c <= 10:
    print(f"Numarul curent este: {c}")
    c += 1

# DEBUGGING = proces prin care analizam codul pentru a vedea datele din memorie in timp real
# Se poate face debug cu ajutorul breakpoint-urilor.
# Acestea se pun printr-un click langa numarul liniei de cod pt care vrem sa analizam datele
# Pentru debug, programul se va rula cu optiunea "Debug" in loc de "Run"

# Exercitiu 2: Vreau sa-i printez pe ecran pe cei 101 dalmatieni
i = 1
while i <= 101:
    print(f"Dalmatiunul curent are numarul: {i}")
    i += 1

# Exercitiu 3: Vreau sa printez suma numerelor de la 1 la 10
j = 0
suma = 0
while j <= 10:
    suma += j
    j += 1
print(f"Suma numerelor este: {suma}")

# Exercitiu 4: Vreau sa parcurg o lista de elemente si sa printez fiecare element
lista_studenti = ["Ramona", "Catalin", "Laurentiu", "George", "Ionut", "Dorin", "Catalin"]
i = 0
while i < len(lista_studenti):
    print(f"Studentul curent este: {lista_studenti[i]}")
    i += 1

# Exercitiu 5: Vreau sa il inlocuiesc pe Dorin cu Andreea
i = 0
while i < len(lista_studenti):
    if lista_studenti[i] == "Dorin":
        lista_studenti[i] = "Andreea"
    i += 1
print(f"Lista finala dupa ce Dorin a fost inlocuit este: {lista_studenti}")

# Exercitiu 5 - break: Vreau sa il inlocuiesc doar pe PRIMUL Catalin din lista cu Dorin
i = 0
while i < len(lista_studenti):
    if lista_studenti[i] == "Catalin":
        lista_studenti[i] = "Dorin"
        break
    i += 1
print(f"Lista dupa inlocuirea lui Catalin : {lista_studenti}")

# break se foloseste pentru a termina executia restului de iteratii indiferent daca conditia mai este indeplinita sau nu

"""
2. For = structura repetitiva care este utilizata atunci cand vrem sa parcurgem o lista
cu scopul de a printa elementele sau de a le modifica,
si respectiv atunci cand vrem sa executam un set de instructiuni de un numar specific de ori (range).

Elementele din care este compus un for:
- inceputul structurii repetitive (for)
- variabila de iteratie
- inceputul range-ului de parcurs (optional, default = 0)
- sfarsitul range-ului de parcurs(obligatoriu) - capatul superior nu este luat in considerare
- pasul range-ului (optional, default = 1)

Forma generala:

    for variabila_de_iteratie in range(inceput, sfarsit, pas):
        <instructiuni>

"""

# Exercitiu 1: Vreau sa parcurg numerele de la 0 la 10 si sa printez care sunt pare/impare:
for i in range(10):
    if i % 2 == 0:
        print(f'Numarul {i} este par')
    else:
        print(f"Numarul {i} este impar")

# nested list- embedded list - lista imbricata - matrice
lista_elemente = [
    [1, "test"],
    [2, "test1"],
    [3, "test2"]
]

for i in range(len(lista_elemente)):
    for j in range(len(lista_elemente[i])):
        print(f"Valoarea curenta a elementului din lista este: {lista_elemente[i][j]}")

# Vrem sa parcurgem o lista de elemente, sa zicem fructe. Vrem sa printem fiecare fruct pe ecran,
# si daca sunt caise sa le inlocuim cu gutui
lista_fructe = ["mere", "pere", "prune", "caise", "struguri"]
for i in range(len(lista_fructe)):
    if lista_fructe[i] == "caise":
        lista_fructe[i] = "gutui"
print(f"Lista de fructe de toamna este: {lista_fructe}")

# Avem o lista de culori. Si vrem sa vindem haine in culorile respective
# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
# adica, daca cumparatorul ne spune ca nu ii place culoarea x,
# ii vom exclude de la prezentare hainele in culoarea respectiva

lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
                            "orange", "verde", "indigo"]

liste_culori_de_exclus = ["rosu", "galben", "roz"]

for i in range(len(lista_culori_disponibile)):
    if lista_culori_disponibile[i] not in liste_culori_de_exclus:
        print(f"Va recomandam haina de culoare {lista_culori_disponibile[i]}")

# SAU

for i in range(len(lista_culori_disponibile)):
    if lista_culori_disponibile[i] in liste_culori_de_exclus:
        continue  # dam skip la restul instructiunilor din for
    print(f"Va recomandam haine in culoarea: {lista_culori_disponibile[i]}")

# continue este o modalitate prin care putem sa sarim peste iteratia curenta
# fara sa iesim din structura repetitiva

"""
foreach = structura repetitiva care este utila mai ales atunci cand vrem sa stergem elemente dintr-o lista
Diferenta intre for si foreach e ca la for stocam indexul in variabila de iteratie
iar la foreach stocam elementul din lista in variabila de iteratie

Sintaxa: 
            for denumire_element in lista_de_elemente:
                <instructiuni de executat>
        
"""
# EXEMPLU: DE CE NU E OK SA FOLOSIM FOR SIMPLU CAND STERGEM ELEMENTE:
# lista_animale = ["elefant", "maimuta", "leu", "pantera", "cocos"]
# for i in range(len(lista_animale)):
#     print(f"Indexul curent este: {i}")
#     print(f"Animalul curent este: {lista_animale[i]}")
#     print(f"Lungimea listei este este: {len(lista_animale)}")
#     if lista_animale[i] == "maimuta":
#         lista_animale.pop(i)
#         lista_animale[i] = "pinguin"
#
# print(f"Lista dupa eliminarea maimutei este: {lista_animale}")
# print(f"Lungimea listei este: {len(lista_animale)}")

# # de recomandat cand vrem sa modificam elemente sa nu folosim for
# # pentru ca dimensiunea listei nu este calculata in mod dinamic
# # si la un moment dar se va incerca sa se acceseze un element de la un index care nu mai exista
#
# # exemplu de foreach
lista_animale = ["elefant", "maimuta", "leu", "pantera", "cocos"]
for animal in lista_animale:
    print(f"indexul curent este: {lista_animale.index(animal)}")
    print(f"animalul curent este: {animal}")
    print(f"lungimea listei este este: {len(lista_animale)}")
    if animal == "maimuta":
        index = lista_animale.index(animal)
        lista_animale.remove(animal)
    print(f"Animalul curent este: {animal}")

print(f"Lista dupa eliminarea maimutei si inserarea pinguinului este: {lista_animale}")

"""
Exceptiile in Python
Ofera un mecanism eficient de identificare si rezolvare a erorilor care apar in timpul executiei unui program.
In limbajul Python exista posibilitatea tratarii exceptiilor prin stabilirea unei cai alternative de continuare
a executiei programului.

Exemple de exceptii:
- ValueError - se intampla cand o functie primeste alt tip de data ca parametru fata de cel asteptat
- AssertionError - cand conditia actuala din assert este diferita de cea asteptata
- SyntaxError - cand o sintaxa nu e respectata [ex: << while True print("yeah") >> - lipseste : dupa conditia while]
- ZeroDivisionError - cand incercam sa impartim un nr la 0

Tratarea exceptiilor se face cu blocul try - except - else - finally

Forma generala:

        try:
            <cod ce s-ar putea sa produca erori in timpul executiei>

        except(cu sau fara tipul erorii specificat, poate fi si except multiplu):
            <cod care se va rula daca prindem eroare>

        else:
            <cod care se executa daca nu au fost erori>

        finally:
            <cod care se executa indiferent s-a produs o Exceptie sau nu>

# try si except sunt obligatorii
# else si finally sunt optionale
"""

# Exercitiu cu WHILE:
# Sa se scrie un program care citeste N numere de la tastatura si va afisa suma acestora.
# Citirea numerelor se face pana cand numarul citit va fi egal cu 0.
# Datele de intrare sunt numere intregi
# Se vor trata Exceptiile de tip ValueError.
# Nota:
# Se va folosi un bloc try-except-else pentru citirea valorii de la tastatura si tratarea erorii
# daca nu se introduce un numar intreg

# try - except - else - finally

suma_numere = 0
caracter_citit = 'x'

while caracter_citit != 0:
    try:
        caracter_citit = int(input("Introduceti o valoare care va fi parte din suma: "))
    except ValueError:
        print("Ati introdus un alt tip de caracter.")
    else:
        suma_numere += caracter_citit


print(f"Suma numerelor citite este {suma_numere}")

# Exercitiu cu WHILE + time:
# Sa se afiseze ora curenta pentru 10 secunde consecutive, cu o pauza de 1 secunda intre fiecare afisare
# Nota: Se va importa modulul <time> si se va folosi functia localtime() din acesta,
# localtime() - functie ce returneaza informatii despre timpul curent (an, luna, zi, ora, minut, secunda, etc)
# pentru a instrui compilatorul sa intrerupa executarea codului pt o secunda, se va folosi instructiunea <time.sleep(1)>

import time

timp_curent = time.localtime()  # creaza o variabila de tip struct_time
print(f'Variabila local_time: {timp_curent}')

print(f'Este ora: {timp_curent.tm_hour}')
print(f'Este minutul: {timp_curent.tm_min}')
print(f'Este secunda: {timp_curent.tm_sec}')

secunde_numarate = 0

while secunde_numarate < 10:
    timp_curent = time.localtime()
    print(f'Este ora {timp_curent.tm_hour}:{timp_curent.tm_min}:{timp_curent.tm_sec}')
    time.sleep(1)
    secunde_numarate += 1

# Exercitiu piramida:
# Se introduce un numar n de la tastatura care va reprezenta inaltimea unei "piramide" de numere
# Sa se afiseze piramida de numere dupa urmatorul pattern:
#
# Pentru n = 3 e va afisa:
#
# 0
# 0 1
# 0 1 2
# 0 1 2 3

n = int(input("Inaltimea piramidei: "))

for i in range(n+1):
    for j in range(0, i+1, 1):
        print(f'{j}', end=" ")  # end = " " instruieste compilatorul sa puna spatiu in loc de rand nou la final de linie
    print('')  # punem linie noua dupa fiecare rand afisat

# Exercitiu *:
# Se introduce un numar n de la tastatura
# In consola se va *
# Sa se afiseze piramida de numere dupa urmatorul pattern:
#
# Pentru n = 5 e va afisa:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input("Inaltimea graficului: "))

for i in range(n):
    for j in range(i):
        print('* ', end="")  # end="" instruieste compilatorul sa nu puna rand nou la final de linie
    print('')  # punem linie noua dupa fiecare rand afisat

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')  # punem linie noua dupa fiecare rand afisat
