# Definim clasa caine
# Constructor explicit pentru proprietatea culoare
# Functii pentru:
# - Latra
# - Descriere
# - Cantarire (se va seta greutatea cainelui prin cantarire)
from abc import ABC, abstractmethod


class Caine:
    nume = None
    culoare = None
    greutate = None
    varsta = 0
    rasa = None

    def __init__(self, nume_primit_din_exterior, culoare_primita_din_exterior):
        self.culoare = culoare_primita_din_exterior
        self.nume = nume_primit_din_exterior

    def latra(self):
        print("ham ham")

    def descriere(self):
        print(f"Cainele {self.nume} are culoarea {self.culoare}")

    # def cantarire(self):
    #     self.greutate = float(input(f"Dati greutatea cainelui {self.nume} "))

    def cantarire(self, greutate_din_ext):
        self.greutate = greutate_din_ext


rexi = Caine("Rexi", "Maro")
lessi = Caine("Lessi", "Alb")

rexi.latra()
lessi.latra()
rexi.descriere()

rexi.cantarire(7.5)

greutate = 8
lessi.cantarire(greutate)
print("")

rexi.greutate = 5
print("")


class FormaGeometrica(ABC):
    PI = 3.14
    culoare = "invizibil"

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):
    __latura = None

    # def __init__(self, latura_din_ext):
    #     self.__latura = latura_din_ext

    def aria(self):
        return self.__latura * self.__latura

    def set_latura(self, latura_din_ext):
        if latura_din_ext <= 0:
            print("Latura nu poate fi negativa")
        else:
            self.__latura = latura_din_ext

    def get_latura(self):
        return self.__latura

    def delete_latura(self):
        del self.__latura


patratel = Patrat()
patratel.set_latura(-5)
patratel.set_latura(5)

arie_patratel = patratel.aria()
print(f'Aria patratului e {arie_patratel}')

latura_patratel = patratel.get_latura()

print(f"Latura patratului patratel: {latura_patratel}")

patratel.delete_latura()

print(f"Latura patratului patratel: {patratel.get_latura()}")

patratel.descriere()


class Cerc(FormaGeometrica):
    __raza = None
    culoare = "verde"

    def __init__(self, raza_cercului):
        self.__raza = raza_cercului

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza_din_ext):
        if raza_din_ext <= 0:
            print("Raza este prea mica")
        else:
            self.__raza = raza_din_ext

    def delete_raza(self):
        del self.__raza

    def aria(self):
        return self.PI * self.__raza * self.__raza

    def descriere(self):
        super().descriere()

        print("Eu nu am colturi")

        print(f"Initial am fost {super().culoare} iar acum sunt {self.culoare}")


cerculet = Cerc(3)
cerculet.descriere()
print(f"Aria cercului este {cerculet.aria()}")