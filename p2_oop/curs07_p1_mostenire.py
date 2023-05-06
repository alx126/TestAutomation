"""
Mostenire = o modalitate prin care putem transmite atribute si metode care sunt definite intr-o clasa parinte
Astfel, clasele 'copii' care extind o clasa 'parinte' vor <<mosteni>> atributele si mertodele acesteia
Mostenirea se poate implementa prin mentionarea numelui clasei parinte intre paranteze rotunde
O clasa copil poate sa mosteneasca de la oricate clase parinte
"""


# Definim clasa Phone
class Phone:
    name = ""
    year = 2019
    turned_on = False
    screen_size = None

    def __init__(self, name, screen_size, turned_on):
        self.name = name
        self.screen_size = screen_size
        self.turned_on = turned_on

    def turn_on(self):
        if self.turned_on:
            print("Telefonul este deja pornit")
        else:
            print("Telefonul a fost pornit...")
            self.turned_on = True

    def print_phone_properties(self):
        print(f" Nume: {self.name}\n An: {self.year}\n Ecran: {self.screen_size}")


# Definim clasa AndroidPhone
# AndroidPhone este SUBCLASA a clasei Phone
# AndroidPhone EXTINDE clasa Phone
class AndroidPhone(Phone):
    android_version = None

    def set_android_version(self, version):
        self.android_version = version

    def print_android_version(self):
        if self.android_version:
            print(f'Telefonul are versiunea Android {self.android_version}')
        else:
            print('Versiunea de Android nu a fost inca setata')


# Definim clasa Iphone
# Iphone este SUBCLASA a clasei Phone
# Iphone EXTINDE clasa Phone
class Iphone(Phone):
    ios_version = None
    cameras = 1

    def set_ios_version(self, version):
        self.ios_version = version

    def print_ios_version(self):
        if self.ios_version:
            print(f'Telefonul are versiunea IOs {self.ios_version}')
        else:
            print('Versiunea de IOs nu a fost setata')


# Definim clasa OnePlus8Pro
# OnePlus8Pro este SUBCLASA a clasei AndroidPhone
# OnePlus8Pro EXTINDE clasa AndroidPhone
class OnePlus8Pro(AndroidPhone):
    os_name = "OxygenOs"

    def print_oneplus_properties(self):
        print(f'Sistemul de operate al OnePlus este {self.os_name}')


# Definim clasa Iphone13Pro
# Iphone13Pro este SUBCLASA a clasei Iphone
# Iphone13Pro EXTINDE clasa Iphone
class Iphone13Pro(Iphone):
    cameras = 3

    def print_iphone_13_properties(self):
        self.print_phone_properties()
        self.print_ios_version()
        # super() poate accesa metode (functii) si proprietati (atribute/field-uri) din clasa parinte
        print(f'Camere foto in clasa parinte (Iphone): {super().cameras}')
        print(f'Camere foto in clasa Iphone13Pro: {self.cameras}')
