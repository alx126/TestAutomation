from abc import ABC, abstractmethod

"""
Abstractizare = modalitate prin care obligam clasele care mostenesc sa defineasca un anumit comportament

Exista doua metode de abstractizare:

a) doar o parte din metodele dintr-o clasa sunt abstracte - clasa se va numi clasa abstracta
Daca definim o clasa copil care mostenste o clasa abstracta / interfata
si nu implementam metodele abstracte, atunci vom primi o eroare

b) toate metodele dintr-o clasa sunt abstracte - in acest caz clasa se va numi <<interfata>>
interfata

Putem spune ca o clasa abstracta functioneaza ca sablon pentru subclase. 
Clasele abstracte nu pot fi instantiate si necesită crearea unor subclase 
pentru a furniza implementari pentru metode abstracte. 

Modulul abc - Abstract Base Classes ne ajuta la crearea claselor abstracte

Orice clasa pe care o dorim sa fie abstracta trebuie sa mosteneasca 
proprietatile clasei ABC (Abstract Base Class/Clasa de Baza Abstracta)
"""


# Definim clasa abstracta Animal, care va fi o interfata
# Clasa Animal devine abstracta prin extinderea lui ABC (Clasa de baza abstracta)
class Animal(ABC):

    # Definim o proprietate abstracta <<sange>>
    # Atentie! Acesta va fi o proprietate (atribut/field)
    # Desi seamana cu definirea unei metode, in clasele care vor extinde clasa Animal, <<sange>> va fi o proprietate
    # Pentru a defini proprietati abstracte, folosim decoratorul @property urmat de @abstractmethod (in ordinea asta)
    # Astfel obligam clasele care extind clasa Animal sa contina un atribut (field/proprietate) cu numele sange
    @property  # decorator care anunta ca este vorba de o proprietate (adica atribut/field)
    @abstractmethod  # anunta ca metoda (in cazul de fata proprietatea) abstracta, deci trebuie implementata in subclasa
    def sange(self):
        pass  # pass se poate folosi in acest caz, pentru a marca faptul ca aici nu este necesara o implementare

    # Definim inca o proprietate abstracta: <<nume>>
    @property
    @abstractmethod
    def nume(self):
        pass

    @abstractmethod  # decorator = element care schimba comportamentul unei metode
    def deplasare(self):
        # putem afisa sau "arunca" o eroare atunci cand uitam sa implementam o metoda abstracta
        raise NotImplementedError

    @abstractmethod
    def scoate_sunet(self):
        pass

    @abstractmethod
    def odihnire(self):
        pass

    # In Python metodele abstracte pot avea implementari default.
    # Ele pot fi invocate prin apelarea functiei super(), care se refera la instructiunile metodei din supercalsa
    # Vom apela super().print_proprietati() intr-un exemplu de mai jos
    @abstractmethod
    def print_proprietati(self):
        print(f'Animalul {self.nume} are sangele {self.sange}')
        self.deplasare()
        self.scoate_sunet()
        self.odihnire()


# Declaram inca o clasa abstracta <<Mamifer>>
# Deoarece dorim sa categorizam animalele cat mai bine, si aceasta clasa va fi abstracta
# Daca clasa mamifer nu ar mosteni si ABC, am fi obligati sa implementam metodele abstracte din clasa Animal
# Intalnim principiul de mostenire multipla
class Mamifer(Animal, ABC):
    sange = "cald"


# Declaram inca o clasa abstracta <<Mamifer>>
class Reptila(Animal, ABC):
    sange = "rece"


# Declaram clasa <<Pisica>>
# Aceasta mosteneste proprietatile de la clasa Mamifer si este obligata sa implementeze tot din clasa Animal
class Pisica(Mamifer):
    nume = "pisica"
    proprietati_speciale = "9 vieti"

    def deplasare(self):
        # super().deplasare()  # daca apelam super() am primi eroare, deoarece nici in superclasa nu e implementata
        print("Merge cu picioarele")

    def scoate_sunet(self):
        print("Scoate sunetul miau miau")

    def odihnire(self):
        print("Doarme ghemotoc cu ochii inchisi")

    def print_proprietati(self):
        # Apeland super().print_proprietati() se vor executa instructiunile din superclasa
        super().print_proprietati()
        # Pe langa ce am executat din superclasa, vrem sa mai adaugam si instructiuni proprii
        print(f"{self.nume} mai are si {self.proprietati_speciale}")


class Sarpe(Reptila):
    nume = "sarpe"

    def deplasare(self):
        print("Merge in zig-zag cu ajutorul muschilor")

    def scoate_sunet(self):
        print("Scoate sunetul sssSSSssSSS")

    def odihnire(self):
        print("Darme cu ochii deschisi")

    def print_proprietati(self):
        super().print_proprietati()