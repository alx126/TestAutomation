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

# Lista tuturor exceptiilor poate fi consultata in documentatia oficiala a Python 3
# https://docs.python.org/3/library/exceptions.html

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

Se pot ridica/arunca exceptii folosind instructiunea <<raise>>

Forma generala:

    if conditie:
        raise NumeExceptie
"""


# Exemplu ZeroDivisionError - impartire la 0


def impartire_numere(a, b):
    rezultat = None

    try:
        rezultat = a / b
    except ZeroDivisionError:
        print(f'{a} nu poate fi impartit la {b}')
    else:
        print(f"Nu am intampinat erori la impartirea lui {a} la {b}")
    finally:
        if rezultat is not None:
            print(f'Rezultatul impartirii este: {rezultat}')
        else:
            print('Nu avem un rezultat')


# Definim o exceptie custom pe care o vom


class InvalidEmailException(Exception):
    """Raised when email address is not valid"""
    pass

    def __init__(self, message="Email address has an invalid format. It should contain <<@>> and <<.com>>"):
        self.message = message
        super().__init__(self.message)


def verificare_adresa_mail(email):
    if "@" not in email and ".com" not in email:
        raise InvalidEmailException


# verificare_adresa_mail("ion.popescu")

try:
    verificare_adresa_mail("ion.popescu")
except InvalidEmailException as e:
    # vom afisa exceptia fara sa o "aruncam"
    print(e)