from curs07_p2_abstractizare import *

# Instantiem un obiect de tip Pisica()
garfield = Pisica()


garfield.print_proprietati()
print("")

snake = Sarpe()
snake.print_proprietati()
print("")

# verificam daca clasa Sarpe este o subclasa a clasei Animal
assert issubclass(Sarpe, Animal), "Eroare, clasa <<Sarpe>> nu este o subclasa a clasei <<Animal>>"

# verificam daca clasa Sarpe este o subclasa a clasei Reptila
assert issubclass(Sarpe, Reptila), "Eroare, clasa <<Sarpe>> nu este o subclasa a clasei <<Reptila>>"

# EROARE:
# # verificam daca clasa Sarpe este o subclasa a clasei Reptila
# assert issubclass(Sarpe, Mamifer), "Eroare, clasa <<Sarpe>> nu este o subclasa a clasei <<Mamifer>>"

# verificam daca obiectul snake este o instanta a clasei Sarpe
assert isinstance(snake, Animal), "Eroare, obiectul <<snake>> nu e subclasa a clasei <<Animal>>"

# verificam daca obiectul snake este o instanta a clasei Reptila
assert isinstance(snake, Reptila), "Eroare, obiectul <<snake>> nu e subclasa a clasei <<Reptila>>"

# EROARE:
# # verificam daca obiectul snake este o instanta a clasei Mamifer
# assert isinstance(snake, Mamifer), "Eroare, obiectul <<snake>> nu e subclasa a clasei <<Mamifer>>"

# Definim un animal nou de speta necunoscuta, adica o vom egala cu None
animal_nou = None

import random

# Daca numarul generat e impar, animalul nou va fi de tip pisica, altfel va fi de tip sarpe
numar = random.randint(1, 2)
if numar % 2 == 0:
    animal_nou = Pisica()
else:
    animal_nou = Sarpe()

# Printam proprietatile animalului
print(f"Animalul creat random este {type(animal_nou).__name__}")
animal_nou.print_proprietati()