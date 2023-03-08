"""
Incapsulare = restrictionarea accesului la anumite atribute (proprietati/field-uri) sau metode (functii)

Incapsularea se face prin intermediul unor proprietati care poarta numele de modificatori de acces:

Modificatorii de acces sunt Private, Protected, Public

- private = atributul sau metoda definite intr-o clasa sunt vizibile doar in clasa respectiva

- protected = atributul sau metoda pot fi utilizate in afara clasei
    printr-un obiect instantiat din clasa respectiva,
    dar acel atribut sau metoda nu va fi sugerat utilizatorului

- public = atributul sau metoda pot fi utilizate oriunde in afara clasei, si ca vor fi sugerate
    utilizatorului la momentul instantierii obiectului

 Note importante:
 1. In java modificatorii de acces sunt specificati in mod explicit
 prin keyword-urile corespunzatoare: public, private, protected

 In python modificatorii de acces sunt specificati in mod indirect in felul urmator:
 - atributele sau metodele public vor fi definite ca atare fara niciun artificiu
 - atributele sau metodele protected for fi precedate de caracterul "_"
 - atributele sau metodele private for fi precedate de dublu "__"

 2. In python atributul/metoda protected pot fi accesate oriunde, dar ele nu vor fi sugerate utilizatorului la scriere
 In java atributul sau metoda protected vor fi accesate doar in acelasi pachet in care se afla clasa
 """


class User:
    __username = None
    __password = None
    __user_data = {}

    def set_username(self, value):
        if '@' in value and '.com' in value:
            self.__username = value
            print(f"Username-ul <<{value}>> a fost salvat cu succes!")
        else:
            print("Username nu a fost setat. Format invalid, reincercati.")

    def get_username(self):
        return self.__username

    def delete_username(self):
        self.__username = None

    def set_password(self, value):
        if len(value) > 7 and self.__contains_uppercase(value):
            self.__password = self.__codifica_pass(value)
        else:
            print("Format invalid. Parola trebuie sa fie de min. 8 caractere si trebuie sa contina min. 1 litera mare")

    def get_password(self):
        return self.__decodifica_pass(self.__password)

    def delete_password(self):
        self.__password = None

    def delete_userdata(self):
        self.__user_data = None

    def __contains_uppercase(self, password):
        avem_uppercase = False
        for letter in password:
            if str(letter).isupper():
                avem_uppercase = True
                break
        return avem_uppercase

    def __codifica_pass(self, password):
        pass_codificat = ""
        for char in password:
            # print(chr(ord(char) + 1))
            pass_codificat += chr(ord(char) + 1)  # luam codul ASCII a caracterului si adunam la el 1
        # print(f"Pass-ul codificat: {pass_codificat}")
        return pass_codificat

    def __decodifica_pass(self, password):
        pass_decodificat = ""
        for char in password:
            # print(chr(ord(char) - 1))
            pass_decodificat += chr(ord(char) - 1)  # luam codul ASCII a caracterului si scadem 1 din el
        # print(f"Pass-ul decodificat: {pass_decodificat}")
        return pass_decodificat


class UserCuDecoratori:

    __username = None
    __password = None


    @property
    def username(self):
        return self.__username()

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        if '@' in value and '.com' in value:
            self.username = value
            print(f"Username-ul <<{value}>> a fost salvat cu succes!")
        else:
            print("Username nu a fost setat. Format invalid, reincercati.")

    @username.getter
    def username(self):
        return self.username

    @username.deleter
    def username(self):
        self.username = None

    @password.setter
    def password(self, value):
        if len(value) > 7 and self.__contains_uppercase(value):
            self.__password = self.__codifica_pass(value)
        else:
            print("Format invalid. Parola trebuie sa fie de min. 8 caractere si trebuie sa contina min. 1 litera mare")

    @password.getter
    def password(self):
        if self.__password is not None:
            return self.__decodifica_pass(self.__password)
        else:
            print("Parola nu este setata")

    @password.deleter
    def password(self):
        self.__password = None

    def __contains_uppercase(self, password):
        avem_uppercase = False
        for letter in password:
            if str(letter).isupper():
                avem_uppercase = True
                break
        return avem_uppercase

    def __codifica_pass(self, password):
        pass_codificat = ""
        for char in password:
            # print(chr(ord(char) + 1))
            pass_codificat += chr(ord(char) + 1)  # luam codul ASCII a caracterului si adunam la el 1
        # print(f"Pass-ul codificat: {pass_codificat}")
        return pass_codificat

    def __decodifica_pass(self, password):
        pass_decodificat = ""
        for char in password:
            # print(chr(ord(char) - 1))
            pass_decodificat += chr(ord(char) - 1)  # luam codul ASCII a caracterului si scadem 1 din el
        # print(f"Pass-ul decodificat: {pass_decodificat}")
        return pass_decodificat