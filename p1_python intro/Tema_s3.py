print('### Exercitii obligatorii ###\n ')

print('### 1 ###\n ')

# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# a. Afiseaz-o
# b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
# varianta actuala (inversata)
# c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
# inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
# asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
# varianta inițială
# Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
# suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
# suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
# găsesc utilitatea în funcție de ce ne dorim in acel moment.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f'Notele muzicale sunt: {note_muzicale}.')

note_muzicale = note_muzicale[::-1]
print(f'Lista inversata cu slicing este: {note_muzicale}.')

note_muzicale.reverse()
print(f'Lista inversata cu functia reverse() devine: {note_muzicale}.')

print('\n### 2 ###\n ')

# 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.

print(f'Nota do apare in lista de {note_muzicale.count("do")} ori.')

print('\n### 3 ###\n ')

# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

lista1.extend(lista2)
print(f'Lista extinsa devine: {lista1}.')

for x in lista2:
    lista1.remove(x)
print(f'Lista micsorata devine: {lista1}.')

for x in lista2:
    lista1.append(x)
print(f'Lista marita devine: {lista1}.')

for x in lista2:
    lista1.remove(x)
print(f'Lista micsorata devine: {lista1}.')


lista1 = lista1 + lista2
print(f'Lista unificata devine: {lista1}.')

print('\n### 4 ###\n ')

# 4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
# folosind o functie si apoi afiseaza din nou lista

lista1.sort()
print(f'Dupa sortare lista devine: {lista1}')

lista1.remove(0)
print(f'Lista din care am sters elementul 0 este: {lista1}.')

print('\n### 5 ###\n ')
# 5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
# urmatoarele:
# - Lista este goala (IF)
# - Lista nu este goala (ELSE)

lista1.insert(0, 0)

if len(lista1) == 0:
    print(f'Lista este goala.')
else:
    print(f'Lista nu este goala.')

print('\n### 6 si 7 ###\n ')
# 6. Foloseste o functie care sa goleasca lista de la exercitiul 3
# 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
# afiseze ca lista e goala

lista1.clear()
if len(lista1) == 0:
    print(f'Lista este goala.')
else:
    print(f'Lista nu este goala.')

print(' \n ### 8 ###\n ')

# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
# afisezi Elevii (cheile)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(f'Elevii sunt urmatorii: {dict1.keys()}.')

print(' \n ### 9 ###\n ')

# 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie

print(f'Ana a luat nota {dict1["Ana"]}.')
print(f'Gigel a luat nota {dict1["Gigel"]}.')
print(f'Dorel a luat nota {dict1["Dorel"]}.')

print(' \n ### 10 ###\n ')

# 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# - Modifica nota lui Dorel in 6
# - Printeaza nota lui dupa modificare

dict1['Dorel'] = 6
print(f'In urma contestatiei Dorel a primit nota {dict1.get("Dorel")}.')

print(' \n ### 11 ###\n ')

# 11. Imagineaza-ti ca Gigel se transfera din clasa.
# - Cauta o functie care sa il stearga
# Vine un coleg nou.
# - Adaugati-l in lista pe Ionica, cu nota 9
# - Printati dictionarul cu noii elevi

print(dict1)
dict1.pop("Dorel")
dict1["Ionica"] = 9
print(f'In urma modificarilor dictionarul arata astfel: {dict1}')

print(f'{dict1.items()}')

print(' \n ### 12 ###\n ')

# 12. Ai urmatoarele seturi:
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)
# Seturile nu accepta duplicate, de aceea valoarea "luni" va fi afisata o singura data
# Seturile nu sunt ordonate, de aceea, la fiecare vizualizare, ordinea elementelor din set se modifica


print(' \n ### 13 ###\n ')

# 13. Foloseste un if si verifica daca:
# - Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
# regasesc intre elementele din setul zile_sapt)
# - Weekend nu este un subset al zilelor din sapt
# Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
# punct de mai sus va fi un boolean

if weekend.issubset(zile_sapt):
    print(f'Weekend este un subset al zilelor din saptamana: {weekend.issubset(zile_sapt)}.')
else:
    print(f'Weekend nu este un subset al zilelor saptamanii.')

if not weekend < zile_sapt:
    print('Weekend nu este un subset al zilelor din saptamana.')
else:
    print('Weekend este un subset al zilelor din saptamana.')

print(' \n ### 14 ###\n ')

# 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
# sunt in weekend si invers)

print(f'Elementele care sunt in zile_sapt si nu sunt in weekend sunt: {zile_sapt - weekend}.')

if weekend - zile_sapt > set():
    print(f'Elementele care sunt in weekend si nu sunt in zile_sapt sunt: {weekend - zile_sapt}.')
else:
    print(f'Toate elementele din weekend se regasesc in zile_sapt. ')

print(' \n ### 15 ###\n ')

# 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
# ambele seturi). Hint: Va puteti folosi de o functie

print(f'Elementele care se afla in ambele seturi sunt: {weekend & zile_sapt}.')

zile_comune = zile_sapt.intersection(weekend)
print(f'Elementele care se afla in ambele seturi sunt: {zile_comune}.')

print('\n\n### Exercitii optionale ###\n ')

print('### 1 ###\n ')

# 1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
# - Declara o lista cu 5 jucatori: lista_jucatori_teren
# - Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
# - Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
# - Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
# - SCHIMBARI_MAX va fi o constanta cu valoarea 3

# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
# - Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
# teren
# - Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
# - Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
# de rezerva
# - Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
# variabilelor voastre)
# Daca jucatorul pe care vrem sa il schimbam nu e in teren:
# - Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Altfel, afisati ecran: ‘mai aveti z schimbari’
# Google search hint: “how to check if item is in list python”

lista_jucatori_teren = ['marin', 'sorin', 'george', 'alin', 'paul']
lista_jucatori_rezerva = ['mihai', 'alexe', 'cristi', 'bogdan', 'viorel']
lista_jucatori_scosi = []
SCHIMBARI_MAX = 3
Schimbari_efectuate = 0


x = lista_jucatori_teren[4]
print(x)

y = lista_jucatori_rezerva[0]
print(y)

if SCHIMBARI_MAX - Schimbari_efectuate > 0:
    if x in lista_jucatori_teren:
        if y in lista_jucatori_rezerva and y not in lista_jucatori_scosi:
            lista_jucatori_teren.remove(x)
            lista_jucatori_rezerva.remove(y)
            lista_jucatori_scosi.append(x)
            lista_jucatori_teren.append(y)
            Schimbari_efectuate += 1
            Schimbari_ramase = SCHIMBARI_MAX - Schimbari_efectuate

            print(f'Schimbari efectuate: {Schimbari_efectuate}')
            print(f'Schimbari ramase: {Schimbari_ramase}')
            print(f'Jucatori in teren: {lista_jucatori_teren}')
            print(f'Jucatori de rezerva: {lista_jucatori_rezerva}')
            print(f'Jucatori scosi: {lista_jucatori_scosi}')
            print(f'A intrat {y}, a iesit {x}. Mai aveti {Schimbari_ramase} schimbari.')
        else:
            print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu e in lista de rezerve.')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu e in teren.')
else:
    print(f'Ati efectuat deja nr maxim de schimbari.')


##### WHILE #####
print('\n\n "WHILE"\n')

while Schimbari_ramase > 0:
    jucator_scos = input(f'Va iesi jucatorul: {lista_jucatori_teren}: ')
    if jucator_scos in lista_jucatori_teren:
        jucator_intrat = input(f'Jucatorul {jucator_scos} va fi inlocuit de {lista_jucatori_rezerva}: ')
        if jucator_intrat in lista_jucatori_rezerva and jucator_intrat not in lista_jucatori_scosi:
            lista_jucatori_teren.remove(jucator_scos)
            lista_jucatori_rezerva.remove(jucator_intrat)
            lista_jucatori_scosi.append(jucator_scos)
            lista_jucatori_teren.append(jucator_intrat)
            Schimbari_efectuate += 1
            Schimbari_ramase = SCHIMBARI_MAX - Schimbari_efectuate

            print(f'Schimbari efectuate: {Schimbari_efectuate}')
            print(f'Schimbari ramase: {Schimbari_ramase}')
            print(f'Jucatori in teren: {lista_jucatori_teren}')
            print(f'Jucatori de rezerva: {lista_jucatori_rezerva}')
            print(f'Jucatori scosi: {lista_jucatori_scosi}')

            print(f'A intrat {jucator_intrat}, a iesit {jucator_scos}.\nMai aveti {Schimbari_ramase} schimbari.')

        elif jucator_intrat not in lista_jucatori_rezerva and jucator_intrat not in lista_jucatori_scosi:
            print(f'Jucatorul {jucator_intrat} nu se afla in lista de rezerve.')
        else:
            print(f'Nu se poate efectua schimbarea.')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_scos} nu e in teren.')

if Schimbari_ramase == 0:
    print(f'Ati efectuat toate schimbarile disponibile.')


