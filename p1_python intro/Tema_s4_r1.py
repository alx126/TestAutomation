print('### Exercitii obligatorii ###\n ')

print('### 1 ###\n ')
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
i = 0
for i in range(len(masini)):
    if masini[i] == "Volvo":
        print(f'Masina mea preferata este {masini[i]}.')
        break

for masina in masini:
    if masina == "Opel":
        print(f'Masina mea preferata este {masina}.')

i = 0
while i < len(masini):
    if masini[i] == "BMW":
        print(f'Masina mea preferata este {masini[i]}.')
        break
    i += 1


print('\n### 2 ###\n ')
# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

i = 0
for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
    # print(masini[i])
else:
    print(f'Lista de masini este: {masini}.')

# print(masini[len(masini)-2].upper())


print('\n### 3 ###\n ')
# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print(f'Am gasit masina dvs {masina}.')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam.')


print('\n### 4 ###\n ')
# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

for masina in masini:
    if masina == 'Lăstun':
        continue
    elif masina == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina {masina}')


print('\n### 5 ###\n ')
# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
#
# masini_vechi = []
#
# for masina in masini:
#     if masina == 'Lăstun':
#         masini.remove(masina)
#         masini_vechi.append(masina)
#         masini.append('Tesla')
#     elif masina == 'Trabant':
#         masini.remove(masina)
#         masini_vechi.append(masina)
#         masini.append('Tesla')
#         print(f'Modele vechi: {masini_vechi}.')
#         print(f'Modele noi: {masini}.')
#

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}.')
print(f'Modele noi: {masini}.')


print('\n### 6 ###\n ')
# 6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printeaza "Pentru un buget de sub 15k puteti alege masina x" iterand prin lista cheilor dictionarului

buget = 15000

for masina, pret in pret_masini.items():
    if pret <= 15000:
        print(f'Pentru un buget de sub 15k puteti alege masina: {masina}.')

for masina in pret_masini.keys():
    if pret_masini[masina] <= buget:
        print(f'Pentru un buget de sub 15k puteti alege masina: {masina}.')


print(f'\n ### Afisare masini in dictionar nou - varianta 1')
masiniBuget = {}
for masina, pret in pret_masini.items():
    if pret <= buget:
        masiniBuget[masina] = pret
print(f'Pentru un buget de sub 15k puteti alege masina: {masiniBuget.keys()}.')


print(f'\n ### Afisare masini in dictionar nou - varianta 2')
masiniBuget = {masina: pret for masina, pret in pret_masini.items() if pret <= buget}

print(f'Pentru un buget de sub 15k puteti alege masina: {masiniBuget.keys()}.')


print(f'\n Afisare masini cu functia filter()')


def masina_buget(pret):
    return pret_masini[pret] <= buget


masini_buget = list(filter(masina_buget, pret_masini.keys()))
print(f'Pentru un buget de sub 15k puteti alege masina: {masini_buget}.')


print('\n### 7 ###\n ')
# 7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

contor = 0
for cifra in numere:
    if cifra == 3:
        contor += 1
print(f'Am gasit cifra 3 de {contor} ori.')


print('\n### 8 ###\n ')
# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
suma = 0
for i in range(len(numere)):
    suma += numere[i]
print(f'Suma numerelor din lista este: {suma}.')

suma = 0
for cifra in numere:
    suma += cifra
print(f'Suma numerelor din lista este: {suma}.')



print('\n### 9 ###\n ')
# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

# print(max(numere))

numar_mare = 0
for i in range(len(numere)-1):
    if numere[i] > numar_mare:
        numar_mare = numere[i]
print(f'Cel mai mare nr este: {numar_mare}.')

numar_mare = 0
for cifra in numere:
    if cifra > numar_mare:
        numar_mare = cifra
print(f'Cel mai mare nr este: {numar_mare}.')


print('\n### 10 ###\n')
# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = - numere[i]
print(numere)

for cifra in numere:
    if cifra > 0:
        cifra = -cifra
print(numere)


print('\n### Exercitii optionale ###\n ')

print('### 1 ###\n ')

# 1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# # Itereaza prin listă alte_numere
# # Populează corect celelalte liste
# # Afișeaza cele 4 liste la final

for numar in alte_numere:
    if numar < 0:
        numere_negative.append(numar)
        #alte_numere.remove(numar)
    elif numar > 0:
        # alte_numere.remove(numar)
        numere_pozitive.append(numar)
        if numar % 2:
            numere_impare.append(numar)
            #alte_numere.remove(numar)
        else:
            numere_pare.append(numar)
            #alte_numere.remove(numar)

for numar in numere_pozitive:
    if numar in alte_numere:
        alte_numere.remove(numar)
for numar in numere_negative:
    if numar in alte_numere:
        alte_numere.remove(numar)

print(f'Numere negative: {numere_negative}.')
print(f'Numere pozitive: {numere_pozitive}.')
print(f'Numere pare: {numere_pare}.')
print(f'Numere impare: {numere_impare}.')
print(f'Alte numere: {alte_numere}.')


print('\n### 2 ###\n')
# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# alte_numere.sort()
# print(f'Lista in ordine crescatoare este: {alte_numere}.')

print(f'### VAR 1 - lista noua ###')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
num = []

while alte_numere:
    numar_min = alte_numere[0]
    for numar in alte_numere:
        if numar < numar_min:
            numar_min = numar
    num.append(numar_min)
    alte_numere.remove(numar_min)
print(f"Lista ordonata crescator este: {num}")


print(f'### VAR 2 - nested for ###')

for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]

print(f"Lista ordonata crescator este: {alte_numere}")


print('\n### 3 ###\n')
# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

import random

numar_secret = random.randint(1, 30)
numar_ghicit = None
print(numar_secret)

while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Alegeti un numar: '))
    if numar_ghicit < numar_secret:
        print('Nr secret e mai mare')
    elif numar_ghicit > numar_secret:
        print('Nr secret e mai mic')
else:
    print('Felicitări! Ai ghicit!')


print('\n### 4 ###\n')
# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333

n = int(input(f'Alegeti un nr de la tastatura: '))
for i in range(n + 1):
    for j in range(i):
        print(f'{i}', end="")
    print('')

print('\n### 5 ###\n')
# 5.
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

for grup_taste in tastatura_telefon:
    for tasta in grup_taste:
        print(f'Cifra curenta este: {tasta}')


