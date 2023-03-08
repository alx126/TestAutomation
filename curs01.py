"""
################# 1. TERMENI GENERALI #################

Compilare
- executarea/rularea codului scris de catre programator din ‘human reading syntax’ in ‘machine language’

IDE
- Integrated Development Environment (Mediu de Dezvoltare Integrat)
- Are terminal, consola, venv (in cazul PyCharm)
- Este locul in care putem sa scriem si sa rulam cod
- Vine in ajutorul programatorilor avand o serie de functionalitati care fac programarea mai usoara
- Ex: PyCharm (Python), IntelliJ (Java), Visual Studio (C/C++/C#), VSCode(mai multe limbaje), etc

Terminal
- o interfata prin care putem comunica cu sistemul de operare
- de aici putem accesa fisiere, putem rula programe, putem modifica setari
- integrat si cu limbajele de programare/frameworkuri (ex: putem rula programe python direct din terminal)

Consola
- interfata pentru output (rezultatul executarii codului) si input (cand se asteapta input de la user)
- in PyCharm consola se gaseste in partea de stanga-jos, tab-ul denumit "Run"

venv (Virtual Environment)
- Multe programe scrise in Python folosesc librarii externe (bucati de cod/package-uri scrise de altii)
- Aceste librarii pot avea mai multe versiuni (se fac imbunatatiri/adaugari de functionalitati noi)
- Unele versiuni ale librariilor externe pot fi compatibile sau nu cu anumite versiuni de Python
- venv este un mediu virtual care ne ajuta sa izolam aceste versiuni in functie de nevoile pe care le avem pt proiect,
- fiecare proiect Python va avea propriul venv in care se vor putea instala/adauga librarii externe
"""

"""
################# 2. COMENTARII ################# 

- sunt linii de cod pe care le putem scrie sub forma de explicatii si care sunt ignorate de compilator

Exista doua tipuri de comentarii:
1. comentarii multi-line -> comentarii care se pot scrie pe mai multe linii. 
Sunt reprezentate de un text scris intre doua perechi de trei ghilimele sau apostroafe.
2. comentarii single-line -> comentarii care se pot scrie pe o singura linie. 
Sunt reprezentate de un text precedat de semnul #

Ca sa putem sa comentam mai multe linii in acelasi timp sau sa comentam automat o linie cu comentariu single line
ne putem folosi de scurtatura CTRL + "/" (pe Windows) sau COMMAND + "/" (pe Mac)
"""

#one line comment

""" Multi - line
comment """

'''Another multi - line
comment'''

print("Hello world")

"""
################# 3. VARIABILE ################# 

- Sunt adrese de memorie la care noi putem sa stocam informatii
- Numele variabilei este de fapt numele adresei de memorie la care sunt stocate informatiile
- Numele variabilelor trebuie sa respecte anumite reguli:
a) trebuie sa inceapa cu litera mica (conventie)
b) nu are voie sa inceapa cu cifra sau caractere speciale (obligatoriu)
c) nu trebuie sa contina spatii (obligatoriu)
d) nu pot fi cuvinte rezervate de Python (obligatoriu), ex: print, False, input
e) numele trebuie sa urmeze formatul camelCase sau snake_case
f) numele variabilelor este case-senstive (adica variabila numepisica nu este egala cu variabila numePisica)
g) numele variabilelor este unic. Daca vom incerca sa facem o redefinire, 
de fapt sistemul nu va aloca o alta adresa de memorie ci va schimba informatia de la adresa de memorie deja alocata
"""

#camelCase
#snake_case
#PascalCase

# Declarare si initializare variabila:
nume = "Andrei"

'''
In randul de mai sus
1. s-a declarat variabila nume (careia i s-a alocat o zona in memorie)
2. i s-a facut initializarea, adica i s-a atribuit valoarea "Alin"

"Alin" trebuie scris intre ghilimele pentru a fi considerat text dat de la tastatura si nu numele unei alte variabile
Daca nu era intre ghilimele, sistemul ar fi cautat variabila numita "Alin". Nu ar fi gasit-o si ar fi returnat eroare
'''

# daca nu folosesc variabila 'nume', ea va fi marcata cu galben ca si atentionare ca nu am folosit continutul anterior
nume = "Andreea"  # momentul in care dau o alta valoare pentru o variabila se numeste suprascriere


prenume, varsta = "Cristi", 25
# am facut o dubla declarare si initializare, care este posibil in Python
# am anuntat sistemul ca vrem sa declaram doua variabile, 'prenume' si 'varsta' prin folosirea virgulei
# in dreapta egalului am specificat valorile cu care vrem sa initializam cele doua variabile, in ordinea declararii lor


"""
################# 4. TIPURI DE DATE (primitive/simple) ################# 

- Tipul datei precizeaza ce valori poate avea acea data (variabila) și ce operatii se pot face cu ea.

Exista patru tipuri de date primitive in Python:
# string -> au valori de tip text
# int -> au valori numerice intregi (pozitive sau negative)
# boolean -> pot avea doar doua valori: True sau False
# float -> pot stoca numere cu zecimale (adica numere cu virgula)

Tipul de data in python nu este specificat in mod explicit ca in Java/C, ci rezulta din valoarea stocata in variabila
Asta este motivul pentru care putem sa facem schimbare de tip de data

Mai exista si tipuri de date derivate, dar ele au la baza tot tipuri de date simple.
"""

# STRING (SIR)
variabila_string = "text"  # am declarat si initializat o variabila cu tipul de date string

# INT (INTEGER/INTREG)
variabila_int = 34

# ATENTIE! Aici este string si nu int:
# variabila_int = "34"

# BOOLEAN
variabila_boolean_true = True
variabila_boolean_false = False

# ATENTIE! Urmatoarea instructiune va da eroare pentru ca va cauta o variabila numita false:
# variabila_boolean_false = false

# ATENTIE! Aici este string si nu boolean:
# variabila_boolean_false = "False"

# FLOAT
variabila_float = 3.14  # am declarat si initializat o variabila float. Obs: se foloseste punct (.) nu virgula (,)

# ATENTIE! Urmatoarea instructiune nu va stoca o valoare, ci va stoca un tuplu (Curs 3):
# variabila_float_redeclarata = 3,14
# print(variabila_float_redeclarata)  # afiseaza un tuplu format din numerele 3 si 14

"""
################# 6. FUNCTIA print() #################

Functia print este o metoda prin care putem sa afisam informatii in consola

Structura functiei print este urmatoarea:
1. numele functiei (print)
2. valoarea pe care vrem sa o afisam (text, numere, caractere speciale etc)
- Daca vrem sa printam text, este foarte important sa fie pus intre ghilimele sau apostroafe. 
- In caz contrar, sistemul va crede ca este o variabila, pe care nu o va gasi si va returna eroare

In limbajele de programare in general semnul ghilimele reprezinta delimitator de text
- Orice text este pus intre ghilimele de inceput si ghilimele de final
- Daca incercam sa scriem un al doilea text intre ghilimele in interiorul unui text intre ghilimele, 
atunci sistemul va considera ghilimelele de inceput al celui de-al doilea text ca fiind sfarsitul primului text     
"""

print("Hello world")
print('Hello world')  # putem sa specificam textul si intre ghilimele

# ATENTIE! Sistemul va considera in cazul urmator ca textul meu este "Hello", iar Anton este o variabila separata
# print("Hello "Anton" ")

# Optiuni pentru problema cu limita de text:
#  1. scriem ghilimele in apostroafe
print('Hello "Anton"')
# 2. scriem apostroafe intre ghilimele
print("Hello 'Anton'")
# 3. folosim escape character "\" care instruieste sistemul sa trateze urmatorul caracter nu ca pe un caracter special
# ci ca pe un text de afisat pe ecran
print("Hello \"Anton\"")
print('Hello \'Anton\'')

"""
PRINT: Concatenare
Concatenare = lipirea a doua texte (string-uri) separate intr-unul singur
"""
# Exemplu:
text1 = "Afara ploua "
text2 = "Imi place? "
text3 = "Nu, as vrea sa ninga. "
string_concatenat = text1 + text2 + text3

print(string_concatenat)

print(text1 + text2 + text3)

ora_curenta = 20
# ATENTIE! Urmatoarea instructiune va returna eroare: TypeError: can only concatenate str (not "int") to str
# print(string_concatenat + "Este ora" + ora_curenta)

# concatenarea se poate face doar intre string-uri
# concatenarea cu alt tip de data este incompatibila
# in cazul asta specific nu va functiona pentru ca semnul "+" are o semnificatie diferita
# pentru string (concatenare) vs int (adunare)

# Optiuni:
# 1. Pot sa definesc direct valoarea orei intre ghilimele
# (nu este neaparat o optiune pentru ca nu putem controla tot timpul tipul de data al variabilelor pe care le primim)
# 2. Type casting
print(string_concatenat + " Este ora " + str(ora_curenta))
# 3. Printare cu formatare
print(f"{string_concatenat} Este ora {ora_curenta}")


"""
################# 7. Assert ################# 
Assert este un cuvant care este tradus ca evaluare
Din punct de vedere tehnic inseamna o comparatie intre doua valori
- Daca comparatia returneaza True, sistemul va merge mai departe cu executarea urmatoarei instructiuni
- Daca comparatia returneaza False, sistemul va opri executia programului curent si va returna eroare: AssertionError
 
Componentele unui assert:
1. keyword-ul assert care anunta sistemul ca urmeaza o evaluare
2. valorea pe care o comparam
3. operatorul de comparare
4. valoarea cu care comparam
5. mesajul de eroare pe care sa il returneze atunci cand comparatia returneaza False (optional)

Este foarte folosit in testele automate.
"""

# imi_place_programarea = False
# assert imi_place_programarea == True, "Eroare, nu imi place programarea"
# print("Am trecut de assert, imi place programarea :)")

# user = "abcUser"
# expected_password ="pass123"
# inserted_password = input("Va rugam sa inserati parola: ")
# print(expected_password==inserted_password) # printeaza rezultatul evaluarii
# assert expected_password==inserted_password,"Eroare: parola gresita, mai aveti doua incercari"

# functia input returneaza valori de tip string.
# Ca sa putem sa le procesam ca int trebuie sa facem type casting
# a = int(input("Va rugam sa introduceti primul numar: "))
# b = int(input("Va rugam sa introduceti al doilea numar: "))
# suma = a + b
# print(suma)


"""
################# 8. STRING SLICING ################# 
Slicing = Modalitate prin care putem sa extragem doar anumite parti dintr-un string (subsiruri)
Slicing-ul se poate face pe baza urmatoarelor elemente:
- pozitie de inceput -> implicit va fi 0 - adica de la inceputul stringului
- pozitie de final -> implicit va fi lungimea stringului - adica pana la final
- pas (cate caractere sa se sara) -> implicit va fi 1 - adica se va afisa fiecare caracter
In general in range-ul pe baza caruia se extrage bucata din string nu se ia in considerare capatul de interval
Exemplu:
Daca ii spun sistemul sa extraga toate caracterele de la pozitia 0 la pozitia 5, de fapt va extrage pana la pozitia 4
"""

poezie = "Cobori in jos Luceafar bland"

# Exercitiu 1: vrem sa extragem toate caracterele din string specificand explicit start-ul si end-ul si pasul implicit
print("Exercitiu 1: " + poezie[0:len(poezie)])

# len(poezie) = 28 -> adica cate caractere sunt in string
# in programare toate elementele dintr-o structura ordonata incep de la indexul 0
# de aceea indexul ultimului element se va afla in pozitia cu 1 mai mica decat lungimea stringului
# avand in vedere ca ultimul caracter se afla in pozita cu 1 mai mica decat lungimea stringului,
# desi capatul de interval nu se ia in considerare nu pierdem ultimul element datorita diferentei intre index si lungime

'''
- Index:                 0  1  2  3  4  5 
- Caracater:             C  o  b  o  r  i
'''


# Exercitiu 2: vrem sa extragem toate caracterele din string folosind start si end implicit
print("Exercitiu 2: " + poezie[:])


# Exercitiu 3: vrem sa extragem toate caracterele din string folosind start si end implicit si pas explicit de 2
# (adica printare din 2 in doua caractere)
print("Exercitiu 3: " + poezie[::2])

# Exercitiu 4: vrem sa extragem toate caracterele din string folosind start si end implicit si pas implicit
print("Exercitiu 4: " + poezie[::])


# Exercitiu 5: vrem sa extragem caracterele incepand de la pozitia 0 pana la pozitia 5 inclusiv
print("Exercitiu 5: " + poezie[0:6])

'''
- Index:                 0  1  2  3  4  5  6  7  8
- Caracater:             F  e  b  r  u  a  r  i  e
- Negative index:       -9 -8 -7 -6 -5 -4 -3 -2 -1
'''

# Exercitiu 6: vrem sa extragem ultimele trei caractere de la final
print("Exercitiu 6: " + poezie[-3:])

# Exercitiu 7: vrem sa printam string-ul in sens invers
print("Exercitiu 7: " + poezie[::-1])


"""
################# 8. METODELE STRING ################# 
Pentru a le putea accesa vom scrie numele string-ului urmat de caracterul "."
"""

propozitie = "Cerul este albastru"

print(propozitie.find("a"))  # va identifica indexul primului caracter a din string
print(propozitie.find("c"))  # va identifica indexul primului caracter c din string
print(f"Caracterul x se afla in pozitia {propozitie.find('X')}")

# Referinta cod ASCII: https://www.ascii-code.com/

print(propozitie.index("C"))
# va identifica indexul primului caracter C din string
# metoda index face exact acelasi lucru ca metoda find
# print(f"Caracterul x se afla in pozitia {poezie.index('Y')}")

# Diferenta intre find si index este ca "find" returneaza -1 in cazul in care caracterul nu e gasit si "index" da eroare

print(propozitie.split())
# functie care sparge string-ul in functie de cuvintele componente.
# rezultatul este o lista
# separatorul implicit este spatiu, dar se poate suprascrie

print(propozitie.split(sep="L"))  # Am suprascris separatorul

print(propozitie.count("a"))  # numara de cate ori apare un anumit substring in string-ul de la care plecam
print(propozitie.isdigit())
# verifica daca toate caracterele dintr-un string sunt cifre
# atentie!!! sunt trei functii care fac asta: isDigit, isNumeric, isDecimal

# Diferenta intre cele trei metode:
#https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python

#Inlocuirea caracterului 'a' cu 'M'
print(propozitie.replace("a", "M"))

#Formatare cu placeholder
print("Primul numar este {}, iar al doilea este {}\n".format('3', 4))
# {} - se numeste placeholder si tine locul unei variabile care se va specifica in metoda format()

#Formatare cu placeholder pe un anumit numar de spatii
print("|{0:8} | {1:10}|".format('Fruct', 'Cantitate'))
print("-------------------------")
print("|{0:8} | {1:^10}|".format('Mere', '1 kg'))
print("|{0:8} | {1:^10}|".format('Portocale', '1 buc'))
print("|{0:8} | {1:^10}|".format('Pere', '1 sac'))

#Rand gol dupa primul tabel
print("\n")

print("Introduceti cantitatea din fiecare fruct:\n")
cantitate_mere = input("Mere: ")
cantitate_portocale = input("Portocale: ")
cantitate_pere = input("Pere: ")

print("|{0:10} | {1:10}|".format('Fruct', 'Cantitate'))
print("-------------------------")
print("|{0:10} | {1:10}|".format('Mere', cantitate_mere))
print("|{0:10} | {1:10}|".format('Portocale', cantitate_portocale))
print("|{0:10} | {1:10}|".format('Pere', cantitate_pere))

