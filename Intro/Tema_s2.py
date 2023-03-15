# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

"""
Structura IF - ELSE este folosita in cazul in care trebuie acoperite doua sau mai multe situatii, executand
instructiuni diferite in functie de fiecare situatie in parte.
"""

# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
# daca este numar intreg mai mare ca 0)

x1 = input('Introduceti un nr natural: ')

if x1.isalpha():
    print(f'{x1} nu este nr natural.')
elif not x1.isnumeric():
    print(f'Nr {x1} nu este nr natural.')
elif int(x1) >= 0:
    x2 = int(x1)
    print(f'Nr {x2} este nr natural.')
else:
    print(f'Nr {x1} nu este nr natural.')


# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x2 = float(input('Introduceti un numar: '))

if x2 < 0:
    print(f'Nr {x2} este negativ.')
elif x2 == 0:
    print(f'Nr {x2} este nr neutru)')
else:
    print(f'Nr {x2} este pozitiv.')


# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x3 = float(input('Introduceti un nr: '))

if -2 <= x3 <= 13:
    print(f'Nr introdus {x3} se afla intre -2 si 13')
else:
    print(f'Nr {x3} nu se afla in intervalul precizat.')


# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs

x = float(input('Nr x este: '))
y = float(input('Nr y este: '))

dif = x-y
dif_int = int(dif)

if dif_int < 5:
    print(f'Diferenta dintre {x} si {y} este {abs(dif_int)}, mai mica de 5.')
else:
    print(f'Diferenta dintre {x} si {y} nu este mai mica de 5.')


# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare

x4 = float(input('Nr x este: '))

if not(5 <= x4 <= 27):
    print(f'Nr {x4} nu se afla in intervalul 5 - 27.')
else:
    print(f'Nr {x4} se afla in intervalul 5 - 27.')

y4 = int(input('Nr y este: '))
if x4 == y4:
    print(f'Numerele introduse sunt egale.')
elif x4 > y4:
    print(f'Nr {x4} este mai mare decat nr {y4}.')
else:
    print(f'Nr {y4} este mai mare decat {x4}.')


# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

x5 = int(input('Nr intreg x este: '))
y5 = int(input('Nr intreg y este: '))
z5 = int(input('Nr intreg z este: '))

if x5 == y5 == z5:
    print(f'Triunghiul este echilateral.')
elif x5 == y5 != z5 or x5 != y5 == z5 or x5 == z5 != y5:
    print(f'Triunghiul este isoscel.')
else:
    print(f'Triunghiul este oarecare.')


# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

# valabil pt alfabetul romanesc
char = input('Litera este: ')

vocale = ['a','A','e','E','i','I','o','O','u','U','ă','Ă','â','Â','î','Î']

if len(char) > 1:
    print(f'Ai introdus prea multe caractere.')
elif char.isnumeric():
    print('Cifrele nu sunt litere.')
elif char in vocale:
    if char.islower():
        print(f'Litera {char} este vocala si este scrisa cu litera mica.')
    elif char.isupper():
        print(f'Litera {char} este vocala si este scrisa cu litera mare.')
elif char not in vocale:
    if char.islower():
        print(f'Litera {char} este consoana si este scrisa cu litera mica.')
    elif char.isupper():
        print(f'Litera {char} este consoana si este scrisa cu litera mare.')
    else:
        print('Iti place sa te joci. Mai incearca, poate nimeresti o litera!')


# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
# a. Peste 9 => A
# b. Peste 8 => B
# c. Peste 7 => C
# d. Peste 6 => D
# e. Peste 4 => E
# f. 4 sau sub => F

nota_ro = float(input('Nota obtinuta este: '))
if 9 < nota_ro <= 10:
    nota_am = 'A'
    print(f'In sistem american nota introdusa este {nota_am}.')
elif 8 < nota_ro <= 9:
    nota_am = 'B'
    print(f'In sistem american nota introdusa este {nota_am}.')
elif 7 < nota_ro <= 8:
    nota_am = 'C'
    print(f'In sistem american nota introdusa este {nota_am}.')
elif 6 < nota_ro <= 7:
    nota_am = 'D'
    print(f'In sistem american nota introdusa este {nota_am}.')
elif 4 < nota_ro <= 6:
    nota_am = 'E'
    print(f'In sistem american nota introdusa este {nota_am}.')
elif 0 <= nota_ro <= 4:
    nota_am = 'F'
    print(f'In sistem american nota introdusa este {nota_am}.')
else:
    print(f'Nu ai introdus o nota valida. Mai incearca o data.')



### OPTIONALE

# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# 2. Verifica daca x are exact 6 cifre
# 3. Verifica daca x este numar par sau impar


x6 = input('Introduceti un numar: ')
length = len(x6.replace('.', ''))

if length >= 4:
    if length == 4:
        print(f'Nr {x6} are exact 4 cifre.')
    elif length == 6:
        print(f'Nr {x6} are exact 6 cifre.')
    else:
        print(f'Nr {x6} are {length} cifre.')
else:
    print(f'Nr {x6} nu are minim 4 cifre, are doar {length} cifre.')

x6 = float(x6)
if int(x6) % 2:
    print(f'Nr {int(x6)} este impar')
else:
    print(f'Nr {int(x6)} este par.')


# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# ele
# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
# lungimea celei de-a treia laturi)


x7 = int(input('Nr intreg x este: '))
y7 = int(input('Nr intreg y este: '))
z7 = int(input('Nr intreg z este: '))

if x7 > y7 and x7 > z7:
    print(f'Nr cel mai mare este x: {x7}.')
elif y7 > x7 and y7 > z7:
    print(f'Nr cel mai mare este y: {y7}.')
elif z7 > y7 and z7 > x7:
    print(f'Nr cel mai mare este z: {z7}.')
elif x7 == y7 > z7:
    print(f'Numerele x si y sunt egale si mai mari decat z.')
elif y7 == z7 > x7:
    print(f'Numerele y si z sunt egale si mai mari decat x.')
elif x7 == z7 > y7:
    print(f'Numerele x si z sunt egale si mai mari decat y.')
else:
    print(f'Numerele sunt egale.')

# x, y, z - unghiuri
suma = x7 + y7 + z7
if suma == 180:
    print(f'Suma unghiurilor este {suma} grade\nTriunghiul este valid.')
else:
    print(f'Suma unghiurilor este {suma} grade,\nTriunghiul nu este valid.')

# x, y, z - lungimile laturilor
if (x7 + y7 > z7) or (x7 + z7 > y7) or (z7 + y7 > x7):
    print('Suma lungimilor a 2 laturi este mai mare decat lungimea celei de-a 3-a laturi.\nTriunghiul este valid.')
else:
    print(f'Triunghiul nu este valid.')


# 6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
# la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
# smarte'

text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Alege un numar: '))
text1 = text[0:len(text)-x]
print(text1)

# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# din primele 5 caractere + ultimele 5

text2 = text[0:5] + text[-5:]
print(text2)


# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '

index = text.find('rock')
text3 = text[0:index]
print(text3)


# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive)

txt = input('Introduceti un string: ')
txt = txt.lower()
assert txt[0] == txt[len(txt)-1], f'Primul si ultimul caracter sunt diferite, {txt[0]} si {txt[len(txt)-1]}.'
print(f'Primul si ultimul caracter sunt la fel, {txt[0]}.')


# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

text = '0123456789'

pare = text[0:len(text):2]
print(f'Stringul cu numere pare este: {pare}.')
cifre_pare = []
cifre_pare.extend(pare)
print(f'Cifrele pare sunt: {cifre_pare}.')

impare = text[1:len(text):2]
print(f'Stringul cu numere impare este: {impare}.')
cifre_impare = []
cifre_impare.extend(impare)
print(f'Cifrele impare sunt: {cifre_impare}.')



### EXERCITII BONUS
"""
#1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte
Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
"""

varsta = int(input('Varsta: '))
if varsta >= 18:
    pasaport = input('Pasaport: introduceti Da sau Nu: ')
    if pasaport == 'Da':
        pasaport = True
    elif pasaport == 'Nu':
        pasaport = False
    else:
        print('Puteti sa introduceti doar Da sau Nu.')

    if pasaport == True:
        print('Va puteti imbarca.')
    elif not pasaport:
        print('Nu va puteti imbarca fara pasaport valabil.')
# elif varsta >= 18 and pasaport == False:
#     print('Nu va puteti imbarca fara pasaport.')
elif 0 < varsta < 18:
    pasaport = input('Pasaport: introduceti Da sau Nu: ')
    if pasaport == 'Da':
        pasaport = True
    elif pasaport == 'Nu':
        pasaport = False
    else:
        print('Puteti sa introduceti doar Da sau Nu.')

    if not pasaport:
        print('Nu va puteti imbarca fara pasaport valabil.')
    elif pasaport == True:
        insotit_de_mama = input('Insotit de mama: introduceti Da sau Nu: ')
        if insotit_de_mama == 'Da':
            insotit_de_mama = True
        elif insotit_de_mama == 'Nu':
            insotit_de_mama = False
        else:
            print('Puteti sa introduceti doar Da sau Nu.')
        #print(insotit_de_mama)

        insotit_de_tata = input('Insotit de tata: introduceti Da sau Nu: ')
        if insotit_de_tata == 'Da':
            insotit_de_tata = True
        elif insotit_de_tata == 'Nu':
            insotit_de_tata = False
        else:
            print('Puteti sa introduceti doar Da sau Nu.')
        #print(insotit_de_tata)

        if not insotit_de_mama and not insotit_de_tata:
            print('Nu va puteti imbarca neinsotit.')
        elif insotit_de_mama == True and insotit_de_tata == True:
            print('Va puteti imbarca.')
        elif insotit_de_mama == True and not insotit_de_tata:
            act_perm_tata = input('Act permisiune tata: introduceti Da sau Nu: ')
            if act_perm_tata == 'Da':
                act_perm_tata = True
            elif act_perm_tata == 'Nu':
                act_perm_tata = False
            else:
                print('Puteti sa introduceti doar Da sau Nu.')
            #print(act_perm_tata)

            if act_perm_tata == True:
                print('Va puteti imbarca.')
            elif not act_perm_tata:
                print('Pentru imbarcare aveti nevoie de permisiunea tatalui.')
        elif not insotit_de_mama and insotit_de_tata == True:
            act_perm_mama = input('Act permisiune mama: introduceti Da sau Nu: ')
            if act_perm_mama == 'Da':
                act_perm_mama = True
            elif act_perm_mama == 'Nu':
                act_perm_mama = False
            else:
                print('Puteti sa introduceti doar Da sau Nu.')
            #print(act_perm_mama)

            if act_perm_mama == True:
                print('Va puteti imbarca.')
            elif not act_perm_mama:
                print('Pentru imbarcare aveti nevoie de permisiunea mamei.')
else:
    print(f'Varsta trebuie sa fie mai mare de 0.')


'''
2. Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
'''

import random
dice_roll = random.randint(1, 6)
#print(dice_roll)

guess = int(input('Ghiceste zarul: '))

if guess < 1 or guess > 6:
    print('Poti introduce numere doar intre 1 si 6.')
elif guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess}, dar a fost {dice_roll}.')
elif guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess}, dar a fost {dice_roll}.')
elif dice_roll == guess:
    print(f'Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}.')




