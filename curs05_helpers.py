def accesare_elemente_dictionar(**kwargs):
    for key, value in kwargs.items():
        print(f"Sucul {key} este de {value}L")
        print("")


def calcul_suma_numere(*args):
    suma = 0
    for arg in args:
        suma = suma + arg
    return suma


def print_nr_vocale_consoane(text):
    nr_vocale = 0
    nr_consoane = 0
    for litera in text:
        if str(litera).lower() in "aeiou":
            nr_vocale += 1
        elif litera == " ":
            continue
        else:
            nr_consoane += 1
    print(f"Textul '{text}' contine {nr_vocale} vocale si {nr_consoane} consoane.")