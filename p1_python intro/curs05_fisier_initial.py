"""
O functie este o serie de instructiuni pe care le scriem o data si le putem utiliza de mai multe ori
Avantajul utilizarii functiilor este dat de economia de cod

Componentele unei functii

cuvantul def -> marcarea inceputului declararii unei functii

numele functiei -> free text, se recomanda sa fie un nume sugestiv

corpul functiei -> instructiuni care vor fi executate o data cu apelarea functiei

parametri -> informatii din exterior de care functia poate sau nu sa aiba nevoie (optionali)

return -> keyword prin care trimitem catre exterior rezultatele functiei

corpul functiei este marcat de indentare fata de marginea fisierului

La definire, ce este intre paranteze se numesc parametrii

La apelare, ce este intre paranteze se numesc argumente

IN PYTHON, O FUNCTIE TREBUIE DECLARATA INAINTE CA ACEASTA SA POATA FI FOLOSITA
"""


# 1. Definirea unei functii simple
def hello_world():
    print("Hello world!")
    print("Invatam sa scriem functii")


# Apelare functie simpla
hello_world()
hello_world()


def calculeaza_suma_intre_doua_numere():
    a = 3
    b = 3
    suma = a + b
    print(f"Suma celor doua numere este {suma}")


calculeaza_suma_intre_doua_numere()
calculeaza_suma_intre_doua_numere()


# 2. Functie cu parametri
def calcul_suma_cu_parametri(a, b):
    suma = a + b
    print(f"Suma intre cele doua numere este {suma}")


nr_1 = int(input('Introduceti primul numar: '))
nr_2 = int(input('Introduceti al doilea numar: '))
nr_3 = input('Introduceti al treilea numar: ')

calcul_suma_cu_parametri(nr_1, nr_2)


# calcul_suma_cu_parametri()
# o sa returneze eroare - TypeError: calcul_suma_cu_parametri() missing 2 required positional arguments: 'a' and 'b'

# calcul_suma_cu_parametri(nr_1)
# o sa returneze eroare - TypeError: calcul_suma_cu_parametri() missing 1 required positional argument: 'b'

# calcul_suma_cu_parametri(nr_1, nr_2, nr_3)
# o sa returneze eroare - TypeError: calcul_suma_cu_parametri() takes 2 positional arguments but 3 were given

# a = 5, b = 6 | a = nr_1, b = nr_2

# Exercitiu: vrem sa verificam care sunt numerele pare dintr-un anumit interval
# aici intalnim conceptul de polimorfism

def sir_numere_pare(range_end, range_beginning=0, range_step=1):
    for i in range(range_beginning, range_end + 1, range_step):
        if i % 2 == 0:
            print(f"Numarul {i} este par")
        else:
            print(f"Numarul {i} este impar")


sir_numere_pare(10)

sir_numere_pare(10, range_step=3)

# 3. Functie cu parametri si return
def calcul_pret_dupa_discount_si_taxe(varsta, sezon, clasa, pret):
    discount = 0
    if varsta > 65:
        discount = 0.15
    else:
        nr_copii = int(input("Va rugam sa introduceti numarul de copii cu care calatoriti: "))
        if nr_copii > 0:
            discount = 0.1
    if sezon == 'iarna':
        discount += 0.1
    if clasa == 1:
        tva = 0.03
    else:
        tva = 0.01
    pret = pret - pret * discount + pret * tva
    return pret


varsta_input = int(input("Va rugam sa introduceti varsta: "))
sezon_input = input("Va rugam sa introduceti sezonul: ")
clasa_input = int(input("Va rugam sa introduceti clasa la care calatoriti: "))
pret_input = int(input("Va rugam sa introduceti pretul de baza al biletului: "))

calcul_pret_dupa_discount_si_taxe(varsta_input, sezon_input, clasa_input, pret_input)
pret_calculat = calcul_pret_dupa_discount_si_taxe(varsta_input, sezon_input, clasa_input, pret_input)
print(f'Pretul calculat este: {pret_calculat}')


# 4. Functie cu numar indefinit de parametri
# aici intalnim conceptul POO de polimorfism
def calcul_suma_numere(*args):
    suma = 0
    for arg in args:
        suma = suma + arg
    return suma


print(calcul_suma_numere(1))
print(calcul_suma_numere(2, 6))
print(calcul_suma_numere(578901256, 789013476, 56))
print(calcul_suma_numere(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27))
# print(calcul_suma_numere("test1","test"))

lista_numere_pare = [0, 2, 4, 6, 8, 10]
print(calcul_suma_numere(*lista_numere_pare))  # aici am facut DESPACHETAREA listei

print(f"Suma numerelor este: {calcul_suma_numere(2, 6)}")
print(f"\nSuma numerelor este: {calcul_suma_numere(7, 8)}")
# lista_numere_pare -> [0,2,4,6,8,10]
# *lista_numere_pare -> 0,2,4,6,8,10

sucuri = {
    "pepsi": 0.33,
    "cola": 1,
    "fanta": 2.5
}


def accesare_elemente_dictionar(**kwargs):
    for key, value in kwargs.items():
        print(f"Sucul {key} este de {value}L")
        print("")


accesare_elemente_dictionar(pepsi=0.25, cola=1.5, fanta=3)

accesare_elemente_dictionar(**sucuri)


def print_nr_vocale_consoane(text):
    nr_vocale = 0
    nr_consoane = 0
    for litera in text:
        if str(litera).isalpha():
            if litera.lower() in "aeiou":
                nr_vocale += 1
            else:
                nr_consoane += 1
    print(f"Textul '{text}' contine {nr_vocale} vocale si {nr_consoane} consoane.")


print_nr_vocale_consoane("Afara cerul este senin")