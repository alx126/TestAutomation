"""
POO = Programare orientata pe obiecte
OOP = Object Oriented Programming

Clasa = structura de tip tipar / blueprint / prototip / reteta care serveste drept ghid pentru un element care ar PUTEA exista

Componentele unei clase:

1. Atribute (field-uri, proprietati) = proprietatile cu care se vor identifica obiectele
- pentru a accesa un atribut dintr-o clasa in interiorul acelei clase se foloseste keyword-ul self
in caz contrar se va considera ca se face referinta catre parametrii metodei
- accesarea unui atribut dintr-o clasa in afara clasei se poate face in urmatoarele moduri:
    a) un obiect instantiat din acea clasa
    b) decoratorul @staticmethod pentru a accesa atributele si metodele clasei
    c) prin conceptul de mostenire a unei clase (vom discuta la cursul 7)
- atributele pot avea valori implicite daca exista niste valori general valabile
- daca nu exista valori general valabile atunci atributele vor avea valoarea initiala None

2. Metode = actiunile pe care le poate face un obiect
                        ATENTIE!!! Metodele sunt de fapt niste functii create in interiorul clasei
                         In afara clasei = functii
                         In interiorul clasei = metode
Obiect = instanta a clasei, reprezentare reala a tiparului reprezentat de clasa
pot sa instantiez oricate obiecte dintr-o anumita clasa

3. Constructor = Element care va fi folosit pentru instantierea obiectelor dintr-o clasa
Scopul unui constructor este de a ajuta sistemul sa instantieze obiectul dintr-o clasa
Exista doua tipuri de constructori:

a) constructor explicit care obliga utilizatorul sa populeze anumite atribute la instantierea	obiectului
si daca este cazul sa defineasca o regula de populare a atributelor

b) constructor implicit care este apelat automat atunci cand nu exista un constructor explicit definit
Pot sa definesc mai multi constructori in aceeasi clasa atata timp cat vor avea un numar diferit de parametri
(method overloading) - polimorfism -> In python nu e posibila definirea mai multor constructori
"""


class Masina:
    culoare = "Fuchsia"
    model = None
    tractiune = "spate"
    propulsia = None
    an_fabricatie = None
    numar_inmatriculare = None
    numar_locuri = None
    consum = None
    cutie_viteza = "manuala"
    viteza_maxima = 150
    viteza_curenta = 0
    faruri = "test"

    # definim constructorul explicit al clasei
    def __init__(self, culoare, model, propulsie, consum, numar_locuri, viteza_maxima, faruri):
        # pentru a ne referi la atributele clasei, se va folosi <<self>>

        # argumentele din __init__ <<culoare, model, propulsie, etc>> nu sunt identice cu field-urile din clasa, ele
        # au fost denumite la fel tocmai pentru a scoate in evidenta diferentele dintre acestea
        # valorile din __init__ vor veni atunci cand vom declara un obiect de tip Masina

        # aici intalnim conceptul de polimorfism, despre care vom discuta la cursul urmator

        # deci <<self.culoare>> se refera la variabila declarata la inceputul clasei,
        # iar <<culoare>> din __init__ va fi valoarea pe care o primeste obiectul de tip Masina() la initializare

        # daca declaram un obiect de tip Masina: bmw = Masina("verde", "X3" ...etc)
        # acel "verde" va inlocui culoarea initiala 'Fuchsia'
        # if culoare == "orange":
        #     self.culoare = 'portocaliu'
        # else:
        #     self.culoare = culoare
        self.model = model
        self.propulsia = propulsie
        self.consum = consum
        self.numar_locuri = numar_locuri
        self.viteza_maxima = viteza_maxima
        self.faruri = faruri

    """
    Actiuni:
    - pornire
    - accelerare
    - decelerare
    - oprire
    - claxon
    """

    def porneste_masina(self):
        self.faruri = "pornite"
        print("Am pornit masina")

    def accelereaza_masina(self, valoare_accelerare):
        if self.viteza_curenta + valoare_accelerare > self.viteza_maxima:
            self.viteza_curenta = self.viteza_maxima
            print(f"Ati atins deja viteza maxima, nu mai puteti accelera. Viteza: {self.viteza_curenta} km/h")
        else:
            self.viteza_curenta += valoare_accelerare
            print(f"Acceleram cu {valoare_accelerare} km/h. Viteza: {self.viteza_curenta} km/h")

    def decelereaza_masina(self, valoare_decelerare):
        if self.viteza_curenta - valoare_decelerare >= 0:
            print(f"Am decelerat cu {valoare_decelerare} km/h. Viteza: {self.viteza_curenta} km/h")
        else:
            print(f"Am decelerat maxim. Viteza: {self.viteza_curenta} km/h")

    def opreste_masina(self):
        if self.viteza_curenta == 0:
            self.faruri = "oprite"
            print("Am oprit masina")

    @staticmethod  # metoda statica (fara self) - se poate accesa fara a crea un obiect de tip Masina
    def claxoneaza_masina():
        print("tiit tiiiit")


print("Instructiune in afara if-ului")

# Ii spunem compilatorului sa ruleze acest cod doar daca acesta e fisierul principal
# acest lucru va
if __name__ == "__main__":
    print("Instructiune in interiorul if-ului")

    # culoare, model, propulsie, consum, numar_locuri, viteza_maxima, faruri
    bmw = Masina("rosu", "X5", "benzina", "a1", 4, 150, "oprite")

    # bmw = Masina()  - nu mai este valid dupa ce avem constructor explicit (cel cu __init__)
    print(f"Masina bmw are culoarea {bmw.culoare}")
    bmw.tractiune = "fata"
    print(f"Masina bmw are tractiunea {bmw.tractiune}")
    print(f"Culoarea implicita din clasa Masina este {Masina.culoare}")
    print(f"Tractiunea implicita din clasa Masina este {Masina.tractiune}")
    print(bmw.faruri)

    skoda = Masina("albastru", "fabia", "hybrid", "a1", 4, 180, "pornite")
    skoda.an_fabricatie = 2021
    print(f"Masina skoda a fost fabricata in anul {skoda.an_fabricatie}")
    bmw.an_fabricatie = 2020
    print(f"Masina bmw a fost fabricata in anul {bmw.an_fabricatie}")
    print(skoda.faruri)

    bmw.porneste_masina()
    print(f"Momentan farurile masinii bmw sunt {bmw.faruri}")
    bmw.accelereaza_masina(10)
    print(f"Viteza curenta a masinii bmw este {bmw.viteza_curenta}")
    bmw.decelereaza_masina(5)
    print(f"Viteza curenta a masinii bmw este {bmw.viteza_curenta}")
    bmw.accelereaza_masina(180)
    print(f"Viteza curenta a masinii bmw este {bmw.viteza_curenta}")
    print(f"Faruri accesate din clasa: {Masina.faruri}")

print("Instructiune dupa if")

print(bmw.culoare)
bmw.culoare = "roz"
print(bmw.culoare)