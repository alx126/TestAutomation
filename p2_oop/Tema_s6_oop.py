print('### Exerciții recomandate ###\n')
print('### 1 ###\n')

from curs06_definire_clasa import Masina

mazda6 = Masina("Rosie", "6", "diesel", 6, 5, 240, "stinse")

mazda6.porneste_masina()
print(f"Verificam farurile: sunt {mazda6.faruri}.")
mazda6.accelereaza_masina(30)
mazda6.accelereaza_masina(100)
mazda6.accelereaza_masina(100)
mazda6.accelereaza_masina(30)
mazda6.decelereaza_masina(40)
mazda6.claxoneaza_masina()
mazda6.decelereaza_masina(200)
mazda6.claxoneaza_masina()
mazda6.opreste_masina()
print(f"Verificam farurile: sunt {mazda6.faruri}.")


print('\n### Exerciții obligatorii ###\n')
print('\n### 1 ###\n')
# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()


class Cerc:
    raza = 0
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}.')

    def aria(self):
        s = self.raza ** 2
        return s

    def diametru(self):
        d = self.raza * 2
        return d

    def circumferinta(self, raza):
        pi = 3.14
        l = 2 * pi * raza
        return l


if __name__ == "__main__":
    cerc = Cerc(2, "albastra")
    cerc.descrie_cerc()
    print(f"Aria cercului cu raza implicita este {cerc.aria()}.")
    print(f"Diametrul cercului este {cerc.diametru()}.")
    print(f"Lungimea cercului cu raza 1 este: {cerc.circumferinta(1)}.")


print('\n### 2 ###\n')
# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().


class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} \n'
              f'si culoarea {self.culoare}.')

    def aria(self):
        s = self.lungime * self.latime
        return s

    def perimetrul(self):
        p = 2 * (self.lungime + self.latime)
        return p

    def schimbă_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


if __name__ == "__main__":
    dreptunghi = Dreptunghi(10, 5, "galben")
    dreptunghi.descrie()
    print(f'Aria dreptunghiului este: {dreptunghi.aria()}.')
    print(f'Perimetrul dreptunghiului este: {dreptunghi.perimetrul()}.')
    dreptunghi.schimbă_culoarea("verde")
    print(f'Dreptunghiul are acum culoarea: {dreptunghi.culoare}.')


print('\n### 3 ###\n')
# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)


class Angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Nume:    {self.nume}\n'
              f'Prenume: {self.prenume}\n'
              f'Salariu: {self.salariu}.')

    def nume_complet(self):
        nume_complet = self.nume + self.prenume
        return nume_complet

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return salariu_anual

    def marire_salariu(self, procent):
        self.salariu *= (1+procent/100)
        return self.salariu


if __name__ == "__main__":
    angajat_1 = Angajat("Marinescu", "Georgel", 7500)
    angajat_1.descrie()
    print(f'{angajat_1.nume_complet()}.')
    print(f'Salariul lunar: {angajat_1.salariu_lunar()}')
    print(f'Salariul anual: {angajat_1.salariu_anual()}')
    angajat_1.marire_salariu(10)
    print(f'Salariul dupa marire devine: {angajat_1.salariu}')


print('\n### 4 ###\n')
# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)


class Cont:
    iban = None
    titular_cont = None
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} '
              f'suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        if self.sold >= suma:
            self.sold -= suma
            print(f'Contul {self.iban} a fost debitat cu suma {suma} lei.\n'
                  f'Soldul curent este {self.sold} lei.')
        else:
            print(f'Fonduri insuficiente.'
                  f'Soldul dvs este {self.sold} lei.')

    def creditare_cont(self, suma):
        self.sold += suma
        print(f'Contul dvs a fost creditat cu suma de {suma} lei.\n'
              f'Soldul curent este {self.sold} lei.')


if __name__ == "__main__":
    cont_bt = Cont("RO99BTRLRONMFRT00001399X", "Marinescu Georgel", 10000)
    cont_bt.afisare_sold()
    cont_bt.debitare_cont(2500)
    cont_bt.debitare_cont(7450)
    cont_bt.debitare_cont(100)
    cont_bt.creditare_cont(100)


print('\n### Exerciții optionale ###\n')
print('\n### 1 ###\n')
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

from datetime import date
from tabulate import tabulate


class Factura:
    seria = "AP"
    numar = 0
    nume_produs = None
    cantitate = 0
    pret_buc = 0

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        print(f'Cantitatea a fost modificata la {self.cantitate}.')

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        print(f'Noul pret este: {self.pret_buc} lei.')

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        print(f'Noua denumire a produsului este {self.nume_produs}.')

    def genereaza_factura(self):#, numar):
        pret_total = self.cantitate * self.pret_buc
        #self.numar = numar
        print("")
        print(f'Factura seria {self.seria} numar {self.numar}')
        print(f'Data: {date.today()}')
        print("")
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, pret_total]], headers=['Produs', 'Cantitate', 'Pret unitar', 'Total'], tablefmt='presto'))
        print("")


if __name__ == "__main__":
    factura_1 = Factura("0001", "Telefon", 5, 900)
    factura_1.genereaza_factura()
    factura_1.schimba_nume_produs("Aspirator")
    factura_1.schimba_cantitatea(3)
    factura_1.schimba_pretul(1850)
    factura_1.genereaza_factura()


print('\n### 2 ###\n')
# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0


class Masina:
    marca = "Kia"
    model = None
    viteza_maxima = 0
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"alb", "negru", "albastru", "rosu", "verde", "turcoaz", "panacotta"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca: {self.marca}\n'
              f'Model: {self.model}\n'
              f'Viteza maxima: {self.viteza_maxima} km/h\n'
              f'Culoare: {self.culoare}\n'
              f'Inmatriculata: {self.inmatriculata}\n'
              f'Viteza actuala: {self.viteza_actuala} km/h.')

    def inmatriculare(self):
        if not self.inmatriculata:
            stare_inmatriculare = True
            self.inmatriculata = stare_inmatriculare

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print(f'Culoarea dorita nu este disponibila.\n'
                  f'Puteti alege din urmatarele culori disponibile: {self.culori_disponibile}.')

    def accelereaza(self, viteza):
        if viteza < 0:
            print(f'Eroare! Valoarea trebuie sa fie pozitiva.')
        elif self.viteza_actuala + viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f'Am atins viteza maxima de {self.viteza_maxima} km/h.')
        else:
            self.viteza_actuala += viteza
            print(f'Acceleram! Viteza actuala este {self.viteza_actuala} km/h.')

    def franeaza(self):
        viteza = 0
        self.viteza_actuala = viteza
        print(f'Am franat, viteza actuala este {self.viteza_actuala} km/h.')


if __name__ == "__main__":
    kia_sportage = Masina("Sportage", 245)
    kia_sportage.descrie()
    kia_sportage.vopseste("alb-perlat")
    kia_sportage.vopseste("turcoaz")
    kia_sportage.descrie()
    kia_sportage.inmatriculare()
    kia_sportage.descrie()
    kia_sportage.accelereaza(50)
    kia_sportage.accelereaza(100)
    kia_sportage.accelereaza(96)
    kia_sportage.franeaza()


print('\n### 3 ###\n')
# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict


class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print(f'Am adaugat task: {nume}\n'
              f'Descriere: {descriere}.\n')


    def finalizeaza_task(self, nume):
        if nume in self.todo.keys():
            self.todo.pop(nume)
            print(f'Taskul {nume} a fost finalizat.')
        else:
            print(f'Taskul {nume} nu exista.')

    def afiseaza_todo_list(self):
        i = 1
        while i <= len(self.todo.keys()):
            for key in self.todo.keys():
                print(f'Task {i}: {key}\n')
                i += 1

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.keys():
            raspuns = input(f'Taskul "{nume_task}" nu este inregistrat.\n'
                            'Doresti sa fie adaugat in lista? Raspunde cu da sa nu: ')
            if raspuns == "nu":
                print(f'La revedere, drum bun!')
            elif raspuns == "da":
                detalii = input(f"Adaugati detalii pentru {nume_task}: ")
                self.todo[nume_task] = detalii
                print(self.todo.items())
            else:
                print("Raspuns incorect, mai incearca.")
        else:
            print(f'Task: {nume_task}\n'
                  f'Detalii: {self.todo[nume_task]}.\n')


if __name__ == "__main__":
    to_do_list = TodoList()
    to_do_list.adauga_task("Imprejmuire santier", "Instalare gard")
    to_do_list.adauga_task("Organizare santier", "Instalare cabluri electrice, fabricare si montaj tablouri electrice, instalare iluminat si prize")
    to_do_list.afiseaza_todo_list()
    to_do_list.afiseaza_detalii_suplimentare("Organizare santier")
    to_do_list.afiseaza_detalii_suplimentare("Instalare impamantare")
    to_do_list.afiseaza_todo_list()
    to_do_list.adauga_task("Instalare paturi de cabluri", "TBD")
    to_do_list.afiseaza_todo_list()
    to_do_list.finalizeaza_task("Imprejmuire santier")
    to_do_list.afiseaza_todo_list()

# Sapare santuri cu adancime min 0.8m, instalare platbanda OlZn 40x4 mmp, instalare cutii separatie