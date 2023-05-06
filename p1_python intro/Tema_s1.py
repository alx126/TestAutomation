# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

'''
O variabila este un spatiu de memorie care poate stoca o valoare.
Ele respecta anumite reguli:
- numele variabilei incepe cu litera mica, nu poate incepe cu cifre si nu contine spatii sau caractere speciale
- nu se pot folosi cuvinte rezervate in Python pt denumirea variabilelor
- numele este unic si este case sensitive
- pt denumirea lor se pot folosi formatele camelCase sau snake_case
Exista 4 tipuri primordiale de variabile:
- string - inlantuire de caractere
- int - numar intreg, fara zecimale
- float - numar zecimal
- boolean - poate avea 2 valori: True sau False
'''

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă :

marca = 'Dacia'
an_fabricatie = 2000
pret = 755.55
inmatriculata = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(marca))
print(type(an_fabricatie))
print(type(pret))
print(type(inmatriculata))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.

pret = round(pret)
print(pret)
print(type(pret))

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f'Vand masina marca {marca}, an fabricatie {an_fabricatie}, pret: {pret} euro.')
if inmatriculata == True:
    print('Stare: inmatriculata.')
else:
    print('Stare: neinmatriculata.')

print('Vand masina marca ' + marca + ', an fabricatie ' + str(an_fabricatie)+', '+'pret: '+ str(pret)
      + ' euro.')
print('Valoarea variabilei "inmatriculata" este: '+ str(inmatriculata))

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

numele = input("Introduceti numele: ")
prenumele = input("Intoduceti prenumele: ")
print(f'Numele complet are {len(numele) + len(prenumele)} caractere.')

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.

lungimea = float(input('Introduceti lungimea dreptunghiului: '))
latimea = float(input('Introduceti latimea dreptunghiului: '))
aria = lungimea * latimea
print(f'Aria dreptunghiului este {aria}.')

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';

# 9. Același string.
# ● Inlocuieste cuvântul 'the' cu 'THE';
# ● Printează rezultatul.

prop = 'Coral is either the stupidest animal or the smartest rock'

print(prop.count("the"))
print(f'Cuvantul "the" apare de {prop.count("the")} ori in textul din enunt.')

print(prop.replace("the", "THE"))

# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.

assert prop.isdigit() == False, "Stringul contine doar numere."
print('Evaluarea a fost corecta.')



### Exerciții Opționale ###

# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.

s = input('Introduceti un string impar: ')

if len(s) == 0:
    print(f'Nu ai introdus nimic.')
elif len(s)%2:
    length = len(s)
    middle = length // 2
    print(f'Caracterul din mijloc este: "{s[middle]}".')
else:
    print(f'Mai baga o fisa! Stringul "{s}" nu este impar.')


# 2. Folosind assert, verifică dacă un string este palindrom.
text = input('Introduceti un string: ')
rev_text = text[::-1]

assert text == rev_text, f'Stringul "{text}" nu este palindrom.'
print(f'Stringul "{text}" este palindrom.')


# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

txt = input("Introduceti un string din 2 cuvinte: ")

cuv1, cuv2, *_ = txt.split()
print(cuv1)
print(cuv2)


# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

a = input("Introduceti un string: ")
a0 = a[0]
print(f'Primul caracter introdus este: "{a0}".')

if a[0].isupper():
    c_lower = a[0].lower()
    a_cap = a0 + a[1:-1].replace(c_lower, a0) + a[-1]
    print(f'Dupa modificare stringul devine: "{a_cap}".')
else:
    a_cap = a0 + a[1:-1].replace(a0, a0.upper())+a[-1]
    print(f'Dupa modificare stringul devine: "{a_cap}".')


# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input("Introduceti userul: ")
pswd = input("Introduceti parola: ")
pass_star = '*' * len(pswd)

print(f'Parola pt user {user} este {pass_star} si are {len(pswd)} caractere.')



