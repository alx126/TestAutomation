from curs07_p4_incapsulare import *

user_exemplu = User()
user_exemplu.set_username("testautomation")

user_exemplu.set_username("testautomation@itfactory.com")

user_exemplu.set_password("Alabalaportocala")
parola = user_exemplu.get_password()
print(f"Parola este {parola}")

parola = user_exemplu.get_password()
print(f"Parola este {parola}")


user_decorat = UserCuDecoratori()

user_decorat.password = "Alabalaportocala"
password = user_decorat.password
print(f"Parola userului cu decorator {password}")
del user_decorat.password

password = user_decorat.password
print(f"Parola userului cu decorator {password}")