"""
Polimorfism = principiu OOP care permite implementarea mai multor functii cu acelasi nume dar comportament diferit
exista mai multe modalitati de implementare a polimorfismului:
a) polimorfism prin definirea unei functii sau metode cu parametri impliciti
b) polimorfism prin definire unei functii sau metode cu *args
c) polimorfism prin reimplementarea metodei din clasa parinte

"""


# 1. Polimorfism prin functii cu parametri default (Method Overloading)
def sir_numere_pare(range_end, range_beginning=0, range_step=1):
    for i in range(range_beginning, range_end + 1, range_step):
        if i % 2 == 0:
            print(f"Numarul {i} este par")
        else:
            print(f"Numarul {i} este impar")


#Apelam aceeasi functie cu sau fara unele argumente default

print('Prima apelare sir_numere_pare():')
sir_numere_pare(10, 0, 1)
print("")

print('A doua apelare sir_numere_pare():')
sir_numere_pare(10, 4)
print("")

print('A treia apelare sir_numere_pare():')
sir_numere_pare(10, range_step=2)
print("")


# 2. Polimorfism prin functii cu *args (Method Overloading)
def calcul_suma_numere(*numbers):
    suma = 0
    for number in numbers:
        suma = suma + number
    return suma


#Apelam aceeasi functie cu numar de argumente diferite
print('Prima apelare calcul_suma_numere():')
print(calcul_suma_numere(1))
print("")

print('Prima apelare calcul_suma_numere():')
print(calcul_suma_numere(2, 6))
print("")

print('Prima apelare calcul_suma_numere():')
print(calcul_suma_numere(578901256, 789013476, 56))
print("")


def accesare_elemente_dictionar(**kwargs):
    for key, value in kwargs.items():
        print(f"Sucul {key} este de {value}L")
    print("")


print('Prima apelare accesare_elemente_dictionar():')
accesare_elemente_dictionar(pepsi=2, cola=3, fanta=5)

print('A doua apelare accesare_elemente_dictionar():')
accesare_elemente_dictionar(pepsi=0.5, cola=0.75, fanta=1, mirinda=2)


# Polimorfism prin reimplementarea metodei din clasa parinte in clasa copil
# Se mai numeste si Method Overriding
class Animal:
    def sound(self):
        print("sunet default")


class Catel(Animal):
    def sound(self):
        print("woof woof")


class Pisica(Animal):
    def sound(self):
        print("miau miau")


# instantiem un obiect de tip Animal
animal_random = Animal()

# Apelam metoda sound()
print('Sunetul animalului default:')
animal_random.sound()
print("")

# instantiem 2 obiecte de tip Catel
catel_1 = Catel()
catel_2 = Catel()

# observam ca metoda sound() si-a schimbat comportamentul in clasa Catel
print('Sunetul animalelor de tip Catel:')
catel_1.sound()
catel_2.sound()
print("")

pisica_1 = Pisica()
pisica_2 = Pisica()

# observam ca metoda sound() si-a schimbat comportamentul in clasa Pisica
print('Sunetul animalelor de tip Pisica:')
pisica_1.sound()
pisica_2.sound()
print("")